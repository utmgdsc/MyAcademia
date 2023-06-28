from textblob import TextBlob


# this is the API for the sentiment analysis

class sentimentAnalysisAPI:

    def __init__(self):
        self.text = ''

    def getSentiment(self, text):
        self.text = text
        textblob = TextBlob(self.text)
        return textblob.sentiment.polarity
