import shlex


def clearing_input(_input: str):
    # Очистка двойных и более пробелов
    _input.strip()
    _input = ' '.join((_input.split()))
    print(_input)

s = input()
clearing_input(s)
import requests

