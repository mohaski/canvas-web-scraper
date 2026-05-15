# Example: Independence and Homogeneity Tests

# Example: Independence and Homogeneity Tests

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example: Independence and Homogeneity Tests

Icon Progress Bar (browser only)

3 min read

Scenario: Memorial Healthcare Analysis Project

You're a junior data analyst at Memorial Healthcare, and your supervisor has asked you to analyze patient data to improve service delivery. You have two key questions to address:

1. Is there a relationship between patient age groups and their preferred appointment times? (Test of Independence)
2. Do different hospital locations show the same distribution of patient satisfaction ratings? (Test of Homogeneity)

### Analyzing in Python: Test of Independence & Test of Homogeneity

Let's analyze both questions using Python:

### Part 1: Test of Independence

Is there a relationship between patient age groups and their preferred appointment times? (Test of Independence)

#### Age Groups vs. Appointment Times

```
import pandas as pd  
import numpy as np  
from scipy.stats import chi2_contingency  
import seaborn as sns  
import matplotlib.pyplot as plt  
  
# Part 1: Test of Independence - Age Groups vs. Appointment Times  
def analyze_appointment_preferences(data):  
    """  
    Analyzes the relationship between patient age groups and appointment preferences  
      
    Parameters:  
        data: DataFrame with columns 'Age_Group' and 'Appointment_Time'  
    """  
    # Create contingency table  
    contingency_table = pd.crosstab(  
        data['Age_Group'],   
        data['Appointment_Time'],  
        margins=True  # Add row and column totals  
    )  
      
    # Remove the totals for the chi-square test  
    test_table = contingency_table.iloc[:-1, :-1]  
      
    # Perform chi-square test  
    chi2_stat, p_value, dof, expected = chi2_contingency(test_table)  
      
    # Create visualization  
    plt.figure(figsize=(12, 5))  
    sns.heatmap(test_table, annot=True, fmt='d', cmap='YlOrRd')  
    plt.title('Patient Appointment Preferences by Age Group')  
    plt.tight_layout()  
      
    # Calculate proportions for easier interpretation  
    proportions = test_table.div(test_table.sum(axis=1), axis=0)  
      
    return {  
        'contingency_table': contingency_table,  
        'chi2_stat': chi2_stat,  
        'p_value': p_value,  
        'dof': dof,  
        'proportions': proportions  
    }
```

### Part 2: Test of Homogeneity

Do different hospital locations show the same distribution of patient satisfaction ratings? (Test of Homogeneity)

#### Patient Satisfaction Across Locations

```
import pandas as pd  
import numpy as np  
from scipy.stats import chi2_contingency  
import seaborn as sns  
import matplotlib.pyplot as plt  
  
# Part 2: Test of Homogeneity - Patient Satisfaction Across Locations  
def analyze_satisfaction_distribution(data):  
    """  
    Compares patient satisfaction distributions across hospital locations  
      
    Parameters:  
        data: DataFrame with columns 'Location' and 'Satisfaction_Rating'  
    """  
    # Create contingency table  
    contingency_table = pd.crosstab(  
        data['Location'],  
        data['Satisfaction_Rating'],  
        margins=True  
    )  
      
    test_table = contingency_table.iloc[:-1, :-1]  
      
    # Perform chi-square test  
    chi2_stat, p_value, dof, expected = chi2_contingency(test_table)  
      
    # Visualize distributions  
    plt.figure(figsize=(12, 5))  
      
    # Convert to percentages for easier comparison  
    proportions = test_table.div(test_table.sum(axis=1), axis=0) * 100  
      
    proportions.plot(kind='bar', stacked=True)  
    plt.title('Satisfaction Ratings Distribution by Location')  
    plt.xlabel('Hospital Location')  
    plt.ylabel('Percentage')  
    plt.legend(title='Satisfaction Rating')  
    plt.tight_layout()  
      
    return {  
        'contingency_table': contingency_table,  
        'chi2_stat': chi2_stat,  
        'p_value': p_value,  
        'dof': dof,  
        'proportions': proportions  
    }  
  
# Generate sample data for demonstration  
np.random.seed(42)  
n_patients = 1000  
  
# Sample data for appointment analysis  
appointment_data = pd.DataFrame({  
    'Age_Group': np.random.choice(  
        ['18-30', '31-50', '51-70', '70+'],  
        size=n_patients,  
        p=[0.25, 0.35, 0.25, 0.15]  
    ),  
    'Appointment_Time': np.random.choice(  
        ['Morning', 'Afternoon', 'Evening'],  
        size=n_patients  
    )  
})  
  
# Sample data for satisfaction analysis  
satisfaction_data = pd.DataFrame({  
    'Location': np.random.choice(  
        ['Downtown', 'North', 'South', 'West'],  
        size=n_patients,  
        p=[0.3, 0.25, 0.25, 0.2]
```

### Potential Analysis Improvements

The analysis could lead to practical improvements such as:

* Optimizing appointment scheduling based on age group preferences
* Identifying best practices from high-performing locations
* Developing targeted improvement strategies for locations with lower satisfaction

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248720

Scraped At: 2026-05-15T10:21:57.093974
