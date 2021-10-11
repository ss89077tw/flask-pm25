from flask import Flask
from datetime import datetime

from flask.templating import render_template
from scrape.pm25 import get_pm25
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('index.html', time=time)

# post函式


@app.route('/pm25-data',methods=['GET', 'POST'])
def pm25_data():
    columns, datas = get_pm25()
    sites, values = [], []
    for data in datas:
        sites.append(data[0])
        values.append(data[-1])

    data = {'sites': sites, 'values': values}

    print(data['site'])

    return json.dumps(data,ensure_ascii=False)


@app.route('/pm25-echarts')
def pm25_echarts():
    return render_template('pm25-echarts.html')


@app.route('/echarts')
def echarts():
    return render_template('echarts.html', time=time)


@app.route('/pm25')
def pm25():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    columns, datas = get_pm25()
    return render_template('pm25.html', **locals())


@app.route('/stock')
def getStock():
    return render_template('stock.html', time=time, stocks=stocks)


if __name__ == '__main__':

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]
    # for stock in stocks:
    #     print(stock['分類'], stock['指數'])

    # return render_template('stock.html',**locals())


@app.route('/sum/x=<x>&y=<y>', methods=['GET'])
def get_Sum(x, y):
    return f'總和為{x+y}'


@app.route('/today/<string:name>')
def getTodayDate(name):
    from datetime import datetime
    print(datetime.now())
    # 字串
    return f'{name} 歡迎光臨<br/> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'


if __name__ == '__main__':
    app.run(debug=True)
