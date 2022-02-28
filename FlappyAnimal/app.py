from flask import Flask, render_template, request, redirect,jsonify
import pymongo as connection

app = Flask(__name__)

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


# Check for Login credintial if not exist redirect to register page 
@app.route('/login', methods = ['GET','POST'])
def loginPage():
    collection = database[collectionName]
    if request.method == 'POST':
        userEmail = request.form['email']
        userPassword = request.form['password'] 
        for value in collection.find():
            if value['Email'] == userEmail and value['Password'] == userPassword:
                return render_template('profile.html')
        return render_template('register.html')
       

# Registration page
@app.route('/register',methods = ['GET','POST'])
def register():
    collection = database[collectionName]

    if request.method == "POST":

        userName = request.form['username']
        email = request.form['email']
        password = request.form['password']
        record = {
           "Username":userName,
           "Email":email,
           "Password":password
        }
        userDetail = collection.insert_one(record)
        print("User registered successfully", userDetail)
        return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)


