from sanic import Sanic
from sanic.response import text, html, json
from sanic_cors import CORS
import time
import urllib
import os
app = Sanic(__name__)
CORS(app)

tv_graph_data = {}
lv_graph_data = {}

fmt = lambda x: time.strftime("%H:%M:%S", time.localtime(x))

@app.route('/', methods=["POST"])
def func(req):
    
    data = urllib.parse.parse_qs(req.body.decode())
    tv = data['tv']
    lv = data['lv']
    if len(tv_graph_data) > 50:
        for k,v in tv_graph_data.items():
            tv_graph_data.pop(k)
            break
        for k,v in lv_graph_data.items():
            lv_graph_data.pop(k)
            break
    now = time.time()
    tv_graph_data[fmt(now)] = int(tv[0])
    lv_graph_data[fmt(now)] = int(lv[0])
    
    return html("<h1>ok</h1>")

@app.route('/graph_data', methods=['GET'])
def func(req):
    a = json({"tv": tv_graph_data, "lv": lv_graph_data})
    return a

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')