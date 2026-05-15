# Examples of Digital Experimentation

# Examples of Digital Experimentation

## ![](https://moringa.instructure.com/courses/1426/files/631696/preview) Example of Digital Experimentation

Icon Progress Bar (browser only)

4 min read

Let's imagine you're a junior data scientist at a company called EduLearn, an online education platform that offers professional development courses. The product team has noticed that while many people browse their course catalog, the conversion rate from browsing to enrollment is lower than desired, currently at 8%.

The marketing team believes that the current course pages might be overwhelming potential students with too much information upfront. They want to test a simplified course page design that emphasizes key benefits and social proof before presenting detailed curriculum information.

Let's walk through how you'd approach this as a data scientist:

### Step 1: Hypothesis Formation and Strategic Planning

**Initial Questions to Consider:**

* What exactly do we want to learn?
* What metrics matter most?
* What could go wrong?

**You work with stakeholders to develop a structured hypothesis:** "Showing a simplified course page with key benefits and student testimonials before curriculum details will increase course enrollment rates by at least 2 percentage points by reducing cognitive load during the decision-making process."

**Key Decision Point:** Metric Selection 

**Primary Metric:** Course enrollment rate (enrollments/page views) 

**Secondary Metrics:**

* Time spent on page (to ensure simplification doesn't reduce engagement)
* Course completion rates (to verify we're not just making it easier to enroll in courses students won't complete)
* Revenue per visitor (to ensure we're not inadvertently reducing premium course enrollments)

### Step 2: Experimental Design Decisions

You need to make several critical decisions:

#### Population Selection

* Include all course pages or just certain categories?
* Include all visitors or only those from specific channels?

**Decision Made:** Start with high-traffic professional development courses only, all traffic sources included. This provides; faster time to statistical significance, more homogeneous course types for cleaner analysis, and sufficient volume for reliable results. 

#### Sample Size Planning - Current Metrics

* 8% baseline conversion rate
* 50,000 monthly visitors to eligible course pages
* Need to detect a 2 percentage point improvement
* 95% confidence level desired

**Decision Made:** Run the test for 4 weeks to get 200,000 visitors total, split evenly between variants. This gives 80% power to detect the target effect size.

### Step 3: Implementation Considerations

#### Key Technical Decisions

**Traffic Allocation:**

* Start with 10% of traffic for one week to verify tracking.
* Ramp up to 50/50 split if no issues found.
* Hold back 10% as control group for long-term comparison.

**User Assignment:**

* Use cookie-based assignment for returning visitors.
* Consider geographic distribution to account for timezone effects.
* Set up user exclusion rules for internal traffic.

### Step 4: Monitoring Plan Critical Checkpoints

**Week 1:**

* Verify tracking accuracy.
* Check for sample ratio mismatch.
* Monitor page load times.
* Review error rates.

**Weeks 2-4:**

* Watch for unusual patterns in secondary metrics.
* Monitor for segment-specific effects.
* Track any customer support tickets related to course pages.

### Step 5: Analysis and Decision Making

**After collecting data, the results:**

* **Control (Original)**: 8.1% conversion rate
* **Treatment (Simplified):** 9.7% conversion rate
* **Statistical Significance:** p < 0.001
* No negative impact on secondary metrics
* Consistent improvement across segments

**Business Impact:**

* 1.6 percentage point improvement in conversion rate
* Projected annual revenue increase: $450,000
* Customer satisfaction scores unchanged
* Course completion rates slightly improved

**Decision Point:** Despite not hitting the original 2 percentage point target, the consistent positive results across all metrics make this a clear win. The team decides to:

1. Roll out the simplified design to all professional development courses.
2. Begin testing similar simplifications in other course categories.
3. Document learnings about cognitive load and user decision-making for future experiments.

This example illustrates how A/B testing involves multiple decision points and requires balancing statistical rigor with business practicality. It also shows how careful planning and monitoring help ensure reliable results that can drive business decisions.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248597

Scraped At: 2026-05-15T10:13:59.255778
