import requests, praw, config, time

url = "https://api.covid19india.org/data.json"

def fetch_data():
    data = requests.get(url)
    data = data.json()
    data = data["statewise"][0]

    data = f'''#Total cases: {data["confirmed"]}

|                |Today                          |Total|
|----------------|-----------------|---------------|
|Active|{data["deltaconfirmed"]}|{int(data["active"])}|
|Deaths|{data["deltadeaths"]}|{data["deaths"]}|
|Recovered|{data["deltarecovered"]}|{data["recovered"]}|

Source updated on: {data["lastupdatedtime"]}
>[Read more](https://github.com/parshnt/covid-19-bot)'''

    return data

def login():
    print("Logging in...")

    reddit = praw.Reddit(username = config.username,
                    password = config.password,
                    # generated after creating Reddit App
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    # user_agent is a unique string that the dev must make
                    # up to describe their bot (using this format is suggested)
                    user_agent = "covid-19 bot v1.0 by @parshnt")

    print("Logged in")
    return reddit

def reply(reddit):

    keyphrase = config.keyword
    sub = config.subredd
    subreddit = reddit.subreddit(sub)
    print("Waiting for calls...")
    for comment in subreddit.stream.comments(skip_existing=True):
        if keyphrase in comment.body:
            try:
                data = fetch_data()
                comment.reply(data)
                print('posted comment:',comment.id)
            except:
                print('too frequent')

    return 0

reddit = login()
reply(reddit)
