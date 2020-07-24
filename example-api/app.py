from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def predictive_request():
    from main import cat
    return cat(request)


if __name__ == '__main__':
    app.run()
