
# Social Media Sentiment Analysis

## Project Overview

This project analyzes social media posts to identify public sentiment and generate actionable insights for marketing and customer engagement strategies.

Natural Language Processing (NLP) techniques are applied to clean textual data and classify posts into **Positive, Negative, and Neutral** sentiment categories. The project also analyzes sentiment trends, platform-level behavior, frequently used terms, and engagement patterns.

## Objective

- Analyze sentiment expressed in social media posts.
- Clean and preprocess textual data for NLP analysis.
- Classify posts as Positive, Negative, or Neutral.
- Visualize sentiment distribution and trends.
- Identify frequently occurring terms using a word cloud.
- Analyze sentiment across different social media platforms.
- Examine engagement patterns associated with different sentiments.
- Generate actionable recommendations for marketing and customer engagement.

## Dataset

The dataset contains **732 social media posts** with information about text, sentiment, timestamp, platform, engagement, country, and temporal attributes.

Important attributes include:

| Attribute | Description |
|---|---|
| Text | Social media post content |
| Sentiment | Sentiment label provided in the dataset |
| Timestamp | Date and time of the post |
| Platform | Social media platform |
| Hashtags | Hashtags associated with the post |
| Retweets | Number of retweets |
| Likes | Number of likes |
| Country | Country associated with the post |
| Year | Year of the post |
| Month | Month of the post |
| Day | Day of the post |
| Hour | Hour of the post |

## Data Preprocessing

The following preprocessing steps were performed:

1. Removed unnecessary index columns.
2. Removed duplicate records.
3. Removed records with missing text.
4. Converted text to lowercase.
5. Removed URLs.
6. Removed user mentions.
7. Removed hashtag symbols while retaining hashtag words.
8. Removed special characters and numbers.
9. Removed English stop words.
10. Converted timestamps into a datetime format.

The original text was retained alongside the cleaned text for comparison and analysis.

## Sentiment Classification

**TextBlob** was used to calculate sentiment polarity for each cleaned social media post.

Polarity ranges from:

```text
-1 → Negative
 0 → Neutral
+1 → Positive
```

The polarity scores were converted into three sentiment categories:

| Polarity | Classification |
|---|---|
| Greater than 0.05 | Positive |
| Between -0.05 and 0.05 | Neutral |
| Less than -0.05 | Negative |

The resulting classification was stored in the `Predicted_Sentiment` column.

The dataset's original `Sentiment` labels were also compared with the TextBlob-generated classifications to examine their agreement.

## Exploratory Analysis

The analysis includes:

- Overall sentiment distribution
- Sentiment percentage distribution
- Sentiment trends over time
- Platform-wise sentiment
- Engagement by sentiment
- Frequently used terms
- Most positive posts
- Most negative posts

## Visualizations

### Sentiment Distribution

A bar chart shows the number of Positive, Negative, and Neutral posts.

### Sentiment Pie Chart

The pie chart represents the percentage contribution of each sentiment category.

### Sentiment Trends Over Time

Monthly sentiment trends are analyzed to identify changes in public perception over time.

### Platform-wise Sentiment

Sentiment distribution is compared across different social media platforms to identify platform-specific differences.

### Word Cloud

A word cloud highlights frequently occurring terms across the analyzed social media posts.

### Engagement Analysis

Average likes and retweets are compared across sentiment categories to understand how different types of posts perform in terms of engagement.

## Key Business Insights

The analysis can help identify:

- Overall public perception of the subject represented in the dataset.
- Periods where negative sentiment increases.
- Platforms with comparatively stronger positive or negative sentiment.
- Frequently discussed topics and terms.
- Sentiment categories receiving higher engagement.
- Posts that may require closer attention from marketing or customer-support teams.

## Marketing Recommendations

Based on the sentiment analysis framework, organizations can:

### Positive Sentiment

- Amplify positive customer experiences.
- Encourage positive user-generated content.
- Highlight successful products, services, or campaigns.
- Engage with highly positive posts to strengthen customer relationships.

### Negative Sentiment

- Identify recurring complaints and concerns.
- Respond quickly to negative feedback.
- Route serious issues to customer-support teams.
- Use frequently occurring negative terms to identify areas for improvement.

### Neutral Sentiment

- Convert neutral interactions into engagement opportunities.
- Provide useful product or service information.
- Use personalized content to encourage stronger engagement.

### Platform Strategy

Platform-specific sentiment analysis can be used to customize content, engagement strategies, and customer-support priorities for different social media channels.

## Project Structure

```text
Project-3-Social-Media-Sentiment-Analysis/
│
├── data/
│   ├── social_media_sentiments.csv
│   └── analyzed_social_media_sentiments.csv
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── visuals/
│   ├── sentiment_distribution.png
│   ├── sentiment_pie_chart.png
│   ├── sentiment_over_time.png
│   ├── sentiment_by_platform.png
│   └── wordcloud.png
│
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- TextBlob
- WordCloud
- Jupyter Notebook

## How to Run

Navigate to the project notebook directory:

```bash
cd "Level-3/Project-3-Social-Media-Sentiment-Analysis/notebooks"
```

Open the notebook:

```bash
jupyter notebook
```

Then open:

```text
sentiment_analysis.ipynb
```

Run the notebook cells sequentially to reproduce the preprocessing, sentiment classification, visualizations, and analysis.

## Output

The analyzed dataset is saved as:

```text
data/analyzed_social_media_sentiments.csv
```

The output contains the original dataset information along with additional analysis fields including:

- `Cleaned_Text`
- `Polarity`
- `Predicted_Sentiment`
- `Month_Date`
- `Total_Engagement`

## Conclusion

The project demonstrates how NLP-based sentiment analysis can be applied to social media data to understand public perception and customer behavior.

By combining sentiment classification with temporal, platform, and engagement analysis, organizations can identify emerging concerns, understand customer reactions, improve communication strategies, and make more informed marketing decisions.