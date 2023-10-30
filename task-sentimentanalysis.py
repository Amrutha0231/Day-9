import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(sentence):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(sentence)
    compound_score = sentiment_score['compound']

    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    user_input = input("Enter a sentence: ")
    sentiment = perform_sentiment_analysis(user_input)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
