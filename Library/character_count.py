# coding: utf-8

import unicodedata


def count_characters(text):

    count = 0

    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1

    return count


def check_text_length(text):

    count = count_characters(text)

    if count > 280:
        text = text[:268] + "..文字数((ry"
    
    return text
