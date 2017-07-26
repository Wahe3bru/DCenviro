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
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    title = "Data Centre Dashboard"
    paragraph = ["graph below"]
    pageType = 'graphs'
    df = pd.read_csv('csv/test.csv', index_col='Date', parse_dates=True)
    dataSet = pandas_highcharts.core.serialize(df, render_to='my-chart', output_type='json')
    return render_template('graph.html', chart=dataSet, title=title, pageType=pageType, paragraph=paragraph)
	
app.run(debug=True)