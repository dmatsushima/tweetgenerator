import tweepy

# APIキーとトークンを設定
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

client = tweepy.Client(bearer_token="")

user = client.get_user(username="")
user_id = user.data.id

# V2 APIを使ってツイートを取得
tweets = client.get_users_tweets(id=user_id, max_results=75)

# ツイートを保存
with open("tweets.txt", "w", encoding="utf-8") as f:
    for tweet in tweets.data:
        f.write(tweet.text + "\n")