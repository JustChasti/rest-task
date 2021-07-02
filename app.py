from flask import Flask, request, jsonify
import json
import requests
import config


app = Flask(__name__)


add = []
find = [] 


@app.route("/", methods=["POST"])
def set_url():
    """ Add new Link"""
    j_reguest = request.json
    add.append({'link': j_reguest['text']})
    print(jsonify(add).json, 'json')
    return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}


@app.route("/", methods=["GET"])
def get_url():
    """ Get link by code"""
    j_reguest = request.json
    find.append({'short': j_reguest['text'], 'addres': request.remote_addr})
    print(jsonify(find).json, 'json')
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/bl", methods=["GET"])
def base_get_link():
    """ Send links to base """
    global add
    sendl = add
    add = []
    return jsonify(sendl)


@app.route("/bs", methods=["GET"])
def base_get_short():
    """ Send shorts to base """
    global find
    sendl = find
    find = []
    return jsonify(sendl)


@app.route("/bs", methods=["POST"])
def link_to_client():
    """ Get links and send to client """
    j_request = request.json
    print('длинные имена получены')
    for i in j_request:
        try:
            answer = requests.post(config.type_server + i['addres'], data=json.dumps({'link': i['link']}), headers=config.headers)
            print(answer)
        except:
            print(request.json)
            print('сервер отверг подключение')
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True)
