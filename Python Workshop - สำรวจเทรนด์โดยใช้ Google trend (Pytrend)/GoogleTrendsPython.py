from pytrends import pytrends
trends=pytrends()
keywords=["bnk48","เลขเด็ด"]
titles=["Interest over time","Related queries"]
for title in titles:
    print(trends.download_report(keywords,title,time="all"))
