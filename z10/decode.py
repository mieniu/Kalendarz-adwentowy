words = []

with open("szyfrogram.in") as ifile:
    words = ifile.read()

def change_letter(i):
    if   i == 'O': return 'A'
    elif i == 'S': return 'I'
    elif i == 'Y': return 'O'
    elif i == 'G': return 'E'
    elif i == 'M': return 'Z'
    elif i == 'C': return 'N'
    elif i == 'T': return 'R'
    elif i == 'Q': return 'W'
    elif i == 'š': return 'S'
    elif i == 'L': return 'T'
    elif i == 'I': return 'C'
    elif i == 'U': return 'Y'
    elif i == '': return 'K'
    elif i == 'F': return 'D'
    elif i == '': return 'P'
    elif i == 'B': return 'M'
    elif i == 'Z': return 'U'
    elif i == 'X': return 'J'
    elif i == 'W': return 'L'
    elif i == 'R': return 'Ł'
    elif i == '': return 'B'
    elif i == '': return 'G'
    elif i == 'A': return 'Ę'
    elif i == '': return 'H'
    elif i == '': return 'Ą'
    elif i == 'P': return 'Ó'
    elif i == '': return 'Ż'
    elif i == 'K': return 'Ś'
    elif i == 'J': return 'Ć'
    elif i == 'H': return 'F'
    elif i == 'N': return 'Ń'
    elif i == 'E': return 'Q'
    elif i == 'ť': return 'Ź'
    elif i == 'D': return 'V'
    elif i == 'V': return 'X'
    elif i in '0123456789!?.;,:- \n\t\"[*())]': return i
    elif i in 'ĹÄĂ': return ''
    else: return '_'

with open("z10_text.out", 'w+') as ofile:
    for i in words:
        ofile.write(change_letter(i))
