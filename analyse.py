from base64 import b64encode, b64decode, b32encode, b32decode
import string
from itertools import product
from tqdm import tqdm

CHARSET = string.printable.encode()
B32_CHARSET = (string.ascii_uppercase + '234567').encode()
ASCII_LOWER = string.ascii_lowercase.encode()
WHITESPACE = string.whitespace.encode()
ALPHA_SPACE = (string.ascii_uppercase + string.ascii_lowercase + string.whitespace).encode()

subs ={"a":["a","A","4","@"],
"b": ["b","B","8","6"],
"c":["c","C","("],
"d":["d","D"],
"e":["e","E","3"],
"f":["f","F"],
"g":["g","G","6","9"],
"h":["h","H","#"],
"i":["i","I","1","|","!"],
"j":["j","J","]",";"],
"k":["k","K"],
"l":["l","L","1","|"],
"m":["m","M"],
"n":["n","N"],
"o":["o","O","0"],
"p":["p","P"],
"q":["q","Q","9"],
"r":["r","R","2"],
"s":["s","S","5","$"],
"t":["t","T","7","+"],
"u":["u","U"],
"v":["v","V"],
"w":["w","W"],
"x":["x","X"],
"y":["y","Y"],
"z":["z","Z","2","%"],
"0":["0"],
"1":["1"],
"2":["2"],
"3":["3"],
"4":["4"],
"5":["5"],
"6":["6"],
"7":["7"],
"8":["8"],
"9":["9"],
" ":[" ","\t"]
}

def all_variations(word):
    ans = [""]
    for leetLetter in [subs[i] for i in word]:
        ans = [x+y for x in ans for y in leetLetter]
    return ans

def variation_gen(word):
    return product(*(subs[i] for i in word))
        

def all_valid_variations(word):
    result = []
    for variation in variation_gen(word):
        if all( i in B32_CHARSET for i in b64encode(''.join(variation).encode())):
            result.append("".join(variation))
    return result

def valid_variation(word):
    for variation in variation_gen(word):
        if all( i in B32_CHARSET for i in b64encode(''.join(variation).encode())):
            return "".join(variation)



NON_LEET = []
for perm in product(string.ascii_lowercase+' ',repeat=3):
    if not valid_variation(''.join(perm)):
        NON_LEET.append(''.join(perm))


    
# FOUND_ASCII_TRIPLES = {}
# FOUND_SPACEY_TRIPLES = {}
# for perm in tqdm(product(B32_CHARSET,repeat=4), ascii=False,desc="Finding Triples",total=36**4):
#     b64_repr = bytes(perm)
#     resultant = b64decode(b64_repr)
#     if resultant.isalpha():
#         try:
#             FOUND_ASCII_TRIPLES[resultant.lower()].append(resultant)
#         except KeyError:
#             FOUND_ASCII_TRIPLES[resultant.lower()] = []
#     elif all(i in ALPHA_SPACE for i in resultant):
#         try:
#             FOUND_SPACEY_TRIPLES[resultant.lower()].append(resultant)
#         except KeyError:
#             FOUND_SPACEY_TRIPLES[resultant.lower()] = []

# UNFOUND_TRIPLES = []
# UNFOUND_WITH_SPACES = []



# def check_with_spaces(substr,dic):
#     return any(chr(i).encode()+substr[1:] in dic for i in WHITESPACE) or any(substr[:-1]+chr(i).encode() in dic for i in WHITESPACE)

# for perm in tqdm(product(ASCII_LOWER,repeat=3),ascii=False,desc="Finding unmatched triples", total=26**3):
#     trial = bytes(perm)
#     if trial not in FOUND_ASCII_TRIPLES:
#         UNFOUND_TRIPLES.append(trial)
#         if not check_with_spaces(trial, FOUND_SPACEY_TRIPLES):
#             UNFOUND_WITH_SPACES.append(trial)

def transform(strng):
    """
    Transform the string to only lower alpha and numerics and spaces
    Converts uppercase to lower case and strips all other characters except 
    space
    """
    for char in string.punctuation+string.whitespace[1:]:
        strng=strng.replace(char,'')
    return strng.lower()+' '*(3-len(strng)%3)
    # return ''.join(strng.split(string.punctuation+string.whitespace[1:])).lower()
    # return strng.strip(string.punctuation+string.whitespace[1:]).lower()


def master_encode(strng):
    strng = transform(strng)
    result = ''
    i = 0 
    while i<len(strng)-3:
        try:

            current = strng[i:i+3] 
            if current in NON_LEET:
                if current[:2]+' ' not in NON_LEET:
                    result+=valid_variation(current[:2]+' ')
                    i+=2
                elif current[0]+'  ' not in NON_LEET:
                    result+=valid_variation(current[0]+'  ')
                    i+=1
                else:
                    result+=valid_variation('  '+current[0])
                    i+=1
            else:
                result+=valid_variation(current)
                i+=3
        except Exception as e:
            print(e,current)
    return result
        
strng_para = "In cryptography, a zero-knowledge proof or zero-knowledge protocol is a method by which one party (the prover) can prove to another party (the verifier) that they know a value x, without conveying any information apart from the fact that they know the value x. The essence of zero-knowledge proofs is that it is trivial to prove that one possesses knowledge of certain information by simply revealing it; the challenge is to prove such possession without revealing the information itself or any additional information"

strng2="""Steganography  is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography comes from Greek steganographia, which combines the words steganos meaning "covered or concealed", and graphia meaning "writing".

The first recorded use of the term was by Johannes Trithemius in his Steganographia, a treatise on cryptography and steganography, disguised as a book on magic. Generally, the hidden messages appear to be (or to be part of) something else: images, articles, shopping lists, or some other cover text. For example, the hidden message may be in invisible ink between the visible lines of a private letter. Some implementations of steganography that lack a shared secret are forms of security through obscurity, and key-dependent steganographic schemes adhere to Kerckhoffs's principle."""


# 'f  ','n  ','r  ','v  ' not there
# ' k ',' w ',' x ',' y ' not there
# '  i' for all i there 

