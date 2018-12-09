from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='public', static_url_path='')

websites = {
    "Google": "http://google.com",
    "Webkinz": "http://webkinz.com",
    "This project": "localhost:5000"
}

@app.route('/')
def home():
    return (render_template('index.html', name='Michael', websites=websites))

@app.route('/addWebsite', methods=['POST'])
def addWebsite():
    data = request.form
    websites[request.form['siteName']] = request.form['siteUrl']
    return(redirect(url_for('home'), code=302))

if __name__ == "__main__":
    app.run(debug=True)