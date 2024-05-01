from flask import Flask, render_template
import json

with open('places.json', 'r', encoding='utf-8') as f:
    places_data = json.load(f)
    
with open('map.geojson', 'r') as f:
    geojson_data = json.load(f)

with open('bounce.geojson', 'r') as f:
    bounce_data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next_page1')
def next_page1():
    return render_template('next_page1.html', geojson_data=json.dumps(geojson_data), bounce_data=json.dumps(bounce_data), places_data=json.dumps(places_data))

@app.route('/next_page1/next_page2')
def next_page2():
    return render_template('next_page2.html')

@app.route('/next_page1/next_page2/next_page3')
def next_page3():
    return render_template('next_page3.html')

if __name__ == '__main__':
    app.run(debug=True)