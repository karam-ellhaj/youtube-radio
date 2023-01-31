from flask import Flask,render_template,request,url_for,redirect,send_file,send_from_directory
from pytube import  YouTube

app = Flask(__name__,static_folder="static")

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method =="GET":
        return render_template("index.html")

    link = request.form["url"]
    path = link.split("/")[-1]+".mp3"

    try:
        send_file("/static/videos/"+path)
        return render_template("done.html",url=url_for("static",filename="videos/"+path))
    except:
        video = YouTube(link)
        video = video.streams.filter(only_audio=True)[-1]
        video.download("static/videos/", filename=path)

    return render_template("done.html",url=url_for("static",filename="videos/"+path))

app.run(host="192.168.8.120",debug=True)