import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = "../data/US_Superstore_data.xls"

df = pd.read_excel(
    DATA_PATH,
    engine="xlrd"
)

# ============================================================
# DATA PREPROCESSING
# ============================================================

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

df = df.dropna(subset=["Order Date", "Sales", "Profit"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)


# ============================================================
# DASH APP
# ============================================================

app = Dash(__name__)

app.title = "US Superstore Sales Dashboard"


# ============================================================
# STYLING
# ============================================================

PAGE_STYLE = {
    "fontFamily": "Arial, sans-serif",
    "backgroundColor": "#f5f6f8",
    "padding": "25px",
}

CARD_STYLE = {
    "backgroundColor": "white",
    "padding": "20px",
    "borderRadius": "6px",
    "boxShadow": "0 1px 4px rgba(0,0,0,0.12)",
    "textAlign": "center",
}

FILTER_STYLE = {
    "backgroundColor": "white",
    "padding": "15px",
    "borderRadius": "6px",
    "boxShadow": "0 1px 4px rgba(0,0,0,0.10)",
}


# ============================================================
# LAYOUT
# ============================================================

app.layout = html.Div(
    style=PAGE_STYLE,
    children=[

        # TITLE
        html.Div(
            [
                html.H1(
                    "US Superstore Sales Dashboard",
                    style={
                        "marginBottom": "5px",
                        "fontSize": "30px"
                    }
                ),

                html.P(
                    "Interactive analysis of sales, profit and order performance",
                    style={
                        "color": "#666",
                        "fontSize": "15px"
                    }
                ),
            ]
        ),

        # ====================================================
        # FILTERS
        # ====================================================

        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "Region",
                            style={"fontWeight": "bold"}
                        ),

                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {
                                    "label": region,
                                    "value": region
                                }
                                for region in sorted(df["Region"].dropna().unique())
                            ],
                            value=list(
                                sorted(df["Region"].dropna().unique())
                            ),
                            multi=True,
                            placeholder="Select Region"
                        ),
                    ],
                    style={"width": "30%"}
                ),

                html.Div(
                    [
                        html.Label(
                            "Category",
                            style={"fontWeight": "bold"}
                        ),

                        dcc.Dropdown(
                            id="category-filter",
                            options=[
                                {
                                    "label": category,
                                    "value": category
                                }
                                for category in sorted(
                                    df["Category"].dropna().unique()
                                )
                            ],
                            value=list(
                                sorted(df["Category"].dropna().unique())
                            ),
                            multi=True,
                            placeholder="Select Category"
                        ),
                    ],
                    style={"width": "30%"}
                ),

                html.Div(
                    [
                        html.Label(
                            "Time Period",
                            style={"fontWeight": "bold"}
                        ),

                        dcc.DatePickerRange(
                            id="date-filter",
                            min_date_allowed=df["Order Date"].min(),
                            max_date_allowed=df["Order Date"].max(),
                            start_date=df["Order Date"].min(),
                            end_date=df["Order Date"].max(),
                            display_format="DD-MM-YYYY"
                        ),
                    ],
                    style={"width": "35%"}
                ),

            ],
            style={
                "display": "flex",
                "gap": "20px",
                "alignItems": "end",
                "marginBottom": "25px",
            }
        ),

        # ====================================================
        # KPI CARDS
        # ====================================================

        html.Div(
            [
                html.Div(
                    [
                        html.H4("Total Sales"),
                        html.H2(id="total-sales")
                    ],
                    style={
                        **CARD_STYLE,
                        "width": "23%"
                    }
                ),

                html.Div(
                    [
                        html.H4("Total Profit"),
                        html.H2(id="total-profit")
                    ],
                    style={
                        **CARD_STYLE,
                        "width": "23%"
                    }
                ),

                html.Div(
                    [
                        html.H4("Total Orders"),
                        html.H2(id="total-orders")
                    ],
                    style={
                        **CARD_STYLE,
                        "width": "23%"
                    }
                ),

                html.Div(
                    [
                        html.H4("Profit Margin"),
                        html.H2(id="profit-margin")
                    ],
                    style={
                        **CARD_STYLE,
                        "width": "23%"
                    }
                ),
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "marginBottom": "25px"
            }
        ),

        # ====================================================
        # CHART ROW 1
        # ====================================================

        html.Div(
            [
                html.Div(
                    dcc.Graph(id="region-chart"),
                    style={
                        "width": "50%",
                        "backgroundColor": "white"
                    }
                ),

                html.Div(
                    dcc.Graph(id="category-chart"),
                    style={
                        "width": "50%",
                        "backgroundColor": "white"
                    }
                ),
            ],
            style={
                "display": "flex",
                "gap": "20px",
                "marginBottom": "25px"
            }
        ),

        # ====================================================
        # MONTHLY SALES
        # ====================================================

        html.Div(
            dcc.Graph(id="monthly-sales-chart"),
            style={
                "backgroundColor": "white",
                "marginBottom": "25px"
            }
        ),

        # ====================================================
        # TOP PRODUCTS
        # ====================================================

        html.Div(
            dcc.Graph(id="top-products-chart"),
            style={
                "backgroundColor": "white"
            }
        ),
    ]
)


