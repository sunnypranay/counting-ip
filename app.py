from flask import Flask, render_template, request, Response
import json


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/count_ips_in_ipsum", methods = ['GET', 'POST'])
def count_ip():
    
    if request.method == "GET":
        return render_template("count-ip.html")
    
    # For command line testing windows
    # curl -X POST http://127.0.0.1:5000/count_ips_in_ipsum -H "Content-Type:application/json" -d "{ \"ips\": [\"1.2.3.4\", \"192.168.1.1\"]}"
    
    elif request.method == "POST":
        try:
            data = request.json['ips']
        except:
            result = {'status': 'Please give input in json format { "ips": ["1.2.3.4", "192.168.1.1"]}'}
            return Response(json.dumps(result), status=422, mimetype='application/json')
        count = 0
        for i in data:
            if len(i) > 0:
                count += 1
            else:
                continue
        result = {'count': count}
        return Response(json.dumps(result), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)