# Ref: https://github.com/bhavaniravi/rasa-site-bot
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])


@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        entities = response.get("entities")
        topresponse = response["topScoringIntent"]
        intent = topresponse.get("intent")
        print("Intent {}, Entities {}".format(intent,entities))
        if intent == "gst-info":
            response_text = gst_info(entities)# "Sorry will get answer soon" #get_event(entities["day"],entities["time"],entities["place"])
        elif intent == "gst-query":
            response_text = gst_query(entities)
        else:
            response_text = get_random_response(intent)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"In short The abortion pill technically called the RU 486 is used for what is called 'medical termination of pregnancy'. It can terminate unwanted pregnancy up to 63 days (nine weeks). After due consultation and counseling and consent by your gynecologists the pill is taken in his presence and 48 hours later prostaglandin (Misoprostol) pessaries are used. This method is successful in around 95% to 98% of cases and has in effect revolutionized early pregnancy abortions over the world. As it avoids surgery and anesthesia it is much cheaper and relatively much safer than surgical abortions."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
