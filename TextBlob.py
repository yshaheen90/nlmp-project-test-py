from textblob import TextBlob

text = "I love using this product!"
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)  # Output ranges from -1 (negative) to 1 (positive)
