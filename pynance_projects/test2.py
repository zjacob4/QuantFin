import pynance as pn

ge = pn.data.get('ge','1962','2015')

print(ge)

#pn.chart.adj_close(ge, title='GE', fname = 'GE.png')

int_test = pn.interest.loanpayment(3000,rate=0.07,npmts=48)
print(int_test)
