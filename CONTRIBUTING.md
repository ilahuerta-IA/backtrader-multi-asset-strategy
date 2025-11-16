# Contributing to Hexa-Asset Multi-Asset Trading System

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Types of Contributions

We welcome the following types of contributions:

### 1. Bug Reports
- Configuration errors
- Logic bugs
- Performance issues
- Documentation errors

### 2. Bug Fixes
- Parameter corrections
- Logic improvements
- Performance optimizations

### 3. Documentation
- Clearer explanations
- Additional examples
- Translation improvements

### 4. New Features
- Additional analytics
- New visualization types
- Strategy enhancements
- Additional assets

## 📋 Before You Start

1. **Search existing issues** - Your issue may already be reported
2. **Check documentation** - Answer might be in the docs
3. **Run backtests** - Verify the issue is reproducible
4. **Review code** - Understand the codebase structure

## 🔧 Development Workflow

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/backtrader-multi-asset-strategy.git
cd backtrader-multi-asset-strategy
```

### 2. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b bugfix/issue-description
```

### 3. Make Changes

- Follow existing code style
- Add comments for complex logic
- Update documentation if needed
- Test your changes thoroughly

### 4. Test Your Changes

```bash
# Run the main backtest
python sunrise_ogle_multi_asset.py

# Verify results match expectations
# Check for errors or warnings
# Validate performance metrics
```

### 5. Commit Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "Fix: Correct XAUUSD pip value calculation"

# Or for features
git commit -m "Feature: Add Sortino ratio calculation"
```

**Commit Message Format:**
```
Type: Brief description (50 chars max)

Detailed explanation if needed (wrap at 72 chars)
- Bullet points for multiple changes
- Reference issue numbers: Fixes #123
```

**Types:**
- `Fix:` - Bug fixes
- `Feature:` - New features
- `Docs:` - Documentation changes
- `Refactor:` - Code restructuring
- `Test:` - Testing improvements
- `Perf:` - Performance improvements

### 6. Push & Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
# Fill in the PR template
```

## ✅ Pull Request Requirements

### Before Submitting

- [ ] Code runs without errors
- [ ] Backtest completes successfully
- [ ] Performance metrics are documented
- [ ] Documentation is updated
- [ ] Commit messages are clear

### PR Description Must Include

1. **What Changed**
   - Clear description of modifications
   - Files affected
   - New functionality added

2. **Why Changed**
   - Problem being solved
   - Issue reference (if applicable)
   - Benefits of the change

3. **Testing**
   - How you tested the change
   - Backtest results (before/after)
   - Any edge cases considered

4. **Performance Impact**
   ```
   Before:
   - Sharpe: 1.24
   - Max DD: -8.34%
   - Total Return: +53.02%
   
   After:
   - Sharpe: 1.28 (+0.04)
   - Max DD: -8.10% (-0.24%)
   - Total Return: +55.43% (+2.41%)
   ```

5. **Breaking Changes**
   - List any breaking changes
   - Migration guide if needed

## 📝 Code Style Guidelines

### Python Style

Follow PEP 8 with these specifics:

```python
# Use meaningful variable names
good: average_true_range = 0.00025
bad:  atr = 0.00025

# Add docstrings for functions
def calculate_position_size(risk_amount, stop_distance):
    """Calculate position size based on risk and stop distance.
    
    Args:
        risk_amount (float): Dollar amount to risk
        stop_distance (float): Distance to stop loss in price units
        
    Returns:
        float: Position size in lots
    """
    return risk_amount / stop_distance

# Use type hints for clarity
def get_atr(self, period: int = 14) -> float:
    """Calculate Average True Range"""
    pass

# Comment complex logic
# Calculate Kelly Criterion optimal position size
# Formula: f* = (p*b - q) / b
# where p = win probability, q = 1-p, b = win/loss ratio
kelly_fraction = (win_rate * payoff_ratio - (1 - win_rate)) / payoff_ratio
```

### Documentation Style

```python
"""
Module: sunrise_ogle_eurusd.py
Description: EURUSD-specific strategy with pullback-window entry logic

Strategy Features:
- EMA confluence for trend detection
- ATR-based volatility filtering
- 3-phase pullback entry system
- Dynamic stop-loss and take-profit

Performance (5 years):
- Return: +30.50%
- Sharpe: 0.89
- Max DD: -10.71%
"""
```

## 🧪 Testing Guidelines

### Required Tests

1. **Full Backtest**
   ```bash
   python sunrise_ogle_multi_asset.py
   ```
   - Must complete without errors
   - Performance metrics must be reasonable
   - Memory usage must be acceptable

2. **Individual Asset Tests**
   ```python
   # Test single asset in isolation
   # Verify parameters are correct
   # Check trade generation
   ```

3. **Edge Cases**
   - Empty data files
   - Missing parameters
   - Extreme volatility periods
   - Zero trades generated

### Performance Benchmarks

Your changes should NOT significantly degrade:

- **Execution Time:** <10 minutes for 5-year backtest
- **Memory Usage:** <2GB RAM
- **Result Quality:** Sharpe ratio within ±0.2 of baseline

## 📊 Performance Testing Template

```markdown
## Performance Test Results

**Test Environment:**
- OS: Windows 10 / macOS / Linux
- Python: 3.8.x
- Backtrader: 1.9.76.123

**Baseline (main branch):**
- Sharpe: 1.24
- Max DD: -8.34%
- Total Return: +53.02%
- Execution Time: 8m 23s

**After Changes:**
- Sharpe: 1.28 (+0.04) ✅
- Max DD: -8.10% (+0.24%) ✅
- Total Return: +55.43% (+2.41%) ✅
- Execution Time: 8m 31s (+8s) ⚠️

**Analysis:**
- Improved risk-adjusted returns
- Slightly reduced drawdown
- Minimal performance impact
- Changes validated ✅
```

## 🚫 What NOT to Submit

- **Over-optimized parameters** - Curve-fitted to historical data
- **Breaking changes** - Without migration guide
- **Untested code** - Code that doesn't run
- **Style violations** - Code that doesn't follow guidelines
- **Large binary files** - Images, data files >10MB
- **Sensitive data** - API keys, passwords, personal info

## 🤝 Code Review Process

1. **Automated Checks**
   - Code style validation
   - Basic functionality tests
   - Performance benchmarks

2. **Maintainer Review**
   - Code quality assessment
   - Performance impact evaluation
   - Documentation review

3. **Feedback & Iteration**
   - Address review comments
   - Make requested changes
   - Re-test after modifications

4. **Merge**
   - Approved PRs are merged
   - Contributors credited
   - Release notes updated

## 💡 Contribution Ideas

### Easy (Good First Issues)
- Fix typos in documentation
- Add code comments
- Improve error messages
- Add parameter validation

### Medium
- Add new performance metrics
- Create additional visualizations
- Optimize calculation speed
- Add unit tests

### Advanced
- Implement SHORT trading
- Add machine learning features
- Multi-timeframe analysis
- New asset classes (crypto, stocks)

## 📧 Questions?

- **Issues:** [GitHub Issues](https://github.com/yourusername/backtrader-multi-asset-strategy/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/backtrader-multi-asset-strategy/discussions)
- **Email:** your.email@domain.com

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Hexa-Asset Multi-Asset Trading System! 🎉
