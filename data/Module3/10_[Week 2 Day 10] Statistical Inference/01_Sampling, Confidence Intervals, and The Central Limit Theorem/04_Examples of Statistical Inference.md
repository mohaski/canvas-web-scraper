# Examples of Statistical Inference

# Examples of Statistical Inference

## ![](https://moringa.instructure.com/courses/1426/files/631696/preview) Examples of Statistical Inference

Icon Progress Bar (browser only)

4 min read

Imagine you've just started as a junior data analyst at an e-commerce company, and your manager gives you your first significant project: "We need to understand our product return rates better. Can you analyze the data and give us a reliable estimate of our overall return rate?"

### The Scenario

Your company, TechStyle, sells clothing online and processes thousands of orders daily. You have access to a database with millions of transactions from the past year, but analyzing all of them would take too long and strain the company's resources.

#### Part 1: Planning Your Sampling Strategy

First, you need to decide how to sample the data. Here's your thought process:

"We have 2.5 million transactions from the past year. I'll need to take a sample that's:

* Large enough to be representative
* Small enough to analyze efficiently
* Structured to account for seasonal variations"

You decide to use stratified sampling, dividing the year into quarters to account for seasonal patterns. This is smarter than simple random sampling because return rates might vary by season (e.g., more returns after holiday shopping).

#### Part 2: The Results- Confidence Interval Creation

"Based on our analysis of 25,000 randomly sampled transactions:

* Our estimated return rate is 12.3%.
* We're 95% confident the true return rate falls between 11.8% and 12.8%.
* This estimate accounts for seasonal variations.
* The sampling method gives us a margin of error of ±0.5 percentage points".

#### Potential Issues and Considerations

Being aware of potential pitfalls is crucial:

* If you hadn't stratified by quarter, holiday returns might have skewed your results.
* If your sample size was too small, your confidence interval would be wider.
* If your sampling wasn't random, you might have introduced bias.

#### Sample Code Solution

```
import pandas as pd  
  
  
def get_stratified_sample(transactions_df, sample_size=25000):  
   """  
   Create a stratified sample of transaction data based on quarters.  
   This helps account for seasonal variations in return rates.  
    
   Parameters:  
   transactions_df: DataFrame with at least a 'date' column  
   sample_size: How many transactions to include in the sample (default: 25000)  
    
   Returns:  
   DataFrame containing the stratified sample  
   """  
   # First, let's add a quarter column to our data  
   # This creates Q1, Q2, Q3, Q4 based on the date  
   df = transactions_df.copy()  
   df['quarter'] = pd.to_datetime(df['date']).dt.quarter  
    
   # Find out what percentage of our data falls into each quarter  
   # For example: Q1: 24%, Q2: 26%, Q3: 23%, Q4: 27%  
   quarter_proportions = df['quarter'].value_counts(normalize=True)  
    
   # Calculate how many samples we should take from each quarter  
   # If we want 25000 total samples and Q1 is 24% of our data,  
   # we should take 6000 samples (24% of 25000) from Q1  
   quarter_sample_sizes = {  
       quarter: int(proportion * sample_size)  
       for quarter, proportion in quarter_proportions.items()  
   }  
    
   # Because we rounded down to whole numbers, we might be a few samples short  
   # Let's add any missing samples to the first quarter  
   total = sum(quarter_sample_sizes.values())  
   if total < sample_size:  
       quarter_sample_sizes[1] += sample_size - total  
    
   # Now let's take our samples from each quarter  
   sampled_data = pd.DataFrame()  # Empty DataFrame to store our samples  
    
   for quarter, size in quarter_sample_sizes.items():  
       # Get all data from this quarter  
       quarter_data = df[df['quarter'] == quarter]  
        
       # Take a random sample from this quarter's data  
       quarter_sample = quarter_data.sample(n=size, random_state=42)  
        
       # Add it to our sampled data  
       sampled_data = pd.concat([sampled_data, quarter_sample])  
    
   return sampled_data  
  
  
# Example of how to use the function:  
def example_usage():  
   # Let's create some example data  
   dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')  
   example_data = pd.DataFrame({  
       'date': dates,  
       'order_id': range(len(dates)),  
       'returned': [False] * len(dates)  # Just placeholder return data  
   })  
    
   # Get our stratified sample  
   sample = get_stratified_sample(example_data, sample_size=100)  
    
   # Let's see how many samples we got from each quarter  
   quarterly_counts = sample['quarter'].value_counts().sort_index()  
   print("\nNumber of samples from each quarter:")  
   for quarter, count in quarterly_counts.items():  
       print(f"Quarter {quarter}: {count} samples")  
  
  
if __name__ == "__main__":  
   example_usage()
```

 Number of samples from each quarter:

* **Quarter 1:** 26 samples
* **Quarter 2:** 24 samples
* **Quarter 3:** 25 samples
* **Quarter 4:** 25 samples

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248559

Scraped At: 2026-05-15T10:11:33.282275
