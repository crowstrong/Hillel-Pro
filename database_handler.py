import sqlite3


def execute_query(query, args=()):
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records


def format_records(records: list) -> str:
    table = '<table>'
    for i in records:
        table += '<tr>'
        for j in i:
            table += '<td>' + str(j) + '</td>'
        table += '</tr>'
    table += '</table>'
    return table



