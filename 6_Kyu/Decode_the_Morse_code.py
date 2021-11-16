import re
def decodeMorse(morse_code):
    morse_code=morse_code.strip()
    letras=[]
    palabras=""
    txt = re.split("\s\s\s",morse_code)
    for i in range (0,len(txt)):
        letras.append(re.split("\s",txt[i]))
    for i in range (0,len(letras)):
        palabras+=' '
        for j in range (0,len(letras[i])):
            letras[i][j]=re.sub(" ", "", letras[i][j])
            letras[i][j]=re.sub(" ", "",letras[i][j])
            x=letras[i][j].replace(letras[i][j],MORSE_CODE[letras[i][j]])
            palabras+=x
    palabras=re.sub(" ", "", palabras,1)
    return(palabras)
