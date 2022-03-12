import string

TRANSLATION = str.maketrans(
    f"{string.ascii_lowercase}-",  # convert lower-case and dash
    f"{string.ascii_uppercase} ",  # to upper case and space
    "_",  # delete underscore
)


def abbreviate(words):
    return "".join(
        [word[0] for word in words.translate(TRANSLATION).split(" ") if word]
    )
