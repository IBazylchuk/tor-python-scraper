from nis import match
import cloudscraper

import flask
from flask import request, jsonify

import helpers
from helpers.socks5 import Socks5

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/scrape",  methods=['POST'])
def api_insert():
  url = request.json.get('url')
  proxy = request.json.get('proxy')
  params = request.json.get('params')
  headers = request.json.get('headers')
  method = request.json.get('method')
  user_agent = request.json.get('user_agent')

  if user_agent:
    browser = { 'custom': user_agent }
  else:
    browser = 'chrome'

  scraper = cloudscraper.create_scraper(browser=browser)

  match proxy:
    case 'tor':
      scraper.proxies = Socks5().random_valid_tor_proxy_url()

  match method:
    case 'post':
      response = scraper.post(url, params=params, headers=headers)
    case _:
      response = scraper.get(url)

  data = {
    'status': response.status_code,
    'body': response.text,
    'url': url
  }

  return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
