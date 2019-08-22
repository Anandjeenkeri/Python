import urllib.request
import pprint
import re
from bs4 import BeautifulSoup


'''
This function will fetch the market profile values such as vah,poc and val from the rudroalogy.in website.
'''
def getMarketProfileValues():
    url = "http://www.rudraology.in/"
    req = urllib.request.Request(url, headers={'User-Agent': "Chrome Browser"})
    page = urllib.request.urlopen(req, timeout=10)
    soup = BeautifulSoup(page, 'html.parser')
    banknifty_page = soup.find('marquee').text.strip()
    pattern = re.compile('BANKNIFTY FUTURES(\s+)VAH : (\d+)(\s+)POC : (\d+)(\s+)VAL : (\d+)')
    result = pattern.search(banknifty_page)
    if result:
        return (result.group(2), result.group(4), result.group(6))
    else:
        print("Error: Failed to get the market profile values")
        exit(1)
'''
This function will fetch the today's banknifty open price
input: NSE indices url
return: banknifty open price
'''
def get_banknifty_open_price():
    pass
    indices_url = ''

'''
This function will analyse the open type based on the banknifty open price. Open price is compared with the previous market profile values to determine the 
open type. 
Based on the open type one can decide trading.
Input: market profile values, banknifty open price
Return: open type
There are four type of open types:
    1) Open ride: open=low or open=high
    2) open test drive
    3)Open test reversal 
    4) Normal day
'''
def analyze_open_type(vah,poc,val,banknifty_open_price):
        if not banknifty_open_price:
            print("Error: Please enter the banknifty open price")
            exit(1)
        if banknifty_open_price > vah:
            print("Open Up drive and bullish ")
        elif banknifty_open_price < val:
            print("Open down drive and bearish")
        elif banknifty_open_price == poc:
            print("Price opened exactly at the previous day poc and day type would be range bound")
        elif banknifty_open_price > poc and banknifty_open_price < vah:
            if banknifty_open_price - poc < vah - banknifty_open_price:
                print("Price opened withing the range and is closer to POC value")
            else:
                print("Price is opened within the range and is closer to VAH")
                print("Please mark the previous RESISTANCE area and trade accordingly")
        elif banknifty_open_price < poc and banknifty_open_price > val:
            if poc - banknifty_open_price < banknifty_open_price - val:
                print("Price opened within the lower poc and is closer to POC and mark the next support area")
            else:
                print("Price opened with the lower POC and is closer to VAL")
                print("\nMark the next support to trade")
        else:
            print("Not able to find the right open type based on the bank nifty open price. Please see chart")

def main():
    vah, poc, val = getMarketProfileValues()
    print(vah, poc, val)
    # Enter the banknifty open price
    open_price = input(">Enter Banknifty open price")
    analyze_open_type(int(vah), int(poc), int(val), int(open_price))

if __name__=="__main__":
    main()