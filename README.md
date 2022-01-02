# youtube like dislike checker
An attempt at creating a web application using flask to check the dislike counts of videos following the removal from Youtube.

Introduction

On 10 November, Youtube made an announcement that it would remove the visibility of the dislike button. I, along with most of the Internet, feel that it is a move that does not make sense. However, it got me thinking if Youtube's Data API would still allow users to extract dislikes even after the removal. At the same time, being more familiar with R's Shiny framework, I wanted to learn about the other widely used framework for making applications but in Python - Flask.

Hence, this very basic app was built following tutorials by Tech with Tim and Alan Jones. The following image shows the basic functionality of the app: 

![video demo 2](https://user-images.githubusercontent.com/88301287/144248822-15ee6435-9b68-4d98-8794-6ae33eed5012.gif)

UPDATE:
YouTube has officially removed dislikes from the API's retrievable statistics, invalidating this application's code.

References:

1. Pedro Hernández: https://medium.com/mcd-unison/youtube-data-api-v3-in-python-tutorial-with-examples-e829a25d2ebd
2. Tech with Tim: https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
3. Alan Jones: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
