alp=[]
def creator(word):
    x=False
    listo=list(word)
    for i in range(len(listo)):
        alp.append(listo[i])

    for i in range(26):
        for j in range(len(alp)):
            if alp[j]==chr(97+i):
                x=True
                exit
        if x:
            x=False
            continue            
        else:
            alp.append(chr(97+i))
    return alp

def fixer(word):
    listo=list(word)
    element_to_remove = " "
    new_list = [elem for elem in listo if elem != element_to_remove]
    for i in range(len(new_list)):
        try:
            int(new_list[i])
            new_list[i]=chr(int(new_list[i])+97)
        except ValueError:
            continue
    return new_list

def letter_positions(word):
    positions = []
    for letter in word:
        position = ord(letter.lower()) - ord('a') + 1
        positions.append(position)
    return positions
def mixer(key,word,alp):
    finalword=[]
    cup=""
    counter=0
    def_alp=alp.copy()
    key_pos=letter_positions(key)
    word_pos=letter_positions(word)
    for i in word_pos:
        for j in range(i-1):
            cup=alp[0]
            alp.pop(0)
            alp.append(cup)
        if counter==len(key_pos):
            counter=0
        numo=key_pos[counter]
        finalword.append(alp[numo-1])
        alp=def_alp.copy()
        counter=counter+1
    return "".join(finalword)