# ============================================================
# CALLBACK
# ============================================================

@app.callback(
    [
        Output("total-sales", "children"),
        Output("total-profit", "children"),
        Output("total-orders", "children"),
        Output("profit-margin", "children"),
        Output("region-chart", "figure"),
        Output("category-chart", "figure"),
        Output("monthly-sales-chart", "figure"),
        Output("top-products-chart", "figure"),
    ],
    [
        Input("region-filter", "value"),
        Input("category-filter", "value"),
        Input("date-filter", "start_date"),
        Input("date-filter", "end_date"),
    ]
)
def update_dashboard(
    selected_regions,
    selected_categories,
    start_date,
    end_date
):

    filtered_df = df.copy()

    # Region filter
    if selected_regions:
        filtered_df = filtered_df[
            filtered_df["Region"].isin(selected_regions)
        ]

    # Category filter
    if selected_categories:
        filtered_df = filtered_df[
            filtered_df["Category"].isin(selected_categories)
        ]

    # Date filter
    if start_date:
        filtered_df = filtered_df[
            filtered_df["Order Date"] >= pd.to_datetime(start_date)
        ]

    if end_date:
        filtered_df = filtered_df[
            filtered_df["Order Date"] <= pd.to_datetime(end_date)
        ]

    # ========================================================
    # KPI CALCULATIONS
    # ========================================================

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_orders = filtered_df["Order ID"].nunique()

    if total_sales != 0:
        profit_margin = (total_profit / total_sales) * 100
    else:
        profit_margin = 0

    # ========================================================
    # REGION SALES
    # ========================================================

    region_data = (
        filtered_df
        .groupby("Region", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    region_fig = px.bar(
        region_data,
        x="Region",
        y="Sales",
        title="Revenue by Region",
        text_auto=".2s"
    )

    region_fig.update_layout(
        margin=dict(l=40, r=20, t=60, b=40)
    )

    # ========================================================
    # CATEGORY SALES
    # ========================================================

    category_data = (
        filtered_df
        .groupby("Category", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    category_fig = px.bar(
        category_data,
        x="Category",
        y="Sales",
        title="Revenue by Product Category",
        text_auto=".2s"
    )

    category_fig.update_layout(
        margin=dict(l=40, r=20, t=60, b=40)
    )

    # ========================================================
    # MONTHLY SALES
    # ========================================================

    monthly_data = (
        filtered_df
        .groupby("Year-Month", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Year-Month")
    )

    monthly_fig = px.line(
        monthly_data,
        x="Year-Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    monthly_fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales",
        margin=dict(l=40, r=20, t=60, b=40)
    )

    # ========================================================
    # TOP PRODUCTS
    # ========================================================

    product_data = (
        filtered_df
        .groupby("Product Name", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales")
    )

    product_fig = px.bar(
        product_data,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Revenue",
        text_auto=".2s"
    )

    product_fig.update_layout(
        margin=dict(l=40, r=20, t=60, b=40)
    )

    # ========================================================
    # RETURN
    # ========================================================

    return (
        f"${total_sales:,.2f}",
        f"${total_profit:,.2f}",
        f"{total_orders:,}",
        f"{profit_margin:.2f}%",
        region_fig,
        category_fig,
        monthly_fig,
        product_fig
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)