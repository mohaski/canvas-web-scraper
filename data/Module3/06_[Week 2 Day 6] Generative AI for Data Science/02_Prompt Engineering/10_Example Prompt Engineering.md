# Example: Prompt Engineering

# Example: Prompt Engineering

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Example: Prompt Engineering

Icon Progress Bar (browser only)

4 min read

**Scenario:** You're working with messy customer survey data that needs cleaning and standardization.

### Basic Data Cleaning Prompt Evolution:

#### Poor Prompt

"Clean this data"

#### Better Prompt

"Write Python code to clean customer survey data"

#### Best Prompt

"Create a Python function for cleaning customer survey data that:

* Utilize Pandas, re, and datetime packages
* Handles missing values in 'age', 'income', and 'satisfaction\_score'
* Standardizes 'email' format and validates
* Converts 'purchase\_date' to datetime format
* Normalizes 'product\_category' to predefined categories
* Creates a data quality report
* Includes error handling and documentation."

The best prompt here requires intimate knowledge of the dataset at hand where preliminary EDA was conducted to understand the specific data cleaning needs and structure of the data. In this case, the appropriate column names from a DataFrame are given and the required cleaning task for each is laid out appropriately.

### Produced Function from Prompt

The produced function might look something like this (from GPT-4o):

```
import pandas as pd  
import re  
from datetime import datetime  
  
def clean_survey_data(df):  
    """  
    Cleans customer survey data in the following ways:  
    - Handles missing values in 'age', 'income', and 'satisfaction_score' columns  
    - Standardizes and validates email addresses  
    - Converts 'purchase_date' to datetime format  
    - Normalizes 'product_category' to predefined categories  
    - Generates a data quality report  
      
    Parameters:  
    df (pd.DataFrame): The DataFrame containing survey data  
      
    Returns:  
    pd.DataFrame: Cleaned survey data  
    pd.DataFrame: Data quality report  
    """  
      
    # Handle missing values  
    for col in ['age', 'income', 'satisfaction_score']:  
        if col in df.columns:  
            # Fill missing numeric values with median  
            df[col].fillna(df[col].median(), inplace=True)  
      
    # Standardize and validate email addresses  
    def validate_email(email):  
        """Returns a lowercase email if valid, otherwise NaN"""  
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  
        if isinstance(email, str) and re.match(email_pattern, email):  
            return email.lower()  
        return None  
      
    if 'email' in df.columns:  
        df['email'] = df['email'].apply(validate_email)  
      
    # Convert 'purchase_date' to datetime  
    if 'purchase_date' in df.columns:  
        df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')  
      
    # Normalize 'product_category'  
    category_mapping = { 'electronics': 'Electronics', 'electronic': 'Electronics', 'home & garden': 'Home & Garden', 'home and garden': 'Home & Garden'} # Add more mappings as needed   
    cleaned_df['product_category'] = cleaned_df['product_category'].str.lower().map(category_mapping)  
    
      
    # Generate data quality report  
    data_quality_report = {  
        'column': [],  
        'missing_values': [],  
        'unique_values': [],  
        'data_type': []  
    }  
      
    for col in df.columns:  
        data_quality_report['column'].append(col)  
        data_quality_report['missing_values'].append(df[col].isnull().sum())  
        data_quality_report['unique_values'].append(df[col].nunique())  
        data_quality_report['data_type'].append(df[col].dtype)  
      
    data_quality_df = pd.DataFrame(data_quality_report)  
      
    return df, data_quality_df
```

#### **Explanation of Each Section**

1. **Missing Values:** Missing values in the age, income, and satisfaction\_score columns are filled with the column median, assuming they’re numeric.
2. **Email Validation:** Uses regex to check if each email matches a typical format and converts valid emails to lowercase. Invalid emails are set to None.
3. **Date Conversion:** Attempts to convert the purchase\_date column to datetime format. Invalid formats are coerced to NaT (missing values for dates).
4. **Product Category Normalization:** Map similar values based on the predefined dictionary which should be expanded based on domain knowledge.
5. **Data Quality Report:** Summarizes missing values, unique values, and data types for each column in a report.

Prompt engineering is an iterative process and there is no ‘final’ answer for any one prompt that you are designing. The better your prompts are at conveying the necessary and appropriate information, the better your generated answers will be in terms of usable code, requiring minimal reworking on your end.

##### **Additional Prompt Options**

We could continue iterating on the prompt above if needed to specify different or more specific tasks. For example, this generated function is using df.fillna() to impute null values based on the median of the column. If our EDA identified potential problems with that approach we could specify a different strategy within the prompt.

We could consider some further functionality as well:

* "Enhance the data cleaning function to include:
  + Outlier detection and handling for numeric columns
  + Custom validation rules for specific fields
  + Logging of all transformations
  + Summary statistics before and after cleaning
  + Option to export cleaning report to Excel"

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248410

Scraped At: 2026-05-15T10:02:12.369917
