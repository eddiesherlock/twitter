import twint
import sys

c = twint.Config()
c.Search = "cancer AND covid-19"
c.Store_csv = True
c.User_full = True
c.Output = "tweets_cancer_intermediate.csv"
c.Resume = 'tweets_cancer_resume_intermediate.csv'
c.Since = "2020-02-23 00:00:00"
c.Lang = 'en'
c.Hide_output = True
c.Debug = True

try:
    twint.run.Search(c)
except Exception as e:
    print(e)

print("end of the program")
sys.exit()