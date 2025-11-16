"""Simple Monthly Statistics Generator
Reads trade report files and generates monthly statistics.
Can be run independently after backtests complete.
"""

import pandas as pd
from pathlib import Path
from collections import defaultdict
import calendar

def generate_monthly_statistics_from_reports(temp_reports_dir, starting_cash=100000):
    """Generate monthly statistics by parsing trade report files
    
    Args:
        temp_reports_dir: Path to directory containing trade report files
        starting_cash: Initial portfolio balance
    """
    print(f"\n" + "="*100)
    print(f"MONTHLY STATISTICS ANALYSIS (from trade reports)")
    print(f"="*100)
    
    temp_reports_path = Path(temp_reports_dir)
    all_trades = []
    
    # Parse all trade report files
    if temp_reports_path.exists():
        for report_file in temp_reports_path.glob('*_trades_*.txt'):
            asset_name = report_file.stem.split('_trades_')[0]
            
            try:
                with open(report_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract trade entries
                    entries = content.split('ENTRY #')
                    
                    for entry in entries[1:]:  # Skip first split (header)
                        try:
                            lines = entry.split('\n')
                            trade_data = {'asset': asset_name}
                            
                            for line in lines:
                                if line.startswith('Time:'):
                                    time_str = line.split('Time:')[1].strip()
                                    trade_data['entry_time'] = pd.to_datetime(time_str)
                                elif line.startswith('Exit Time:'):
                                    time_str = line.split('Exit Time:')[1].strip()
                                    trade_data['exit_time'] = pd.to_datetime(time_str)
                                elif line.startswith('PnL:'):
                                    pnl_str = line.split('PnL:')[1].strip().replace('$', '').replace(',', '')
                                    trade_data['pnl'] = float(pnl_str)
                                elif line.startswith('Direction:'):
                                    trade_data['direction'] = line.split('Direction:')[1].strip()
                            
                            if 'entry_time' in trade_data and 'pnl' in trade_data:
                                all_trades.append(trade_data)
                        except Exception as e:
                            continue
                            
            except Exception as e:
                print(f"[WARNING] Could not parse {report_file.name}: {e}")
                continue
    
    if not all_trades:
        print("[INFO] No trade report files found or no trades to analyze")
        print(f"[INFO] Trade reports should be in: {temp_reports_path}")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(all_trades)
    df['year_month'] = df['entry_time'].dt.to_period('M')
    df['year'] = df['entry_time'].dt.year
    df['month'] = df['entry_time'].dt.month
    df['date'] = df['entry_time'].dt.date
    df['is_winner'] = df['pnl'] > 0
    
    # ================================================================
    # TABLE 1: MONTHLY ENTRY STATISTICS
    # ================================================================
    print(f"\nMONTHLY ENTRY STATISTICS")
    print(f"{'Year':<6} {'Month':<10} {'Total':>8} {'Winners':>8} {'Losers':>8} {'Max/Day':>8}")
    print(f"-" * 60)
    
    monthly_entries = df.groupby('year_month').agg({
        'pnl': 'count',
        'is_winner': ['sum', lambda x: (~x).sum()],
        'date': lambda x: x.value_counts().max()
    }).reset_index()
    
    monthly_entries.columns = ['year_month', 'total', 'winners', 'losers', 'max_daily']
    monthly_entries['year'] = monthly_entries['year_month'].dt.year
    monthly_entries['month'] = monthly_entries['year_month'].dt.month
    
    yearly_totals = defaultdict(lambda: {'total': 0, 'winners': 0, 'losers': 0, 'max_daily': 0})
    
    for _, row in monthly_entries.iterrows():
        year = row['year']
        month = row['month']
        month_name = calendar.month_abbr[month]
        
        total = int(row['total'])
        winners = int(row['winners'])
        losers = int(row['losers'])
        max_daily = int(row['max_daily'])
        
        yearly_totals[year]['total'] += total
        yearly_totals[year]['winners'] += winners
        yearly_totals[year]['losers'] += losers
        yearly_totals[year]['max_daily'] = max(yearly_totals[year]['max_daily'], max_daily)
        
        print(f"{year:<6} {month_name:<10} {total:>8} {winners:>8} {losers:>8} {max_daily:>8}")
    
    # Print yearly totals
    print(f"-" * 60)
    for year in sorted(yearly_totals.keys()):
        data = yearly_totals[year]
        print(f"{year:<6} {'TOTAL':<10} {data['total']:>8} {data['winners']:>8} "
              f"{data['losers']:>8} {data['max_daily']:>8}")
    
    # ================================================================
    # TABLE 2: MONTHLY PROFITABILITY (%)
    # ================================================================
    print(f"\nMONTHLY PROFITABILITY (% relative to accumulated balance)")
    print(f"{'Year':<6} {'Month':<10} {'PnL ($)':>12} {'Return (%)':>12} {'Cumulative':>12}")
    print(f"-" * 60)
    
    monthly_pnl = df.groupby('year_month')['pnl'].sum().reset_index()
    monthly_pnl['year'] = monthly_pnl['year_month'].dt.year
    monthly_pnl['month'] = monthly_pnl['year_month'].dt.month
    
    cumulative_balance = starting_cash
    yearly_returns = defaultdict(float)
    
    for _, row in monthly_pnl.iterrows():
        year = row['year']
        month = row['month']
        month_name = calendar.month_abbr[month]
        monthly_profit = row['pnl']
        
        monthly_return = (monthly_profit / cumulative_balance) * 100 if cumulative_balance > 0 else 0
        cumulative_balance += monthly_profit
        yearly_returns[year] += monthly_return
        
        print(f"{year:<6} {month_name:<10} ${monthly_profit:>10,.2f} {monthly_return:>11.2f}% "
              f"${cumulative_balance:>10,.2f}")
    
    # Print yearly totals
    print(f"-" * 60)
    for year in sorted(yearly_returns.keys()):
        year_return = yearly_returns[year]
        print(f"{year:<6} {'TOTAL':<10} {'':<12} {year_return:>11.2f}% {'':<12}")
    
    print(f"="*100)
    print(f"[INFO] Monthly statistics generated from {len(all_trades)} trades")
    print(f"[INFO] Data source: Trade report files in {temp_reports_path}")
    print(f"[INFO] This data can be exported for further analysis")


if __name__ == '__main__':
    # Run as standalone script
    BASE_DIR = Path(__file__).resolve().parent
    TEMP_REPORTS_DIR = BASE_DIR / 'temp_reports'
    
    generate_monthly_statistics_from_reports(TEMP_REPORTS_DIR, starting_cash=100000)
