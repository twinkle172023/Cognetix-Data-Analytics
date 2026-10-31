# COVID-19 Data Report

## Project Overview

This project analyzes global COVID-19 case progression using historical daily case data. The analysis focuses on confirmed cases, deaths, recoveries, active cases, and daily changes to understand how the pandemic progressed over time.

The project was developed using Python and Pandas for data processing and Matplotlib and Seaborn for visualization.

## Objective

Analyze global COVID-19 data to:

- Understand daily and cumulative case progression.
- Analyze confirmed cases, deaths, and recoveries over time.
- Calculate daily changes in reported cases.
- Identify peak daily cases, deaths, and recoveries.
- Visualize overall case progression using line and bar charts.
- Apply a linear trend line to observe the overall direction of confirmed cases.

## Dataset

**Source:** Kaggle — COVID-19 Dataset  
**Dataset:** Coronavirus COVID-19 Report  
**Primary file:** `covid_19_clean_complete.csv`

The dataset contains day-to-day COVID-19 information across countries and regions, including confirmed cases, deaths, recovered cases, active cases, geographic coordinates, and WHO region information. The Kaggle dataset also provides other files containing country-level, day-wise, USA county-level, and latest COVID-19 information.

### Dataset Files

The downloaded dataset contains:

- `country_wise_latest.csv`
- `covid_19_clean_complete.csv`
- `day_wise.csv`
- `full_grouped.csv`
- `usa_county_wise.csv`
- `worldometer_data.csv`

For the main analysis, `covid_19_clean_complete.csv` was selected because it provides daily country-level case information required for the project.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset Dimensions

The selected dataset contains:

- **49,068 records**
- **10 columns**
- **188 unique dates**
- Date range: **22 January 2020 to 27 July 2020**

### Main Columns

| Column | Description |
|---|---|
| `Province/State` | Province or state information where available |
| `Country/Region` | Country or region name |
| `Lat` | Latitude |
| `Long` | Longitude |
| `Date` | Date of observation |
| `Confirmed` | Cumulative confirmed cases |
| `Deaths` | Cumulative deaths |
| `Recovered` | Cumulative recovered cases |
| `Active` | Active cases |
| `WHO Region` | WHO geographical region |

## Data Cleaning

The dataset was inspected before analysis.

### Missing Values

The only substantial missing values were found in `Province/State`.

- `Province/State`: 34,404 missing values
- `Country/Region`: 0
- `Date`: 0
- `Confirmed`: 0
- `Deaths`: 0
- `Recovered`: 0
- `Active`: 0
- `WHO Region`: 0

The missing `Province/State` values were retained because they do not affect the global case aggregation.

### Duplicate Records

No duplicate rows were identified.

```text
Duplicate rows: 0
```

### COVID-19 Metric Validation

The main COVID-19 metrics were checked for missing and negative values.

The following columns were validated:

- `Confirmed`
- `Deaths`
- `Recovered`

No missing or negative values were found in these metrics.

## Data Preparation

The `Date` column was converted to Pandas datetime format and the dataset was sorted chronologically.

To analyze global progression, country-level records were aggregated by date.

```python
daily_global = (
    df.groupby("Date")[["Confirmed", "Deaths", "Recovered", "Active"]]
      .sum()
      .reset_index()
)
```

This produced a global daily dataset containing **188 daily observations**.

## Daily Case Calculation

Since Confirmed, Deaths, and Recovered represent cumulative values, daily changes were calculated using the difference between consecutive dates.

```python
daily_global["New Cases"] = daily_global["Confirmed"].diff().fillna(0)
daily_global["New Deaths"] = daily_global["Deaths"].diff().fillna(0)
daily_global["New Recovered"] = daily_global["Recovered"].diff().fillna(0)
```

These values were used to analyze daily COVID-19 progression.

## Global Case Progression

By the final date available in the dataset, **27 July 2020**, the global totals were:

| Metric | Total |
|---|---:|
| Confirmed Cases | 16,480,485 |
| Deaths | 654,036 |
| Recovered | 9,468,087 |
| Active Cases | 6,358,362 |

These values represent the cumulative totals recorded in the dataset up to 27 July 2020.

## Trend-Line Analysis

A linear trend line was fitted to the cumulative confirmed-case data using NumPy's `polyfit()` function.

```python
slope, intercept = np.polyfit(x, y, 1)
```

The trend line provides a simplified representation of the overall direction of confirmed case progression throughout the analyzed period.

The trend-line visualization is included separately from the cumulative case chart to clearly distinguish the observed data from the fitted overall trend.

## Visualizations

The project includes the following visualizations:

### 1. Confirmed Cases Trend

Shows the cumulative global confirmed COVID-19 cases over time.

### 2. Deaths and Recoveries Trend

Compares the cumulative number of deaths and recovered cases throughout the analyzed period.

### 3. Daily New Cases

Shows the number of newly confirmed cases reported globally each day.

### 4. Daily Deaths and Recoveries

Compares daily new deaths with daily new recoveries.

### 5. Confirmed Cases with Trend Line

Shows cumulative confirmed cases together with a fitted linear trend line to illustrate the overall progression.

All visualizations are stored in the `visuals/` directory.

## Key Observations

- Global confirmed COVID-19 cases increased substantially throughout the analyzed period.
- The cumulative confirmed-case curve shows a strong upward progression.
- Daily case counts increased considerably compared with the early period of the dataset.
- Recoveries increased continuously as the number of confirmed cases grew.
- Deaths also increased over the analyzed period, although at a lower magnitude than confirmed cases.
- The trend-line analysis confirms an overall upward direction in confirmed cases.

## Project Structure

```text
Project-3-COVID-19-Data-Report/
│
├── data/
│   ├── country_wise_latest.csv
│   ├── covid_19_clean_complete.csv
│   ├── day_wise.csv
│   ├── full_grouped.csv
│   ├── usa_county_wise.csv
│   ├── worldometer_data.csv
│   └── global_daily_covid_analysis.csv
│
├── notebooks/
│   └── covid19_data_analysis.ipynb
│
├── visuals/
│   ├── confirmed_cases_trend.png
│   ├── confirmed_cases_trend_line.png
│   ├── daily_new_cases.png
│   ├── daily_deaths_recoveries.png
│   └── deaths_recoveries_trend.png
│
└── README.md
```

## Conclusion

This project demonstrates a complete data-analysis workflow for historical COVID-19 data, including dataset inspection, validation, cleaning, aggregation, daily metric calculation, trend analysis, and visualization.

The analysis provides a clear view of global COVID-19 case progression between January and July 2020 and demonstrates how Pandas and Python visualization libraries can be used to transform raw epidemiological data into meaningful insights.

## Future Improvements

The project can be extended by:

- Adding an interactive Plotly dashboard.
- Allowing users to filter by country.
- Adding date-range filtering.
- Comparing COVID-19 progression between selected countries.
- Adding regional analysis using WHO regions.
- Adding additional statistical or forecasting models.

## Data Source

Kaggle — COVID-19 Dataset by Devakumar K. P.

The dataset documentation identifies the underlying sources as the Johns Hopkins University CSSE COVID-19 repository and Worldometer data.