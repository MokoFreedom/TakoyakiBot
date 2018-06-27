# coding: utf-8

import unicodedata
import os


def count_characters(text):

    count = 0
    new_text = ""

    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1
        if count <= 265:
            new_text += c
        else:
            break

    return new_text


def check_text_length(text):

    new_text = count_characters(text)

    return new_text
