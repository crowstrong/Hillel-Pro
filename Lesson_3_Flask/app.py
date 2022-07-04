import string

from flask import Flask
from random import choice, randint

import pandas as pd


app = Flask(__name__)


@app.route('/password')
def password_generator() -> str:
    password_options: str = ''.join(choice(
        string.ascii_letters + string.punctuation + string.digits) for x in range(randint(10, 20)))
    return password_options


@app.route('/csv')
def get_average_parameters():
    dataset = pd.read_csv('hw.csv')
    average = dataset.mean()
    return f"Average Height: {average.values[1:2]}, Average Weight: {average.values[2:]}"


if __name__ == '__main__':
    app.run(debug=True)
