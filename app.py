#flask
from flask import Flask ,request
app=Flask(__name__)

@app.route("/hello/<int:a>")
def fun(a):
    # return f"<p>Hi,I am hari!</p>{request.base_url.strip('http://').split('/')}"
    return f"a:{a}"

app.run(debug=True,host="0.0.0.0")