# Example: Generating Python and SQL Code

# Example: Generating Python and SQL Code

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Example: Generating Python and SQL Code

Icon Progress Bar (browser only)

5 min read

**Scenario:** You are working as a Junior Data Analyst at a retail department store.

**Monthly Customer Purchase Analysis Task:** Analyze customer purchase patterns from monthly sales data to identify top customers and their buying trends.

**Real-world Example**: A retail store uses this analysis to:

* Identify top 20% of customers generating 80% of revenue.
* Spot customers whose purchases are declining.
* Recognize seasonal buying patterns.
* Plan inventory based on customer preferences.

### Step-by-Step AI-Assisted Process

To get the most out of AI assistance, you'd need to go through the steps of understanding the data you have, figuring out what you want to do with it, and honing in on the right prompts. Here's a more detailed look at that process:

#### 1. Initial Data Understanding

* Review raw data structure:
  + Sales transactions
  + Customer information
  + Purchase dates and amounts
* Identify analysis goals:
  + Find top customers
  + Calculate purchase frequencies
  + Identify buying patterns

#### 2. Data Preparation Planning

Prompt AI to help with:

* Loading data efficiently
* Cleaning missing values
* Converting date formats
* Creating basic aggregations

**Example Prompt:**

"I'm a junior data analyst working with sales data in a CSV file. The file has columns: customer\_id, purchase\_date, amount, product\_category. Can you help me write Python code using pandas to:

* Load the data
* Convert purchase\_date to datetime
* Handle any missing values
* Show basic summary statistics.

I need clear comments explaining each step."

#### 3. Basic Analysis Structure

Request AI Assistance for:

* Grouping by customer
* Calculating key metrics
* Basic statistical analysis
* Initial visualizations

**Example Prompt:**

"Using the sales dataframe, help me create Python and Pandas code to:

* Calculate total purchases per customer
* Find the average order value
* Count number of orders per customer
* Identify the top 10 customers by total spend

Please include error handling and comments explaining the analysis."

#### 4. Visualization Planning

Ask AI to help create:

* Monthly trend charts
* Customer segments
* Purchase distributions
* Summary visualizations

**Example Prompt:** "Using the customer purchase summary data, show me how to create the following python visualizations:

* A bar chart showing top 10 customers by spend
* A line plot showing monthly sales trends
* A histogram of order values
* Use matplotlib or seaborn with clear labels and titles.

Please ensure that all visualizations do not use scientific notation.”

These prompts are:

* Specific about the data
* Clear about desired outcomes
* Broken into steps
* Request explanations
* Focus on business value

### Debugging Code Example

**Scenario: Monthly Sales Report Error**

You're trying to create a monthly sales summary but your code isn't working as expected and you are getting results you know are incorrect based on your domain knowledge and validations.

**Original Problematic Code Situation:**

* Sales data won't group correctly by month
* Calculations showing incorrect totals
* Some customers missing from analysis
* Visualization shows wrong date range

#### Debugging Process Using AI

1. **Initial Error Assessment Prompt to AI:** "I'm getting incorrect totals when grouping sales by month. Here's my current code and the error I'm seeing. What could be causing this and how can I fix it?"
2. **Data Validation Check Prompt to AI:** "How can I check if my date columns are in the correct format? Some dates seem to be missing from my analysis. Need code to verify date formatting and identify any issues."
3. **Aggregation Review Prompt to AI:** "My customer totals aren't matching our reports. Can you help me verify my groupby operations and suggest ways to validate the calculations?"

#### Common Issues and Solutions

1. **Date Format Problems**  
   * **Issues**: Mixed date formats, incorrect parsing
   * **AI Help:** Request code to standardize dates
   * **Verification:** Check unique date values
2. **Missing Data Impact**  
   * **Issues:** NaN values affecting calculations
   * **AI Help:** Ask for proper null handling
   * **Verification:** Count missing values
3. **Grouping Errors**  
   * **Issues:** Incorrect aggregation levels
   * **AI Help:** Review groupby operations
   * **Verification**: Cross-check totals

#### Effective AI Usage for Debugging

* Clear Problem Description
* Explain the issue
* Show error messages
* Provide context
* State expected results

### SQL Query Example

**Scenario:** The Head of Sales wants to identify customer purchasing patterns during the holiday season (October through December 2023) to plan for 2024.

**Task:** Write a SQL query to find the top 100 customers based on total spending during holiday months, including their average order value and number of orders. We're only interested in customers who made at least 3 purchases during this period. Include their customer tier (Bronze: <$1000, Silver: $1000-$5000, Gold: >$5000) based on their total spending.

**How to Approach Using AI:**

#### 1. Break Down Requirements

* Time period: Oct-Dec 2023
* Metrics needed:
  + Total spending per customer
  + Average order value
  + Number of orders
  + Customer tier (based on given conditions)
* Conditions:
  + Minimum 3 purchases
  + Top 100 customers based on total spend during time period

#### 2. Clarify Table Structure

Prompt to AI:

"I'm working with data in a SQL database that has the following tables:

* **orders** (order\_id, customer\_id, order\_date, order\_amount)
* **customers** (customer\_id, customer\_name, email)

Help me structure a query to get these required metrics:

* Total spend per customer
* Average order value
* Total number of orders per customer
* Customer tier based on total spending (Bronze: <$1000, Silver: $1000-$5000, Gold: >$5000)

Please filter results based on the following criteria:

* Minimum of 3 purchases within range of Oct-Dec, 2023
* Top 100 customers based on total spend”

#### 3. Build Query Components

Ask AI to help with:

* Date filtering logic
* Customer spending aggregation
* Tier classification
* Minimum purchase filter
* Final sorting and limiting

#### 4. Validation Points

Request AI Assistance to:

* Check date format handling
* Verify aggregation logic
* Confirm tier calculations
* Test filter conditions

These examples of customer purchase analysis, code debugging, and SQL query writing demonstrate how you can leverage both traditional data analysis tools and generative AI to solve real-world retail business problems. They show you how to break down complex tasks into manageable steps while using AI as an assistant to help with coding, troubleshooting, and query optimization.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248424

Scraped At: 2026-05-15T10:02:44.138669
