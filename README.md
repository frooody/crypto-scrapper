# Crypto Scrapper
Here is a small script that collects information about most popular existing cryptocurrencies and transfers information about them into csv file
## Requirements
1. Python (https://www.python.org/downloads/)
*cmd extensions:*
2. BeautifulSoup4 (pip install beautifulsoup4)
3. Requests (pip install requests)
## Work principle
The script goes to *https://coinmarketcap.com/* and takes the name of crypto + price. Then it puts the data into csv file. Example: *Bitcoin,$41638.39*.
## Usage
Navigate to your project directory.
Type to cmd: 
```sh
$ python crypto-scrapper.py
```
## Additionally
By default script is creating one csv file per minute. If you want to change this value, go to crypto-scrapper.py. In the line 42:
```python
time.sleep(60)
```
сhange *60* for as many seconds as you want the program to wait before creating a new csv file.

# Result
After setup you'll have ready small script that automatically collect the information about cryptocurrency and puts it into csv file every 60(or any amount that you want) seconds.
