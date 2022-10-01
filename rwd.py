import requests
import json

URL = 'https://random-word-api.herokuapp.com/word?number='


def get_words(num: int) -> str:
    response = requests.get(URL + str(num)).text
    if num >= 10_000:
        raise StopIteration("Max generation of words = 10_000")
    else:
        yield from json.loads(response)


if __name__ == "__main__":
    for i in get_words(10):
        print(i)
