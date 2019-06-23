from flask import Flask, url_for, request, render_template, abort, redirect, jsonify
import requests
import os

app = Flask(__name__)

app_urls = {
	1: "app_1",
    2: "app_2",
    3: "app_3",
    4: "app_4"
}

def recon_path(app_list):
    path = ""
    length = len(app_list)
    for app in app_list:
        if length > 1:
            path += str(app) + "-"
        else:
            path += str(app)
        length -= 1
    return path

@app.route('/')
def hello_world():
    return 'Hello world! from app_4, host: ' +  str(os.uname()[1])

@app.route('/<app_path>/<int:num>', methods=['GET', 'POST'])
def post_to_micro(app_path, num):
	resp = requests.get("http://numbersapi.com/{}".format(num))
	value = len(resp.text) * 12

	if len(app_path) == 1:
		return "Result: " + str(value) + "\n4ping4"
	else:
		app_list = app_path.split("-")
		route = "http://" + app_urls[int(app_list[1])] + ":5000"+ "/" + recon_path(app_list[1:]) + "/" + str(value)
		resp = requests.get(route)
    	return resp.text + "\n---->4via4"

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5000)












