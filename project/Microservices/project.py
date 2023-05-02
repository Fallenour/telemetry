from flask import Flask
import requests
import jsonify
import random


list = [

    "20180101 23:01:05.001|1001|101|98|25|20|99.9|TSTAT",
    "20180101 23:01:26.011|1001|101|98|25|20|99.8|TSTAT",
    "20180101 23:02:09.014|1001|101|98|25|20|89.3|TSTAT",
    "20180101 23:02:10.021|1001|101|98|25|20|89.4|TSTAT",
    "20180101 23:05:05.021|1001|101|98|25|20|89.9|TSTAT",
    "20180101 23:05:07.421|1001|17|15|9|8|7.9|BATT",
    "20180101 23:04:06.017|1001|101|98|25|20|89.9|TSTAT",

]


app = Flask(__name__)

@app.route("/", methods=["GET"])

def h():
    chosen = random.choice(list)
    print("{}".format(chosen))
    return chosen

if __name__=="__main__":
  app.run(host="0.0.0.0", port=8010)