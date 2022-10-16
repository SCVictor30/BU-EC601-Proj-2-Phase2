# Imports the Google Cloud client library
import os
from google.cloud import language_v1
import numpy as np

# Instantiates a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './chromatic-music-364719-f8f080adcfa5.json'
client = language_v1.LanguageServiceClient()


# The text to analyze
texts = ["Who thinks to do some shit like this", "Jalin really doing whatever he wants"]
tmp = []
for text in texts:
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment
    tmp.append(sentiment.score)
print(np.average(tmp))
    # print("Text: {}".format(text))
    # print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))