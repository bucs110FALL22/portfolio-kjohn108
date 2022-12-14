from Rates import StatsAPI
from Info import BitcoinInfo
  
def convert_to_btc():
  stat = StatsAPI()
  data = stat.get()
  all_currencies = data.keys()
  print("The possible currencies are", all_currencies)

  key1 = input("what type of currency do you have? ")
  quantity = int(input("How much money do you have? "))
  conversion_rate = data[key1]
  num_of_btc = round((quantity / conversion_rate), 5)
  print("you could have",num_of_btc, "bitcoin")
  return num_of_btc
  
  '''
  Init API class StatsAPI and converts from currency to bitcoin
  args: none
  return: (int) number of bitcoins you could have with amount of currency 
  '''

def find_percent():
  info = BitcoinInfo()
  bit = info.get()
  
  total_btc = int((bit['tsupply']))
  your_btc = (convert_to_btc())
  percent = (your_btc / total_btc) * 100
  print("you have", percent, "% of the total bitcoin")
  
  '''
  Init API class BitcoinInfo and calculates percent of total bitcoin
  args: none
  return: none
  '''
