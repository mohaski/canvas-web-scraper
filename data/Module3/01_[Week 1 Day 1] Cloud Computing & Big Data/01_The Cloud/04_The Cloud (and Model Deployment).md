# The Cloud (and Model Deployment)

# The Cloud (and Model Deployment)

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) The Cloud (and Model Deployment)

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

For this part, we are going to walk through deploying a model as an API, i.e. using the cloud with data science. While we have not yet learned about machine learning models, we can begin to learn the process for deploying them now.

* [Deploying a Model as an API](#dpPanel0Content)
* [Deploying a Model as an API with Cloud Functions](#dpPanel1Content)
* [Deploying a Model as an API with Flask](#dpPanel2Content)
* [Deploying a Model as a Full-Stack Web App](#dpPanel3Content)
* [Deploying a Model as a Full-Stack Web App with Flask](#dpPanel4Content)
* [Deploying a Model as a Full-Stack Web App with Dash](#dpPanel5Content)

### Deploying a Model as an API

[![Client desktop on the left with a Requests arrow in the middle pointing to a server on the right. A Responses arrow is under the Requests arrow in the middle pointing back to the client desktop.](https://moringa.instructure.com/courses/1426/files/631350/download)](https://moringa.instructure.com/courses/1426/files/631350/download "Client desktop on the left with a Requests arrow in the middle pointing to a server on the right. A Responses arrow is under the Requests arrow in the middle pointing back to the client desktop.")

Once you have a pickled model, in theory anyone who can execute Python code can then un-pickle the model and use it to make predictions.

However, what if you want someone to be able to use your model even if they aren't running Python code? For example, what if the model is being used in the context of a website or a mobile app?

In that case, developing an HTTP API can be useful because this protocol is compatible with many different programming languages.

An example interaction with a model deployed as an API would be:

1. Client request: `POST /predict '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'`
2. Server response: `'{"predicted_class": 0}'`

Just like there are multiple tools that can make a POST request (Python requests library, cURL in the terminal, JavaScript fetch in a web application), there are multiple ways you can build your server.

### Deploying a Model as an API with Cloud Functions

[![Input x going into a Function f: box and Output f(x) coming out of the bottom.](https://moringa.instructure.com/courses/1426/files/631478/download)](https://moringa.instructure.com/courses/1426/files/631478/download "Input x going into a Function f: box and Output f(x) coming out of the bottom.")The most minimal way to deploy a machine learning model is to create a cloud function. This means that you created a pickled model, write a few lines of Python code specifying how to un-pickle the model and use it to make predictions, and deploy it with a cloud service designed for this purpose.

Below is an example of the process of developing and deploying a Google Cloud function, including the process of pickling a full pipeline, which includes machine learning modeling. While ML modeling has not be introduced yet, for the sake of showing how the cloud works, it is included in the code. That being said, nothing hinges on the understanding of what the ‘prediction’ model is doing.

The complete Google Cloud function looks like this:

```
import json  
import joblib  
  
def iris_prediction(sepal_length, sepal_width, petal_length, petal_width):  
    with open("model.pkl", "rb") as f:  
        model = joblib.load(f)  
    X = [[sepal_length, sepal_width, petal_length, petal_width]]  
    predictions = model.predict(X)  
    prediction = int(predictions[0])  
    return {"predicted_class": prediction}  
  
def predict(request):  
    request_json = request.get_json()  
    result = iris_prediction(**request_json)  
    return json.dumps(result)  
  
 
```

While they involve writing the least amount of code of any model deployment option, cloud functions can be tricky to configure within the cloud service. Looking at the code above you might notice that the predict function is never actually invoked in the code -- when you configure the cloud function, you have to specify that this function should be called. You will also need to configure the cloud function so that it can accept public web requests, and typically you won't be able to test anything on your local computer, so this can be a slow back-and-forth of tweaking the configuration until it works.

We found that the Google Cloud functions were the easiest to work with, but you also might want to check out [AWS Lambda Functions


Links to an external site.](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html) and [Azure Functions


Links to an external site.](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python).

### Deploying a Model as an API with Flask

[![](https://moringa.instructure.com/courses/1426/files/631369/download)](https://moringa.instructure.com/courses/1426/files/631369/download)Flask is a microframework for web development with Python. It can be used for full-stack web applications, but it's also very popular for deploying machine learning models as APIs. In fact, the Google Cloud function Python tooling that is used in the curriculum lesson linked above uses Flask "under the hood"!

Here is that same cloud function, rewritten as a Flask app:

```
from flask import Flask, request  
import joblib  
import json  
  
app = Flask(__name__)  
  
def iris_prediction(sepal_length, sepal_width, petal_length, petal_width):  
    with open("model.pkl", "rb") as f:  
        model = joblib.load(f)  
    X = [[sepal_length, sepal_width, petal_length, petal_width]]  
    predictions = model.predict(X)  
    prediction = int(predictions[0])  
    return {"predicted_class": prediction}  
  
@app.route('/', methods=['GET'])  
def index():  
    return 'Hello, world!'  
  
@app.route('/predict', methods=['POST'])  
def predict():  
    request_json = request.get_json()  
    result = iris_prediction(**request_json)  
    return json.dumps(result)
```

It's definitely a bit longer than the cloud function version, but it has two benefits:

1. You can actually run the server on your local computer, which makes debugging much faster and easier.
2. Rather than using Google Cloud functions (a paid service, although there are free credits when you sign up), you can use Heroku to deploy your API, which is 100% free for up to 5 apps. (You can also deploy using an EC2 instance or other cloud container if your model is too large/slow for Heroku.)

Besides Heroku and AWS EC2, you can also host flask apps with Azure App Service, DigitalOcean, Google Cloud App Engine, and AWS Elatic Beanstalk.

### Deploying a Model as a Full-Stack Web App

An API interface is very useful, but you also might want something more interactive and impressive for your data science portfolio. Developing a full-stack web app means that there is a web page interface, so once your app is deployed, someone can load it directly in the browser and generate model predictions by clicking on the page.

### Deploying a Model as a Full-Stack Web App with Flask

[![Diagram of the exchange process between Client and Server including Controller, Model, and View.](https://moringa.instructure.com/courses/1426/files/631358/download)](https://moringa.instructure.com/courses/1426/files/631358/download "Icons made by Freepik from www.flaticon.com")


Icons made by Freepik from www.flaticon.com

The same microframework described for deploying a model as an API can also be used to make a full-stack web app. This requires that you write HTML and CSS (and optionally JavaScript) as well as Python in order to create the "view" component of the model-view-controller (MVC) framework.

**Pros:**

* If you already have experience with HTML and CSS, this approach can allow you to flex your creativity and make something very polished that shows off all of your skills. You can add as many pages as you want (e.g. to create a portfolio website rather than a single-page application).
* You can generate data visualizations in Python with Matplotlib (don't need to learn any new plotting libraries).

**Cons:**

* If you don't have any experience with HTML and CSS, the learning curve can be steep. These languages don't produce straightforward error messages like Python does, so it can be quite difficult to know where your mistakes are.
* Unless you know JavaScript and are prepared to work with a library like D3.js, your visualizations aren't going to be interactive.

If you are interested in using this approach, check out [this template repository


Links to an external site.](https://github.com/learn-co-students/capstone-flask-app-template-082420), which includes instructions in the README for modifying the HTML and Python code so that it will work for your project.

### Deploying a Model as a Full-Stack Web App with Dash

**[![Dash menu of an Iris Information page section.](https://moringa.instructure.com/courses/1426/files/631480/download)](https://moringa.instructure.com/courses/1426/files/631480/download "Dash menu of an Iris Information page section.")**

**Plotly Dash** (also just referred to as Dash) is "the most downloaded, trusted framework for building machine learning web apps in Python" (source). It allows you to create interactive websites that make predictions from machine learning models, all without writing HTML, CSS, or JavaScript directly.

Dash is built on top of Flask, so it can be deployed using Heroku as well. Check out this link for an [example app hosted on Heroku


Links to an external site.](https://calm-bastion-07515.herokuapp.com/) (might take a while to load if it hasn't been used in a while).

### Challenges and Common Issues

#### Configuration Challenges with Cloud Functions:

* **Challenge:** Cloud functions, while minimal in terms of code, can be tricky to configure. The function must be set up to handle public requests, and testing often requires deploying the function in the cloud rather than locally, leading to a slow development cycle.
* **Addressing the Challenge:** To reduce configuration errors, carefully follow the cloud provider’s setup documentation and use logging tools to troubleshoot issues. Using services like Google Cloud Functions or AWS Lambda often involves trial and error, so learners should anticipate some back-and-forth while testing.
* **Common Issue:** New users often forget to enable public access or set proper permissions for their cloud functions. Ensure proper security settings while making the function accessible publicly.

#### Choosing Between Cloud Functions and Flask for API Deployment

* **Pros (Cloud Functions):** Cloud functions require minimal code and can scale automatically, making them ideal for lightweight applications. No need to maintain server infrastructure.
* **Cons (Cloud Functions):** Harder to debug due to cloud-only testing, and there may be cold start delays when the function is not in use.
* **Pros (Flask):** Flask allows for easier debugging locally and greater control over routing and app structure. Flask is flexible for complex applications and can be integrated into more extensive services like full web apps.
* **Cons (Flask):** Flask requires you to manage the server or choose a hosting platform like Heroku, and scaling is not automatic (unlike cloud functions).

#### Complexity of Full-Stack Web App Development

* **Challenge:** Building a full-stack web app requires knowledge of front-end languages (HTML, CSS, JavaScript) in addition to Python. This can be overwhelming if you don't have web development experience.
* **Addressing the Challenge:** Start with simple APIs (like those built with Flask) before progressing to full-stack development. You can also use frameworks like Dash, which simplify web development by reducing the need for front-end programming.
* **Common Issue:** When working with HTML/CSS for the first time, debugging issues (like layout and styling problems) can be difficult due to uninformative error messages.

#### Deploying on Free Platforms Like Heroku

* **Pros:** Heroku offers a free tier that makes it accessible for beginners who want to deploy machine learning models as APIs or web apps. It integrates well with Flask and allows easy deployment from a GitHub repository.
* **Cons:** The free tier has limitations, such as slower processing and potential downtime when the app is idle (cold starts). Additionally, Heroku's storage is temporary, so any file uploads will be lost after the app restarts.

### Decision Points and Their Impact

#### Using Cloud Functions vs. Flask

* **Decision Point:** Deciding between cloud functions and Flask depends on the complexity of the project and the need for local testing.
* **Impact:** Cloud functions are faster to deploy but harder to debug locally, which can slow down development if frequent changes are needed. Flask, while requiring more initial setup, enables faster iterations since you can test everything on your local machine before deploying to a platform like Heroku.
* **When to Use Cloud Functions:** For small-scale, stateless machine learning models where you want minimal overhead.
* **When to Use Flask:** When you need more flexibility or plan to build more complex applications that require persistent data or advanced routing.

#### Choosing Between an API vs. Full-Stack Web App

* **Decision Point:** Deciding whether to build a simple API or a full-stack web app depends on the project's end goal.
* **Impact:** APIs are more lightweight and can be integrated into various platforms like mobile apps, websites, or other services. Full-stack web apps, however, allow for a more interactive and polished user interface, which can be helpful in portfolios or user-driven applications.
* **Pros of API Deployment:** Lightweight, easy to integrate with various systems, and quick to deploy.
* **Cons of API Deployment:** Limited user interaction beyond sending and receiving data via HTTP requests.
* **Pros of Full-Stack Web App:** More user-friendly, especially for non-technical users, and allows you to showcase your web development skills.
* **Cons of Full-Stack Web App:** Requires knowledge of front-end technologies, which can have a steep learning curve.

#### Flask vs. Dash for Full-Stack Apps

* **Decision Point:** Deciding between using Flask for full-stack development (which requires front-end development skills) or Dash (which focuses on data visualization and interaction without needing HTML/CSS/JavaScript knowledge).
* **Impact:** Flask gives more control and flexibility, but Dash simplifies the process for those primarily interested in showcasing data science skills without diving into web design.
* **When to Use Dash:** If the project focuses on presenting interactive data visualizations and you want to minimize front-end coding. Dash is excellent for building data-driven dashboards.
* **When to Use Flask:** If you want more customization and control over the look and feel of the website or plan to build a larger web application.

### Summary

For a junior data scientist, deploying a machine learning model as an API is essential for making their models accessible beyond Python environments, such as in web and mobile applications. This section explains how to convert a pickled model into an API, which can receive data (e.g., features like sepal\_length), make predictions, and return results via HTTP requests.

Two common methods are discussed: using cloud functions (e.g., Google Cloud Functions or AWS Lambda) for minimal server-side code, or Flask for more flexibility, including local testing and easier debugging. Flask-based deployments are also compatible with platforms like Heroku for free hosting.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248190

Scraped At: 2026-05-15T09:48:33.972366
