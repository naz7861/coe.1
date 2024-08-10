import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace these with your Azure Text Analytics endpoint and API key
endpoint = "YOUR_ENDPOINT_HERE"
api_key = "YOUR_API_KEY_HERE"

def authenticate_client():
    credential = AzureKeyCredential(api_key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return client

def sentiment_analysis(client, reviews):
    response = client.analyze_sentiment(documents=reviews)
    return response

def main():
    client = authenticate_client()
    
    reviews = [
        "I absolutely loved this movie! It was fantastic and had a great storyline.",
        "The movie was okay, but the ending was quite predictable.",
        "I didn't enjoy the movie at all. It was boring and too long."
    ]
    
    response = sentiment_analysis(client, reviews)
    
    for i, doc in enumerate(response):
        print(f"Review: {reviews[i]}")
        print(f"Sentiment: {doc.sentiment}")
        print(f"Positive Score: {doc.confidence_scores.positive:.2f}")
        print(f"Neutral Score: {doc.confidence_scores.neutral:.2f}")
        print(f"Negative Score: {doc.confidence_scores.negative:.2f}")
        print()

if __name__ == "__main__":
    main()
