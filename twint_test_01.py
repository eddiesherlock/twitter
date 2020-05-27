import twint

# Configure
# c = twint.Config()
# c.Username = "realDonaldTrump"
# c.Search = "fruit"
#
# # Run
# twint.run.Search(c)

# c = twint.Config()

# c.Username = "realDonaldTrump" ## Twitter screen_name
# c.Custom["tweet"] = ["id"]
# c.Custom["user"] = ["bio"]
# c.Limit = 10
# c.Store_csv = True
# c.Output = "none"
#
# twint.run.Search(c)

c = twint.Config()

c.Search = "data science" ## 關鍵字搜尋
# Custom output format
c.Format = "Username: {username} |  Tweet: {tweet}" ##格式化Pandas
c.Limit = 1
c.Pandas = True

twint.run.Search(c)