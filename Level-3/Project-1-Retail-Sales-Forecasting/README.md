# Retail Sales Forecasting

## Project Overview

This project focuses on analyzing historical retail sales data to identify sales trends, seasonal patterns, peak demand periods, and store-level performance. A basic time series forecasting approach is then used to predict future weekly sales and generate inventory planning recommendations.

The project uses the Walmart retail sales dataset containing weekly sales information along with store characteristics and external factors such as holidays, temperature, fuel prices, markdowns, CPI, and unemployment.

---

## Objective

The main objectives of this project are to:

- Analyze historical retail sales trends.
- Identify seasonal patterns and peak sales periods.
- Compare sales performance across stores and departments.
- Examine the relationship between holidays and sales.
- Build a basic time series forecasting model.
- Compare Moving Average and ARIMA forecasting approaches.
- Forecast sales for the next 12 weeks.
- Provide inventory and restocking recommendations based on forecasted demand.

---

## Dataset

The project uses three related datasets:

### 1. Sales Dataset

Contains weekly sales information for individual stores and departments.

Important columns include:

- `Store`
- `Dept`
- `Date`
- `Weekly_Sales`
- `IsHoliday`

### 2. Stores Dataset

Contains information about individual stores.

Important columns include:

- `Store`
- `Type`
- `Size`

### 3. Features Dataset

Contains additional external factors associated with stores and dates.

Important columns include:

- `Store`
- `Date`
- `Temperature`
- `Fuel_Price`
- `MarkDown1` to `MarkDown5`
- `CPI`
- `Unemployment`
- `IsHoliday`

---

## Project Workflow

```text
Raw Retail Datasets
        |
        v
Data Loading
        |
        v
Data Cleaning
        |
        v
Dataset Merging
        |
        v
Feature Engineering
        |
        v
Exploratory Data Analysis
        |
        +----------------------+
        |                      |
        v                      v
Trend & Seasonality       Store & Department
Analysis                  Analysis
        |                      |
        +----------+-----------+
                   |
                   v
              Time Series
               Preparation
                   |
                   v
          Train / Test Split
                   |
          +--------+--------+
          |                 |
          v                 v
    Moving Average       ARIMA
          |                 |
          +--------+--------+
                   |
                   v
             Model Evaluation
                   |
                   v
          12-Week Forecast
                   |
                   v
       Inventory Recommendations
```

---

## Data Preprocessing

The following preprocessing steps were performed:

- Loaded all three CSV datasets using Pandas.
- Converted the `Date` columns into datetime format.
- Checked and removed duplicate records.
- Merged the sales, store, and feature datasets using `Store` and `Date`.
- Replaced missing markdown values with zero.
- Created additional time-based features:
  - Year
  - Month
  - Month Name
  - Week
- Created an aggregated weekly sales time series for forecasting.
- Saved the cleaned and merged dataset as `merged_retail_sales.csv`.

---

## Exploratory Data Analysis

The analysis examined several aspects of retail sales performance.

### Weekly Sales Trend

Overall weekly sales were aggregated across all stores and departments to understand long-term sales movement and identify major fluctuations.

### Monthly Sales Analysis

Sales were aggregated by year and month to identify changes in monthly demand and recurring seasonal patterns.

### Seasonality

Average sales were calculated for each calendar month to identify months associated with relatively higher or lower demand.

### Holiday Analysis

Sales during holiday and non-holiday weeks were compared to determine whether holidays influenced overall demand.

### Store Performance

Total sales were calculated for each store to identify the highest-performing stores.

### Department Performance

Department-level sales were analyzed to identify departments contributing the most to total revenue.

### Peak Sales Weeks

The highest-selling weeks were identified to highlight periods requiring additional inventory planning.

---

## Forecasting Methodology

The aggregated weekly sales series was divided into:

- **Training data:** Historical observations excluding the final 12 weeks.
- **Testing data:** Final 12 weeks used for evaluating forecasting performance.

Two basic forecasting approaches were evaluated.

### Moving Average

