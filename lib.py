lookup_table = ["A", "Á", "B", "C", "D", "E", "É", "F", "G", "H", "I", "Í", "J",
                "K", "L", "M", "N", "O", "Ó", "Ö", "Ő", "P", "Q", "R", "S", "T",
                "U", "Ú", "Ü", "Ű", "V", "W", "X", "Y", "Z", "a", "á", "b", "c",
                "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n",
                "o", "ó", "ö", "ő", "p", "q", "r", "s", "t", "u", "ú", "ü", "ű",
                "v", "w", "x", "y", "z", ",", "?", ";", ".", ":", "-", "_", "*",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "§", "'", '"',
                "+", "!", "%", "/", "=", "(", ")", "~", "ˇ", "^", "˘", "°", "˛",
                "`", "˙", "´", "˝", "¨", "¸", "|", "{", "}", "<", ">", "#", "&",
                "@", " "]


def obfuscate(filename: str, strings: list):
    ids = []
    bin_l = [hex(99), hex(116), hex(102), hex(45), hex(49), hex(54), hex(len(strings))]
    all_chars = 0
    for a in strings:
        all_chars += len(a)
    str_num = len(strings)
    str_i = 0
    str_i_l = []
    for b in range(str_num):
        str_i_l.append(0)
    while not len(ids) == all_chars * 2:
        cs = strings[str_i]
        if str_i_l[str_i] > len(cs) - 1:
            fail = True
        else:
            fail = False
        if not fail:
            cc = cs[str_i_l[str_i]]
            ids.append(str_i)
            ids.append(lookup_table.index(cc))
            str_i_l[str_i] += 1
        if str_i == str_num - 1:
            str_i = 0
        else:
            str_i += 1
    for f in ids:
        bin_l.append(hex(f))
    binary = bytearray(int(x, 16) for x in bin_l)
    with open(filename, "wb") as file:
        file.write(binary)
    return bin_l


def decode_binary(filename: str):
    with open(filename, "rb") as o:
        file = o.read()
    hx = [f"0x{byte:02x}" for byte in file]
    ids = [f"{int(lu_id, 16)}" for lu_id in hx]
    return ids


def decode(filename: str):
    ids = decode_binary(filename)
    if not ids[:6] == ['99', '116', '102', '45', '49', '54']:
        raise TypeError("File not a cff file.")
    str_num = int(ids[6])
    ids = ids[7:]
    str_id = 0
    strings = []
    for _ in range(str_num):
        strings.append([])
    for num in [number for number in range(0, len(ids), 2)]:
        strings[int(ids[num])].append(lookup_table[int(ids[num + 1])])
    final_str = []
    for string in strings:
        final_str.append(''.join(string))
    return final_str
