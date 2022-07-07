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
            'first_name': fake_instance.first_name(),
            'last_name': fake_instance.last_name(),
            'email': fake_instance.unique.email(),
            'password': fake_instance.password(length=random.randint(10, 20)),
            'birthday': str(fake_instance.date_of_birth(minimum_age=18, maximum_age=28))
        } for data in range(quantity)
    ]
    df = pd.DataFrame(columns=['First Name', 'Last Name', 'Email', 'Password', 'Birthday'])
    for p in students_data:
        df = pd.concat([df, pd.DataFrame(p, index=[0])], ignore_index=True)
        df.to_csv('students_data.csv', index=False)

    app.config.update(JSON_SORT_KEYS=False)

    return jsonify(students_data)


def currency_checking(existing, request):
    if request not in existing:
        return abort(400, f'Incorrect currency code. Existing codes: {existing}')


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
    url: dict = requests.get('https://bitpay.com/currencies').json()
    url: list = url['data']

    currency_codes: list = [currency['code'] for currency in url]

    currency_checking(currency_codes, currency)

    response: dict = requests.get(f'https://bitpay.com/api/rates/{currency}').json()
    rate: float = round(response['rate'] * int(count), 2)
    symbol: str = next(bitpay_currency['symbol'] for bitpay_currency in url if bitpay_currency['code'] == currency)
    current_datetime = datetime.now()
    return f'{count} BTC = {rate}{symbol} for the current date {current_datetime}'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
