# Example: Advanced Tableau

# Example: Advanced Tableau

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Example: Advanced Tableau

Icon Progress Bar (browser only)

2 min read

**Marketing Campaign Performance Dashboard Scenario:** You're a junior marketing analyst working at a major clothing company, tasked with creating an interactive dashboard to track the performance of multiple marketing campaigns across different channels/avenues of expenditure. Your company wants to know which campaigns perform better within each channel to target their spending more appropriately.

![Flow chart of raw Data Sources, Parameters, LOD expressions, Dashboard Actions, and Dynamic Calculations.](https://moringa.instructure.com/courses/1426/files/631490/download)

### Parameter Controls

Using Tableau you create custom parameters that enable high level control over the dashboard.

**Example:**

* **Date Ranges:** One week (last seven days), One month, Last Quarter, Custom
  + By setting specific and commonly used ranges it allows for a user of the dashboard to rapidly select/filter data based on the range given.
  + This allows for the dashboard to be dynamic and serve potentially multiple purposes.
* **Performance Metric:** ROI, Cost per Click, Conversion Rate, Total Spend etc…
  + You can create a metric selector parameter that will allow a user to rapidly transition between different metrics of interest.
  + Again allowing for increased dynamics and multiple purposes.

### Dynamic Calculations

Using Tableau you create custom calculated fields that allow you dynamic filtering and analysis based on the two important/key features, the different marketing campaigns and the different marketing channels.

Think of this as something akin to grouping and aggregating data based on column values except here the dashboard can dynamically update based on a user's selected values.

```
// ROI Calculation with LOD  
{FIXED [Campaign Name]:   
    SUM([Revenue]) / SUM([Cost])}  
  
// Channel Performance  
{INCLUDE [Channel]:   
    AVG([Conversion Rate])}
```

### Dashboard Actions

Using Tableau you create several dashboard actions that allow for more comprehensive interactivity and filtering.

**Example:**

* Click campaign name and/or channel to filter all charts.
* Hover over channel to highlight related metrics.
* Select date range to dynamically update calculations.
* Select performance metric to dynamically show different KPIs.

**Implementation Tips:**

* Start with core metrics before adding complexity.
* Use clear naming conventions.
* Add helpful tooltips for new users.
* Include a "Reset All" button for filters.

 This example shows how advanced Tableau features create a practical, interactive tool for daily marketing analytics tasks while making complex data accessible to all stakeholders.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248462

Scraped At: 2026-05-15T10:04:55.465078
