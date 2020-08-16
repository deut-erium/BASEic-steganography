from base64 import b64encode, b64decode, b32encode, b32decode
import string
from itertools import product
from tqdm import tqdm

CHARSET = string.printable.encode()
B32_CHARSET = (string.ascii_uppercase + string.digits).encode()
ASCII_LOWER = string.ascii_lowercase.encode()
WHITESPACE = string.whitespace.encode()
ALPHA_SPACE = (string.ascii_uppercase + string.ascii_lowercase + string.whitespace).encode()

    
FOUND_ASCII_TRIPLES = {}
FOUND_SPACEY_TRIPLES = {}
for perm in tqdm(product(B32_CHARSET,repeat=4), ascii=False,desc="Finding Triples",total=36**4):
    b64_repr = bytes(perm)
    resultant = b64decode(b64_repr)
    if resultant.isalpha():
        try:
            FOUND_ASCII_TRIPLES[resultant.lower()].append(resultant)
        except KeyError:
            FOUND_ASCII_TRIPLES[resultant.lower()] = []
    elif all(i in ALPHA_SPACE for i in resultant):
        try:
            FOUND_SPACEY_TRIPLES[resultant.lower()].append(resultant)
        except KeyError:
            FOUND_SPACEY_TRIPLES[resultant.lower()] = []

UNFOUND_TRIPLES = []
UNFOUND_WITH_SPACES = []

def check_with_spaces(substr,dic):
    return any(chr(i).encode()+substr[1:] in dic for i in WHITESPACE) or any(substr[:-1]+chr(i).encode() in dic for i in WHITESPACE)

for perm in tqdm(product(ASCII_LOWER,repeat=3),ascii=False,desc="Finding unmatched triples", total=26**3):
    trial = bytes(perm)
    if trial not in FOUND_ASCII_TRIPLES:
        UNFOUND_TRIPLES.append(trial)
        if not check_with_spaces(trial, FOUND_SPACEY_TRIPLES):
            UNFOUND_WITH_SPACES.append(trial)

def master_encode(strng):
    result = b''
    index = 0
    while index<len(strng):
        current = strng[index:index+3]
