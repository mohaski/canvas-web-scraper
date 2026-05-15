# Example: Tableau Public - Visualizations and Dashboards

# Example: Tableau Public - Visualizations and Dashboards

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Example: Tableau Public - Visualizations and Dashboards

Icon Progress Bar (browser only)

3 min read

### **Scenario: Regional Performance Analysis for TechGadget Retail Chain**

You are a junior data analyst at TechGadget, a nationwide electronics retail chain. The company's CEO has noticed inconsistent profit margins across different regions and has tasked your team with creating a comprehensive dashboard to analyze regional performance and product profitability. As the newest member of the analytics team, you've been given the responsibility to build this dashboard using Tableau.

#### **Dashboard Objective**

Create an interactive dashboard that allows executives to:

* Visualize profit distribution across different states and regions.
* Analyze profit trends over time for each region.
* Identify top-performing and underperforming products.
* Understand the relationship between sales volume and profitability.

##### Dashboard Components

1. Profit Map

* A filled map of the United States showing profit by state
* Color gradient: Red for losses, yellow for break-even, green for highest profits
* Tooltip: State name, total profit, top-selling product

1. Regional Profit Bar Chart

* Horizontal bar chart displaying total profit for each region
* Bars sorted in descending order of profit
* Color-coded bars matching the region colors used throughout the dashboard

1. Monthly Profit Trend Line Chart

* Line chart showing profit trends over the past 12 months
* Separate lines for each region, color-coded to match other visualizations
* Option to overlay trend lines

1. Product Performance Scatter Plot

* X-axis: Total Sales
* Y-axis: Profit Margin (%)
* Each point represents a product
* Size of points indicates sales volume
* Color of points represents product category
* Tooltip: Product name, category, sales, profit margin, and units sold

1. Top/Bottom Products Table

* Switchable view between top 10 and bottom 10 products
* Columns: Rank, Product Name, Category, Total Sales, Profit Margin (%), Units Sold
* Sortable columns

##### Interactive Elements

* Region filter (multi-select)
* Date range selector (defaulted to last 12 months, but adjustable)
* Product Category filter (multi-select)
* Profit/Loss toggle for the map (to focus on either profitable or unprofitable areas)

##### Implementation Steps

1. Connect to the TechGadget sales database in Tableau.
2. Create individual sheets for each visualization:

* **Profit Map:** use the geographic field for states and sum of profit for color.
* **Regional Profit Bar Chart:** use regions on rows and sum of profit on columns.
* **Monthly Profit Trend:** use months on columns and sum of profit on rows, with region on color.
* **Scatter Plot:** use sum of sales on columns and average profit margin on rows, with sum of units sold on size and category on color.
* **Top/Bottom Products Table:** use table calculation to rank products by profit margin.

1. Create calculated fields for Profit Margin (%) and any other necessary metrics.
2. Design the dashboard layout, ensuring a logical flow of information.
3. Add interactivity by creating filters and ensuring they apply to all relevant sheets.
4. Format the dashboard with TechGadget’s branding colors and add explanatory titles and legends.
5. Test the dashboard thoroughly, ensuring all interactions work as expected.
6. Present the dashboard to your team lead for review before the executive meeting.

This example demonstrates how you would apply Tableau skills in a real-world retail scenario. It incorporates various chart types, interactivity, and focuses on delivering actionable insights about regional and product performance. As a junior analyst, this project allows you to showcase your ability to translate business questions into data visualizations and create a tool that can drive decision-making at the executive level.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248372

Scraped At: 2026-05-15T10:00:01.933260
