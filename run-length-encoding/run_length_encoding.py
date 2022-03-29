import itertools
from typing import Iterable


def decode(string: str) -> str:
    return "".join(decode_iter(string))


def encode(string: str) -> str:
    return "".join(encode_iter(string))


def decode_iter(string: str) -> Iterable[str]:
    """yield decoded elements"""
    count = 0
    for char in string:
        if char.isdigit():
            count *= 10
            count += int(char)
            continue

        if count:
            yield char * (count - 1)
            count = 0
        yield char


def encode_iter(string: str) -> Iterable[str]:
    """yield encoded elements"""
    while string:
        current_char = string[0]
        next_group = list(itertools.takewhile(lambda ch: ch == current_char, string))
        yield f"{len(next_group)}{current_char}" if len(
            next_group
        ) > 1 else current_char
        string = string[len(next_group) :]
