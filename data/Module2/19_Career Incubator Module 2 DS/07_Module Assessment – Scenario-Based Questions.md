# Module Assessment – Scenario-Based Questions

# Module Assessment – Scenario-Based Questions

Each question presents a realistic data science scenario and asks you to apply module concepts. Read each scenario carefully before selecting your answer.

 

## **Question 1**

|  |  |
| --- | --- |
| **You have completed an EDA showing that customer churn increases sharply for users who have not logged in for 21+ days. You must present this finding to two groups in the same afternoon: (1) the engineering team who will build a re-engagement notification system, and (2) the VP of Marketing who will approve the budget. What is the most effective communication approach?** | |
| **A** | Use the same slide deck for both audiences but speak to each group differently. |
| **B** | **Prepare separate presentations: show the engineering team the statistical model details and confidence intervals; show the VP the churn rate trend in plain language with a projected revenue impact.  ✓ CORRECT** |
| **C** | Lead with the revenue impact for both audiences, since money motivates everyone. |
| **D** | Skip the VP meeting and send an email summary — executives don't need the details. |
| **Instructor Rationale:**  *Answer B demonstrates audience calibration: the technical team needs the model details to build correctly, while the VP needs the business case. Using the same deck risks confusion for both (A). Leading with revenue for engineers is misaligned to their decision (C). Skipping stakeholder engagement is a project management failure (D).* | |

 

## **Question 2**

|  |  |
| --- | --- |
| **You are creating a visualization showing the relationship between monthly advertising spend (KSh 0–5M) and monthly new customer acquisitions (0–2,000 customers) across 36 months of data. Which chart type is most appropriate?** | |
| **A** | Stacked bar chart grouped by quarter |
| **B** | **Scatter plot with a trend line (regression line)  ✓ CORRECT** |
| **C** | Pie chart showing share of spend by month |
| **D** | Line chart with two y-axes — one for spend, one for acquisitions |
| **Instructor Rationale:**  *A scatter plot is the correct choice for visualizing the relationship (correlation) between two continuous variables. The question asks about the relationship, not the trend over time. A stacked bar chart is for part-to-whole comparisons (A). A pie chart cannot show relationships (C). A dual-axis line chart could show trends over time but obscures the relationship between the variables and is easily misread (D).* | |

 

## **Question 3**

|  |  |
| --- | --- |
| **Your manager asks you to write an executive summary of your analysis by 9 AM tomorrow. The first sentence of your draft reads: 'Using a random forest classifier with 87% cross-validated accuracy, we identified the top three features predictive of customer lifetime value: recency, frequency, and average order value.' What is the primary problem with this sentence as an executive summary opener?** | |
| **A** | It is factually incorrect — cross-validation is not an appropriate metric for a random forest. |
| **B** | **It leads with methodology rather than the business insight, making it inaccessible to a non-technical executive.  ✓ CORRECT** |
| **C** | It is too short. Executive summaries should open with more context. |
| **D** | It uses passive voice, which weakens the impact. |
| **Instructor Rationale:**  *The sentence is technically accurate but it is written for a data scientist, not an executive. The most effective executive summary leads with the business finding ('The three factors that most predict how much a customer will spend over their lifetime are how recently they bought, how often they buy, and their average order size'). Methodology belongs later, if at all. (A) is incorrect — cross-validation is appropriate. (C) and (D) are minor issues that are not the primary problem.* | |

 

## **Question 4**

|  |  |
| --- | --- |
| **You are two weeks into a six-week data project when you discover that the primary dataset is missing 40% of values for one of your key variables. This variable is essential to your original analysis plan. What is the correct project management response?** | |
| **A** | Continue with the original plan and note the data gap in a footnote of the final report. |
| **B** | **Immediately stop work, inform your project sponsor of the risk, and propose three options: imputation with documented assumptions, finding a proxy variable, or descoping that dimension of the analysis.  ✓ CORRECT** |
| **C** | Delete the incomplete records and proceed with the 60% that are complete. |
| **D** | Extend the project deadline by two weeks without informing the stakeholders. |
| **Instructor Rationale:**  *This is a scope and risk management decision. Discovering a material data quality issue requires immediate stakeholder communication and a structured decision about how to proceed — not a unilateral choice to proceed anyway (A, C) or to hide a timeline change (D). Offering three options demonstrates professional judgment and keeps the sponsor in control of the trade-off decision.* | |

 

## **Question 5**

|  |  |
| --- | --- |
| **You are showing an audience a bar chart comparing quarterly sales across five regions. One region (Northern) has a bar that is noticeably taller than the others. An audience member says: 'This clearly shows Northern is outperforming the others.' What additional context should you immediately provide as the presenter?** | |
| **A** | Agree with the observation and move on — the chart speaks for itself. |
| **B** | **Note whether Northern had a larger sales team, a different product mix, or any other structural differences that could explain the gap — correlation does not imply causation from one chart alone.  ✓ CORRECT** |
| **C** | Tell the audience member that they are misreading the chart. |
| **D** | Add a trend line to the bar chart to show the growth rate. |
| **Instructor Rationale:**  *A single bar chart showing absolute values cannot explain why a region performs better. A responsible data communicator immediately contextualizes findings — is it headcount? Geography? Product? This demonstrates the difference between data literacy and data communication. (A) is passive and potentially misleading. (C) is confrontational and incorrect — the observation is valid but incomplete. (D) adds information but does not address the underlying causation question.* | |

 

