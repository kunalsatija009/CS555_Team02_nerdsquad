from flask import Flask, render_template, request, redirect,jsonify
import pymongo as connection
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
# Connection to the mongoDB database
db_name = "FlappyAnimal"
dbConnection = connection.MongoClient( "mongodb://localhost:27017/")


# Check for database else will create one
def checkDB(db_name, dbConnection):
    dbList = dbConnection.list_database_names()
    print(dbList)
    if db_name in dbList:
         print("Database is already exists")
    else:
        database = dbConnection[db_name]
        print("Database with db_Name created", database)


# Check for collection in Database
collectionName = "UserDetails"
database = dbConnection[db_name]
def check_collection(collectionName,database):
    collectionList = database.list_collection_names()
    print(collectionList)

    if collectionName in collectionList:
        print(collectionName + "Collection is exists")
        
    else:
        collection = database[collectionName]
        print("collection with collectionName is created", collection)

# Routing the Home/Login Page
@app.route('/',methods = ['GET','POST'])
def homePage():
    return render_template('login.html')

# Routing the Register Page
@app.route('/signUp',methods = ['GET','POST'])
def signUpPage():
    return render_template('register.html')

# Check for Login credintial if not exist redirect to register page 
@app.route('/login', methods = ['GET','POST'])
def loginPage():
    collection = database[collectionName]
    if request.method == 'POST':
        email = request.form['email']
        userPassword = request.form['password'] 
        for value in collection.find():
            if value['Email'] == email and  bcrypt.check_password_hash(value['Password'], userPassword):
                return render_template('profile.html')
        return render_template('register.html')
       

# Registration page
@app.route('/register',methods = ['GET','POST'])
def registerPage():
    collection = database[collectionName]

    if request.method == "POST":

        userName = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = {
           "Username":userName,
           "Email":email,
           "Password":bcrypt.generate_password_hash(password)
        }
        userDetail = collection.insert_one(user)
        print("User registered successfully", userDetail)
        return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)


