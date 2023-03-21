from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('DZ16-page1.htm')

@app.route('/2')
def page2():
    return render_template('DZ16-page2.htm')

if __name__ == '__main__':
    app.run()
