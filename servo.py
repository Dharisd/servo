import serial
from flask import Flask,request,jsonify,render_template
import time
app = Flask(__name__)
global connectd
connects = 0




def move(angle):

    if angle == '49':
        ser.write(chr(49).encode())
        print ("command sent")
    elif angle == '48':
        ser.write(chr(48).encode())
        print ("command sent")


    
@app.route("/", methods=["GET"])  
def serve():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def turn():
    angle = request.form["angle"]
    print (angle)
    move(angle)
    return("request sent to servo")

@app.route("/connect", methods=['POST'])
def connect():
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

