import random


import requests
import pandas as pd

from datetime import datetime
from flask import Flask, jsonify, abort
from faker import Faker
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

fake_instance = Faker('uk_UA')

app = Flask(__name__)
app.config.update(JSON_SORT_KEYS=False)


@app.route('/students')
@use_kwargs(
    {
        'quantity': fields.Int(
            load_default=50,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location='query'
)
def generate_students(quantity):
    students_data: list = [
        {
            'First_name': fake_instance.first_name(),
            'Last_name': fake_instance.last_name(),
            'Email': fake_instance.unique.email(),
            'Password': fake_instance.password(length=random.randint(10, 20)),
            'Birthday': str(fake_instance.date_of_birth(minimum_age=18, maximum_age=28))
        } for data in range(quantity)
    ]
    df = pd.DataFrame(students_data)
    df.to_csv('students_data.csv', index=False)

    return jsonify(students_data)


@app.route('/btc')
@use_kwargs(
    {
        'count': fields.Int(
            load_default=1,
            validate=[validate.Range(min=1)]
        ),
        'currency': fields.Str(
            load_default='USD'
        )
    },
    location='query'
)
def get_bitcoin_value(count, currency) -> str:
    url = requests.get('https://bitpay.com/currencies').json()
    url = url['data']

    currency_codes = [currency['code'] for currency in url]
    if currency not in currency_codes:
        abort(400, f'Incorrect currency code. Existing codes: {currency}')

    response = requests.get(f'https://bitpay.com/api/rates/{currency}').json()
    rate = round(response['rate'] * int(count), 2)
    symbol = next(bitpay_currency['symbol'] for bitpay_currency in url if bitpay_currency['code'] == currency)
    return f'{count} BTC = {rate}{symbol} for the current date {datetime.now()}'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
