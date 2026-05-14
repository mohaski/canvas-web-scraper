# Lab: Widget Sales

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Lab: Widget Sales

![Man interacting with charts on a tablet at a desk](https://moringa.instructure.com/courses/1406/files/624747/download?)
Imagine you are a junior analyst for a company that sells widgets for use across many different industries/markets. Your boss has asked you to give her a summary of widget sales across these markets for the past year. She wants to know:

* What has been the typical sales volume across markets?
* How variable have sales been across the different markets this past year?
* How much has the company been characteristically spending in different advertising media (TV, radio, and newspaper) across the different markets for the past year?

You have been given a dataset (in CSV format) that contains sales and advertising budget information that you will require for your analysis. There are four columns:

1. **Sales:** the number of widgets sold (in thousands)
2. **TV:** the amount of money (in thousands of dollars) spent on TV ads
3. **Radio:** the amount of money (in thousands of dollars) spent on radio ads
4. **Newspaper:** the amount of money (in thousands of dollars) spent on newspaper ads

You will be using your new knowledge of measures of central tendency and dispersion to aid you in addressing some of the questions that your boss has posed.

### Tools and Resources

* [GitHub Repository


  Links to an external site.](https://github.com/flatiron-school/DS_Course0_Week1_Module3_StatMeasLab)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

* [Step 1: Sales Data Summary](#dpPanel0Content)
* [Step 2: Typical Sales Volume](#dpPanel1Content)
* [Step 3: Dispersion of Sales Volume](#dpPanel2Content)

### Step 1: Sales Data Summary

```
# Run this cell without changes  
  
import csv
```

1. Use the csv DictReader to load the dataset into a list of dictionaries and save it to a variable data.  

   ```
   # Replace None with appropriate code  
   data = None
   ```
2. Extract sales numbers for each market in the dataset as a list and save it to a variable “sales”. Then save TV, Radio, and Newspaper advertising expenditures to lists called “tv”, “radio” and “newspaper” respectively.  

   ```
   # Replace None with appropriate code  
     
   sales = None  
   tv = None  
   radio = None  
   newspaper = None
   ```
3. Provide a summary of the data by:  
   1. Getting the number of markets your company has been engaged in this past year
   2. Use in-built Python functions to get the minimum and maximum sales across all markets operated in.  

      ```
      # Replace None with appropriate code  
      num_markets = None  
      min_sales = None  
      max_sales = None  
        
      print(f"""  
        
      This dataset contains records for {num_markets} markets  
        
      The fewest sales for any market was {min_sales} thousand widgets  
        
      The most sales for any market was {max_sales} thousand widgets  
      """)
      ```
   3. Run this code to create a histogram of all sales data:  

      ```
      # Run this cell without changes  
      import matplotlib.pyplot as plt  
      %matplotlib inline  
        
      fig, ax = plt.subplots(figsize=(10, 5))  
        
      ax.hist(sales, bins=15)  
      ax.set_xlabel("Sales (thousands of widgets)")  
      ax.set_ylabel("Count")  
        
      ax.set_title("Distribution of Sales across Markets");
      ```

### Step 2: Typical Sales Volume

Now let us address the first business question: *What has been the typical sales volume across markets?*

Based on the histogram, choose an appropriate measure of central tendency for widget sales. Use whatever method you wish to calculate your chosen metric—making any required imports in the cell.

```
# Replace None or <None> with appropriate code  
# make any imports here  
  
# Assign measure_central_tendency to the mean, median, or mode of the sales data  
measure_central_tendency = None  
  
print(f"""  
Typical sales volume is {measure_central_tendency} thousand widgets  
  
   
  
""")
```

### Step 3: Dispersion of Sales Volume

Now that we have a number to represent the typical sales volume, let's answer the second question: *How variable have sales been across markets?*

1. Based on the histogram, choose an appropriate measure of dispersion for widget sales. Use whatever method you wish to calculate your chosen metric—making any required imports in the cell.  

   ```
   # Replace None or <None> with appropriate code  
   # make any imports here  
     
   # Assign measure_dispersion  
   measure_dispersion = None
   ```
2. And now to answer the final question: *How much has the company characteristically been spending on different advertising media (TV, radio, and newspaper) across the different markets for the past year?*
   1. Calculate the median expenditure for each media.  

      ```
      # Replace None or <None> with appropriate code  
        
      # make any imports here  
        
      median_tv_expenditure = None  
      median_radio_expenditure = None  
      median_newspaper_expenditure = None
      ```
   2. Calculate the IQR for each media.  

      ```
      # Replace None or <None> with appropriate code  
        
      # make any imports here  
        
      iqr_tv_expenditure = None  
      iqr_radio_expenditure = None  
      iqr_newspaper_expenditure = None
      ```

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243548

Scraped At: 2026-05-14T20:52:05.781019
