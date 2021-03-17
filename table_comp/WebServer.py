from flask import Flask
import Parsing
app = Flask(__name__)





from flask import request

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    reply_user,infoOut = Parsing.superSearch(request.args.get("comp"))
    print(infoOut)
    return str(infoOut)


@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)