A 4-week moving average was used as a baseline forecasting method.

The forecast uses the recent average sales level to estimate upcoming demand.

### ARIMA

An ARIMA `(1,1,1)` model was trained on the historical weekly sales series.

The model was evaluated against the final 12 weeks of actual sales using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The model comparison is available in the notebook through the `model_comparison` DataFrame.

---

## Forecasting Results

The forecasting stage compares the Moving Average and ARIMA models using their prediction errors.

The model with the lower evaluation error was selected as the preferred forecasting approach for the final 12-week forecast.

The selected model was then retrained using the complete historical time series and used to generate forecasts for the next 12 weeks.

The resulting forecast is stored in:

```text
data/future_sales_forecast.csv
```

---

## Demand Classification

Forecasted weekly sales were compared with the historical average weekly sales.

Demand was classified using the following thresholds:

| Condition | Demand Level |
|---|---|
| Forecast > 110% of historical average | High Demand |
| Forecast < 90% of historical average | Low Demand |
| Otherwise | Normal Demand |

This classification provides a simple framework for translating the forecast into inventory decisions.

---

## Inventory Recommendations

Based on the forecasted demand level:

### High Demand

- Increase inventory levels.
- Replenish stock earlier.
- Prepare for increased customer demand.
- Prioritize frequently sold products.

### Normal Demand

- Maintain normal inventory levels.
- Follow regular replenishment schedules.
- Monitor changes in upcoming forecasts.

### Low Demand

- Avoid excessive inventory accumulation.
- Maintain lower stock levels where appropriate.
- Reduce the risk of overstocking and unnecessary holding costs.

---

## Visualizations

The project generates the following visualizations:

- Weekly sales trend
- Monthly sales trend
- Monthly seasonality
- Holiday vs non-holiday sales
- Top-performing stores
- Top-performing departments
- Peak sales weeks
- Actual vs predicted sales
- Future 12-week sales forecast

All visualizations are stored in the `visuals/` directory.

---

## Project Structure

```text
Project-1-Retail-Sales-Forecasting/
│
├── data/
│   ├── sales data-set.csv
│   ├── stores data-set.csv
│   ├── Features data set.csv
│   ├── merged_retail_sales.csv
│   └── future_sales_forecast.csv
│
├── notebooks/
│   └── retail_sales_forecasting.ipynb
│
├── visuals/
│   ├── weekly_sales_trend.png
│   ├── monthly_sales_trend.png
│   ├── seasonality.png
│   ├── holiday_sales.png
│   ├── top_stores.png
│   ├── top_departments.png
│   ├── peak_sales_weeks.png
│   ├── actual_vs_predicted.png
│   └── future_sales_forecast.png
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Scikit-learn
- Jupyter Notebook

### Key Techniques

- Data Cleaning
- Data Integration
- Exploratory Data Analysis
- Time Series Analysis
- Moving Average Forecasting
- ARIMA Forecasting
- Model Evaluation
- Demand Classification
- Inventory Planning

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/twinkle172023/Cognetix-Data-Analytics.git
```

### 2. Navigate to the project

```bash
cd Cognetix-Data-Analytics/Level-3/Project-1-Retail-Sales-Forecasting
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/retail_sales_forecasting.ipynb
```

Run the notebook cells sequentially.

---

## Output Files

The project produces two important processed datasets:

**`merged_retail_sales.csv`**

Contains the cleaned and integrated retail sales dataset.

**`future_sales_forecast.csv`**

Contains the 12-week sales forecast together with demand classification.

---

## Conclusion

This project demonstrates how historical retail sales data can be transformed into actionable demand insights using Python and basic time series forecasting.

The analysis identifies sales trends, seasonal behavior, high-performing stores and departments, and peak demand periods. Moving Average and ARIMA models provide a comparison between a simple baseline forecasting technique and a statistical time series model.

The final forecast can support inventory planning by identifying periods of expected high, normal, or low demand, helping businesses plan replenishment and reduce the risk of both stockouts and overstocking.