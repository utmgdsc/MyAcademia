from transformers import AutoTokenizer
from transformers import TFAutoModelForSequenceClassification
import tensorflow as tf
from textblob import TextBlob

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)

class SentimentAnalysis:
    def __init__(self, text):
        self.text = text

    """
    This function will use the vader model to analyze the sentiment of the text
    This is more of a basic or naive approach to sentiment analysis as it 
    checks for the polarity of each word in the text and then gives the
    sentiment of the text based on average of the polarity of each word.
    """
    def vaderModel(self):
        textblob = TextBlob(self.text)
        return textblob.sentiment.polarity

    def roBERTaModel(self):
        encoded_text = tokenizer(self.text, return_tensors='tf')
        output = model(**encoded_text)
        scores = output[0][0].numpy()
        scores = tf.nn.softmax(scores)
        scores_dict = {
            'roberta_neg' : scores[0].numpy(),
            'roberta_neu' : scores[1].numpy(),
            'roberta_pos' : scores[2].numpy()
        }
        return scores_dict

    def roBERTaModelResult(self):
        result = self.roBERTaModel()
        return result['roberta_neg'] * -1 + result['roberta_neu'] * 0 + result['roberta_pos'] * 1

sea = SentimentAnalysis("you are very very very very bad")
print(sea.roBERTaModelResult())
print(sea.vaderModel())
