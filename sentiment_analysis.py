# Required libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import warnings

# Suppress specific spaCy similarity warning
warnings.filterwarnings("ignore", message=r".*\[W007\].*", category=UserWarning)

# Load the dataset
dataframe = pd.read_csv(
    'amazon_product_reviews.csv',
    dtype={1: 'object', 10: 'object'}
)

# Preprocess the data
def preprocess_data(data):
    """Remove missing values and stop words from the dataset."""
    clean_data = data.dropna(subset=['reviews.text'])
    nlp = spacy.load('en_core_web_sm')
    clean_data.loc[:, 'reviews.text'] = clean_data['reviews.text'].apply(lambda x: " ".join([word.text for word in nlp(x) if not word.is_stop]))
    return clean_data

clean_data = preprocess_data(dataframe)

# Load spaCy model and add TextBlob component for sentiment analysis
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def analyze_sentiment(review_text):
    """Analyze sentiment of the given review text and return sentiment label."""
    doc = nlp(review_text)
    polarity = doc._.blob.polarity
    if polarity > 0:
        return 'Positive'
    if polarity < 0:
        return 'Negative'
    return 'Neutral'

# Compare the similarity of two product reviews
def compare_similarity(review_text1, review_text2):
    """Calculate and return the similarity score between two review texts."""
    doc1 = nlp(review_text1)
    doc2 = nlp(review_text2)
    return doc1.similarity(doc2)

# Top-level code
sample_reviews = clean_data['reviews.text'][:5]
results = [analyze_sentiment(review) for review in sample_reviews]

for review, sentiment in zip(sample_reviews, results):
    print(f"\nReview: {review}\nSentiment: {sentiment}\n")

review1 = clean_data['reviews.text'].iloc[0]
review2 = clean_data['reviews.text'].iloc[1]

similarity_score = compare_similarity(review1, review2)
print(f"\nSimilarity score between two reviews: {similarity_score}")

print("\nThank you!\n")