## **Question 6**

|  |  |
| --- | --- |
| **A colleague presents a donut chart with 11 segments to show the percentage breakdown of customer support tickets by issue type. Six of the 11 segments are under 5% each. What is the most fundamental visualization design problem?** | |
| **A** | Donut charts are never appropriate for professional presentations. |
| **B** | **The chart violates the principle of pre-attentive processing: human eyes cannot accurately compare areas and angles of many small segments. A horizontal bar chart sorted by frequency would allow instant comparison.  ✓ CORRECT** |
| **C** | The color palette is probably wrong — 11 colors are hard to distinguish. |
| **D** | The legend should be embedded in the chart rather than placed to the side. |
| **Instructor Rationale:**  *The core problem is that pie/donut charts are weak encoders for many-category comparisons because humans are poor at judging angles and areas. With 11 segments, this is especially problematic. A sorted bar chart encodes information in bar length, which humans compare accurately and quickly. (A) is too absolute — donut charts can work for 2–4 segments. (C) is a real secondary problem, but not the fundamental one. (D) is a minor formatting preference.* | |

 

## **Question 7**

|  |  |
| --- | --- |
| **You are scoping a new 10-week data project. Your project sponsor wants weekly status updates but has only 15 minutes available each week. What is the most effective communication format for these weekly updates?** | |
| **A** | A detailed written report covering all work completed that week |
| **B** | A verbal catch-up call covering everything the team did |
| **C** | **A structured one-page status summary: progress against milestones, key decisions needed, one risk flagged, and next steps — delivered by email before the call so the sponsor can pre-read  ✓ CORRECT** |
| **D** | A full slide deck updated each week to reflect current progress |
| **Instructor Rationale:**  *A one-page pre-read maximizes the sponsor's limited time by eliminating information dumps during the meeting. The sponsor can pre-read and arrive with questions, making the 15 minutes decision-focused. A detailed report (A) exceeds what a sponsor can digest weekly. A verbal-only update (B) is inefficient and leaves no written record. A full deck (D) is disproportionate for a 15-minute check-in.* | |

 

## **Question 8**

|  |  |
| --- | --- |
| **You have built a model that predicts hospital readmission risk with 85% accuracy. The hospital administrator wants to present this to the Board as '85% accuracy.' What is the most important caveat you should raise before approving this framing?** | |
| **A** | **Accuracy is a misleading metric when the classes are imbalanced. If only 10% of patients are readmitted, predicting 'no readmission' for everyone would also give 90% accuracy. The Board needs to understand precision, recall, or F1-score to evaluate real predictive value.  ✓ CORRECT** |
| **B** | 85% accuracy is too low for medical applications and should not be presented at all. |
| **C** | The Board will not understand any accuracy metric so you should present it as a risk score instead. |
| **D** | You should round up to 90% for a cleaner presentation. |
| **Instructor Rationale:**  *This question tests both statistical literacy and ethical communication. Class imbalance makes raw accuracy misleading in medical contexts — a model that predicts no one will be readmitted could have 90% 'accuracy' while being completely useless. A responsible data communicator raises this before the metric is misrepresented to a Board making resource decisions. (B) is incorrect — 85% may be acceptable depending on context. (C) avoids the problem rather than solving it. (D) is unethical.* | |

 

## **Question 9**

|  |  |
| --- | --- |
| **Your team is behind schedule on a data project. The root cause is that data cleaning took three times longer than estimated. Going forward, which project management practice would most directly prevent this problem in future projects?** | |
| **A** | Hire more junior analysts for future data cleaning tasks |
| **B** | **Add a formal data quality assessment sprint at the start of future projects — before any analysis begins — to sample the data, profile it, and update time estimates based on actual quality  ✓ CORRECT** |
| **C** | Avoid projects where data quality is unknown |
| **D** | Use agile methodology — daily standups would have caught the delay earlier |
| **Instructor Rationale:**  *The systematic fix is to treat data quality assessment as a planned work item, not an assumption. A data profiling sprint early in the project converts an unknown risk into a known variable that can be estimated and communicated. (A) addresses symptoms, not the planning failure. (C) is not realistic — most real-world datasets have quality issues. (D) helps detect the delay earlier but does not prevent the root cause.* | |

 

## **Question 10**

|  |  |
| --- | --- |
| **You have created a dashboard for a retail client that shows daily sales, inventory levels, and customer foot traffic. During the demo, the client says: 'This is great, but can you also add social media sentiment analysis and competitor price tracking?' How should you respond?** | |
| **A** | Agree immediately — the client is always right and these are reasonable additions |
| **B** | Decline firmly — the scope was defined upfront and cannot change |
| **C** | **Acknowledge the request positively, note that these are out of the original scope, and propose a formal scope change process — including impact on timeline and cost — before committing to anything  ✓ CORRECT** |
| **D** | Add the features over the weekend without telling anyone, then present the expanded dashboard as a bonus |
| **Instructor Rationale:**  *This is a classic scope creep scenario. The professional response acknowledges the value of the request without committing to it, and introduces a structured change management process. (A) is scope creep — agreeing without assessing impact is poor project management. (B) is inflexible and damages the client relationship. (D) sets a dangerous precedent and hides information from stakeholders.* | |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/252683

Scraped At: 2026-05-14T21:26:04.630012
