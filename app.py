from flask import Flask 

app=Flask(__name__)


@app.route('/')
def index():
    return "this deployement is the second one  dockerized"




if __name__=='__main__':
    app.run()
