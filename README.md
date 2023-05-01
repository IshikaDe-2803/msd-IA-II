<h1>Microservices for Video Streaming Website using Django REST API</h2>

<h2>Introduction</h2>
StreamCastle is a video streaming website where users can view videos, upload their own videos and additionally like and comment on them too.
Building a scalable and reliable video streaming platform is important. One of the approaches to building a scalable and reliable video streaming platform is to use a microservices architecture. 
With this project, we implement this microservices architecture by using the Django REST API framework.

<h2>Architecture</h2>
The website uses a microservices architecture, which is an architectural style that structures an application as a collection of small, independent services. The services communicate with each other through APIs.
The Video Streaming Website consists of two microservices:

* Video API: Handles video uploads, retrieval and streaming.
* Comments API:  Allows clients to create and retrieve comments.

The main_app acts as a gateway that uses the comments_api and video_api microservices to provide the necessary functionality for the video streaming website.

![architecture](https://user-images.githubusercontent.com/79038075/235450540-15b8bf0e-4ce1-4a19-aba7-b02edb5e94dd.png)

<h2>Implementation</h2>
We used the Django REST API framework to create our microservices, which allowed us to easily create RESTful APIs that our main app could consume. We created separate Django apps for each microservice and defined models and views for each app. We also used Django's serializer classes to serialize and deserialize data between our microservices and the main app.

<h3>Functions</h3>

* Video Uploading and Streaming
* Commenting System

<h3>Testing and Quality Assurance</h3>
We created unit tests to ensure that our microservices interacted correctly with the main app using Jenkins.

<h2>References</h2>

* https://www.django-rest-framework.org/tutorial/1-serialization/#tutorial-1-serialization 
* https://microservicesdocumentation.readthedocs.io/en/latest/contributing/python.html


