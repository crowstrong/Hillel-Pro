from flask import Flask

from webargs import fields
from webargs.flaskparser import use_kwargs

from database_handler import execute_query, format_records

app = Flask(__name__)


@app.route('/price')
@use_kwargs(
    {
        'country': fields.Str(required=False, missing=None)
    },
    location='query'
)
def order_price(country) -> str:
    if country:
        sales_by_country = f'''SELECT BillingCountry ,COUNT(*), (UnitPrice * SUM(Quantity)) FROM invoice_items
                    INNER JOIN invoices AS i ON i.InvoiceId = invoice_items.InvoiceId
                    WHERE i.BillingCountry = \'{country}\''''
        records_country = execute_query(sales_by_country)
        if records_country[0][0] != None:
            return format_records(records_country)
        else:
            return f'Items for \'{country}\' not found'
    else:
        sales_by_all_countries = '''SELECT BillingCountry , COUNT(*), (UnitPrice * SUM(Quantity)) FROM invoice_items
                    INNER JOIN invoices AS i ON i.InvoiceId = invoice_items.InvoiceId
                    GROUP BY i.BillingCountry'''
        records_countries = execute_query(sales_by_all_countries)
        return format_records(records_countries)


@app.route('/info')
@use_kwargs(
    {
        'track': fields.Int(required=False, missing=1),
    },
    location="query"
)
def get_all_info_about_track(track) -> str:
    query = f'''SELECT artist.Name, album.title, track.name, genre.name,
       track.composer, track.milliseconds, track.bytes, media.name, track.unitprice
        FROM tracks AS track
        INNER JOIN artists AS artist ON artist.ArtistId = track.AlbumId
	    INNER JOIN albums AS album ON album.albumid = track.albumid
	    INNER JOIN genres AS genre ON genre.genreid = track.genreid
	    INNER JOIN media_types AS media ON media.mediatypeid = track.mediatypeid
	    WHERE TrackID = {track}'''
    records_info = execute_query(query)

    return format_records(records_info)


@app.route('/time')
def get_sum_tracks() -> str:
    query = 'SELECT SUM(Milliseconds) FROM tracks'
    records_tracks = execute_query(query)
    hours = round(int(records_tracks[0][0]) / 1000 / 60 / 60)
    return f'Time of all tracks of all albums in hours is {hours}h'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
