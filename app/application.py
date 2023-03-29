import string
from secrets import randbelow


def generate(length: int) -> str:
    """Function that generates the password of given length to command line

    Params
    ______
    length: int
        The length of the password

    Returns
    _______
    password: str
        Randomly generated password of given length
    """

    # Options for character pool include alphanumeric & special characters
    characters = string.ascii_lowercase + \
        string.ascii_uppercase + string.punctuation + string.digits
    char_length = len(characters)

    password = ''

    # Generate that sucker
    for _ in range(length):
        password = f'{password}{characters[randbelow(char_length)]}'
    return password
