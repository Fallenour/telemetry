from flask import Flask
import requests
import jsonify
import random


list = [

    "20180101 23:01:09.521|1000|17|15|9|8|7.8|BATT",
    "20180101 23:01:38.001|1000|101|98|25|20|102.9|TSTAT",
    "20180101 23:01:49.021|1000|101|98|25|20|87.9|TSTAT",
    "20180101 23:02:11.302|1000|17|15|9|8|7.7|BATT",
    "20180101 23:03:03.008|1000|101|98|25|20|102.7|TSTAT",
    "20180101 23:03:05.009|1000|101|98|25|20|101.2|TSTAT",
    "20180101 23:04:11.531|1000|17|15|9|8|7.9|BATT",

]


app = Flask(__name__)

@app.route("/", methods=["GET"])

def h():
    chosen = random.choice(list)
    print("{}".format(chosen))
    return chosen

if __name__=="__main__":
  app.run(host="0.0.0.0", port=8010)