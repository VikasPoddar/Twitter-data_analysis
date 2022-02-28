import twint
import time 
import datetime

filename = "twitter_dataset_"
# library used - twint 

# fileformat - twitter_dataset_year_month_day_hour_minute
while(True):
    try:
        # set of keyword used for collecting the tweets
        keywords = ['russia','war', 'Ukraine', 'worldwar3', 'warandeconomy', 'worldeconomy', 'stockmarket', 'bsc', 'nsc','oilprices', 'decliningeconomy','indianukraine', 'UkraineRussie','Russia','Ukrainecrisis','kyiv','wareconomy','fallineconomy']
        join_keywords = ' OR '.join(keywords)
        c = twint.Config()
        c.Search = join_keywords 
        c.Limit = 20000000 # current limit on tweet
        c.Store_csv = True
        now = datetime.datetime.now()
        now_time= str(now.year)+""+str(now.month)+""+str(now.day)+""+str(now.hour)+""+str(now.minute)
        c.Output = filename +now_time+".csv"
        c.Lang = "en"
        twint.run.Search(c)
    except Exception as e:
        pass
