# sentiment
Capstone Project - Data Science Bootcamp.
This Python script serves as a comprehensive tool for sentiment analysis and similarity comparison of Amazon product reviews. Here's a detailed breakdown of its functionality:

Libraries and Data Loading:

The script imports necessary libraries such as Pandas for data manipulation and spaCy for natural language processing (NLP).
It loads a dataset containing Amazon product reviews from a CSV file using Pandas.
Data Preprocessing:

Missing values in the 'reviews.text' column are removed to ensure data cleanliness.
Stop words are eliminated from each review text using spaCy's English language model to focus on meaningful content.
Sentiment Analysis:

The script utilizes spaCy's TextBlob component for sentiment analysis, which assigns a polarity score to each review indicating its sentiment (positive, negative, or neutral).
A function 'analyze_sentiment' is defined to analyze the sentiment of a given review text and return the corresponding sentiment label.
Similarity Comparison:

Another function 'compare_similarity' is created to calculate the similarity score between two review texts using spaCy's similarity feature.
This score indicates how closely related two reviews are in terms of content.
User Interaction:

The script presents a sample of review texts to the user along with their sentiment analysis results.
It then computes and displays the similarity score between the first two reviews in the dataset.
Error Handling:

The script suppresses specific warning messages related to spaCy similarity to enhance user experience.
Error handling mechanisms are in place to guide users in case of invalid inputs or unexpected issues during execution.
Overall, this script demonstrates proficiency in data preprocessing, sentiment analysis, and similarity comparison, making it a valuable tool for extracting insights from Amazon product reviews and understanding customer sentiments effectively.
