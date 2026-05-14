# Defining Data Collection and Sampling Techniques

# Defining Data Collection and Sampling Techniques

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Defining Data Collection and Sampling Techniques

Icon Progress Bar (browser only)

11 min read

Generally speaking, collected data is a **sample** from the larger set of examples existing in the world (**population**). Let us flush out the fundamental concepts of population and sample and the connection between the two.

* **Population:** The population represents the entire collection of elements relevant to a given research question. This can be finite, like all customers of a specific online retailer, or effectively infinite, like all social media users worldwide. An understanding of the structure and composition characteristics of a population is crucial for designing an appropriate data collection strategy.
* **Sample:** Due to practical limitations or resource constraints, we often resort to studying a sample, a subset of the population chosen for data collection. Elements of a sample are selected from the population **at random**. The big idea, of course, is that this randomly selected subset is representative of the population – allowing us to draw inferences about the larger group.  
  ![People icons representing a population and the process of sampling.](https://moringa.instructure.com/courses/1406/files/624694/download)
* **Sampling Bias:** Sampling bias occurs when the sample chosen from a population does not accurately represent the entire population. This can happen because some members of the population have a higher chance of being selected than others. The result is a skewed sample that misrepresents the true characteristics of the population. This bias can lead to misleading inferences and undermines the generalizability of research findings.

### Sample Size and Strategies for Data Collection

There are two main considerations when collecting data (a sample) that we wish to use in making inferences about a population:

**Sample Size:** You need to collect a sample of adequate size to ensure that your collected sample can reliably be used to infer statistical characteristics of your population. This seems straightforward enough but it turns out that estimating the minimum number of samples you need is not necessarily straightforward. It relies heavily on what you know about the population and the complexity of its structure. In addition, it will depend on the quantities/relationships you are interested in. A systematic consideration lies in the domains of experimental design and statistical learning theory — subjects out of scope for this course. But it is important to be aware that a paucity of data is a problem.

**Sampling strategy:** The manner in which the random sampling is carried out will also affect how well a sample reflects the population. There are many sampling strategies that exist which aim to preserve the representativeness of a sample. What method you choose will depend on the structure of the population relevant to the problem (if known) *and* limitations in the data acquisition process. There are four sampling techniques that are most important.

### Simple Random Sampling (SRS)

Simple random sampling involves picking a subset of members from a given population out at random. This process assumes that you have access to the entire population and that you have a method of random selection that ensures that each member could be chosen with equal probability. Assigning a unique number to each member and selecting a sample by lottery might be one way this could be achieved.

![Simple Random Sampling Process Illustration with steps to take](https://moringa.instructure.com/courses/1406/files/624996/download)

**Example:** You had a population of ~700 8th graders in a very large school and wanted to get a broad idea of their current BMIs (body-mass index). You could access every member of the population and measure their BMI but this would be a pain. However, you surmise that you could get an idea of how BMIs are distributed within the grade by simple random sampling of a much smaller subset of ~ 30 students from the population. Thus you get all the students in a gym, have them draw numbers and call out thirty of those numbers at random. Then you measure the BMIs for these thirty individuals.

* **Strengths:** SRS is efficient to implement and statistically straightforward.
* **Weaknesses:** SRS can be problematic for populations that are heterogenous and particularly where different subgroups have differing degrees of representation in the population. Simple random sampling can result in a sample being drawn that does not maintain the proportion of each subgroup present in the population.

### Stratified Sampling

This technique divides the population into subgroups or strata based on relevant characteristics (e.g., age bracket, sex, ethnicity). Random samples are then drawn from each subgroup proportional to the relative sizes in the population. This method ensures that representation of various subgroups within the sample are commensurate with the population.

![Stratified sampling example of different populations respecting the population proportions ](https://moringa.instructure.com/courses/1406/files/624712/download)

* **Strengths:** Stratified sampling is ideal for ensuring representation of subgroups within the population are preserved in a sample.
* **Weaknesses:** Stratified sampling requires knowledge of relevant stratification variables and the proportion of each strata within a population. It also can be more logistically complex to implement than SRS given the need to sort each member of a population into the correct strata before executing sampling.

### Cluster Sampling

![](https://moringa.instructure.com/courses/1406/files/625276/download)

This sampling strategy is useful when you need to collect data over a vast geographical area or over a large number of organizations/groups. A simple example would be a survey study testing sentiment about wind parks in rural farming communities across America.

Going around and getting population level data is unfeasible. This is where cluster sampling comes in. The big idea here is that you randomly sample clusters of the population. In the above case, each rural farming community is a cluster. You would then randomly sample these clusters thus constructing a randomly chosen set of rural farming communities from which you will test individuals for sentiment.

#### One vs. Two Stage Clustering

The simplest version of cluster sampling, known as **single-stage cluster sampling**, would be that your clusters are chosen from a pool by random selection and that you survey all members within each cluster.

A straightforward extension is **two-stage cluster sampling**. This is where you randomly select clusters and then get a random sample of a subset of members from each cluster. This would be done in cases where collecting all data from a given cluster is impractical (e.g., surveying every household in selected mid-sized urban cities to assess internet usage patterns in mid-sized urban centers across America). We illustrate the distinction below:

![Single stage clustering and two stage clustering comparison](https://moringa.instructure.com/courses/1406/files/624849/download)

Random selection first occurs for clusters at the population level. Random selection then occurs again within each cluster.

##### **Random Selection Considerations**

The process of cluster sampling can be tricky and easily introduce bias. One major concern centers about the random cluster selection process. If you are conducting two-stage cluster sampling, there is the added concern of what sampling strategy you employ within a given cluster.

**Simple Random Cluster Sampling:** The easiest case is when the clusters that you draw from do not themselves occupy strata (i.e. groups of clusters) with different typical characteristics and representation in the population. In this case, you can use *simple random sampling* of clusters (i.e. select rural farming communities using SRS from the population of such communities across the US). Then you could select all members of each community in a single-cluster sampling scheme. Or if you are conducting two-stage cluster sampling and expect no strata relevant to the survey within each community, you can use SRS within each cluster.

**When Life Gets More Complicated:** It may be that there are, in fact, strata of clusters on the population level. Rural farming communities that center on live-stock may have different concerns about wind parks than those occupied mainly in crop farming. There may also be strata based on which state each community is located in – i.e. different states have different tax incentives for allowing wind farms to be built on or near your property. In these cases, you would need to employ stratified sampling strategies at the cluster level before figuring out how you sample within each cluster. After this, if employing two-step cluster sampling, you need to see whether simple random selection or stratified sampling is required. As you can see, this can be a tricky business. *Cluster sampling needs to be done with care if it is to reflect population level statistics.*

* **Strengths:** Cluster sampling can be cost-effective and efficient for geographically dispersed populations.
* **Weaknesses:** Cluster sampling can lead to biased estimates if clusters are not representative of the population. Ensuring that this is the case requires a good deal of research and logistics/planning.

### Sequential Sampling

Some data is, by nature, collected and analyzed sequentially. This is a case where the sampling is not fixed in advance. Rather, you are faced with a stream of events from which you sample as required. A classic case would be when doing quality analysis on a manufacturing line. You want to periodically test whether manufacturing conditions have changed in some way that affects the overall rate of defect introduction to part production. While it would be prohibitive to carefully inspect each part being produced, you might sequentially sample every 1000th piece being produced and measure defects systematically. As you take more samples, you can potentially get more confident estimates of whether conditions on the manufacturing line have changed.

![Sequential sampling of boxed products on an conveyor](https://moringa.instructure.com/courses/1406/files/624692/download)

Sequential sampling is also common when data is hard to acquire and therefore sampling events can not occur very frequently. Here, you have no choice but to sample sequentially and build up estimates of a given quantity you are interested in – as well as your confidence in this estimate – as you go. A nice example of this is when measuring the extent and nature of a contaminant plume in groundwater. Drilling into aquifers can be an expensive and very tricky process. Careful initial sampling can provide a first quantification of plume extent and suggest where to sample next. As  high quality samples are built up in sequence, once can start to build robust estimates of plume extent and composition. This, in turn, will inform possible containment and cleanup strategies.

* **Strengths:** Sequential sampling is a natural option when the data naturally comes in as a stream. It can also be very good when measure when resources are limited and measurements are hard. Sequential sampling can enable you to determine where best to sample next to get robust and accurate estimates with as few measurements as possible.
* **Weaknesses:** Sequential sampling requires careful design and requires some expertise in statistical inference.

### How Does it Work?

There are two ways in which you will encounter sampling strategy considerations. The first will be when you are actually designing an experiment and considering how your data ought to be collected to optimize representation.

The second involves looking retrospectively at a dataset you have been handed or acquired from another source. In this case, you will likely need to think about how the data was collected (i.e. the random sampling strategies employed) and whether it supports unbiased estimation of a relevant characteristic of the population you are trying to uncover.  If not, you might possibly have to consider strategies to modify or resample the dataset using the aforementioned strategies to better reflect what you know about the population.

### Conceptualize Sampling

Sampling type with definition and example

| Concept | Definition | Example |
| --- | --- | --- |
| Simple Random Sampling (SRS) | Each member of the population has an equal probability of being selected. | Selecting 100 students from a school list using a random number generator to understand average test scores. |
| Stratified Sampling | The population is divided into subgroups (strata) based on relevant characteristics, and a random sample is drawn proportionally from each subgroup. | Dividing a customer base by age group (strata) and then randomly selecting 100 customers from each age group to understand product preferences. |
| Cluster Sampling | The population is divided into groups (clusters) based on convenience or geographical location. A random sample of clusters is selected, and members within those clusters are included in the sample. | Selecting a random sample of schools from different districts (clusters) and surveying students within those schools to understand student attitudes towards a new curriculum. |
| Sequential Sampling | Data is collected and analyzed sequentially. Based on the initial analysis, a decision is made to either collect more data or stop. | A market researcher interviews potential customers about a new product concept. After 20 interviews, if a clear preference emerges, they stop collecting data. If the results are inconclusive, they continue interviewing until a statistically significant conclusion is reached. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243520

Scraped At: 2026-05-14T20:49:01.207817
