# TRADE TICKER API
* get ticker symbol from company name, currency etc and vice versa

[Application link](https://trade-ticker.herokuapp.com/)

## How to Use
* To get ticker from name
```python
import requests
import json

payload = {'name': 'EUR/USD', 'kind': 'match'}
r = requests.get('http://127.0.0.1:5000/ticker', params=payload)
data = json.loads(r.content)
print(data)

```
* result
```python
[{'Category Name': 'missing', 'Country': 'missing', 'Exchange': 'CCY', 'Name': 'EUR/USD', 'Ticker': 'EURUSD=X'}]
```


* To get name from ticker
```python
import requests
import json

payload = {'ticker': 'GOOG', 'kind': 'match'}
r = requests.get('http://127.0.0.1:5000/name', params=payload)
data = json.loads(r.content)
print(data)
```
* result
```json
[{"Category Name":"Internet Information Providers","Country":"USA","Exchange":"NMS","Name":"Alphabet Inc.","Ticker":"GOOG"},{"Category Name":"Internet Information Providers","Country":"USA","Exchange":"NMS","Name":"Alphabet Inc.","Ticker":"GOOGL"},{"Category Name":"Internet Information Providers","Country":"Mexico","Exchange":"MEX","Name":"Alphabet Inc.","Ticker":"GOOG.MX"},{"Category Name":"missing","Country":"Switzerland","Exchange":"EBS","Name":"Alphabet Inc.","Ticker":"GOOGL.SW"},{"Category Name":"Internet Information Providers","Country":"Mexico","Exchange":"MEX","Name":"Alphabet Inc.","Ticker":"GOOGL.MX"},{"Category Name":"Internet Information Providers","Country":"Argentina","Exchange":"BUE","Name":"Alphabet Inc.","Ticker":"GOOGL.BA"},{"Category Name":"missing","Country":"Italy","Exchange":"TLO","Name":"AZIONE ALPHABET - CLASS A","Ticker":"GOOGL.TI"},{"Category Name":"missing","Country":"Brazil","Exchange":"SAO","Name":"Alphabet, Inc.","Ticker":"GOOG35F.SA"},{"Category Name":"missing","Country":"Brazil","Exchange":"SAO","Name":"Alphabet, Inc.","Ticker":"GOOG34F.SA"},{"Category Name":"missing","Country":"Brazil","Exchange":"SAO","Name":"Google Inc.","Ticker":"GOOG34.SA"},{"Category Name":"missing","Country":"Brazil","Exchange":"SAO","Name":"Google Inc.","Ticker":"GOOG35.SA"}]
```