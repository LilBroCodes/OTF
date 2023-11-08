import helper as ctflib

texts = ["All she wanted was the answer, but she had no idea how much she would hate it.",
         "He was an introvert that extroverts seemed to love.",
         "Flash photography is best used in full sunlight.",
         "Green should have smelled more tranquil, but somehow it just tasted rotten.",
         "It was the first time he had ever seen someone cook dinner on an elephant.",
         "He decided that the time had come to be stronger than any of the excuses he'd used until then."]

ctflib.obfuscate("obfsc.ctf", texts)
txt = ctflib.decode("obfsc.ctf")

with open("decoded.txt", "w") as file:
    file.writelines([string + '\n' for string in texts])
