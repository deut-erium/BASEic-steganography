# BASEic-steganography
A base confusing stenographic library to generate valid strings which can be decoded in multiple bases

**confusion of the highest orda**
## Usage
```
usage: encode.py [-h] [--input] [--show] [--file FILE]

optional arguments:
  -h, --help   show this help message and exit
  --input      read a single line directly from input
  --show       shows the transformed input which results in correct
               encoding
  --file FILE  reading text from file for conversion
```
## How it works
Currently it substitutes the word with its valid ascii leet variation such that the leet variation encodes to a base64 string containing only base32 characters.  

|character| substituting ascii leet|
|:-:|:--:|
|"a"|"a", "A", "4", "@"|
|"b"|"b", "B", "8", "6"|
|"c"|"c", "C", "("|
|"d"|"d", "D"|
|"e"|"e", "E", "3"|
|"f"|"f", "F"|
|"g"|"g", "G", "6", "9"|
|"h"|"h", "H", "#"|
|"i"|"i", "I", "1", "|", "!"|
|"j"|"j", "J", "]", ";"|
|"k"|"k", "K"|
|"l"|"l", "L", "1", "|"|
|"m"|"m", "M"|
|"n"|"n", "N"|
|"o"|"o", "O", "0"|
|"p"|"p", "P"|
|"q"|"q", "Q", "9"|
|"r"|"r", "R", "2"|
|"s"|"s", "S", "5", "$"|
|"t"|"t", "T", "7", "+"|
|"u"|"u", "U"|
|"v"|"v", "V"|
|"w"|"w", "W"|
|"x"|"x", "X"|
|"y"|"y", "Y"|
|"z"|"z", "Z", "2", "%"|
|"0"|"0"|
|"1"|"1"|
|"2"|"2"|
|"3"|"3"|
|"4"|"4"|
|"5"|"5"|
|"6"|"6"|
|"7"|"7"|
|"8"|"8"|
|"9"|"9"|
|" "|" ", "\t", "_"|

## TODO
- [ ] Ranking of possible leet variations, such that most suitable leet variation is selected
- [ ] Extension of leet to all possible unicode variations for a string
- [ ] Extension to other inter-base conversion rather than only base32 and base64
- [ ] Producing strings which base32 decode to somewhat meaningful
