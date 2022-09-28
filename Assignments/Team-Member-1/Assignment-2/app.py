from flask import Flask,render_template

app=Flask(__name__)



@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login1.html')

@app.route('/home')
def home():
    return render_template('INDEX.html')





if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
