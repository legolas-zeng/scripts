# coding=utf-8
# @Time    : 2020/6/10 10:52
# @Author  : zwa
# @Motto   ：❤lqp 

import prometheus_client
from prometheus_client import Counter, Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

app = Flask(__name__)

g = Gauge("random_value", "Random value of the request")

requests_total = Counter("request_count", "Total request cout of the host")

@app.route("/metrics")
def s():
    with open("F:\\a.txt", 'r') as f:
        num = f.read()
    g.set(num)
    return Response(prometheus_client.generate_latest(g),
                    mimetype="text/plain")


@app.route('/')
def index():
    requests_total.inc()
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0")