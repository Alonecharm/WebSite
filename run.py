# encoding: utf-8
import config
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def base():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()