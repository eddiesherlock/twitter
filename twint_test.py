import twint
import json

c = twint.Config()
c.Search = "neo4j OR \"graph database\" OR \"graph databases\" OR graphdb OR graphconnect OR @neoquestions OR @Neo4jDE OR @Neo4jFr OR neotechnology"
c.Store_json = True
c.Custom["user"] = ["id", "tweet", "user_id", "username", "hashtags", "mentions"]
c.User_full = True
c.Output = "tweets.json"
c.Since = "2019-05-20 16:47:01"
c.Hide_output = True

twint.run.Search(c)

