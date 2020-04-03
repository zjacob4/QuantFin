import ffn


data = ffn.get('msft,aapl,spy,mdt,jnj,syk,gild,lvmuy,tif', start='2014-01-01', end='2018-01-01')
print(data.head())

returns = data.to_log_returns().dropna()
print(returns.head())


#ax = returns.hist(figsize=(12,5))
#ax.plot()

cor = returns.corr().as_format('.2f')
#print(cor)


cor_heat = returns.plot_corr_heatmap()
cor_heat.savefig("heatgraph2.png")

perf =data.calc_stats()
print(perf.display())

clust = ffn.core.calc_ftca(returns,threshold=0.5)
print(clust)
