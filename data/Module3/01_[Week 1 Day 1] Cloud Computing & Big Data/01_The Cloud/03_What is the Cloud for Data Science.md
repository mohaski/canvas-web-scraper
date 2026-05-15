# What is the Cloud for Data Science?

# What is the Cloud for Data Science?

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631314/preview) What is the Cloud for Data Scientists?

Icon Progress Bar (browser only)

15 min read

In data science, **cloud computing** refers to the use of remote servers, storage, and computing power accessible via the internet, rather than relying on local machines or on-premises infrastructure. Here are key terms and concepts related to cloud computing in data science:

### On-Premises Computing

Traditional IT setup where a company buys and maintains its own servers locally. This setup is less flexible and may lead to underused resources during low traffic and potential overloads during high demand.

### Cloud Platform

A cloud platform provides remote infrastructure that can be accessed on-demand via the internet. Major providers include AWS, Microsoft Azure, and Google Cloud. These platforms allow organizations to scale their resources based on need, paying only for what they use, without the need for local hardware.

### Scalability

One of the key advantages of cloud computing. It refers to the ability to increase or decrease resources (like storage and processing power) as demand changes, ensuring performance efficiency without overspending on unused capacity.

### On-Demand Resources

Cloud services allow users to request resources when needed and automatically adjust based on real-time demands, ensuring agility and preventing server overloads or underuse.

### Agility and Performance

The cloud offers greater agility by providing flexible and dynamic resources, leading to better performance. This is crucial for data scientists who often work with large datasets and need fast, powerful computations.

By using the cloud, data scientists can efficiently store, process, and analyze massive amounts of data without the constraints of local hardware, making it essential for modern data science workflows.

### How Does the Cloud Work for Data Scientists?

In a programming and data science context, cloud computing refers to accessing computing resources (servers, storage, databases, etc.) over the internet, instead of relying on local hardware. The cloud provides on-demand resources that developers and data scientists can utilize to build, deploy, and scale applications. Here’s how it works and why it’s significant in a technical context:

* **Infrastructure as a Service (IaaS):** Cloud platforms like AWS, Azure, and Google Cloud provide virtual machines, storage, and networking resources. Developers can write code or develop applications and run them on these virtual servers without managing physical hardware. This allows for flexibility and scalability based on workload demands.
* **Scalable Storage and Processing:** For tasks like machine learning, big data analysis, or any computation-heavy application, cloud services automatically allocate more or fewer resources based on real-time demand. This is especially important when working with large datasets or training machine learning models, where local machines would lack sufficient power.
* **APIs and Cloud Services Integration:** Many cloud platforms offer APIs and pre-built services that can be integrated into code. For instance, a data scientist working with Python can use cloud services to access storage (e.g., Amazon S3), or leverage powerful machine learning tools (e.g., AWS SageMaker) directly in their programming environment. This simplifies the process of building and deploying complex applications.
* **Software as a Service (SaaS):** Cloud-based software tools (e.g., Jupyter Notebooks hosted on the cloud, or version control tools like GitHub) are often used in programming. These services allow for collaboration, code sharing, and seamless workflow integration, making it easier for teams to work together without managing infrastructure.
* **Automated Scaling and Performance Management:** When running web applications or services, cloud platforms ensure that resources are automatically scaled based on traffic or data load. This prevents crashes or slow performance during peak demand times, ensuring that applications run smoothly without manual intervention.

### Relevance in Software Development and Data Science

For programmers and data scientists, cloud computing is highly significant because it removes the need for complex hardware setups and manual management. Instead, they can focus on writing code and solving business problems while the cloud handles resource allocation, scaling, and performance optimization.

For example, a developer building a web app doesn’t have to worry about server maintenance; instead, they can deploy the app on a cloud platform and scale resources automatically. Similarly, a data scientist analyzing massive datasets can use cloud-based storage and processing tools to handle large-scale computations efficiently.

Cloud computing empowers developers and data scientists by providing flexible, scalable, and on-demand resources, allowing them to build and run applications more efficiently without worrying about underlying infrastructure.

