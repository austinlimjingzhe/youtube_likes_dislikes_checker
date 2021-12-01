import googleapiclient.discovery
from flask import Flask, render_template, redirect, url_for, request
import os
import json
import pandas as pd
import plotly.graph_objs as go
import plotly

os.chdir("C:\\Users\\User\\OneDrive\\Desktop\\Youtube Likes-Dislike Ratio")

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        yt_url=request.form["url"]
        return redirect(url_for("results", yt_url=yt_url))
    else:
        return render_template("home.html")

@app.route("/<yt_url>")
def results(yt_url):
    vid_id=yt_url
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "**********************************"
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    search_vid = youtube.videos().list(id=vid_id,part="statistics,snippet").execute()
    
    thumbnail=search_vid["items"][0]["snippet"]["thumbnails"]["standard"]["url"]
    vid_title=search_vid["items"][0]["snippet"]["title"]
    like_count=search_vid["items"][0]["statistics"]["likeCount"]
    dislike_count=search_vid["items"][0]["statistics"]["dislikeCount"]

    data=pd.DataFrame([["likes",int(like_count)],["dislikes",int(dislike_count)]],columns=["metric","value"])
    layout=go.Layout(annotations=[dict(text='Likes/Dislikes Ratio',font_size=10, showarrow=False)])
    fig=go.Figure(data=[go.Pie(textinfo="label+value",textposition="auto",labels=data["metric"],values=data["value"],hole=0.5,name="Likes/Dislikes Ratio",marker={"colors":["#27AE60","#E74C3C"]},showlegend=False)],layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("results.html",content=[thumbnail,vid_title,like_count,dislike_count],graphJSON=graphJSON)
   
if __name__=="__main__":
    app.run()