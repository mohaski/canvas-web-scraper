# Technical Lesson: Digital Experimentation- TechHealth Mobile App

# Technical Lesson: Digital Experimentation- TechHealth Mobile App

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson: Digital Experimentation- TechHealth Mobile App

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 1 hour**

You're a junior data scientist at TechHealth, a telemedicine company that connects patients with healthcare providers through a mobile app. The product team has noticed that while many patients schedule appointments, there's a significant drop-off between scheduling and attending the virtual consultations. The current attendance rate is 75%, and each missed appointment costs the company $45 in provider compensation.

The team hypothesizes that the current appointment reminder system (a single email 24 hours before) isn't effective enough. They want to test whether adding SMS reminders will improve attendance rates.

NOTE: A good portion of this process and code falls way more heavily into software engineering and data engineering than it does Data Science. We do not expect students to necessarily be able to produce the exact code. As the Data Scientist in the chain it is still vitally important that you understand the considerations and challenges so as to help set up A/B tests.

The video below will guide you through each step of the AB Testing Technical Lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of A/B Testing and Digital Experimentation.

[VIDEO LINK](https://player.vimeo.com/video/1060681558?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

* [Step 1: Structuring the Business Hypothesis](#dpPanel0Content)
* [Step 2: Technical Implementation](#dpPanel1Content)
* [Step 3: Monitoring and Analysis System](#dpPanel2Content)
* [Step 4: Running the Analysis](#dpPanel3Content)
* [Step 5: Preparing the Results Report](#dpPanel4Content)

### Step 1: Structuring the Business Hypothesis

Let's start by transforming this business question into a testable hypothesis. When transforming a business problem into an experiment, we need to be much more precise than simply asking "Will SMS reminders help?" Let's examine how we structure this properly:

```
experiment_definition = {  
    "business_question": "Will SMS reminders increase appointment attendance?",  
    "null_hypothesis": "Adding SMS reminders has no effect on appointment attendance rates",  
    "alternative_hypothesis": "Adding SMS reminders increases appointment attendance rates",  
    "minimum_detectable_effect": 0.05,  # 5% improvement needed to justify SMS costs  
    "primary_metric": "appointment_attendance_rate",  
    "secondary_metrics": [  
        "patient_satisfaction_score",  
        "provider_satisfaction_score",  
        "support_contact_rate"  
    ],  
    "guardrail_metrics": [  
        "app_crash_rate",  
        "system_error_rate"  
    ]  
}
```

This structured definition serves several crucial purposes:

* **The minimum detectable effect (5%) is carefully chosen because:**
  + SMS messages cost approximately $0.05 each.
  + The company loses $45 per missed appointment.
  + We need enough improvement to offset the SMS costs.
* **Secondary metrics help us understand broader impacts**:
  + Patient satisfaction tells us if people find the reminders annoying.
  + Provider satisfaction captures the doctor's perspective.
  + Support contact rate helps us monitor if the change creates confusion.
* **Guardrail metrics protect us from technical issues**:
  + App crash rate ensures our changes don't destabilize the system.
  + System error rate monitors for backend problems.

### Step 2: Technical Implementation

First, let's create the experiment infrastructure:

```
import hashlib  
from datetime import datetime  
from typing import Dict, List, Optional  
  
class Experiment:  
    def __init__(self, experiment_id: str, traffic_percentage: float = 0.5):  
        self.experiment_id = experiment_id  
        self.traffic_percentage = traffic_percentage  
        self.start_time = datetime.now()  
          
    def get_variant(self, user_id: str) -> str:  
        """  
        Deterministically assign users to variants using hashing  
          
        Args:  
            user_id: Unique identifier for the user  
              
        Returns:  
            str: 'control' or 'treatment'  
        """  
        # Create a deterministic hash combining user_id and experiment_id  
        hash_input = f"{user_id}:{self.experiment_id}".encode('utf-8')  
        hash_value = int(hashlib.sha256(hash_input).hexdigest(), 16)  
          
        # Use the hash to determine variant  
        is_in_experiment = (hash_value % 100) < (self.traffic_percentage * 100)  
        if not is_in_experiment:  
            return 'excluded'  
              
        return 'treatment' if (hash_value % 2) == 0 else 'control'  
          
    def is_eligible(self, user: Dict) -> bool:  
        """  
        Determine if a user is eligible for the experiment  
          
        Args:  
            user: Dictionary containing user information  
              
        Returns:  
            bool: Whether the user is eligible  
        """  
        return (  
            user.get('has_phone_number', False) and  # Must have phone number  
            user.get('communication_preferences', {}).get('sms_enabled', False) and  # SMS opted-in  
            user.get('appointment_count', 0) > 0  # Not their first appointment  
        )  
  
class ReminderExperiment(Experiment):  
    def __init__(self):  
        super().__init__('reminder_optimization_2024Q1')  
        self.metrics_calculator = MetricsCalculator()  
        self.notification_system = NotificationSystem()  
          
    def send_reminders(self, appointment: Dict) -> None:  
        """  
        Send reminders based on experiment variant  
          
        Args:  
            appointment: Dictionary containing appointment information  
        """  
        user_id = appointment['user_id']  
        variant = self.get_variant(user_id)  
          
        # Both groups get email  
        self.notification_system.send_email(  
            user_id=user_id,  
            template='appointment_reminder',  
            appointment_details=appointment  
        )  
          
        # Treatment group also gets SMS  
        if variant == 'treatment':  
            self.notification_system.send_sms(  
                user_id=user_id,  
                template='appointment_reminder_sms',  
                appointment_details=appointment  
            )  
          
        # Log the reminder event  
        self.log_reminder_event(user_id, variant, appointment['appointment_id'])
```

The technical implementation requires careful consideration of several factors. Let's break down the key components:

```
class Experiment:  
    def __init__(self, experiment_id: str, traffic_percentage: float = 0.5):  
        self.experiment_id = experiment_id  
        self.traffic_percentage = traffic_percentage  
        self.start_time = datetime.now()
```

**This base class initialization is important because:**

* The experiment\_id creates a unique identifier for tracking
* traffic\_percentage allows for gradual rollout (starting with 50% of users)
* start\_time helps with temporal analysis

 The variant assignment method is particularly crucial:

```
def get_variant(self, user_id: str) -> str:  
    """  
    Deterministically assign users to variants using hashing  
    """  
    hash_input = f"{user_id}:{self.experiment_id}".encode('utf-8')  
    hash_value = int(hashlib.sha256(hash_input).hexdigest(), 16)
```

**We use a cryptographic hash function (SHA-256) because:**

* It provides uniform distribution of users between variants
* It's deterministic - the same user always gets the same variant
* It's not reversible - we can't manipulate assignments
* The combination of user\_id and experiment\_id ensures independence between experiments

The eligibility checking is also critical:

```
def is_eligible(self, user: Dict) -> bool:  
    """  
    Determine if a user is eligible for the experiment  
    """  
    return (  
        user.get('has_phone_number', False) and  
        user.get('communication_preferences', {}).get('sms_enabled', False) and  
        user.get('appointment_count', 0) > 0  
    )
```

 These eligibility criteria are carefully chosen:

* Having a phone number is obviously required for SMS
* SMS opt-in respects user preferences and legal requirements
* Previous appointment history helps reduce noise in our data

### Step 3: Monitoring and Analysis System

Now let's implement the analysis system:

```
class MetricsCalculator:  
    def __init__(self):  
        self.db = DatabaseConnection()  
          
    def calculate_attendance_rate(self, variant: str,   
                                start_date: datetime,   
                                end_date: datetime) -> float:  
        """  
        Calculate attendance rate for a variant  
          
        Args:  
            variant: 'control' or 'treatment'  
            start_date: Start of analysis period  
            end_date: End of analysis period  
              
        Returns:  
            float: Attendance rate  
        """  
        query = """  
        SELECT   
            COUNT(CASE WHEN attended = TRUE THEN 1 END) * 100.0 / COUNT(*) as attendance_rate  
        FROM appointments  
        WHERE variant = %(variant)s  
            AND appointment_time BETWEEN %(start_date)s AND %(end_date)s  
        """  
          
        return self.db.execute_query(query, {  
            'variant': variant,  
            'start_date': start_date,  
            'end_date': end_date  
        })  
          
    def calculate_confidence_interval(self,   
                                   control_successes: int,   
                                   control_trials: int,  
                                   treatment_successes: int,   
                                   treatment_trials: int,  
                                   confidence_level: float = 0.95) -> Dict:  
        """  
        Calculate confidence interval for difference in proportions  
        """  
        from statsmodels.stats.proportion import proportion_effectsize  
        from statsmodels.stats.proportion import proportion_confint  
          
        # Calculate effect size  
        effect_size = (treatment_successes/treatment_trials) - (control_successes/control_trials)  
          
        # Calculate confidence interval  
        ci_low, ci_high = proportion_confint(count=treatment_successes,  
                                           nobs=treatment_trials,  
                                           alpha=(1 - confidence_level))  
          
        return {  
            'effect_size': effect_size,  
            'confidence_interval': (ci_low, ci_high)
```

The metrics calculator is where statistical rigor meets business reality:

```
def calculate_attendance_rate(self, variant: str,   
                            start_date: datetime,   
                            end_date: datetime) -> float:  
    query = """  
    SELECT   
        COUNT(CASE WHEN attended = TRUE THEN 1 END) * 100.0 / COUNT(*) as attendance_rate  
    FROM appointments  
    WHERE variant = %(variant)s  
        AND appointment_time BETWEEN %(start_date)s AND %(end_date)s  
    """
```

 This query is designed to:

* Calculate a true rate rather than raw numbers.
* Filter by specific date ranges to account for seasonality.
* Use parameterized queries for security.
* Handle NULL values appropriately.

 The confidence interval calculation is particularly important:

```
def calculate_confidence_interval(self,   
                               control_successes: int,   
                               control_trials: int,  
                               treatment_successes: int,   
                               treatment_trials: int,  
                               confidence_level: float = 0.95) -> Dict:
```

 We use proportion confidence intervals because:

* Attendance is a binary outcome (attended/didn't attend).
* We need to account for different sample sizes between groups.
* 95% confidence level is standard in business settings.

### Step 4: Running the Analysis

After collecting data for four weeks, let's analyze the results:

```
def analyze_experiment_results():  
    calculator = MetricsCalculator()  
      
    # Get results for both variants  
    control_metrics = calculator.get_metrics('control')  
    treatment_metrics = calculator.get_metrics('treatment')  
      
    # Calculate primary metric impact  
    attendance_impact = {  
        'control_rate': control_metrics['attendance_rate'],  
        'treatment_rate': treatment_metrics['attendance_rate'],  
        'absolute_improvement': (  
            treatment_metrics['attendance_rate'] -   
            control_metrics['attendance_rate']  
        ),  
        'relative_improvement': (  
            (treatment_metrics['attendance_rate'] -   
             control_metrics['attendance_rate']) /   
            control_metrics['attendance_rate'] * 100  
        )  
    }  
      
    # Calculate statistical significance  
    stats_results = calculator.calculate_confidence_interval(  
        control_metrics['attended'],  
        control_metrics['total'],  
        treatment_metrics['attended'],  
        treatment_metrics['total']  
    )  
      
    # Calculate business impact  
    business_impact = {  
        'monthly_appointments': 10000,  # from business data  
        'cost_per_missed_appointment': 45,  # dollars  
        'projected_annual_savings': (  
            10000 * 12 * attendance_impact['absolute_improvement'] * 45  
        )  
    }  
      
    return {  
        'metrics_impact': attendance_impact,  
        'statistical_results': stats_results,  
        'business_impact': business_impact  
    }
```

 The analysis needs to consider multiple aspects:

```
def analyze_experiment_results():  
    calculator = MetricsCalculator()  
      
    # Get results for both variants  
    control_metrics = calculator.get_metrics('control')  
    treatment_metrics = calculator.get_metrics('treatment')
```

We calculate both absolute and relative improvements:

* Absolute improvement (percentage points) is easier to communicate
* Relative improvement helps compare to other initiatives
* Both are needed for proper business decision making

```
business_impact = {  
        'monthly_appointments': 10000,    
        'cost_per_missed_appointment': 45,  
        'projected_annual_savings': (  
            10000 * 12 * attendance_impact['absolute_improvement'] * 45  
        )  
    }
```

 The business impact calculation:

* Uses actual appointment volume
* Includes real costs of missed appointments
* Projects annual impact for budget planning
* Can be used for ROI calculations

### Step 5: Preparing the Results Report

```
def generate_experiment_report(results: Dict) -> str:  
        """  
        Generate a comprehensive experiment report  
        """  
        report = f"""  
        A/B Test Results: Appointment Reminder Optimization  
        ================================================  
  
       Experiment Overview:  
       - Duration: 4 weeks  
       - Total Participants: {results['control_size'] + results['treatment_size']}  
       - Control Group Size: {results['control_size']}  
       - Treatment Group Size: {results['treatment_size']}  
  
       Results:  
       - Control Attendance Rate: {results['metrics_impact']['control_rate']:.1f}%  
       - Treatment Attendance Rate: {results['metrics_impact']['treatment_rate']:.1f}%  
       - Absolute Improvement: {results['metrics_impact']['absolute_improvement']:.1f}                    percentage points  
       - Relative Improvement: {results['metrics_impact']['relative_improvement']:.1f}%  
  
       Statistical Significance:  
       - P-value: {results['statistical_results']['p_value']:.4f}  
       - Confidence Interval: ({results['statistical_results']['confidence_interval'][0]:.1f}%,   
                           {results['statistical_results']['confidence_interval'][1]:.1f}%)  
  
       Business Impact:  
       - Projected Annual Savings:   
        ${results['business_impact']['projected_annual_savings']:,.2f}  
       - Implementation Cost (SMS): ${results['business_impact']['sms_cost']:,.2f}  
       - Net Annual Impact: ${results['business_impact']['net_impact']:,.2f}  
  
       Recommendation:  
       Based on the {results['metrics_impact']['absolute_improvement']:.1f} percentage point   
       improvement in attendance rates and projected annual savings of   
       ${results['business_impact']['net_impact']:,.2f}, we recommend implementing   
       SMS reminders for all appointments.  
  
       Next Steps:  
       1. Gradually roll out SMS reminders to all users over 4 weeks  
       2. Monitor system performance and costs during rollout  
       3. Conduct follow-up analysis after full rollout to verify results at scale  
       """  
      
    return report
```

The report structure follows a specific narrative:

1. Context and setup (what we tested and why)
2. Raw results (what happened)
3. Statistical validation (can we trust it)
4. Business impact (what it means)
5. Recommendation (what to do next)

This structure helps stakeholders:

* Quickly understand the key findings.
* Trust the statistical validity.
* See the business value.
* Know what actions to take.

### Considerations

When implementing digital experimentation and A/B testing, several critical decision points require careful consideration. Here are the key challenges and decisions teams commonly face, along with strategies for addressing them:

#### Hypothesis Formation and Metric Selection

**Challenge:** Teams often struggle with translating business questions into testable hypotheses and selecting appropriate metrics.Pros and cons of different approaches:

***Primary Metric Selections***

**Single Primary Metric**

* Pros: Clear decision-making, easier statistical analysis, focused development
* Cons: May miss important side effects, could lead to local optimization

**Multiple Primary Metrics**

* Pros: More comprehensive view of impact, catches unintended consequences
* Cons: Harder to reach statistical significance, complex decision making

***Guard Rail Metrics***The technical implementation demonstrates selecting both business and technical guardrails:

**Business guardrails (e.g., satisfaction scores)**

* Pros: Protects core business metrics, catches negative side effects
* Cons: Can slow down experimentation, may create false alarms

**Technical guardrails (e.g., error rates)**

* Pros: Early warning system for technical issues, prevents system degradation
* Cons: Requires additional monitoring infrastructure, can increase complexity

#### User Assignment and Traffic Allocation

**Challenge**: Determining how to assign users to variants while maintaining experimental validity.

*Traffic Allocation Strategies*

**Immediate 50/50 Split**

* Pros: Faster time to significance, simpler analysis
* Cons: Higher risk if issues occur, less time for technical validation

**Gradual Ramp-up**

* Pros: Safer rollout, allows for early issue detection
* Cons: Longer experiment duration, more complex analysis

***User Assignment Methods:*** The lesson shows using hash-based assignment:

**Cookie-based Assignment**

* Pros: Simple implementation, works for anonymous users
* Cons: Less stable across devices, can be cleared by users

**User ID-based Assignment**

* Pros: Consistent across sessions, more stable measurement
* Cons: Requires logged-in users, may introduce selection bias

#### Analysis and Monitoring

**Challenge**: Determining when and how to analyze results while maintaining statistical validity.

*Analysis Timing*

**Fixed Duration**

* Pros: Prevents p-hacking, clear resource allocation
* Cons: Might miss seasonal effects, could run longer than needed

**Sequential Analysis**

* Pros: Can end early on clear results, more efficient
* Cons: More complex statistics, higher risk of false positives

#### Eligibility Criteria

**Challenge**: Balancing between experimental cleanliness and business impact. The lesson demonstrates careful eligibility screening:

**Strict Criteria** (e.g., requiring previous appointment history)

* Pros: Cleaner data, more reliable results
* Cons: Smaller sample size, may not represent all users

**Loose Criteria**

* Pros: Larger sample size, more representative results
* Cons: Noisier data, harder to reach significance

#### Implementation Considerations

**Challenge**: Technical implementation complexity vs. measurement accuracy. The lesson shows a complex implementation with proper instrumentation:

**Full Featured System**

* Pros: Accurate measurement, robust experimentation
* Cons: High development cost, complex maintenance

**Minimal Viable Implementation**

* Pros: Faster to market, simpler maintenance
* Cons: May miss edge cases, less reliable data

#### Common Pitfalls to Address

**Sample Ratio Mismatch**: The lesson emphasizes checking for uneven variant distribution

* **Solution:** Implement automated monitoring and alerts for traffic splits

**Novelty Effects**: Users may behave differently simply because something is new

* **Solution:** Run experiments long enough for behavior to stabilize

**Interaction Effects**: Multiple concurrent experiments may interfere

* **Solution:** Implement proper experiment isolation and interaction tracking

**Data Quality Issues**: Missing or incorrect tracking can invalidate results

* **Solution:** Implement thorough QA processes and data validation checks

 Understanding these considerations helps teams make better decisions during experiment design and implementation, ultimately leading to more reliable results and better business decisions.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248603

Scraped At: 2026-05-15T10:14:18.942322
