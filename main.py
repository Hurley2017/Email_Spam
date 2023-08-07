from flask import Flask, request, render_template
from Model import retCheck

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Greet():
    return render_template('page.html')

@app.route('/classify', methods=['POST'])
def Classify():
    response = {"status": "failed", "message": ""}
    data = request.json
    text = data["text"]
    response["status"] = "success"
    response["message"] = retCheck(text)
    return response


if __name__ == "__main__":
    app.run(debug=True)