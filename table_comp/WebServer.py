from flask import Flask, render_template
import Parsing, HTML

app = Flask(__name__)


from flask import request

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    reply_user,infoOut = Parsing.superSearchS(request.args.get("comp"))
    print(infoOut)
    if infoOut[0]=='Не найденно':
        infoOut[0]='Не найденно+Не найденно+Не найденно+Не найденно+Не найденно+Не найденно'
        HTML.createTable(infoOut)
    else:
        HTML.createTable(infoOut)
    return render_template('reply.html')


@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)