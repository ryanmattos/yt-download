import pathlib
import flask
from pytube import YouTube
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route( '/download', methods=['POST'] )
def getYTVideo():
   data = request.get_json(force = True)

   if not data:
      return "You must provide a video link to download."

   path = str(pathlib.Path().absolute())

   yt = YouTube(data['link'])

   ys = yt.streams.get_highest_resolution()

   print("Downloading video...")
   ys.download(path + '/yt-videos')
   print("Download completed!")

   return "<p>Video Downloaded!</p>"
app.run()