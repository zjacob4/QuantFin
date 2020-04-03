import pytrends
from pytrends.request import TrendReq
#google_username = "<>@gmail.com"
#google_password = "<>"
#path = ""

pytrend=TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')

pytrend.build_payload(kw_list=['pizza', 'bagel'])

kw_list = ['blockchain']



current = pytrends.trending_searches(pn='united_states')

#results = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=1, year_end=2019, month_end=1, day_end=1, hour_end=1)

print(current)
#print(results)


