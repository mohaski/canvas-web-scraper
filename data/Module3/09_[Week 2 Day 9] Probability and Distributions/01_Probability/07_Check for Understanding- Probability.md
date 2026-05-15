# Check for Understanding- Probability

# Check for Understanding- Probability

## ![](https://moringa.instructure.com/courses/1078/files/560252/preview) Check for Understanding- Probability

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

A data scientist is analyzing customer churn data and finds that 20% of all customers churn within 6 months, but among customers who file a support ticket, 40% churn within 6 months. What type of probability is the 40% figure?

Prior probability
:   Incorrect. This is incorrect because prior probability represents the initial probability of an event without considering any additional information (in this case, it would be the 20% overall churn rate). The 40% figure takes into account the condition of filing a support ticket.

Conditional probability
:   **Correct.**This is conditional probability because we're looking at the probability of churning given that a specific condition (filing a support ticket) has occurred. We write this as P(Churn|Support Ticket) = 0.40. The fact that this is higher than the overall churn rate (20%) suggests that customer service issues may be a significant factor in churn.

Independent probability
:   Incorrect. This is incorrect because independent probability means two events have no influence on each other. Here, we can see that filing a support ticket and churning are clearly related (40% vs 20% rates), so they are not independent events.

[Check Answer](#)

A machine learning model predicts customer lifetime value (CLV). Given the following:

* Prior belief: 30% of customers have high CLV
* Among high-CLV customers, 80% make frequent purchases
* Among low-CLV customers, 20% make frequent purchases

If a new customer makes frequent purchases, what is the probability they are a high-CLV customer?

30%
:   Incorrect. This is incorrect because this is just the prior probability of a customer having high CLV. It doesn't take into account the new information that the customer makes frequent purchases, which changes the probability.

63%
:   **Correct.**This requires Bayes' Theorem: P(High CLV|Frequent) = P(Frequent|High CLV) × P(High CLV) / P(Frequent) where P(Frequent) = 0.8 × 0.3 + 0.2 × 0.7 = 0.38 Therefore: (0.8 × 0.3) / 0.38 = 0.63 or 63%

44%
:   Incorrect. This is incorrect because this number doesn't properly apply Bayes' Theorem to combine the prior probability (30%) with the conditional probabilities of frequent purchases given CLV status (80% for high, 20% for low).

[Check Answer](#)

A data scientist observes that 15% of users click on recommended products, 25% click on trending products, and 5% click on both. When calculating the probability that a user clicks on either recommended OR trending products, they need to account for overlapping clicks. Which probability law is being applied here?

Law of Total Probability
:   Incorrect. This is incorrect because this law is used to calculate probabilities across mutually exclusive partitions of a sample space. Here, we're dealing with overlapping events, not partitions.

Multiplication Law of Probability
:   Incorrect. This is incorrect because this law is used to find the probability of two events occurring together (the intersection). Here, we're trying to find the probability of either event occurring (the union), which requires subtracting the overlap to avoid double counting.

Addition Law of Probability
:   **Correct.**This is a perfect example of the Addition Law of Probability. When we want to find the probability of either event occurring (recommended OR trending clicks), we need to add the individual probabilities (15% + 25%) but subtract the overlap (5%) to avoid double-counting. Using the Addition Law: P(Recommended or Trending) = P(Recommended) + P(Trending) - P(Both) = 0.15 + 0.25 - 0.05 = 0.35 or 35%. This shows why understanding overlap is crucial in real-world analytics.

[Check Answer](#)

When analyzing purchase data, a data scientist notices that buying product A has no impact on the likelihood of buying product B. The probability of buying each product remains unchanged regardless of whether the other was purchased. What type of events are these?

Independent events
:   Correct: These are independent events because the occurrence of one event (buying product A) doesn't affect the probability of the other event (buying product B). In mathematical terms, P(B|A) = P(B). This is particularly important in market basket analysis and recommendation systems, where understanding product purchase independence helps in creating accurate recommendation algorithms. Note that independence is different from mutual exclusivity - independent events can actually occur together, they just don't influence each other's probabilities.

Conditional events
:   Incorrect. This is incorrect because conditional events specifically refer to situations where one event's probability depends on the occurrence of another event. In this case, the probability of buying product B is explicitly stated to NOT depend on buying product A.

Dependent events
:   Incorrect. This is incorrect because dependent events are those where the probability of one event is affected by the occurrence of another event. Here, we're told that buying product A has no impact on buying product B, which is the opposite of dependency.

[Check Answer](#)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248511

Scraped At: 2026-05-15T10:08:48.844564
