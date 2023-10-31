from flask import Flask, render_template,request,jsonify,send_file

app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.route('/',methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/login',methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

@app.route('/home',methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)