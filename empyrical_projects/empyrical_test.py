import numpy as np
from empyrical import max_drawdown, alpha_beta
import ffn


data = ffn.get('BA,CCL,UAL,LVMUY,KO,SFTBY,SBUX,BRK-B,AAPL,GOLD', start='2000-01-01', end='2020-01-01')
print(data.head())

data2 = ffn.get('BA',start='2000-01-01', end='2020-01-01')
returns2 = data2.to_log_returns().dropna()

returns = data.to_log_returns().dropna()
print(returns.head())

bench_data = ffn.get('SPY', start='2000-01-01', end='2020-01-01')

bench_returns = bench_data.to_log_returns().dropna()


maxdraw = max_drawdown(returns)
print('max')
print(maxdraw)


alpha, beta = alpha_beta(returns2,bench_returns)
print('alpha')
print(alpha)
print('beta')
print(beta)
