# Youtube Likes-Dislikes Checker
An attempt at creating a web application using flask to check the dislike counts of videos following the removal from Youtube.

<h1>Introduction</h1>

On 10 November, Youtube made an announcement that it would remove the visibility of the dislike button. I, along with most of the Internet, feel that it is a move that does not make sense. However, it got me thinking if Youtube's Data API would still allow users to extract dislikes even after the removal. At the same time, being more familiar with R's Shiny framework, I wanted to learn about the other widely used framework for making applications but in Python - Flask.

In this app, I wanted to be able to visualize the likes-dislikes ratio of a video that a user can search up based on the videos' video ID. A <code>plotly</code> donut chart was used as it is in my opinion very aesthetically pleasing.

Hence, this very basic app was built following tutorials by Tech with Tim and Alan Jones. The following image shows the basic functionality of the app: 

![video demo 2](https://user-images.githubusercontent.com/88301287/144248822-15ee6435-9b68-4d98-8794-6ae33eed5012.gif)

<h1>Tools:</h1>

1. Flask
2. Plotly
3. Youtube API
4. Heroku

<h1>Planned Improvements</h1>

Some ways that the app's functionality can be improved is through:

1. An improved search experience: Searching by title or channel
2. A "Double-Up" feature: 2 videos are searched and displayed side-by-side for comparison

<h1></h1>
<h1>UPDATE!<br>
YouTube has officially removed dislikes from the API's retrievable statistics, invalidating this application's code.</h1>

<h1>References:</h1>

1. Pedro Hernández: https://medium.com/mcd-unison/youtube-data-api-v3-in-python-tutorial-with-examples-e829a25d2ebd
2. Tech with Tim: https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
3. Alan Jones: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
