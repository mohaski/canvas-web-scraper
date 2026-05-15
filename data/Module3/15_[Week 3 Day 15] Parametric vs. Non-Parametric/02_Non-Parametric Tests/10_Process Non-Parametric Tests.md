# Process: Non-Parametric Tests

# Process: Non-Parametric Tests

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631704/preview) Process of Non-Parametric Tests

Icon Progress Bar (browser only)

2 min read

This process helps ensure that your analysis is both statistically sound and practically meaningful. Each step builds on the previous ones, creating a logical flow from initial assessment to final interpretation.

### Step 1: Assess Your Data and Research Question

Before choosing any test, you need to thoroughly understand what you're working with and what you're trying to learn. This foundational step shapes all subsequent decisions.

This connects directly to performing EDA. You need to evaluate whether parametric tests are unsuitable for use. This step confirms that you really need non-parametric methods. Sometimes what seems like a clear violation of parametric assumptions might be manageable through transformations.

Check if you are meeting your necessary assumptions via both visuals and tests. Determine if transformations will make logical sense and work or will you need to revert to non-parametric tests instead.

### Step 2: Select the Appropriate Non-parametric Test

With a clear understanding of your data and confirmation that non-parametric methods are needed, you can choose the right test for your situation.

* Two Independent Groups: Mann-Whitney U
* Paired Samples: Wilcoxon Signed-Rank
* Multiple (>2) Groups: Kruskal-Wallis
* Correlation: Spearman's Rank
* Categorical Data: Fisher's Exact or Chi-Square

### Step 3: Implement the Test and Check Assumptions

Even non-parametric tests have some assumptions, though fewer than parametric tests. This step ensures your chosen test is valid for your data. Most tests assume independent observations (other than Wilcoxon).

### Step 4: Interpret Results and Assess Practical Significance

The final step involves not just looking at p-values but understanding what the results mean in your practical business context.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248755

Scraped At: 2026-05-15T10:24:01.397746
