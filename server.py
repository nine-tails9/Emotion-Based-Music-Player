from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template, send_from_directory
import EmotionRecog
from EmotionRecog import predict
from flask_cors import CORS
# import EmotionRecog
# from EmotionRecog import predict
app = Flask(__name__)
cors = CORS(app)
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/recognize')
def emotion():
	lan = request.args.get('path')
	x = str(emotions[predict(lan)[0]])
	return jsonify(
        emotion=str(x)
    )

if __name__ == '__main__':
   app.run()