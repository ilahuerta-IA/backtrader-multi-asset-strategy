# Changelog

All notable changes to the Hexa-Asset Multi-Asset Trading System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added
- Initial release of Hexa-Asset Multi-Asset Trading System
- 6 asset strategies: EURUSD, USDCHF, GBPUSD, AUDUSD, XAUUSD, XAGUSD
- Pullback-window entry system with 3-phase logic
- ATR-based dynamic risk management
- Ray Dalio All-Weather portfolio allocation
- Comprehensive performance analysis documentation
- Monthly heatmap visualizations
- Trade reporting system with detailed entry/exit logs
- Portfolio aggregation and risk metrics
- Interactive charts with mouse hover functionality

### Features
- **Risk Management:**
  - 1% risk per trade (conservative Kelly sizing)
  - Dynamic stop-loss: 2.5× ATR
  - Dynamic take-profit: 6.5× ATR
  - 50+ consecutive loss protection

- **Entry Logic:**
  - EMA confluence detection (Fast > Medium > Slow)
  - ATR volatility filtering (optimal range: 0.0002-0.0005)
  - Pullback system (1-3 red candles)
  - Window breakout confirmation (1-3 bars)
  - Time-session filtering (asset-specific)

- **Portfolio Diversification:**
  - 20% USDCHF (deflation hedge)
  - 18% XAUUSD (inflation hedge)
  - 16% EURUSD (developed market)
  - 16% GBPUSD (volatility capture)
  - 16% AUDUSD (risk-on/off barometer)
  - 15% XAGUSD (commodity exposure)

- **Performance:**
  - Total Return: +53.02% (5 years)
  - Annual CAGR: 8.89%
  - Max Drawdown: -8.34%
  - Sharpe Ratio: 1.24
  - Profit Factor: 1.53

### Fixed
- **CRITICAL:** USDCHF hardcoded override bug in `_apply_forex_config()`
  - All assets were incorrectly overridden with USDCHF parameters
  - Disabled method across all 6 strategy files
  - Impact: Fixed incorrect position sizing and trade generation

- **CRITICAL:** XAUUSD/XAGUSD forex parameter contamination
  - Gold: Changed pip_value from 0.0001 to 0.01
  - Gold: Changed lot_size from 100,000 to 100
  - Silver: Changed pip_value from 0.0001 to 0.001
  - Silver: Changed lot_size from 100,000 to 5,000
  - Impact: Fixed zero position sizing and $0 P&L issues

- **Configuration Mismatches:**
  - EURUSD: Fixed LONG_ATR_MAX (0.000600 → 0.000499)
  - EURUSD: Fixed LONG_USE_PULLBACK_ENTRY (False → True)
  - EURUSD: Fixed USE_TIME_RANGE_FILTER (False → True)
  - GBPUSD: Fixed USE_TIME_RANGE_FILTER (True → False for 24/7 trading)
  - XAUUSD: Fixed USE_TIME_RANGE_FILTER (True → False for 24/7 trading)
  - Impact: Aligned all strategies with profitable original configurations

- **Display Issues:**
  - Unicode encoding errors in Windows console (✅ ❌ → [OK] [ERROR])
  - Risk percent formatting in portfolio summary
  - Removed extra decimal places in trade reports

### Documentation
- Complete performance analysis (Ernest P. Chan + Ray Dalio frameworks)
- Yearly breakdown with Sharpe ratios and CAGR
- Correlation matrices showing diversification benefits
- Monthly performance heatmaps (entries, profitability)
- Bug fix documentation (3 detailed markdown files)
- Optimization roadmap with expected improvements
- Live trading preparation guidelines

### Testing
- 5-year backtest validation (2020-2025)
- 644 total trades across 6 assets
- Statistical significance: 6.4× minimum sample size
- Multiple market regime testing (trending, choppy, volatile)

## [Unreleased]

### Planned Features
- [ ] Enable SHORT trading on all assets
- [ ] Machine learning entry timing optimization
- [ ] Multi-timeframe analysis (15-min, 1-hour)
- [ ] Additional assets (NZD/USD, USD/CAD, EUR/GBP)
- [ ] Commodity futures (Crude Oil, Natural Gas, Copper)
- [ ] Dynamic Kelly position sizing
- [ ] Regime detection system
- [ ] Real-time monitoring dashboard
- [ ] Automated live trading integration

### Known Issues
- None currently reported

### Future Improvements
- Reduce execution time (currently ~8-10 minutes for full backtest)
- Add unit tests for critical functions
- Improve memory efficiency for large datasets
- Add real-time data streaming capability
- Implement automated parameter optimization

---

## Version History

- **1.0.0** (2025-11-16): Initial production release
- **0.9.0** (2025-11-02): Beta testing phase
- **0.5.0** (2025-10-15): Alpha development phase
- **0.1.0** (2025-09-01): Initial development start

---

## Migration Guide

### From Beta (0.9.0) to Production (1.0.0)

**Breaking Changes:**
- None - Backward compatible

**New Features:**
- Comprehensive documentation added
- GitHub repository structure
- Automated testing workflow

**Upgrade Steps:**
1. Pull latest code from main branch
2. Review updated README.md
3. Check docs/ folder for new analysis
4. Run backtest to verify everything works

### Configuration Changes
No changes required. All existing configurations remain valid.

---

*For detailed changes, see individual commit messages and pull requests.*
