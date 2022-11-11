from flask import Flask,render_template,request,url_for,redirect,send_file
from pytube import  YouTube

app = Flask(__name__,static_folder="static")

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method =="GET":
        return render_template("index.html")

    link = request.form["url"]

    # with open("./static/videodb.vd","r") as vdb:
    #     videos = vdb.readlines(-1)
    # if not link in videos:
    #     video = YouTube(link)
    #     video = video.streams.order_by("resolution").filter(res="720p", audio_codec="mp4a.40.2")[0]
    #     video.download("static/videos/",filename=link+".mp4")
    #     with open("./static/videodb.vd", "w") as vdb:
    #         vdb.write(link+"\n")
    return send_file("static/watch?v=0MhVkKHYUAY.mp4")

app.run(debug=True)