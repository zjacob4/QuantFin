import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = 'XxAWyRFPJcRKxDhyJm-V'


cons_sent_ind = quandl.get("UMICH/SOC1")

print(cons_sent_ind)


plt.plot(cons_sent_ind)
plt.xlabel('Date')
plt.ylabel('CSI')
plt.title('UMichigan Consumer Sentiment Index')
plt.savefig('CSI_plot.png')


inv_sent = quandl.get("AAII/AAII_SENTIMENT", authtoken="XxAWyRFPJcRKxDhyJm-V")

print(inv_sent)

plt.plot(inv_sent)
plt.xlabel('Date')
plt.ylabel('Investor Sentiment')
plt.title('Investor Sentiment Time Series')
#plt.legend()
plt.savefig('aaii_plot.png')

