import serial
from flask import Flask,request,jsonify,render_template,flash
import time
app = Flask(__name__)

connects = 0
app.config.update(
    SECRET_KEY="YDFGUDGFU+6"
)




def move(angle):

    if angle == 'on':
        ser.write(chr(49).encode())
        print ("command sent")
    elif angle == 'off':
        ser.write(chr(48).encode())
        print ("command sent")


    
@app.route("/", methods=["GET"])  
def serve():
    flash("servo control")
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def turn():
    angle = request.form["angle"]
    if angle == "off":
        move("off")
        return(jsonify("on","180"))
    elif angle == "on":
        move("on")
        return(jsonify("off","0"))

@app.route("/connect", methods=['POST'])
def connect():
    global connects
    global ser
    if connects == 0 and request.form["action"] != "view":
        try:
            ser = serial.Serial("COM5", 9600,timeout=0)
            time.sleep(2)
        except:
            print("connection error")
            return(jsonify("connect","conection failed"))
            connects = 0
        connects = 1
        return(jsonify("disconnect","connected"))
    else:
        return(jsonify("disconnect","connected"))

    print("connection succeeded")

