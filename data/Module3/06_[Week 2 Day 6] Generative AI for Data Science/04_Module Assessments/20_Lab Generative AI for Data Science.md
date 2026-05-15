# Lab: Generative AI for Data Science

## ![](https://moringa.instructure.com/courses/1426/files/631398/preview?) Lab: Generative AI for Data Science

In this lab, you will work on three separate real-world scenarios. Each scenario will have a task for you to complete, along with a discussion component highlighting differences in generated code based on the individual prompts used. The focus is on learning how different prompting strategies can lead to various generated solutions.

Recall the prompt engineering process:

1. Problem Definition & Scope
2. Context Setting & Framework
3. Initial Prompt Construction
4. Refinement & Testing
5. Iteration & Optimization

As well as the more general process for generating code:

1. Requirement Analysis & Planning
2. Development Strategy
3. Iterative Code Generation
4. Testing & Validation
5. Refinement & Optimization

### Instructions

You will be working in an independent Jupyter notebook for each exercise where you will enter the information below. For each exercise, you will share the prompts used and the resulting generated code in the respective canvas discussion. As a part of this discussion, be sure to explain why you set up your prompt in that manner and any potential hurdles you may have encountered.

**For each exercise:**

1. Write your AI prompt.
2. Save the generated code.
3. Document any follow-up prompts.
4. Share results with your peers.

```
# Your Prompt:  
[Copy your prompt here]  
  
# Generated Code:  
[Copy the AI-generated code]  
  
# Follow-up Prompts:  
[List any clarifying prompts you used]  
  
# Final Solution:  
[Your working code after refinements]
```

After you have completed the AI prompts and code portion of the lab, you must complete the discussion portion that follows in this module. The questions are included here and in the discussion prompt.

#### [Scenario 1: Retail Inventory Analysis](#dpPanel0)

**Scenario:** You're working at a retail chain analyzing inventory turnover. The store manager needs to understand stock movement patterns to optimize ordering.

**Data Structure: DataFrame**

* product\_id
* category
* stock\_level
* last\_restock\_date
* sales\_last\_30\_days
* supplier\_lead\_time
* unit\_cost

**Task: Generate code to:**

* Calculate inventory turnover rates.
* Identify slow-moving items.
* Predict potential stockouts.
* Create visualizations.

**Discussion Questions to Answer:**

1. How did different prompts handle date calculations?
2. What visualization approaches were suggested?
3. How was error handling implemented?

#### [Scenario 2: Website Analytics Debug](#dpPanel1)

**Scenario:** The marketing team reports that the user engagement metrics code is showing impossible results (bounce rates over 100%, negative session times).

**Problematic Code:**

```
def analyze_user_engagement(logs_df):  
    metrics = {  
        'bounce_rate': logs_df.groupby('session_id')['page_views'].apply(  
            lambda x: x == 1).mean(),  
        'avg_session_time': logs_df.groupby('session_id')['duration'].sum(),  
        'pages_per_session': logs_df.groupby('session_id')['page_views'].mean()  
    }  
      
    device_metrics = logs_df.groupby('device_type').agg({  
        'session_id': 'count',  
        'duration': 'mean',  
        'page_views': 'sum'  
    })  
      
    return metrics, device_metrics
```

**Task:**

* Debug the calculations.
* Add data validation.
* Implement proper time calculations.
* Create summary visualizations.

**Discussion Questions:**

1. How did different prompts approach error identification?
2. What validation methods were suggested?
3. How was time handling improved?

#### [Scenario 3: Customer Segmentation Query](#dpPanel2)

**Scenario:** The product team needs to segment customers based on their purchasing behavior for a new feature rollout.

**Database Schema:**

* user\_activity
  + user\_id
  + last\_login\_date
  + feature\_usage\_count
  + account\_type
* transactions
  + transaction\_id
  + user\_id
  + transaction\_date
  + amount
  + platform
* user\_preferences
  + user\_id
  + communication\_preference
  + interface\_theme
  + notification\_settings

**Task: Create a SQL query to identify:**

* Active users (logged in last 30 days)
* Filter by high-value customers (top 20% by spending)
* User preference trends for the identified customers

**Discussion Points:**

1. How were percentile calculations handled?
2. What approaches to date filtering were used?
3. How was the query optimized, CTE, subquery etc…?

### Submission and Grading Criteria

1. Review the rubric below for grading criteria.
2. Complete this assignment using a Jupyter Notebook.
3. When you are ready, submit a link to your notebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248434

Scraped At: 2026-05-15T10:03:17.527421
