import openai

# OpenAI APIキーを設定
openai.api_key = ""


def generate_tweet_based_on_previous_tweets():
    # tweets.txtを読み込む
    with open("tweets.txt", "r", encoding="utf-8") as file:
        tweets = file.readlines()

    # ツイートの内容を文字列として連結
    previous_tweets = "\n".join(tweets)  # 最新の5ツイートを利用する（適宜変更）

    # 新しいインターフェースを使用してリクエストを送る
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # 使いたいモデルを指定（例えば gpt-4 や gpt-3.5-turbo など）
        prompt=f"以下のツイートを元に新しいツイートを作成してください:\n{previous_tweets}",
        max_tokens=100  # 生成するトークンの最大数を指定
    )

    # 生成されたツイートのテキストを返す
    return response.choices[0].text.strip()

# ツイートを生成して表示
new_tweet = generate_tweet_based_on_previous_tweets()
print(new_tweet)