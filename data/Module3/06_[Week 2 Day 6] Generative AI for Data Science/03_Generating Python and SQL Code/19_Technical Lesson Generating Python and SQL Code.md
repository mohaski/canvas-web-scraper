# Technical Lesson: Generating Python and SQL Code

# Technical Lesson: Generating Python and SQL Code

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Generating Python and SQL Code

* [Page: Introduction to Generative AI for Data Science (1 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248390 "Page: Introduction to Generative AI for Data Science (1 of 22)")
* [Page: Introduction to Generative AI (2 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248394 "Page: Introduction to Generative AI (2 of 22)")
* [Page: What is Generative AI? (3 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248395 "Page: What is Generative AI? (3 of 22)")
* [Page: Example: Generative AI (4 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248397 "Page: Example: Generative AI (4 of 22)")
* [Page: Process: Generative AI (5 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248399 "Page: Process: Generative AI (5 of 22)")
* [Page: Summary: Generative AI (6 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248401 "Page: Summary: Generative AI (6 of 22)")
* [Page: Check for Understanding: Generative AI (7 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248403 "Page: Check for Understanding: Generative AI (7 of 22)")
* [Page: Introduction to Prompt Engineering (8 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248407 "Page: Introduction to Prompt Engineering (8 of 22)")
* [Page: What is Prompt Engineering? (9 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248409 "Page: What is Prompt Engineering? (9 of 22)")
* [Page: Example: Prompt Engineering (10 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248410 "Page: Example: Prompt Engineering (10 of 22)")
* [Page: Process: Prompt Engineering (11 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248411 "Page: Process: Prompt Engineering (11 of 22)")
* [Page: Summary: Prompt Engineering (12 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248413 "Page: Summary: Prompt Engineering (12 of 22)")
* [Page: Check for Understanding: Prompt Engineering (13 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248415 "Page: Check for Understanding: Prompt Engineering (13 of 22)")
* [Page: Introduction to Generating Python and SQL Code (14 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248419 "Page: Introduction to Generating Python and SQL Code (14 of 22)")
* [Page: What is AI with Python and SQL Code? (15 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248422 "Page: What is AI with Python and SQL Code? (15 of 22)")
* [Page: Example: Generating Python and SQL Code (16 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248424 "Page: Example: Generating Python and SQL Code (16 of 22)")
* [Page: Process: Generating Python and SQL Code (17 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248426 "Page: Process: Generating Python and SQL Code (17 of 22)")
* [Page: Summary: Generating Python and SQL Code (18 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248428 "Page: Summary: Generating Python and SQL Code (18 of 22)")
* [Page: Current: Technical Lesson: Generating Python and SQL Code (19 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248430 "Page: Current: Technical Lesson: Generating Python and SQL Code (19 of 22)")
* [Lab: Generative AI for Data Science (20 of 22), Assignment](https://moringa.instructure.com/courses/1426/modules/items/248434 "Lab: Generative AI for Data Science (20 of 22), Assignment")
* [Module Lab Discussion: Generative AI for Data Science (21 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248436 "Module Lab Discussion: Generative AI for Data Science (21 of 22)")
* [Quiz: Generative AI for Data Science (22 of 22)](https://moringa.instructure.com/courses/1426/modules/items/248438 "Quiz: Generative AI for Data Science (22 of 22)")

*​*

**Estimated Completion Time:** 1 hour

This lesson demonstrates using generative AI to produce python code in order to analyze historical weather data to identify temperature trends and precipitation patterns. It also covers utilizing generative AI to help you debug code snippets that are not working correctly and provide a solution. Finally, it will cover an exercise using generative AI to produce SQL query syntax in order to fetch specific data.

**Note:** There are three scenarios for you to review in this technical lesson.

### Video Walkthroughs: Generative AI

The videos below will guide you through each step of the lesson. You can follow along with the videos to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of generating python and SQL code.

#### **Part 1**

[VIDEO LINK](https://player.vimeo.com/video/1038346127?h=192b241a5b)

#### **Part 2**

[VIDEO LINK](https://player.vimeo.com/video/1038346203?h=55062e3f38)

#### **Part 3**

[VIDEO LINK](https://player.vimeo.com/video/1038346328?h=e221db69f5)

### Resources

If you want to follow along and practice, you'll need to make sure you have:

* Python (pandas, matplotlib, seaborn)
* Jupyter Notebook
* Generative AI tool (ChatGPT/Claude)

### Instructions

#### Scenario 1

As a junior data analyst at a local agriculture consulting firm, you need to help farmers understand weather patterns for crop planning. The agriculture team needs insights on monthly temperature and rainfall patterns from 2020-2023 to help local farmers optimize planting schedules.

* [Step 1. Requirement Analysis & Planning](#dpPanel0Content)
* [Step 2. Development Strategy](#dpPanel1Content)
* [Step 3. Iterative Code Generation](#dpPanel2Content)
* [Step 4. Testing and Validation](#dpPanel6Content)
* [Step 5. Refinement & Optimization](#dpPanel7Content)

##### Step 1. Requirement Analysis & Planning

**Business Need:** Analyze 2020-2023 weather patterns for agriculture planning

**Objectives:**

* Identify temperature trends
* Analyze precipitation patterns
* Determine seasonal changes
* Find extreme weather events

**Data Structure:**

* **Columns/Fields:**
  + date (daily readings)
  + max\_temp (numeric)
  + min\_temp (numeric)
  + precipitation (numeric)
  + humidity (numeric)
  + wind\_speed (numeric)
* **Need to Create:**
  + Monthly temperature averages
  + Seasonal rainfall patterns
  + Extreme weather identification
  + Clear visualizations to display the above information

##### Step 2. Development Strategy

We will use ChatGPT 4o as the AI model. Break the task down into smaller more manageable components:

1. Data Processing:   
   1. Load data
   2. Clean/validate
   3. Create time-based features (month)
2. Analysis Components:  
   1. Temperature calculations (average daily → average month)
   2. Precipitation analysis (grouping by month)
   3. Seasonal patterns
3. Visualization Elements:  
   1. Temperature trends
   2. Rainfall distributions
   3. Seasonal comparisons

We can even use a prompt to help in the planning process as well.

**Planning Prompt:**

"I need to analyze weather data (temperature and rainfall) for agricultural planning. Help me structure the analysis approach for:

1. Data validation
2. Monthly patterns
3. Seasonal trends

Please outline the key steps and considerations."

###### AI Response

For analyzing weather data to support agricultural planning, here's a structured approach to cover each aspect: data validation, monthly patterns, and seasonal trends.

1. **Data Validation**

* **Identify Missing Values:** Check for and handle missing values in the dataset (imputation if gaps are small, otherwise exclusion or flagging for longer periods).
* **Outlier Detection:** Identify unusual values using statistical methods (e.g., z-scores) or visualization (e.g., box plots) for temperature and rainfall.
* **Consistency Checks:** Confirm data consistency across variables. For example, verify that high rainfall doesn’t coincide with unusually high temperatures unless there’s a plausible explanation (e.g., tropical climates).
* **Temporal Gaps and Continuity:** Ensure data continuity, particularly for identifying trends. Address irregular time intervals if they exist.
* **Source Validation:** Verify that data is from reliable sources (e.g., meteorological agencies) to ensure data quality.

2. **Monthly Patterns**

* **Calculate Monthly Averages:** Calculate average temperatures and rainfall for each month across the dataset period to understand typical monthly conditions.
* **Variability and Extremes:** Assess variability within each month by looking at standard deviations or ranges to identify months with high variability in weather patterns.
* **Seasonal Events and Anomalies:** Track significant monthly anomalies like unexpected rainfall spikes or temperature drops.
* **Visualization:** Use line plots or bar charts to show monthly temperature and rainfall trends, which makes it easy to spot recurring monthly patterns and anomalies.

3. **Seasonal Trends**

* **Seasonal Aggregation:** Aggregate data into seasons (e.g., Winter, Spring, Summer, Fall) to observe broader seasonal shifts.
* **Trend Analysis:** Identify long-term trends within each season. For instance, check if summer temperatures are increasing over the years or if there’s a trend toward wetter winters.
* **Cross-Season Comparisons:** Compare seasons to evaluate shifts in seasonality that could affect crop planning, like changes in the timing of wet or dry seasons.
* **Climate Anomalies and Extremes:** Detect extreme weather events like droughts, floods, or heatwaves that could disrupt typical seasonal patterns.
* **Visualization:** Plot seasonal trends over multiple years to observe both cyclical patterns and any consistent shifts, using rolling averages or smoothing to highlight long-term trends.

Would you like to explore specific statistical or visualization tools to apply in any of these steps?

##### Step 3. Iterative Code Generation

###### [Data Loading and Validation Prompt](#dpPanel3)

"I have weather data with columns: date, max\_temp, min\_temp, precipitation, humidity, wind\_speed. Help me write Python code to load and validate this data for analysis of temperature and rainfall patterns. Use Pandas to load in the data. Ensure proper validation and error handling"

###### AI Response

```
import pandas as pd  
import numpy as np  
  
# Load data  
def load_weather_data(file_path):  
    try:  
        # Load the CSV data  
        df = pd.read_csv(file_path, parse_dates=['date'])  
        print("Data loaded successfully.")  
        return df  
    except FileNotFoundError:  
        print("Error: File not found.")  
        return None  
    except pd.errors.ParserError:  
        print("Error: Parsing error, please check the file format.")  
        return None  
    except Exception as e:  
        print(f"Unexpected error: {e}")  
        return None  
  
# Data validation function  
def validate_weather_data(df):  
    if df is None:  
        print("No data to validate.")  
        return None  
  
    # Check for missing values  
    missing_values = df.isnull().sum()  
    print("Missing values per column:")  
    print(missing_values)  
  
    # Handle missing values  
    if missing_values.any():  
        # Drop rows with missing dates  
        df = df.dropna(subset=['date'])  
        # Fill missing values in other columns with column median as a placeholder  
        df.fillna(df.median(numeric_only=True), inplace=True)  
        print("Missing values handled (dropped rows with missing dates, filled other columns with median).")  
  
    # Check for duplicates  
    duplicate_rows = df.duplicated().sum()  
    if duplicate_rows > 0:  
        df = df.drop_duplicates()  
        print(f"Removed {duplicate_rows} duplicate rows.")  
  
    # Outlier detection for temperature and precipitation  
    # Define acceptable ranges based on historical norms  
    temp_bounds = (-30, 50)  # Example bounds for temperature in Celsius  
    precip_bounds = (0, 500) # Example bounds for precipitation in mm  
  
    outliers_temp = (df['max_temp'] < temp_bounds[0]) | (df['max_temp'] > temp_bounds[1]) | \  
                    (df['min_temp'] < temp_bounds[0]) | (df['min_temp'] > temp_bounds[1])  
    outliers_precip = (df['precipitation'] < precip_bounds[0]) | (df['precipitation'] > precip_bounds[1])  
  
    outlier_counts = {  
        'Temperature Outliers': outliers_temp.sum(),  
        'Precipitation Outliers': outliers_precip.sum()  
    }  
    print("Outlier counts:")  
    print(outlier_counts)  
  
    # Flag or remove extreme outliers based on user preference (e.g., removing for analysis simplicity)  
    df = df[~(outliers_temp | outliers_precip)]  
    print("Outliers removed.")  
  
    # Validate data consistency (e.g., max_temp should be >= min_temp)  
    inconsistent_temps = (df['max_temp'] < df['min_temp']).sum()  
    if inconsistent_temps > 0:  
        print(f"Found {inconsistent_temps} rows with inconsistent temperature values. Correcting values.")  
        # Swapping values where min_temp > max_temp  
        df.loc[df['max_temp'] < df['min_temp'], ['max_temp', 'min_temp']] = \  
            df.loc[df['max_temp'] < df['min_temp'], ['min_temp', 'max_temp']].values  
  
    return df  
  
# Usage example  
file_path = 'your_weather_data.csv'  # Replace with your file path  
df = load_weather_data(file_path)  
df = validate_weather_data(df)  
  
# If you want to view the cleaned dataset  
print("Cleaned data:")  
print(df.head())
```

**Explanation of Key Steps**

1. **Loading the Data**: Handles file-related errors, ensures the date column is parsed as a date.
2. **Missing Values**:  
   * Reports missing values per column.
   * Drops rows with missing dates, as dates are typically crucial for time series analysis.
   * Fills other missing values with the median of each column (a placeholder approach).
3. **Duplicate Rows:** Removes any duplicate rows for accuracy.
4. **Outlier Detection**:  
   * Sets bounds for max\_temp, min\_temp, and precipitation. You can adjust these bounds based on your data's expected ranges.
   * Counts outliers in temperature and precipitation and removes them from the dataset.
5. **Consistency Check**:  
   * Ensures that max\_temp is always greater than or equal to min\_temp.
   * Swaps values when min\_temp exceeds max\_temp.

###### [Data Analysis Prompt](#dpPanel4)

"Help me create python code to calculate monthly averages for temperature and precipitation using the data previously discussed, including proper error handling and seasonal breakdowns."

###### AI Response

```
import pandas as pd  
  
def calculate_monthly_averages(df):  
    try:  
        if 'date' not in df or 'max_temp' not in df or 'min_temp' not in df or 'precipitation' not in df:  
            raise ValueError("Dataframe must contain 'date', 'max_temp', 'min_temp', and 'precipitation' columns.")  
  
        # Ensure 'date' column is a datetime type  
        df['date'] = pd.to_datetime(df['date'], errors='coerce')  
        if df['date'].isnull().any():  
            raise ValueError("Invalid date values found after parsing. Please ensure date format is consistent.")  
          
        # Calculate average temperature as (max_temp + min_temp) / 2  
        df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2  
  
        # Extract month and year from the date  
        df['month'] = df['date'].dt.month  
        df['year'] = df['date'].dt.year  
  
        # Monthly averages for temperature and precipitation  
        monthly_averages = df.groupby('month').agg({  
            'avg_temp': 'mean',  
            'precipitation': 'mean'  
        }).rename(columns={'avg_temp': 'monthly_avg_temp', 'precipitation': 'monthly_avg_precipitation'}).reset_index()  
  
        print("Monthly averages calculated successfully.")  
        print(monthly_averages)  
  
        return monthly_averages  
  
    except ValueError as ve:  
        print(f"ValueError: {ve}")  
        return None  
    except Exception as e:  
        print(f"Unexpected error: {e}")  
        return None  
  
def calculate_seasonal_averages(df):  
    try:  
        # Define seasons (adjust based on hemisphere as needed)  
        season_mapping = {  
            12: 'Winter', 1: 'Winter', 2: 'Winter',  
            3: 'Spring', 4: 'Spring', 5: 'Spring',  
            6: 'Summer', 7: 'Summer', 8: 'Summer',  
            9: 'Fall', 10: 'Fall', 11: 'Fall'  
        }  
        df['season'] = df['month'].map(season_mapping)  
  
        # Seasonal averages for temperature and precipitation  
        seasonal_averages = df.groupby('season').agg({  
            'avg_temp': 'mean',  
            'precipitation': 'mean'  
        }).rename(columns={'avg_temp': 'seasonal_avg_temp', 'precipitation': 'seasonal_avg_precipitation'}).reset_index()  
  
        print("Seasonal averages calculated successfully.")  
        print(seasonal_averages)  
  
        return seasonal_averages  
  
    except KeyError as ke:  
        print(f"KeyError: {ke} - Ensure 'month' column exists in the dataframe.")  
        return None  
    except Exception as e:  
        print(f"Unexpected error: {e}")  
        return None  
  
# Usage example, assuming df is the validated dataframe  
monthly_averages = calculate_monthly_averages(df)  
seasonal_averages = calculate_seasonal_averages(df)
```

**Explanation of Key Steps**

1. Monthly Averages Calculation:  
   * Checks if the required columns are in the dataframe, ensuring the presence of 'date', 'max\_temp', 'min\_temp', and 'precipitation'.
   * Computes avg\_temp as the average of max\_temp and min\_temp.
   * Extracts the month and year from the date column.
   * Groups data by month and calculates the mean for avg\_temp and precipitation.
2. Seasonal Averages Calculation:  
   * Maps each month to a season (Winter, Spring, Summer, Fall). Adjust the season\_mapping dictionary if you need a different seasonal breakdown.
   * Groups data by season and calculates the mean for avg\_temp and precipitation.

**Error Handling**

* **ValueError:** Checks for necessary columns and valid date format, ensuring that the data is ready for monthly and seasonal aggregations.
* **KeyError:** Checks for the existence of a month column, which is required for seasonal mapping.
* **General Exception Handling:** Catches unexpected errors for troubleshooting.

This code will output the calculated monthly and seasonal averages, displaying the results for quick review. Let me know if you'd like any further customization!

**NOTE:** While this code seems to be great it also gave us two separate functions, we could maybe try and have it simplify the code by providing a follow-up enhancement prompt. The second function relies on the first being run in order to create the month column. It might make more sense to combine these into a singular function. This would fall under the Refinement & Optimization step of the process (step 5).

**Enhanced Prompt:** “Could you combine both of these functions into one to simply the usage and creation of new columns”

###### AI Response

```
import pandas as pd  
  
def calculate_monthly_and_seasonal_averages(df):  
    try:  
        # Check for required columns  
        required_columns = {'date', 'max_temp', 'min_temp', 'precipitation'}  
        if not required_columns.issubset(df.columns):  
            raise ValueError("Dataframe must contain 'date', 'max_temp', 'min_temp', and 'precipitation' columns.")  
  
        # Ensure 'date' column is datetime type  
        df['date'] = pd.to_datetime(df['date'], errors='coerce')  
        if df['date'].isnull().any():  
            raise ValueError("Invalid date values found after parsing. Please ensure date format is consistent.")  
  
        # Calculate average temperature as (max_temp + min_temp) / 2  
        df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2  
  
        # Extract month from date  
        df['month'] = df['date'].dt.month  
  
        # Define season mapping  
        season_mapping = {  
            12: 'Winter', 1: 'Winter', 2: 'Winter',  
            3: 'Spring', 4: 'Spring', 5: 'Spring',  
            6: 'Summer', 7: 'Summer', 8: 'Summer',  
            9: 'Fall', 10: 'Fall', 11: 'Fall'  
        }  
        df['season'] = df['month'].map(season_mapping)  
  
        # Calculate monthly averages  
        monthly_averages = df.groupby('month').agg({  
            'avg_temp': 'mean',  
            'precipitation': 'mean'  
        }).rename(columns={'avg_temp': 'monthly_avg_temp', 'precipitation': 'monthly_avg_precipitation'}).reset_index()  
  
        # Calculate seasonal averages  
        seasonal_averages = df.groupby('season').agg({  
            'avg_temp': 'mean',  
            'precipitation': 'mean'  
        }).rename(columns={'avg_temp': 'seasonal_avg_temp', 'precipitation': 'seasonal_avg_precipitation'}).reset_index()  
  
        print("Monthly and seasonal averages calculated successfully.")  
        print("Monthly Averages:")  
        print(monthly_averages)  
        print("\nSeasonal Averages:")  
        print(seasonal_averages)  
  
        return monthly_averages, seasonal_averages  
  
    except ValueError as ve:  
        print(f"ValueError: {ve}")  
        return None, None  
    except KeyError as ke:  
        print(f"KeyError: {ke} - Ensure all required columns are present.")  
        return None, None  
    except Exception as e:  
        print(f"Unexpected error: {e}")  
        return None, None  
  
# Usage example, assuming df is the validated dataframe  
monthly_averages, seasonal_averages = calculate_monthly_and_seasonal_averages(df)
```

###### [Data Visualization Prompt](#dpPanel5)

"Use Seaborn and matplotlib to create python visualization code to show:

1. **Line plot**: Monthly temperature trends
2. **Bar plot:** Seasonal rainfall patterns
3. **Box plot:** Temperature extremes by month
4. Make sure to include clear labels and titles
5. Utilize the data aggregated from previous functions."

###### AI Response

```
import seaborn as sns  
import matplotlib.pyplot as plt  
  
def plot_weather_trends(monthly_averages, seasonal_averages, df):  
    # 1. Monthly Temperature Trends  
    plt.figure(figsize=(10, 6))  
    sns.lineplot(data=monthly_averages, x='month', y='monthly_avg_temp', marker='o')  
    plt.title("Monthly Average Temperature Trend")  
    plt.xlabel("Month")  
    plt.ylabel("Average Temperature (°C)")  
    plt.xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun",   
                                           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])  
    plt.grid(True)  
    plt.show()  
  
    # 2. Seasonal Rainfall Patterns  
    plt.figure(figsize=(8, 6))  
    sns.barplot(data=seasonal_averages, x='season', y='seasonal_avg_precipitation', palette='cool')  
    plt.title("Seasonal Average Rainfall")  
    plt.xlabel("Season")  
    plt.ylabel("Average Precipitation (mm)")  
    plt.grid(axis='y')  
    plt.show()  
  
    # 3. Temperature Extremes by Month  
    plt.figure(figsize=(10, 6))  
    sns.boxplot(data=df, x='month', y='avg_temp', palette='viridis')  
    plt.title("Temperature Extremes by Month")  
    plt.xlabel("Month")  
    plt.ylabel("Temperature (°C)")
```

##### Step 4. Testing and Validation

It's crucial to test and validate LLM-generated code for several key reasons:

1. Hallucination Risk  
   * LLMs can generate code that looks plausible but contains subtle errors or non-existent functions
   * They may mix different library versions or create invalid syntax that appears correct at first glance
   * The code might be structurally sound but solve the wrong problem
2. Context Limitations  
   * LLMs may miss important edge cases or fail to account for specific system requirements
   * They lack real-world testing environment awareness
   * Generated code might not handle error conditions properly
3. Security Concerns  
   * LLMs might inadvertently generate code with security vulnerabilities
   * They may include deprecated or unsafe functions
   * Input validation and sanitization might be incomplete
4. Performance Considerations  
   * Generated code might not be optimized for performance
   * Resource usage and scalability issues might not be apparent
   * There could be hidden inefficiencies in algorithms or data structures
5. Integration Issues  
   * The code might not properly integrate with existing systems
   * Dependencies and version compatibility need verification
   * Environment-specific configurations might be incorrect

An initial inspection of the generated code/functions shows no major errors or concerns. We addressed some slight optimization issues as well by asking for both analysis functions (month and season) to be combined into one.

You could even use your Generative AI tool to generate code that will produce a sample of synthetic data that matches the appropriate structure in order to test out your functions on ‘known’ information to ensure calculations are being run correctly.

```
import pandas as pd  
import numpy as np  
  
def generate_synthetic_weather_data(start_date='2023-01-01', end_date='2023-12-31'):  
    # Generate date range  
    dates = pd.date_range(start=start_date, end=end_date, freq='D')  
    num_days = len(dates)  
  
    # Generate temperature data  
    # Average temperature variations, can vary by location and climate specifics  
    max_temps = np.random.normal(loc=25, scale=10, size=num_days)  # mean=25, std=10  
    min_temps = max_temps - np.random.normal(loc=10, scale=2, size=num_days)  # mean difference from max  
  
    # Ensure min_temp does not exceed max_temp  
    min_temps = np.minimum(max_temps - 1, min_temps)  
  
    # Generate precipitation data (mm)  
    precipitation = np.random.gamma(shape=2, scale=5, size=num_days)  # Gamma distribution for positive skew  
  
    # Introduce dry and wet spells  
    precipitation[np.random.rand(num_days) > 0.8] = 0  # 80% chance of no rain  
  
    # Generate humidity data (%)  
    humidity = np.random.normal(loc=70, scale=10, size=num_days).clip(30, 100)  # mean=70%, bounded by [30, 100]  
  
    # Generate wind speed data (km/h)  
    wind_speed = np.random.normal(loc=15, scale=5, size=num_days).clip(0, 50)  # mean=15 km/h, bounded by [0, 50]  
  
    # Combine into a DataFrame  
    data = pd.DataFrame({  
        'date': dates,  
        'max_temp': max_temps.round(1),  
        'min_temp': min_temps.round(1),  
        'precipitation': precipitation.round(1),  
        'humidity': humidity.round(1),  
        'wind_speed': wind_speed.round(1)  
    })  
  
    return data  
  
# Generate synthetic data  
synthetic_weather_data = generate_synthetic_weather_data()  
print(synthetic_weather_data.head())  
  
monthly_averages, seasonal_averages = calculate_monthly_and_seasonal_averages(synthetic_weather_data)  
  
  
plot_weather_trends(monthly_averages, seasonal_averages, synthetic_weather_data)  
  
synthetic_weather_data[synthetic_weather_data['month'] == 1]['avg_temp'].mean(), monthly_averages.iloc[0]['monthly_avg_temp']
```

**Output:**

```
(20.716129032258063, 20.716129032258067)
```

##### Step 5. Refinement & Optimization

Given our use of good prompt engineering practices above, the code produced requires little refinement for our purposes. We showcased how to ask the Generative AI tool to simplify the two functions into one, streamlining that analysis function so it makes more sense for the flow of our code. A next step might be to incorporate these generated functions into a python script to run our analysis and produce the visualizations seamlessly in one step. We could use AI prompting to help accomplish this as well.

The one big thing we could ask the Generative model to help us with is to create docstring documentation for each of these functions. We should have asked for this in the prompts themselves but can certainly have it generate them afterwards. Documentation is vitally important!

**Simple Docstring Prompt:**

“Could you please generate short doc strings for each of the functions you created above”

###### AI Response

```
def load_weather_data(file_path):  
    """  
    Loads weather data from a CSV file and parses the date column.  
  
    Parameters:  
    - file_path (str): Path to the CSV file.  
  
    Returns:  
    - DataFrame: Loaded weather data with parsed dates, or None if an error occurs.  
    """  
  
def validate_weather_data(df):  
    """  
    Validates the weather data by checking for missing values, duplicates,   
    outliers, and consistency issues in temperature and precipitation data.  
  
    Parameters:  
    - df (DataFrame): The weather data to validate.  
  
    Returns:  
    - DataFrame: Cleaned and validated DataFrame or None if validation fails.  
    """  
  
def calculate_monthly_and_seasonal_averages(df):  
    """  
    Calculates monthly and seasonal averages for temperature and precipitation.  
  
    Parameters:  
    - df (DataFrame): The weather data with 'date', 'max_temp', 'min_temp', and 'precipitation' columns.  
  
    Returns:  
    - Tuple(DataFrame, DataFrame): Monthly averages DataFrame and seasonal averages DataFrame.  
    """  
  
def plot_weather_trends(monthly_averages, seasonal_averages, df):  
    """  
    Generates plots for monthly temperature trends, seasonal rainfall patterns,  
    and monthly temperature extremes.  
  
    Parameters:  
    - monthly_averages (DataFrame): Monthly aggregated temperature and precipitation data.  
    - seasonal_averages (DataFrame): Seasonal aggregated temperature and precipitation data.  
    - df (DataFrame): Original weather data including daily temperature data for extremes analysis.  
  
    Returns:  
    - None: Displays plots for analysis.  
    """
```

### Scenario 2: E-commerce Returns Debug

**E-commerce Returns Debug Scenario:** A colleague's code for analyzing product returns is producing incorrect results. The total return rate seems unusually high, and some categories are showing over 100% return rates.

#### **The Problematic Code:**

```
def calculate_return_rates(sales_df):  
    returns = len(sales_df[sales_df['return_flag'] == True])  
    total = len(sales_df)  
      
    category_returns = sales_df.groupby('category')['return_flag'].count()  
    category_totals = sales_df.groupby('category')['order_id'].count()  
      
    return {  
        'overall_rate': returns/total,  
        'category_rates': category_returns/category_totals  
    }
```

#### **Task:**

Use AI to:

* Identify the bugs
* Fix the calculation
* Add proper validation
* Implement error handling

#### **Prompt:**

“Help me debug and fix this return rate calculation code. The current code is showing rates over 100% and seems incorrect. Include an explanation of the fix that was implemented. Please also include error handling. I have provided the code here: <insert code from above>”

##### AI Response

The primary issue here is with calculating category\_returns. The code currently counts all entries in each category rather than specifically counting returns, which can lead to incorrect and inflated return rates. I'll correct this by filtering the return\_flag column for each category before counting.

Here’s the modified code with added error handling and an explanation of the implemented changes:

```
def calculate_return_rates(sales_df):  
    try:  
        # Ensure 'return_flag' column exists and is boolean  
        if 'return_flag' not in sales_df.columns or sales_df['return_flag'].dtype != 'bool':  
            raise ValueError("DataFrame must contain a 'return_flag' column with boolean values.")  
  
        # Ensure 'category' and 'order_id' columns exist  
        if 'category' not in sales_df.columns or 'order_id' not in sales_df.columns:  
            raise ValueError("DataFrame must contain 'category' and 'order_id' columns.")  
  
        # Calculate total returns and total entries  
        returns = sales_df['return_flag'].sum()  # Only summing True values for returns  
        total = len(sales_df)  
  
        # Calculate returns and totals by category  
        category_returns = sales_df[sales_df['return_flag'] == True].groupby('category')['return_flag'].count()  
        category_totals = sales_df.groupby('category')['order_id'].count()  
  
        # Calculate return rates with error handling for zero division  
        overall_rate = returns / total if total > 0 else 0  
        category_rates = (category_returns / category_totals).fillna(0)  # Avoid NaN from zero division  
  
        return {  
            'overall_rate': overall_rate,  
            'category_rates': category_rates.to_dict()  
        }  
  
    except ValueError as e:  
        print(f"Error: {e}")  
        return None  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  
        return None
```

**Explanation of Fixes:**

1. **Category Return Calculation:** We fixed the category\_returns calculation by filtering return\_flag == True before grouping by category. This way, only the rows where a return actually occurred are counted, avoiding over-counting.
2. **Error Handling:**  
   * **Missing Columns and Data Types:** Added checks to ensure required columns exist with expected data types, raising an error with a helpful message if not.
   * **Zero Division:** Guarded the overall rate calculation to avoid division by zero and used .fillna(0) for category rates to handle any potential zero division at the category level.
3. **Return Format:** Converted the category\_rates output to a dictionary for easier access and use in subsequent code.

### Scenario 3: Marketing Campaign Query

**Marketing Campaign Query Scenario:** The marketing team needs to identify customers for a targeted email campaign based on specific purchasing behaviors.

* [SQL Database Schema](#dpPanel8Content)
* [Task](#dpPanel9Content)
* [Prompt](#dpPanel10Content)
* [AI Response](#dpPanel11Content)

#### SQL Database Schema

**customers:**

* customer\_id
* email
* join\_date
* region

**purchases:**

* purchase\_id
* customer\_id
* purchase\_date
* amount
* product\_id

**products:**

* product\_id
* Category
* price\_tier

#### Task

Generate a SQL query to find:

* Customers who made purchases in the last 3 months
* Spent over $500 total
* Bought products from at least 2 different categories
* Located in specific regions

#### Prompt

“Help me write a SQL query to find customers for a marketing campaign based on the given conditions below. The SQL database contains the following tables and fields:

* **customers**
  + customer\_id -
  + email -
  + join\_date -
  + region
* **purchases**
  + purchase\_id
  + customer\_id
  + purchase\_date
  + amount
  + product\_id
* **products**
  + product\_id
  + category
  + price\_tier

**Conditions:**

* Customers who made purchases in the last 3 months
* Spent over $500 total
* Bought products from at least 2 different categories
* Located in specific regions”

#### AI Response

```
WITH recent_purchases AS (  
    SELECT   
        p.customer_id,  
        SUM(p.amount) AS total_spent,  
        COUNT(DISTINCT pr.category) AS category_count  
    FROM   
        purchases p  
    JOIN   
        products pr ON p.product_id = pr.product_id  
    WHERE   
        p.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)  
    GROUP BY   
        p.customer_id  
),  
qualified_customers AS (  
    SELECT   
        rp.customer_id  
    FROM   
        recent_purchases rp  
    WHERE   
        rp.total_spent > 500  
        AND rp.category_count >= 2  
)  
  
SELECT   
    c.customer_id,  
    c.email,  
    c.join_date,  
    c.region  
FROM   
    customers c  
JOIN   
    qualified_customers qc ON c.customer_id = qc.customer_id  
WHERE   
    c.region IN ('Region1', 'Region2', 'Region3'); -- Replace with specific regions
```

**Explanation of the Query:**

1. **recent\_purchases CTE**:  
   * Joins purchases and products to find purchases in the last 3 months and calculates the total amount spent by each customer and the number of distinct categories they purchased from.
2. **qualified\_customers CTE**:  
   * Filters customers who spent over $500 and bought from at least 2 different categories.
3. **Final SELECT**:  
   * Joins customers with qualified\_customers and filters for the specified regions.

### Common Challenges

1. **Data Type Management Challenge**  
   * AI may generate code without proper data type handling.
   * Datetime conversions often need specific formatting.
   * Numeric calculations might have precision issues.
   * **Solution:** Better engineering of prompt to include specific data validations, provide sample data format so model can infer, specify rounding or not for numerical calculations.
2. **Error Handling Challenge**  
   * Generated code often lacks robust error handling.
   * Edge cases might be overlooked.
   * Missing data handling needs attention.
   * **Solution:** Prompt engineering again! Providing sample of data can really help the model infer the structure and potential edge cases, give it examples of extreme edge cases to ensure it can handle them, specify exact null value/missing data handling techniques that you want (i.e. do not impute null values, use median, impute based on season, etc…).
3. **Performance Considerations**  
   * AI might generate inefficient code.
   * Large dataset handling needs optimization.
   * Memory usage might be excessive.
   * **Solution:** Manually inspecting all code generated will help you catch inefficiencies if they exist. Example of generated code using iterrows() to loop through a DataFrame when Pandas has implemented a more efficient way to accomplish this. Including in prompt the memory usage is an issue to consider. Utilize role-based prompting to have the generative AI model attempt to improve its own code performance.
4. **Documentation and Maintainability**  
   * AI-generated code might lack proper documentation.
   * Variable names might be unclear.
   * Code structure might be confusing.
   * **Solution:** Better prompt engineering, specify the data structure and any naming conventions to follow to ensure variables align. Ask the generative model to explain its output to you, and/or provide documentation for the code produced generated.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248430

Scraped At: 2026-05-15T10:03:03.714368
