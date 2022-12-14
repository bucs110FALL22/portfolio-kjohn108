import requests 

class BitcoinInfo: 
  
  def __init__(self):
    self.url = ("https://api.coinlore.net/api/ticker/?id=90")
    
  def get(self):
    r = requests.get(self.url)
    response = r.json()
    
    res =response[0]
    
    return(res)
    '''
    Pull info from API
    args: self
    return: (dict) data from API
    '''

