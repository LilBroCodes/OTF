Version 1.0
# Otf (Obfuscated Text Format) Documentation
## Usage:
### Functions:
#### Obfuscate:
Function that generates the .otf file, takes a filename, and a list of strings to obfuscate.

Example:

obfuscate("obfuscated.otf", ["string1", "string2"]) ->
file obfuscated.otf
#### Decode:
Function that takes a filename, and returns the list of strings in that file.

Example:
<br>
print(decode("obfuscated.otf")) ->
[string 1, 2, 3, 4 ...]
## Data structure:
### Headers:
The .otf file has two headers, both at the start of the file. the first 6 hex bytes will always be 63 74 66 2D 31 36, so ctf-16, which
references the old name of the file format, compact file format, with 16 indicating the fact that it is hex.

The second header, is at byte 7, which indicates the number of strings the file contains.

After the two headers, every even byte is an index to the lookup table*, with the previous bit referencing what string is the character for.
So the file will look like this: 
<headers> string id, character id, string id, character id...

Example: 01 09 02 32, which will be: string 1 : "H", string 2 : "W".

## * Lookup table:
["A", "Á", "B", "C", "D", "E", "É", "F", "G", "H", "I", "Í", "J",
"K", "L", "M", "N", "O", "Ó", "Ö", "Ő", "P", "Q", "R", "S", "T",
"U", "Ú", "Ü", "Ű", "V", "W", "X", "Y", "Z", "a", "á", "b", "c",
"d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n",
"o", "ó", "ö", "ő", "p", "q", "r", "s", "t", "u", "ú", "ü", "ű",
"v", "w", "x", "y", "z", ",", "?", ";", ".", ":", "-", "_", "*",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "§", "'", '"',
"+", "!", "%", "/", "=", "(", ")", "~", "ˇ", "^", "˘", "°", "˛",
"`", "˙", "´", "˝", "¨", "¸", "|", "{", "}", "<", ">", "#", "&",
"@", " "]