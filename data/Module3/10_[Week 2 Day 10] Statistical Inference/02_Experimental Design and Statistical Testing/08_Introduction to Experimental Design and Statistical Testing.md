# Introduction to Experimental Design and Statistical Testing

# Introduction to Experimental Design and Statistical Testing

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Introduction to Experimental Design and Statistical Testing

* [Page: Introduction to Statistical Inference (1 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248552 "Page: Introduction to Statistical Inference (1 of 16)")
* [Page: Introduction to Sampling, Confidence Intervals, and The Central Limit Theorem (2 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248556 "Page: Introduction to Sampling, Confidence Intervals, and The Central Limit Theorem (2 of 16)")
* [Page: What is Statistical Inference? (3 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248558 "Page: What is Statistical Inference? (3 of 16)")
* [Page: Examples of Statistical Inference (4 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248559 "Page: Examples of Statistical Inference (4 of 16)")
* [Page: Process of Statistical Inference (5 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248560 "Page: Process of Statistical Inference (5 of 16)")
* [Page: Summary of Statistical Inference (6 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248562 "Page: Summary of Statistical Inference (6 of 16)")
* [Page: Check for Understanding: Sampling, Confidence Intervals, and The Central Limit Theorem (7 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248564 "Page: Check for Understanding: Sampling, Confidence Intervals, and The Central Limit Theorem (7 of 16)")
* [Page: Current: Introduction to Experimental Design and Statistical Testing (8 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248566 "Page: Current: Introduction to Experimental Design and Statistical Testing (8 of 16)")
* [Page: What is Experimental Design and Statistical Testing?  (9 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248568 "Page: What is Experimental Design and Statistical Testing?  (9 of 16)")
* [Page: Example of Experimental Design and Statistical Testing  (10 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248570 "Page: Example of Experimental Design and Statistical Testing  (10 of 16)")
* [Page: Process of Experimental Design and Statistical Testing  (11 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248571 "Page: Process of Experimental Design and Statistical Testing   (11 of 16)")
* [Page: Summary: Experimental Design and Statistical Testing (12 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248572 "Page: Summary: Experimental Design and Statistical Testing (12 of 16)")
* [Page: Check for Understanding: Experimental Design and Statistical Testing (13 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248575 "Page: Check for Understanding: Experimental Design and Statistical Testing (13 of 16)")
* [Page: Technical Lesson: Experimental Design and Statistical Testing (14 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248577 "Page: Technical Lesson: Experimental Design and Statistical Testing (14 of 16)")
* [Lab: Experimental Design and Statistical Testing (15 of 16), Assignment](https://moringa.instructure.com/courses/1426/modules/items/248580 "Lab: Experimental Design and Statistical Testing (15 of 16), Assignment")
* [Quiz: Statistical Inference (16 of 16)](https://moringa.instructure.com/courses/1426/modules/items/248583 "Quiz: Statistical Inference (16 of 16)")

3 min read

In modern data-driven organizations, making reliable decisions requires both careful experimental design and rigorous statistical testing.

Imagine you're a data scientist at an e-commerce company, and your product manager asks:

***"Will changing our website's 'Buy Now' button from blue to green increase purchases?"***

While it might be tempting to just make the change and see what happens, proper experimental design combined with statistical testing helps us be confident that any changes we observe are actually due to our modifications and not random chance or other factors.

When you're designing an experiment or analysis, you start with a question about a population, like all your website visitors or all your customers. Since it's usually impossible or impractical to study the entire population, you work with a sample. **The way you collect and analyze this sample is crucial to making valid conclusions.**

The process flows naturally from design to analysis:

1. **Experimental Design** forms the foundation, helping us plan how to collect reliable data.
2. **Statistical Testing** provides the framework for drawing valid conclusions from that data.

Imagine you're working at an e-commerce company, and the marketing team has launched a new email campaign. They believe it will increase average order value by at least $5 compared to the current campaign. Your job is to determine if there's statistical evidence to support this claim.

The distribution of order values typically follows patterns we can model mathematically. For example, order values might follow a normal distribution, or for count data, a Poisson distribution. Understanding these distributions is crucial because they form the basis for our statistical tests.

Now, let's frame this as a statistical (hypothesis) test:

* **Null Hypothesis (H₀):** The new email campaign has no effect on average order value (μnew - μold = 0)
* **Alternative Hypothesis (H₁)**: The new email campaign increases average order value (μnew - μold)

This is where probability distributions come in. **Under the null hypothesis, we can calculate the probability of seeing our observed difference in order values if there truly was no effect.** This probability (the p-value) helps us decide whether to reject the null hypothesis in favor of the alternative hypothesis. This procedure is known as hypothesis or statistical testing and allows one to provide a measure of confidence when comparing differences in experimental groups.

In your day-to-day work as a data scientist, you'll use these concepts to:

* Design and analyze A/B tests for website changes, email campaigns, or product features.
* Evaluate the effectiveness of new algorithms or models.
* Make data-driven recommendations to stakeholders.
* Validate whether observed differences are statistically significant.
* Draw reliable conclusions from data.

The key is understanding that this isn't just about running tests; **it's about running the right tests in the right way to get reliable answers.** Poor experimental design or incorrect statistical analysis can lead to false conclusions and costly business mistakes.

### Resources

* [Documentation for power analysis in python using statsmodels


  Links to an external site.](https://www.statsmodels.org/dev/stats.html#power-and-sample-size-calculation)
* [Further reading into different measures of effect size


  Links to an external site.](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/effect-size/)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248566

Scraped At: 2026-05-15T10:12:01.607066
