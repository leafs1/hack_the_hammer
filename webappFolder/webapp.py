from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



app = Flask(__name__, static_folder='public', static_url_path='')

directions = {
    "a": ""
}

items = ["sneakers", "heels", "boots", "running_shoes", "top", "bottoms", "sweaters", "coat", "scarf"]

#wishlist holds items selected from the user
wishlist = []


@app.route('/')
def home():
    return (render_template('index.html', directions=directions, items=items, wishlist=wishlist))

#@app.route('/addDirection', methods=['POST'])
#def addWebsite():
#    data = request.form
#    directions[request.form['startPoint']] = request.form['endPoint']
#    return(redirect(url_for('home'), code=302))

@app.route('/addItem', methods=['POST'])
def additem():
    data = request.form
    wishlist.append(data['items'])
    print(data)
    print(wishlist)

    return (redirect(url_for('home'), code=302))





cred = credentials.Certificate('shoppermapper-56b08-firebase-adminsdk-tk39h-442f6f8488.json')
default_app = firebase_admin.initialize_app(cred)


# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://shoppermapper-56b08.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())



if __name__ == "__main__":
    app.run(debug=True)