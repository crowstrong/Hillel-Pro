from flask import Flask

from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from database_handler import execute_query, format_records

app = Flask(__name__)


@app.route('/stats_by_city')
@use_kwargs(
    {
        "genre": fields.Str(
            required=True,
            validate=validate.Regexp("[a-zA-Z\s\W]")
        )
    },
    location="query"
)
def stats_by_city(genre):
        query = f'''
            SELECT BillingCountry, max(count)
            FROM (
            SELECT genres.Name, invoices.BillingCountry, COUNT(invoices.BillingCountry) as count
            FROM genres
            INNER JOIN tracks ON genres.GenreId = tracks.GenreId
            INNER JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
            INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
            GROUP BY genres.Name, invoices.BillingCountry
            )
            WHERE Name=\'{genre}\'
            '''
        genre_format = execute_query(query)
        if genre_format[0][0] != None:
            return format_records(genre_format)
        else:
            return f'Genre \'{genre}\' is not found'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
