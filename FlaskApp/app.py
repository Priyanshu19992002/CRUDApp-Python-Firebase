import pyrebase
import numpy
from flask import *

#Add your database config part in the below code
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)

#Main Page Reading all existing page
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = request.form.to_dict()
        db.child('name').push(user)
        return redirect('/')
    else:
        data = db.child('name').get()
        return render_template('index.html',t=data.val())

#Create New User Page
@app.route('/new', methods=['GET'])
def newuser():
    return render_template('new.html')

#Updating Existing user
@app.route('/<id>',methods = ['GET','POST'])
def getuser(id):
    if request.method == 'POST':
        userdata = request.form.to_dict()
        db.child('name').child(id).update(userdata)
        return redirect('/')
    else:
        data = db.child('name').child(id).get();
        return render_template('edit.html',t=data.val(),userid=id)

#Deleting Existing User  
@app.route('/<id>/delete', methods = ['GET','POST'])
def deleteuser(id):
    if request.method == 'POST':
        db.child('name').child(id).remove()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
