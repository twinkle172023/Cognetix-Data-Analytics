# Customer Segmentation using K-Means Clustering

## Project Overview

This project performs customer segmentation using **K-Means clustering** to identify groups of customers with similar purchasing patterns and behaviors. The segmentation can support data-driven marketing, personalized campaigns, customer retention, and targeted promotional strategies.

The analysis uses customer demographic, purchasing, engagement, and promotional behavior to create meaningful customer segments.

## Objective

- Clean and preprocess customer data.
- Engineer meaningful customer behavior features.
- Normalize numerical features for clustering.
- Identify distinct customer groups using K-Means clustering.
- Analyze the characteristics of each segment.
- Develop marketing recommendations for each customer group.

## Dataset

The dataset contains customer demographic and marketing behavior information, including:

- Income
- Recency
- Product spending
- Purchase channels
- Deal purchases
- Website visits
- Campaign responses
- Household information

The dataset was cleaned before clustering by removing duplicate records and handling missing values.

## Feature Engineering

Two additional behavioral features were created:

### Total Spending

Total amount spent across:

- Wines
- Fruits
- Meat products
- Fish products
- Sweet products
- Gold products

### Total Purchases

Total purchases made through:

- Web
- Catalog
- Store

## Clustering Features

The following features were selected for customer segmentation:

| Feature | Description |
|---|---|
| Income | Customer income |
| Recency | Number of days since the customer's last purchase |
| Total_Spending | Total customer spending across products |
| NumDealsPurchases | Purchases made using deals |
| Total_Purchases | Total purchases across available channels |
| NumWebVisitsMonth | Monthly website visits |

Campaign response variables were not used as clustering features because the objective was to segment customers based on their existing behavior.

## Data Preprocessing

The following preprocessing steps were performed:

1. Removed duplicate records.
2. Removed records containing missing values.
3. Created behavioral features.
4. Selected relevant numerical attributes.
5. Applied `StandardScaler` to normalize the features.
6. Evaluated different cluster counts using clustering diagnostics.
7. Selected **4 clusters** for the final business segmentation.

## Exploratory Data Analysis

EDA was performed to understand the distribution and relationships between customer attributes.

The analysis included:

- Feature distribution analysis
- Correlation heatmap
- Spending and purchase behavior
- Customer engagement patterns
- Cluster distribution

## K-Means Clustering

K-Means clustering was used to divide customers into four groups.

```python
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

cluster_labels = kmeans.fit_predict(X_scaled)
```

The **Elbow Method** and **Silhouette Analysis** were used to evaluate candidate cluster counts before finalizing the segmentation.

## Customer Segments

The final clustering produced four customer segments containing **2,216 customers**.

| Segment | Income | Recency | Total Spending | Deal Purchases | Total Purchases | Web Visits | Customers |
|---|---:|---:|---:|---:|---:|---:|---:|
| Loyal Customers | 34,816.19 | 24.03 | 120.60 | 1.93 | 6.37 | 6.50 | 562 |
| Discount Seekers | 53,800.62 | 48.24 | 705.82 | 5.72 | 16.54 | 6.85 | 330 |
| Low Engagement Users | 36,728.22 | 75.35 | 132.54 | 1.94 | 6.67 | 6.22 | 535 |
| High Spenders | 74,536.64 | 49.27 | 1,234.06 | 1.45 | 19.29 | 3.22 | 789 |

### 1. Loyal Customers

These customers show the **most recent purchasing activity**, with an average recency of approximately 24 days. Their spending and purchase frequency are relatively moderate.

**Recommended strategy:**
- Introduce loyalty programs.
- Provide repeat-purchase incentives.
- Use personalized product recommendations.
- Encourage gradual increases in basket value.

### 2. Discount Seekers

This segment has relatively high purchasing activity and the **highest deal usage**, making promotional offers an important part of their purchasing behavior.

**Recommended strategy:**
- Provide targeted coupons.
- Create promotional bundles.
- Run seasonal discount campaigns.
- Use offers while maintaining acceptable profit margins.

### 3. Low Engagement Users

These customers have the **highest recency value**, indicating that they have not purchased recently. Their spending and purchase frequency are also relatively low.

**Recommended strategy:**
- Launch re-engagement campaigns.
- Send personalized reminders.
- Provide targeted promotional offers.
- Recommend products based on previous purchases.

### 4. High Spenders

This segment has the **highest income, spending, and purchase frequency**. They also have relatively low website visits, suggesting that their strong purchasing behavior does not depend heavily on frequent website visits.

**Recommended strategy:**
- Offer premium products and services.
- Create VIP loyalty benefits.
- Provide personalized recommendations.
- Introduce exclusive rewards and experiences.

## Visualizations

The project generates the following visualizations:

- Feature distributions
- Correlation heatmap
- Elbow curve
- Cluster scatter plot
- Cluster heatmap
- Cluster distribution
- Customer segment visualization

These visualizations help identify differences between customer groups and interpret the resulting clusters.

## Project Structure

```text
Project-2-Customer-Segmentation/
│
├── data/
│   ├── customer_data.csv
│   └── customer_segments.csv
│
├── notebooks/
│   └── customer_segmentation.ipynb
│
├── visuals/
│   ├── feature_distributions.png
│   ├── correlation_heatmap.png
│   ├── elbow_curve.png
│   ├── cluster_scatter.png
│   ├── cluster_heatmap.png
│   ├── cluster_distribution.png
│   └── customer_segments.png
│
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## How to Run

Navigate to the project notebook directory and open:

```text
notebooks/customer_segmentation.ipynb
```

Run the notebook cells sequentially to reproduce the preprocessing, clustering analysis, visualizations, and customer segmentation results.

## Output

The final segmented customer dataset is saved as:

```text
data/customer_segments.csv
```

The file contains the original customer information along with:

- Cluster assignment
- Customer segment
- Total spending
- Total purchases

## Conclusion

K-Means clustering successfully identified four distinct customer segments based on purchasing behavior, spending, engagement, and promotional activity.

The segmentation provides a practical foundation for targeted marketing strategies. High-value customers can receive premium experiences, discount-driven customers can be targeted with controlled promotions, loyal customers can be encouraged through retention programs, and low-engagement customers can be targeted through reactivation campaigns.