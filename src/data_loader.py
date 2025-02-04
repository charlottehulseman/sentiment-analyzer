import gzip
import json
import pandas as pd

def load_data(file_path):
    data = []
    with gzip.open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df[['reviewText', 'overall']]  # Select relevant columns

def preprocess_data(df):
    # Map ratings to sentiments: 1-2 → Negative, 3 → Neutral, 4-5 → Positive
    def map_sentiment(rating):
        if rating <= 2:
            return 'negative'
        elif rating == 3:
            return 'neutral'
        else:
            return 'positive'

    df['sentiment'] = df['overall'].apply(map_sentiment)
    return df[['reviewText', 'sentiment']]