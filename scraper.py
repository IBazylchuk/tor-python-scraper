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
  url = request.values.get('url')
  proxy = request.values.get('proxy')

  scraper = cloudscraper.create_scraper(browser='chrome')

  match proxy:
    case 'tor':
      scraper.proxies = Socks5().random_valid_tor_proxy_url()

  # if proxy == 'tor':
  #   proxies
  # else if proxy == ''
  # # scraper.proxies = proxies
  response = scraper.get(url)

  data = {
    'status': response.status_code,
    'body': response.text,
    'url': url
  }

  return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
