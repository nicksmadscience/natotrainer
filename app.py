from flask import Flask, Response, request, send_from_directory, render_template
import json

from natotrainer import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("frontpage.html")




@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)


@app.route("/getcode")
def getcode_r():
	faa = "faa" in request.args
	call = "call" in request.args
	return Response(json.dumps(getcode(faa, call)), mimetype="text/json")



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode')
	args = parser.parse_args()

	if args.mode == "run":
		app.run(debug=True, host="0.0.0.0", port=5001)