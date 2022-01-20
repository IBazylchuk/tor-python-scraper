from random import sample
import cloudscraper

class Socks5:
  def tor_proxy_config(self):
    return {
        'host': 'localhost',
        'first_port': 9101,
        'last_port': 9191
    }

  # def proxy_url(self, proxy):
  #   return "socks5://#{proxy}"

  def get_proxies(self, proxy_port):
    return {
        "http": "socks5://localhost:" + str(proxy_port),
        "https": "socks5://localhost:" + str(proxy_port)
    }

  def get_working_proxy(self, proxy_port):
    scraper = cloudscraper.create_scraper()

    proxies = Socks5().get_proxies(proxy_port)
    scraper.proxies = proxies
    response = scraper.get('https://check.torproject.org')

    if 'Congratulations. This browser is configured to use Tor.' in response.text:
      return proxies
    else:
      return None

  def random_valid_tor_proxy_url(self):
    available_tor_ports = list(range(self.tor_proxy_config()['first_port'], self.tor_proxy_config()['last_port']))

    num = len(available_tor_ports)
    for _ in range(num):
      if len(available_tor_ports) == 0:
        print('No valid TOR proxies available')
        return None

      proxy_port = sample(available_tor_ports, 1)[0]

      proxies = self.get_working_proxy(proxy_port)

      if proxies:
        return proxies

      available_tor_ports.remove(proxy_port)

