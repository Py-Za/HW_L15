from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/exchange_from_pln")
def exchange_from_pln():
    value = float(request.args["value"])
    to_currency = request.args["to_curr"]
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{to_currency}/")
    rate = float(response.json()['rates'][0]['mid'])
    return {
        "value": value,
        "from": "pln",
        "to": to_currency,
        "result": value/rate
    }
# http://127.0.0.1:5000/exchange_from_pln?value=10&to_curr=usd

@app.route("/exchange_to_pln")
def exchange_to_pln():
    value = float(request.args["value"])
    from_currency = request.args["from_curr"]
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{from_currency}/")
    rate = float(response.json()['rates'][0]['mid'])
    return {
        "value": value,
        "from": from_currency,
        "to": "pln",
        "result": value*rate
    }
# http://127.0.0.1:5000/exchange_to_pln?value=10&from_curr=usd

@app.route("/XD")
def XD():
    value = float(request.args["value"])
    from_currency = request.args["from_curr"]
    to_currency = request.args["to_curr"]
    response1 = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{from_currency}/")
    rate1 = float(response1.json()['rates'][0]['mid'])
    response2 = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{to_currency}/")
    rate2 = float(response2.json()['rates'][0]['mid'])
    return {
        "value": value,
        "from": from_currency,
        "to": to_currency,
        "result": value*rate1/rate2
    }
# http://127.0.0.1:5000/XD?value=10&from_curr=usd&to_curr=aud
