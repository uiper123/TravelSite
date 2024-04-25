from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next_page1')
def next_page1():
    return render_template('next_page1.html')

@app.route('/next_page1/next_page2')
def next_page2():
    return render_template('next_page2.html')

@app.route('/next_page1/next_page2/next_page3')
def next_page3():
    return render_template('next_page3.html')

if __name__ == '__main__':
    app.run(debug=True)