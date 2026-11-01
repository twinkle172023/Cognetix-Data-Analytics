# Project 2 - Bank Customer Churn Analysis

## Objective

The objective of this project is to analyze bank customer churn data and identify the key factors associated with customers leaving the bank.

The analysis focuses on customer demographics, account characteristics, activity levels, financial attributes, and their relationship with customer churn.

## Dataset

The project uses the Bank Customer Churn dataset containing customer-level banking information.

The primary target variable is:

- `Exited` - Indicates whether the customer left the bank (`1`) or remained with the bank (`0`).

Important attributes include:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Ownership
- Active Membership
- Estimated Salary

The dataset contains 10,000 customer records and 14 columns in the commonly distributed `Churn_Modelling.csv` version. 

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
Project-2-Bank-Customer-Churn-Analysis/
│
├── data/
│   └── Churn_Modelling.csv
│
├── notebooks/
│   └── bank_customer_churn_analysis.ipynb
│
├── visuals/
│   ├── churn_distribution.png
│   ├── age_distribution.png
│   ├── balance_distribution.png
│   ├── credit_score_distribution.png
│   ├── churn_by_geography.png
│   ├── churn_by_activity.png
│   ├── churn_by_tenure.png
│   └── correlation_heatmap.png
│
└── README.md
```

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Inspected the dataset structure, data types, and statistical summary.
3. Checked for missing values.
4. Checked and removed duplicate records where applicable.
5. Examined categorical variables and their unique values.
6. Removed identifier columns that are not useful for churn analysis:
   - `RowNumber`
   - `CustomerId`
   - `Surname`
7. Verified the numerical and categorical variables before performing exploratory analysis.

## Exploratory Data Analysis

The analysis examines the relationship between customer churn and important customer attributes.

### Churn Distribution

The distribution of customers who stayed with the bank and customers who exited was analyzed to understand the overall churn pattern.

### Age Analysis

Customer age distributions were compared between retained and churned customers to determine whether age is associated with higher churn.

### Balance Analysis

Account balances were analyzed to identify differences between customers who remained with the bank and those who exited.

### Credit Score Analysis

Credit scores were examined to determine whether customers with different credit profiles show different churn behavior.

### Tenure Analysis

Customer tenure was analyzed to determine whether the length of the customer relationship influences churn.

### Activity Analysis

The relationship between active membership and churn was analyzed to determine whether inactive customers are more likely to leave.

### Geographic Analysis

Churn rates were compared across different geographical regions.

### Gender Analysis

Customer churn was compared across gender categories to identify potential differences in churn behavior.

### Product Analysis

The number of banking products held by customers was analyzed against churn.

### Credit Card Analysis

Customers with and without credit cards were compared to examine their relationship with churn.

## Correlation Analysis

A correlation matrix was created for the numerical variables.

A heatmap was used to visually analyze relationships between customer attributes and the `Exited` variable.

The analysis helps identify variables that have stronger associations with customer churn and provides a basis for further investigation.

## Visualizations

The project includes multiple visualizations, including:

- Churn distribution charts
- Age distributions
- Balance distributions
- Credit score distributions
- Churn by geography
- Churn by gender
- Churn by tenure
- Churn by active membership
- Churn by number of products
- Churn by credit card ownership
- Correlation heatmap
- Comparative boxplots

## Key Business Questions

The analysis helps answer the following questions:

1. What proportion of customers have churned?
2. Which age groups show higher churn?
3. Does customer activity influence churn?
4. How does churn vary across geographical regions?
5. Does customer tenure have a relationship with churn?
6. Are customers with different credit scores more likely to churn?
7. Does account balance differ between retained and churned customers?
8. Does the number of products held by a customer affect churn?
9. Is credit card ownership associated with customer retention?
10. Which customer attributes show the strongest relationship with churn?

## Key Insights

The exploratory analysis is used to identify customer segments with comparatively higher churn and understand the characteristics associated with customer attrition.

The analysis particularly evaluates:

- Customer age
- Account balance
- Credit score
- Tenure
- Active membership
- Geography
- Number of products
- Credit card ownership

These findings can help a bank identify customer groups that may require targeted retention strategies.

## Recommendations

Based on the observed churn patterns, banks can consider:

- Developing targeted retention campaigns for high-risk customer segments.
- Increasing engagement with inactive customers.
- Monitoring customers with unusual or unfavorable account characteristics.
- Improving customer engagement and loyalty programs.
- Using churn-related customer attributes to develop future predictive models.

## Conclusion

This project demonstrates how exploratory data analysis can be used to understand customer churn in the banking sector.

Using Pandas, Matplotlib, and Seaborn, customer characteristics were analyzed from multiple perspectives, including demographics, account behavior, financial attributes, and customer activity.

The analysis provides a foundation for identifying potential churn drivers and developing data-driven customer retention strategies. It can also serve as a starting point for building a machine learning model to predict customers who are at risk of leaving the bank.