from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
      """
      Analyze review sentiment:
      Positive / Negative / Neutral
      """

      sentiment_score = sia.polarity_scores(text)

      compound = sentiment_score["compound"]

      if compound >= 0.05:
            return {
                  "label": "Positive",
                  "score": compound,
                  "color": "success"
            }

      elif compound <= -0.05:
            return {
                  "label": "Negative",
                  "score": compound,
                  "color": "danger"
            }

      else:
            return {
                  "label": "Neutral",
                  "score": compound,
                  "color": "secondary"
            }