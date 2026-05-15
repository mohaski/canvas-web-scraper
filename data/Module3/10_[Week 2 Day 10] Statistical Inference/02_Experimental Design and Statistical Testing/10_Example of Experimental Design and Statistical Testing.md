# Example of Experimental Design and Statistical Testing

# Example of Experimental Design and Statistical Testing

## ![](https://moringa.instructure.com/courses/1426/files/631696/preview) Example: Experimental Design and Statistical Testing

Icon Progress Bar (browser only)

5 min read

You're a junior data analyst at Morning Brew, and the company has introduced a new brewing method at select locations. The Operations Manager claims this new method maintains coffee at a hotter temperature when served to customers. Your task is to determine if there's statistical evidence supporting this claim.

### Business Context

* Customer satisfaction strongly correlates with coffee serving temperature.
* The ideal serving temperature is between 175-185°F.
* The old brewing method averages around 172°F.
* The new method claims to serve at 182°F.

First, we need to **clearly state what we're testing**: "Does the new brewing method actually produce hotter coffee than our current method?" Start with two competing theories:

1. **The Null Hypothesis (H₀):** The new method doesn't produce hotter coffee. This is like saying "nothing special is happening".
2. **The Alternative Hypothesis (H₁):** The new method does produce hotter coffee.

#### Planning Our Data Collection

We need to be thoughtful about how we collect our evidence. Think about variables that might affect coffee temperature:

* Time of day
* Ambient temperature
* How long after brewing we measure
* Which barista is making the coffee

To make our test fair, **we need to control for these factors**. We might decide to:

* Take measurements at the same times each day.
* Use the same thermometer.
* Measure immediately after brewing.
* Train baristas to follow exact procedures.

#### Collecting the Data

Just like a chef doesn't judge a recipe based on one dish, we need multiple measurements. You decide to measure a sample of cups from each method.

You **use a power analysis to determine the necessary sample size** in order to limit how much coffee you are collecting data from in order to minimize day-to-day business operations.

#### Looking at Initial Patterns

Before doing any complex statistics, we look at the basic patterns.

* **Old method average:** about 178°F
* **New method average:** about 182°F
* **Difference:** about 4°F hotter with the new method

This looks promising, but we need to be sure this difference isn't just random chance. After all, even with the same brewing method, we don't get exactly the same temperature every time.

#### Conducting the Statistical Test

Now we ask the key question: ***"If the new method actually made no difference (if H₀ were true), how likely would we be to see a difference this large just by chance?"***

This is where the p-value comes in. In our case, we **calculate how likely it would be to see a 4°F difference if there really was no actual difference** in temperature between methods. If this probability (the p-value) is very small (less than 5%), we conclude the difference is real, not just random chance.

#### Interpreting the Results

Let's say our test shows the difference is statistically significant (p < 0.05). What does this really mean? It tells us:

* The temperature difference we observed is very unlikely to have happened by chance.
* We have good evidence that the new method really does produce hotter coffee.
* We can be confident (at our alpha level) in reporting this finding to management.

### Scenario: Mobile App Navigation Redesign

Imagine you've joined a mobile app company as a junior data scientist. The product team has redesigned the app's navigation menu, claiming it will help users find features more quickly. Your task is to design and analyze an experiment to test if the new navigation actually improves user experience.

#### Planning Our Data Collection

First, we transform the broad business question into specific, **measurable research questions:**

* "Does the new navigation design reduce the time users take to find and access key features?"
* "Does it decrease the number of navigation errors users make?"

We carefully specify our variables:

##### Primary Outcome Variables

* Time to complete common tasks (measured in seconds)
* Success rate in finding specific features (binary yes/no)
* Number of navigation errors (count)

##### Control Variables (things we keep constant)

* App performance/speed
* Feature functionality
* Content availability
* Time of day for measurements

##### Potential Confounding Variables

* User experience level
* Device type
* App version
* Network conditions

#### Initial Patterns

To ensure valid results, we implement several controls:

##### For User Assignment

* Use a random hash of user IDs to consistently assign users to either control (old navigation) or treatment (new navigation) group
* Ensure new users are evenly distributed between groups
* Keep users in the same group throughout the experiment

##### For Environmental Factors

* Only include users on the latest app version
* Record and account for device types
* Measure during normal usage periods

#### Conducting the Statistical Analysis

We set up our hypothesis test:

* **Null Hypothesis (H₀)**: The new navigation design does not reduce task completion time
* **Alternative Hypothesis (H₁)**: The new navigation design reduces task completion time.

With known current task completion times averaging 45 seconds with a standard deviation of 12 seconds, we:

1. Set significance level α = 0.05.
2. Determine we want to detect a minimum improvement of 5 seconds.
3. Calculate required sample size using power analysis.
4. Plan to run a one-sided t-test (since we're only interested in improvement).

#### Interpreting Results

After collecting data from our predetermined sample size, we:

1. Clean and validate the data.
2. Check assumptions about normality and variance.
3. Conduct our statistical test.
4. Interpret results in both statistical and practical terms.

**For example, if we find:**

* **Mean task time (old navigation):** 44.8 seconds
* **Mean task time (new navigation)**: 38.2 seconds
* **p-value:** 0.003
* **Observed reduction:** 6.6 seconds (14.7% improvement)

**We can conclude** that the new navigation system shows both statistical significance (p < 0.05) and practical significance (exceeding our minimum desired improvement of 5 seconds)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248570

Scraped At: 2026-05-15T10:12:14.791506
