import requests
import json

URL = 'https://random-word-api.herokuapp.com/word?number='


def get_words(num: int, unique_words: set) -> str:
    if num >= 10_000:
        raise StopIteration("Max generation of words = 10_000")
    else:
        count = 0
        while count < num:
            portion = num - count
            print(f'words already received: {count}, more requested: {portion}')
            response = requests.get(f'{URL}{portion}').text
            words = json.loads(response)
            for word in words:
                if not word in unique_words:
                    yield word
                    unique_words.update([word])
                    count += 1


if __name__ == "__main__":
    unique_words = set()
    words = []
    for _ in range(5):
        for i in get_words(9_999, unique_words):
            words.append(i)
        print('-' * 45)
    print(f'Received unique words: {len(set(words))}, should be received: {5 * 9_999}')
