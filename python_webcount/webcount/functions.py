import requests


def most_common_word(words: list, text: str):
    word_frequency = {wrd: text.count(wrd) for wrd in words}
    return sorted(words, key=word_frequency.get)[-1]


def most_common_word_in_web_page(words, url):
    response = requests.get(url)
    text = response.text
    return most_common_word(words, text)
