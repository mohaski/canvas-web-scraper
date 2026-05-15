# Lab: A/B Testing- Digital Experimentation

## ![](https://moringa.instructure.com/courses/1426/files/631644/preview?) Lab: A/B Testing- Digital Experimentation

You're a junior data scientist at BookWise, a popular online reading subscription platform that offers unlimited access to ebooks and audiobooks for a monthly fee. **The product team has identified a concerning trend**: while new user sign-ups are strong, only 35% of users convert from the free trial to a paid subscription.

The team **hypothesizes that the current onboarding experience, which immediately prompts users to browse the full catalog, might be overwhelming**. They propose testing a guided onboarding experience where users select their preferred genres and reading habits first, followed by a curated selection of books matching their interests.

**Your task is to design and plan an A/B test to evaluate this hypothesis.** Rather than implementing the technical solution, you'll focus on developing the experimental framework and decision-making process.

### Tools and Resources

* [A/B Testing Lab Template:


  Links to an external site.](https://docs.google.com/spreadsheets/d/1P3IEZP4xaCLcvEhXG-Z_WU3aQ88MLSaWTFFG3GmIM_0/copy "Link") Create a copy of this template to use for completing this lab.

### Instructions

For each step of the experimentation process, answer the following reflection questions. Provide detailed explanations for your thinking and decision-making process.

#### **Tips for Success**

* Take time to think through each step before writing your answers.
* Be specific and provide clear reasoning for your decisions.
* Consider multiple perspectives: user, business, and technical.
* Make your assumptions explicit.
* Think about how different parts of your experiment design connect.
* Draw on examples from the technical lesson to inform your thinking.

#### [Part 1: Hypothesis Formation](#dpPanel0)

When crafting a hypothesis for A/B testing, we need to be much more precise than simply saying "We think this change will help." A good hypothesis is specific, measurable, and tied to business outcomes. Think about what exactly we expect to change and why. Consider both the direct effects we're hoping for and potential indirect effects we should monitor.

1. **Write a formal hypothesis statement** for this experiment. Why did you structure it this way? Think about: What specific outcome do you expect? What's the mechanism by which your change will create this outcome? How will you measure success?
2. **What would you select as your primary metric? Why?**   
     
   **Consider:** Which metric most directly measures the outcome you care about? What are the trade-offs between different possible metrics? How will you ensure the metric is both meaningful and measurable?
3. List **three secondary metrics you would track**. Explain why each is important.
4. What are **potential confounding variables** you need to consider?

#### [Part 2: Experimental Design](#dpPanel1)

Designing an experiment involves careful balancing of statistical validity, practical constraints, and business needs. We need to ensure our experiment will detect meaningful changes while running within a reasonable timeframe. As you work through these questions, think about how each decision affects both the reliability of our results and our ability to act on them.

1. **How would you define the minimum detectable effect for this experiment?** Walk through your reasoning. You won’t have exact numbers, instead describe what you would need to consider.
2. **What user segments might be particularly important to analyze? Why?**
3. **How long would you run this experiment?** Explain your reasoning considering:

* + Current conversion rate (35%)
  + MDE of a relative increase in conversion rate of 5%
  + Approximately 2,000 new trial users per week
  + Business desire to make a decision within 8 weeks

#### [Part 3: Technical Setup Planning](#dpPanel2)

Just as a building needs a solid foundation, A/B tests require robust technical infrastructure to produce reliable results. While you may not implement the technical components yourself, understanding these elements helps you design better experiments and communicate effectively with engineering teams. Consider how technical decisions impact experimental validity and your ability to trust the results. Think about both obvious and subtle ways that implementation choices could introduce bias or measurement errors into your experiment.

1. **What could cause sample ratio mismatch in this experiment? List three potential issues.**   
     
   *Think about: How might the new onboarding flow itself affect user behavior? What technical issues could arise when tracking users across multiple pages? How might different devices or connection speeds impact our measurement?*
2. **How would you validate that users are being assigned correctly to variants?**   
     
   *Consider: What patterns would indicate proper assignment? How could you verify consistency across sessions? What edge cases should you check for?*

#### [Part 4: Risk Assessment](#dpPanel3)

Every experiment carries risks - to user experience, to data quality, and to business metrics. A thorough risk assessment helps us prevent problems before they occur and catch issues early if they do arise. Think about risks from multiple angles: technical, user experience, and business perspectives.

For each risk you identify, try to think through both the immediate impact and potential downstream effects. Consider how risks might compound or interact with each other.

1. What are **three potential risks to the validity of this experiment?**
2. For each risk identified, explain:

* Why it's concerning.
* How you would mitigate it.
* What guardrail metrics you would implement to monitor it.

#### [Part 5: Risk Analysis](#dpPanel4)

A good analysis plan thinks beyond just "did it work?" to "how and why did it work?" and "for whom did it work?" By planning our analysis in advance, we avoid the temptation to cherry-pick results and ensure we can draw meaningful conclusions from our experiment.  
  
Think about how you'll handle different scenarios, both expected and unexpected. Consider what additional information you might need to understand your results fully.

1. **Under what conditions would you consider this experiment** a:

* Clear success
* Clear failure
* Inconclusive result requiring further investigation

2. **What segments of users would you plan to analyze separately?** Why?
3. **How would you handle edge cases** like users who start the trial but don't complete the onboarding process?

#### [Part 6: Business Impact Analysis](#dpPanel5)

Ultimately, experimentation needs to drive business value. This section asks you to connect statistical results to real business outcomes. Remember that business impact goes beyond just immediate revenue - consider long-term effects, resource requirements, and operational impacts.  
  
When calculating business impact, be explicit about your assumptions and consider both optimistic and pessimistic scenarios. Think about what factors might affect the reliability of your projections.

1. **If the experiment shows a 6 percentage point improvement in conversion rate:**

* What other factors would you consider before recommending full rollout?
* If this was less than the desired MDE, what might make you still consider recommending the change?

2. **What would your rollout strategy look like if the test is successful?**

### Submission and Grading Criteria

1. Review the rubric below for grading criteria before beginning this assignment.
2. Make a copy of [A/B Testing Lab Template


   Links to an external site.](https://docs.google.com/spreadsheets/d/1P3IEZP4xaCLcvEhXG-Z_WU3aQ88MLSaWTFFG3GmIM_0/copy "Link") complete the lab steps.
3. When you are done,[download your final spreadsheet as an .xlsx file](#transformedTip0Content).
4. Submit your final lab by uploading it below.

File/Download/Microsoft Excel (.xlsx)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248606

Scraped At: 2026-05-15T10:14:33.431016
