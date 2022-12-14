import requests

class StatsAPI: 
  def __init__(self):
    self.url =("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc.json")

  def get(self):
    r = requests.get(self.url)
    response = r.json()

    if response.get('btc'):
      return response['btc']
    else:
      return None

    '''
    Pull info from API
    args: self
    return: (dict) data from API
    '''
