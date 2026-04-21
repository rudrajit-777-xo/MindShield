from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon', quiet=True)
# Initialize once
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores = analyzer.polarity_scores(text) #scores = {'neg': 0.6,'neu': 0.3,'pos': 0.1,'compound': -0.7}

   
    compound = scores['compound'] #Take the final compound score from the analysis result

    # Classification
    if compound >= 0.05:
        return "Positive", compound
    elif compound <= -0.05:
        return "Negative", compound
    else:
        return "Neutral", compound