from flask import Flask, Response, request, send_from_directory, render_template
import json, markdown, os

from natotrainer import *

app = Flask(__name__)

@app.route("/")
def hello_world():
	mode = request.args.get("mode") if "mode" in request.args else "normal"
	return render_template("frontpage.html", mode=mode)




@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)


@app.route("/getcode")
def getcode_r():
	faa = "faa" in request.args
	call = "call" in request.args
	ean = "ean" in request.args
	ca = "ca" in request.args
	return Response(json.dumps(getcode(faa, call, ean, ca)), mimetype="text/json")



def openmarkdownpage(mdfile):
    with open(os.path.dirname(os.path.realpath(__file__)) + mdfile, "r", encoding='utf-8') as md_file:
        return render_template("document.html", md=markdown.markdown(md_file.read(), extensions=['pymdownx.tilde', 'tables']))
    

    

@app.route("/readme")
def readme():
	return openmarkdownpage("/README.md")


@app.route("/guide")
def guide():
	return render_template("guide.html")




if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode')
	args = parser.parse_args()

	if args.mode == "run":
		app.run(debug=True, host="0.0.0.0", port=5001)