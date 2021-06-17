from pytrends.request import TrendReq
import matplotlib.pyplot as plt
pytrend=TrendReq()
kw_list=['เลขเด็ด','หวย']
pytrend.build_payload(kw_list,cat='16',geo='TH',timeframe='now 7-d')
dic=pytrend.related_queries()

for x in dic:
    print("-----------------")
    for y in dic[x]:
        print(y,':',dic[x][y])
