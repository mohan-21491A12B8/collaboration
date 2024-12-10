from flask import Flask, render_template, request ,redirect
app=Flask(__name__)
@app.route(" ", methods=["GET"])
def homepage():
    return "<h1>Collaboration Project</h1>"

@app.route("/home", methods=["GET"])
def frontend():
    return render_template("index.html")

database={}

@app.route("/reg_data", methods=["POST"])
def get_reg_data():
    user={}        #newly used 6-12-2024 after noon 
    name=request.form["u_name"]
    email=request.form["u_email"]
    phone=request.form["u_num"]
    password=request.form["u_pwd"]

    user["user_name"]=name
    user["user_email"]=email
    user["user_phone"]=phone
    user["user_pwd"]=password
    database[name]=user        
    return redirect("/home")

@app.route("/view",methods=["GET"])
def view_database():
    return database

app.run(debug=True)