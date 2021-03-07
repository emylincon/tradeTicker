from flask import Flask, jsonify, request, render_template, url_for
import pandas as pd

app = Flask(__name__)


class Data:
    def __init__(self):
        self.df = pd.read_csv('data/data.csv')
        self.df = self.df.fillna('missing')

    def ticker_match(self, ticker, kind='match'):    # kind = match or contains
        if kind == 'match':
            return self.df[self.df['Ticker'].str.match(ticker, case=False)].to_dict('records')
        else:
            return self.df[self.df['Ticker'].str.contains(ticker, case=False)].to_dict('records')
    
    def name_match(self, name, kind='match'):
        if kind == 'match':
            return self.df[self.df['Name'].str.match(name, case=False)].to_dict('records')
        else:
            return self.df[self.df['Name'].str.contains(name, case=False)].to_dict('records')


Record = Data()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/ticker')
def get_ticker():
    name, kind = request.args.get('name'), request.args.get('kind')
    return jsonify(Record.name_match(name=name, kind=kind))


@app.route('/name')
def get_name():
    ticker, kind = request.args.get('ticker'), request.args.get('kind')
    return jsonify(Record.ticker_match(ticker=ticker, kind=kind))


# if __name__ == '__main__':
#     app.run(debug=True)

# print(Data().name_match('EUR/USD'))

