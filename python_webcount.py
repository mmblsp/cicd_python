import requests


def most_common_worl_in_web_page(words, url):
    response = requests.get(url)
    text = response.text

    word_frequency = {wrd: text.count(wrd) for wrd in words}
    return sorted(words, key=word_frequency.get)[-1]


if __name__ == "__main__":
    most_common = most_common_worl_in_web_page(
        ['python', 'Python', 'programming'],
        'https://python.org'
    )
    print(most_common)
