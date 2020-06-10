# coding=utf-8
# @Time    : 2020/6/10 10:42
# @Author  : zwa
# @Motto   ：❤lqp

import prometheus_client
from prometheus_client import Counter
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

app = Flask(__name__)

requests_total = Counter("request_count", "Total request cout of the host")

#counter类型

@app.route("/metrics")
def requests_count():
    requests_total.inc()
    # requests_total.inc(2) 每一次刷新会增加2
    return Response(prometheus_client.generate_latest(requests_total),
                    mimetype="text/plain")


@app.route('/')
def index():
    requests_total.inc()
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
