from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/picture')
def picture():
    roll = request.args.get('roll')
    return render_template('picture.html', roll = roll)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
