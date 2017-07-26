from flask import Flask, render_template, request
import pandas as pd
import pandas_highcharts.core

app = Flask(__name__)

@app.route('/')
def main():
    title = "Data Centre Environment"
    pageType = 'main'
    paragraph = ["This will display the ten most recent temperature & humidity reports",
    "other stats to be included are:", "highest recorded value(time stamped)","mean values","etc"]
    return render_template('header.html', title=title, pageType=pageType, paragraph=paragraph)

	
@app.route('/about')
def about():
    title = "What the Why?"
    pageType = 'about'
    paragraph = ["Currently under development", "proposed features list to be updated", "current focus is on MVP!"]
    return render_template('header.html', title=title, paragraph=paragraph, pageType=pageType)
	
@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'stock', chart_height = 500):
    title = "Data Centre Dashboard"
    paragraph = ["graphs below"]
    pageType = 'graphs'
    df = pd.read_csv('csv/test.csv', index_col='Date', parse_dates=True)
    dataSet = pandas_highcharts.core.serialize(df, render_to='my-chart', output_type='json', title='Temperature')
    bf = pd.read_csv('csv/test2.csv', index_col='Date', parse_dates=True)
    dataSet2 = pandas_highcharts.core.serialize(bf, render_to='my-chart2', output_type='json', title='Humidity')
    tlog = str(df[-1:])[-1:]
    hlog = str(bf[-1:])[-1:]
    ttime= str(df[-1:])[-15:-1] 
    htime= str(bf[-1:])[-15:-1]
    return render_template('graph2.html', chart=dataSet, chart2=dataSet2, title=title, pageType=pageType, paragraph=paragraph, tlog=tlog, hlog=hlog,ttime=ttime, htime=htime)
	
app.run(debug=True)