* [Why Would a Data Scientist Use Cloud Services?](#dpPanel0Content)
* [Cloud Instances/Containers](#dpPanel3Content)
* [Cloud Storage](#dpPanel4Content)
* [Pickling](#dpPanel5Content)

#### Why Would a Data Scientist Use Cloud Services?

The two main reasons a data scientist would use cloud services are to **get more computing power** and to **deploy machine learning models**.

* [More Computing Power](#dpPanel1Content)
* [Deploying ML Models](#dpPanel2Content)

##### More Computing Power

Particularly with large datasets and tools like grid search that fit many different model iterations, training a model can take a long time on a personal computer. Maybe you have already had the experience of running a model and having to step away from the computer for minutes or even hours as the fan spins and the computer works hard to perform all of the necessary computations.

###### **Hardware Acceleration**

![Close up view of the capacitors inside of a GPU.](https://moringa.instructure.com/courses/1426/files/631522/download)
As much as software libraries like NumPy or Spark can improve the efficiency of code, there is a limit to how much of a difference they can make, depending on the actual hardware of your computer.

As a general concept, hardware acceleration means using purpose-built hardware rather than general-purpose hardware.

###### Machine Learning Models

In the case of machine learning, this typically means running your code on a **GPU**, rather than a CPU. A CPU can do everything that a GPU can do, but it is not optimized for it, so it will likely take more time. This blog argues that a CPU is to a GPU as a horse and buggy is to a car.

One approach you might take would be to purchase a more powerful computer, with a GPU, more RAM, etc. and just use it for training models. But that can easily get very expensive!

With a cloud service, you can train a machine learning model using GPU hardware, so the training should complete much more quickly than on a typical personal computer. And unlike having a dedicated computer, you're only paying for the computing power when you need it!

###### Cloud Instances/Containers with GPUs

[![SSH Client and SSH Server send and receive diagram.](https://moringa.instructure.com/courses/1426/files/631395/download)](https://moringa.instructure.com/courses/1426/files/631395/download "SSH Client and SSH Server send and receive diagram.")

A cloud instance means you can run a customized, fully-fledged computer in the cloud. This often gives you the most fine-grained control but can also be much more expensive because they are not designed specifically for machine learning. Typically you will need to connect to a cloud instance via SSH, and you'll need to be comfortable navigating in a terminal interface.

AWS Elastic Compute Cloud (EC2) is probably the most well-known cloud instance, and our analysis found that it was mentioned in about 2% of entry-level Data Scientist job postings.

##### Deploying ML Models

While we are still learning the key skills and tooling to become a data scientist, we can mention one of the key aspects of data science here, viz. machine learning modeling, and then deploying those models.

Some key tools and techniques to be aware of for deploying models include model persistence (pickling), deploying as an API, and deploying as a full-stack web app.

###### Model Persistence

Recall that there is a difference between a file on disk and a variable in memory. Variables in memory only persist until the notebook kernel is shut down, whereas files on disk persist as long as there is functional storage hardware.

When you first train a model, it only exists in memory. The process for storing it on disk is called pickling. This is a type of serialization where the trained model gets stored in a file, conventionally using a .pkl extension.

The easiest way to get started with utilizing a GPU is by using a **cloud notebook**.

###### Cloud Notebooks

A cloud notebook means that you can work in a familiar notebook interface, while at the same time using more-powerful computational resources. You usually don't have to install or configure anything -- you can just start coding in a super-powerful cloud environment. Sometimes these cloud environments even have built-in GitHub integration, so you can complete the entire development process in the cloud! Some past Flatiron students have found cloud notebooks to be extremely helpful for building the kinds of models they wanted to build in the time they had.

There are also some downsides to cloud notebooks to be aware of:

* Sometimes you don't have precise control over the available **Python packages** and their versions. So, for example, you might want to use the latest version of TensorFlow, but the service you're using might not support it yet.
* Paid tools (including the AWS and Google Cloud Platform tools listed below) can quickly get very **expensive**. In particular, be very careful about completing tutorials or running other people's projects, because it's easy to use up a lot of compute resources. You will typically get some free credits when signing up for these services, and we recommend that you save them for your own portfolio projects. Make sure you always shut down your notebook instance when you're not using it.
* Some of these notebooks don't work with a straightforward file system like you do on your everyday DS setup. Instead of simply being able to call pd.read\_csv to open a file, you'll likely need to interact with a web API to pull in your data from a storage bucket or other virtual storage location.

Some popular cloud notebooks include:

* **[AWS SageMaker


  Links to an external site.](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html):** Professional-grade cloud JupyterLab instances (paid service, some free credits may be available).
* **[Google Cloud Notebooks


  Links to an external site.](https://cloud.google.com/vertex-ai/docs/workbench/user-managed?hl=en_US):** Professional-grade cloud JupyterLab instances (paid service, some free credits may be available).
* **[Google Colab


  Links to an external site.](https://research.google.com/colaboratory/):** More like the "Google Docs" of notebooks: not quite the same as a Jupyter notebook, and doesn't have access to a file system, but very fast to get started and 100% free.
* **[Kaggle Kernels


  Links to an external site.](https://www.kaggle.com/code):** Not exactly a Jupyter notebook, but a similar interface from Kaggle. Great if you're using a dataset from Kaggle Free, although you're limited to 30 hours per week of GPU time.
  + [Instructions on how to set up a GPU


    Links to an external site.](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu)
  + [Full documentation


    Links to an external site.](https://www.kaggle.com/docs/notebooks)
* **[Databricks Community Edition


  Links to an external site.](https://databricks.com/product/faq/community-edition):** Not exactly a Jupyter notebook, but a similar interface from Databricks. Free cloud Spark cluster functionality.

#### Cloud Instances/Containers

Sometimes you want to be able to run a full-fledged cloud computer, not just a notebook. With cloud instances, you can provision the necessary compute resources for completing essentially any task! You get root access to the file system and can run long-running scripts without overheating your personal computer. With Docker, you can even develop the code locally then deploy it online to speed up processing times.

There are also some downsides of cloud instances to be aware of:

* Similar to cloud notebooks, paid cloud instances can get very **expensive**. Pay particular attention to the amount of storage you are using, since a storage-specific solution might be a lot cheaper than a general-purpose cloud instance.
* Cloud instances require some **systems administration** skills. You'll likely need to configure access permissions and ports. Most containers are Linux-based so you'll need to be comfortable navigating and installing things using the terminal.

Some popular cloud instances include:

* [AWS EC2


  Links to an external site.](https://aws.amazon.com/ec2/):
  + [Instructions on training deep learning models with GPUs on EC2


    Links to an external site.](https://aws.amazon.com/blogs/machine-learning/train-deep-learning-models-on-gpus-using-amazon-ec2-spot-instances/)
* [Google Cloud Compute Engine


  Links to an external site.](https://cloud.google.com/compute/docs):
  + [Instructions on using GPUs for training models with Google Cloud Platform


    Links to an external site.](https://cloud.google.com/ai-platform/training/docs/using-gpus)
* [Azure Virtual Machines


  Links to an external site.](https://docs.microsoft.com/en-us/azure/virtual-machines/): Because this is made by Microsoft, they're one of the few places that offers Windows virtual machines
* [Oracle Cloud Infrastructure


  Links to an external site.](https://www.oracle.com/cloud/): Generous free tier

#### Cloud Storage

It's annoying to have huge data files taking up space on your laptop, and if you want to train your model in the cloud, your data also needs to be in the cloud. But for reasons related to hardware acceleration, it can get pretty expensive to store large datasets in general-purpose cloud services like an EC2 instance or a cloud VM. That's when cloud storage services become useful.

There are many different kinds of cloud storage tools, but they fall roughly into three categories: **file storage systems, cloud storage buckets, and cloud databases**.

##### Cloud File Storage

This type of cloud storage is probably most familiar to you already. Cloud file storage includes something like Dropbox or Google Drive, where files are stored in directories that can be navigated in a way that is similar to the file system on your local computer.

While there are professional-grade cloud tools for this such as AWS Elastic File System (EFS), Azure Files, and Google Cloud Filestore, the main takeaway you should have is the contrast between file storage and the storage approaches described below.

##### Cloud Storage Buckets

Also known as **object storage services**, cloud storage buckets are great for storing raw files, e.g. folders full of images, CSVs, or JSONs. Unlike cloud file storage, files are not stored in directories. Instead, all data is stored in a "flat" system where it can be retrieved by name. This lack of hierarchy makes cloud storage buckets faster to use and more cost efficient than traditional file storage.

Typically these services are not free, although they are fairly cheap (2-5 cents per GB per month) and typically come with some free credits.

Some major providers of cloud storage buckets include:

* [AWS S3


  Links to an external site.](https://aws.amazon.com/s3/getting-started/)
* [Google Cloud Storage


  Links to an external site.](https://cloud.google.com/storage/)
* [Azure Storage


  Links to an external site.](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction)

AWS S3 is the oldest and tends to have the most integration support with other platforms, although you may need to use Google storage if you're using other Google products or Azure storage if you're using other Azure products. Google Cloud Functions, for example, rely on source code being stored in Google Cloud Storage.

##### Cloud Databases

Databases are a familiar concept, but thus far we have mainly practiced using SQLite. If you're working with production-scale SQL data, it's best not to save it in a SQLite file but rather to store it on a database server.

Most likely your projects in this program will not require you to use a production-scale database, but this is an opportunity to practice if you want to prepare for on-the-job tasks.

Some major providers of cloud databases include:

* [Heroku Postgres


  Links to an external site.](https://www.heroku.com/postgres)
* [MongoDB Atlas


  Links to an external site.](https://www.mongodb.com/cloud/atlas)
* [AWS Aurora


  Links to an external site.](https://aws.amazon.com/rds/aurora/)
* [AWS RDS


  Links to an external site.](https://aws.amazon.com/rds/)

##### Pickling a Model

Pickling is a way of saving (serializing) a Python object (in this case, a trained machine learning model) to a file. This allows you to store the model after it has been trained so that it can be reused without retraining. Once a model is pickled, it is saved as a binary file that can be transferred or shared.

##### Un-pickling a Model

Un-pickling is the process of loading (deserializing) a saved model back into memory. Once the model is un-pickled, it can be used to make predictions in the same way it would have been if it had just been trained. For example, after un-pickling a model, you can pass new data to it and it will output predictions based on its previous training.

##### Anyone with Python Can Use the Model

Theoretical Access: If someone has the pickled model file and knows how to write basic Python code, they can load the model (un-pickle it) and use it to make predictions. They don’t need to retrain the model or have access to the original dataset—it’s already encapsulated in the trained model. This is particularly useful for sharing models with others in a development or deployment scenario. For example, after you train a model, you can give the pickled version to other developers or data scientists, and they can load the model into their Python environment and use it.

##### Cloud Deployment Context for Pickling

Why this matters in cloud deployment: When deploying a machine learning model as an API or as part of a cloud function, the model is usually pickled. The cloud service or API can then un-pickle the model when it’s needed, and use it to make predictions without retraining the model. In the cloud, this allows for efficient use of resources. You only train and pickle the model once, and from then on, the model can be un-pickled and used in any environment that supports Python (e.g., a web app or mobile app via API).

### Conceptualize the Cloud for Data Scientists

[![](https://moringa.instructure.com/courses/1426/files/631443/download)](https://moringa.instructure.com/courses/1426/files/631443/download)

Choosing a Cloud Service

| Cloud Service | How Popular for Data Scientists | Benefits | Drawbacks |
| --- | --- | --- | --- |
| Amazon Web Services (AWS) | Highly popular due to extensive data science tools (S3, SageMaker, Redshift). | * Scalable and flexible resources for big data and ML tasks. * Large ecosystem with a variety of services for analytics, AI, and data storage. * Strong global presence and reliability. | * Can become expensive if resources are not optimized. * Complexity in managing and configuring services. |
| Microsoft Azure | Growing in popularity, especially in enterprise environments. | * Seamless integration with Microsoft tools (Excel, Power BI). * Strong support for AI and machine learning services (Azure Machine Learning). * Good hybrid cloud options for businesses transitioning from on-premises. | * Can have a steeper learning curve for non-Microsoft ecosystems. * Pricing structure can be complex. |
| Google Cloud Platform (GCP) | Increasingly popular due to powerful data science tools like BigQuery and TensorFlow. | * Advanced data analysis tools (BigQuery) and machine learning (TensorFlow). * Strong in AI/ML capabilities with pre-built models and infrastructure. * Simple pricing structure. | * Limited global data centers compared to AWS and Azure. * Smaller ecosystem than AWS or Azure, less enterprise adoption. |
| IBM Cloud | Niche adoption, used by businesses with a focus on AI/ML and enterprise solutions. | * Strong focus on AI/ML (Watson) and big data analytics. * Good for regulated industries due to strong security and compliance tools. * Hybrid cloud capabilities for complex deployments. | * Less popular than AWS, Azure, and GCP in the general data science community. * Fewer third-party integrations and community support. |
| Oracle Cloud | Less popular but used in enterprise environments with Oracle-based infrastructure. | * Strong database management tools. * Integration with Oracle products (e.g., Oracle Database, ERP systems). * Good performance for data-heavy applications. | * More niche, primarily used in enterprises already using Oracle systems. * Not as developer-friendly or flexible as other cloud platforms. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248188

Scraped At: 2026-05-15T09:48:26.910517
