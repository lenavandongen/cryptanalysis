"""for most functions it will take temp_text as an input, but will turn this
into either the text as lowercase, as this is easier to work with, or remove all
punctuation, again for simplicity"""

import readline #allows you to re input what was inputted before by pressing the up arrow
from math import *
from itertools import permutations
from collections import Counter

file = ["", ""]
with open("/home/lena/Documents/cipher_challenge_text.txt", "r") as temp_file:
    file[0] = temp_file.read()

MENU = """
h / help:       gives options
f / frequency:  will give you a list of the frequency of the letters
l / length:     gives you the length of the text, and all the factor pairs
q / quit:       exit the program
b / backwards   prints the text reversed

w               will write the previous text to a file
w upper         will write the previous text in uppercase to a file
u 0             will use the original text to work with
u 1             will use the written text to work with

p / print:      prints the coded text
p plain:        prints without punctuation or spaces
p space:        prints without punctuation, but with spaces

c / caesar:     tries to do a caesar cipher based on letter frequency
c plain:        gives the caesar cipher based on letter frequencies without spaces
c 6:          - tries to do a caesar cipher (6)
c ab:         - tries to do a caesar cipher (1)

s ab,eg:      - substitutes the first letter for the second letter
ss / save:      saves the substitutions made in the previous command
ss clear:       returns the encoded message to the original
sr ab         - replaces any lowercase letters that had already been substituted
sl              gives a list of all subsitutions made

k myword      - does a keyword substitution with the given word (each letter must be unique)
at / atbash     does an atbash cipher (reverses alphabet)
#af / affine

ioc:            draws out the IOC for each key length
v 3:          - calculates a key, given the key length, (3)
v abc:        - does a vigenere cipher (using the key abc)
v / vigenere:   does a vigenere cipher on the text

fb              bigrams
#ft              trigrams
t               lists the most common trigrams and their frequencies
td              gives the distances of the most common trigram
td abc          gives the distances of the trigram given (abc)

g c 7         - will print out a grid (7 columns) going down the columns
g r 7         - will print out a grid (with 7 columns) going across the rows
ct c/r 43210      - columnar transposition, given the order of the columns (reversed)
"""



e_f_letters = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
E_F_VALUES = [0.1202, 0.091, 0.0812, 0.0768, 0.0731, 0.0695, 0.0628, 0.0602, 0.0592, 0.0432, 0.0398, 0.0288, 0.0271, 0.0261, 0.0230, 0.0211, 0.0209, 0.0203, 0.0182, 0.0149, 0.0111, 0.0069, 0.0017, 0.0011, 0.0010, 0.0007]

def frequency_order(raw_text, repeats):
    """ analyses the frequency of each letter, and puts them is a list in order
    of size. You can let it only do a certain number of letters, but the program
    tends to use all 26"""
    text = raw_text.lower()
    frequencies = [0 for _ in range(26)]
    for i in text:
        if i.isalpha():
            frequencies[ord(i)-97] +=1
    r_values = []
    for _ in range(repeats):
        r_values.append(chr(frequencies.index(max(frequencies)) + 97))
        frequencies[frequencies.index(max(frequencies))] = -1
    return(r_values)

def frequency_nums(temp_text):
    '''returns a list of the frequencies of the letters, sorted by size'''
    text = remove_punct(temp_text, False)
    t_frequencies = [0.0 for _ in range(26)]
    frequencies = []
    for i in text:
        if i.isalpha():
            t_frequencies[ord(i)-97] += 1.0/len(text)
    for i in range(26):
        frequencies.append(max(t_frequencies))
        t_frequencies.remove(max(t_frequencies))
    return(frequencies)

def frequency_graphics(inputs):
    for i in range(26):
        print("{}: ".format(e_f_letters[i]), end = "")
        for j in range(ceil(E_F_VALUES[i]*750)):
            print("\u2500", end ="")
        print()
    print("\n")
    for i in range(26):
        print("   ", end = "")
        for j in range(ceil(inputs[i]*750)):
            print("\u2500", end = "")
        print()

def remove_punct(text, space):
    """removes all punctuation, and allows you to choose whether to keep spaces
    (the space parameter is a boolean, where True is keeping the spaces)"""
    new_text = ""
    for i in text:
        if i.isalpha() or i.isnumeric() or i in "+#":
            new_text += i.lower()
        elif space and i == " ":
            new_text += " "
    return(new_text)


def choose_key(new_e):
    """ Does the logic to turn a letter into a number (the distance it is away
    from the letter "e") """
    key = ((ord("e")) - (ord(new_e))) % 26
    return(key)

################################################################################
def caesar(temp_text, key):
    """does the actual caesar cipher, given the text and a key (it will move
    everything forwards by the key)"""
    text = temp_text.lower()
    new_text = ""
    for i in text:
        if i.isalpha():
            caesar_letter = ord(i) + key
            if caesar_letter > 122:
                caesar_letter -= 26
            new_text += chr(caesar_letter)
        else:
            new_text += i
    return(new_text)

def substitute(text, subs):
    """subs is a 2 letter string, and it will replace all instances of subs[0]
    with subs[1] in the text"""
    new_text = ""
    for i in text:
        replaced = False
        for j in subs:
            if j[0] == i.lower() and i.lower() != i:
                new_text += j[1]
                replaced = True
        if not replaced:
            new_text += i
    return(new_text)

def sub_lower(text, subs):
    """same function as substitute, but instead of subtituting uppercase letters
    it does lowercase letters"""
    new_text = ""
    for i in text:
        replaces = False
        for j in subs:
            if j[0] == i:
                new_text += j[1]
                replaced = True
        if not replaces:
            new_text += i
    return(new_text)

def affine_encrypt(text, a, b):
    new_text = ""
    for i in text:
        if i.isalpha():
            new_text += chr((( (ord(i.lower())-98) * a )+b)%26 + 97)
        elif i == " ":
            new_text += " "
    return(new_text)

def affine_decrypt(text, a, b):
    ai = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
    new_text = ""
    for i in text:
        if i.isalpha():
            new_text += chr((ai[a]*(ord(i.lower()) - 97 - b))%26 + 97)
        elif i == " ":
            new_text += " "
    return(new_text)

def affine_prob(text):
    legal_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    possible = [[] for _ in range(26*len(legal_a))]
    for a in legal_a:
        for b in range(26):
            possible[legal_a.index(a)*len(legal_a) + b].append(a)
            possible[legal_a.index(a)*len(legal_a) + b].append(b)
            total = 0
            for i in range(26):
                total += affine_single(chr(i+97), a, b)
            possible[legal_a.index(a)*len(legal_a) + b].append(total)
    minimum = 0
    min_val = 0
    for i in range(len(possible)):
        if possible[i][2] < minimum:
            minimum = possible[i][2]
            min_val = i
    return(min(possible))

def affine_single(letter, a, b):
    return chi_squared(letter, affine_decrypt(letter, a, b))

def atbash(temp_text):
    text = temp_text.lower()
    new_text = ""
    for i in text:
        if i.isalpha():
            new_text += chr( 122 - (ord(i) - 97))
        else:
            new_text += i
    return(new_text)

def keyword(text, word):
    subs = []
    for i in range(len(word)):
        subs.append(word[i] + chr(i+97))
    lastcipher = ord(word[-1])
    lastplain = len(word) + 97 - 1
    while not lastplain>=(97+25):
        if not chr((lastcipher+1-97)%26+97) in word:
            subs.append(chr( (lastcipher+1 - 97)%26 + 97) + chr(lastplain+1))
            lastplain+=1
        lastcipher= (lastcipher+1 - 97)%26 + 97
    return(subs)
################################################################################

COMMON_BIGRAMS = "th 1.52,he 1.28,in 0.94,er 0.94,an 0.82,re 0.68,nd 0.63,at 0.59,on 0.57,nt 0.56,ha 0.56,es 0.56,st 0.55,en 0.55,ed 0.53,to 0.52,it 0.50,ou 0.50,ea 0.47,hi 0.46,is 0.46,or 0.43,ti 0.34,as 0.33,te 0.27,et 0.19,ng 0.18,of 0.16,al 0.09,de 0.09,se 0.08,le 0.08,sa 0.06,si 0.05,ar 0.04,ve 0.04,ra 0.04,ld 0.02,ur 0.02".split(",")
for i in range(len(COMMON_BIGRAMS)): COMMON_BIGRAMS[i] = COMMON_BIGRAMS[i].split(" ")

def display_freqs(freqList,total):
    for i in range(len(freqList)):
        bar = ""
        for j in range(ceil(freqList[i][1]/total*2000)):
            bar += "\u2500"
        print(freqList[i][0],bar)

def typ_bigram_freq():
    co_bi = COMMON_BIGRAMS
    total_freq = 0
    for i in range(len(co_bi)):
        co_bi[i][1] = float(co_bi[i][1])
        total_freq = round(total_freq + co_bi[i][1],2)
    display_freqs(co_bi,total_freq*3)

def check_freqs(message, show):
    message = message.lower()
    message_bigrams = []
    co_bi = COMMON_BIGRAMS
    total_freq = 0
    for i in range(len(co_bi)):
        bigram_freq = message.count(co_bi[i][0])
        message_bigrams.append([co_bi[i][0],bigram_freq])
        total_freq = total_freq + bigram_freq
    if show == True: display_freqs(message_bigrams,int(len(message)-1),)
    return message_bigrams

def compare_freqs(message):
    message = message.lower()
    message_freqs = check_freqs(message, False)
    display_freqs(message_freqs,len(message)-1)
    total_bigram_types = 0
    for i in range(len(message_freqs)):
        if message_freqs[i][1] > 0: total_bigram_types += 1


################################################################################

E_ALPHA_VALUES = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.0230, 0.0203, 0.0592, 0.0731, 0.0010, 0.0069, 0.0398, 0.0261, 0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.091, 0.0288, 0.0111, 0.0209, 0.0017, 0.0211, 0.0007]

def guess_vigenere(temp_text, length):
    #will guess each individual letter for all the letters in the length of the keyword
    text = remove_punct(temp_text, False)
    text_sections = [text[i::length] for i in range(length)]
    key_list = [guess_one_letter(text_sections[i]) for i in range(length)]
    key = "".join(key_list)
    return(key)

def guess_one_letter(text):
    '''will convert a number into a letter that it expects the key to be'''
    place = lowest_difference(text)
    letter = chr(place + 97)
    return(letter)

def lowest_difference(text):
    '''creates a list of the difference for all the letters, and then returns
    the lowest one'''
    f = []
    for i in range(26):
        letter = chr(i + 97)
        f.append(chi_squared(text, letter))
    value = min(f)
    value_place = f.index(value)
    return(value_place)

def chi_squared(text, letter):
    '''find the difference between the frequency and english and squares it, for
    a single letter'''
    number = ord(letter) - 97
    total = 0
    for i in range(26):
        check_l = chr(((i + number)%26)+97) #suggested letter, going up alphabetically
        poss_f = individual_frequency(text, check_l) #decimal value
        difference = (poss_f - E_ALPHA_VALUES[i])**2
        total += difference
    return(total)

def individual_frequency(text, letter):
    '''returns a percentage (decimal) of how often the letter is in the text'''
    count = 0
    for i in text:
        if i == letter:
            count += 1
    frequency = count/len(text)
    return(frequency)

def vigenere(temp_text, temp_key):
    """given a key and the text, this will decode a vigenere-encoded text"""
    text = remove_punct(temp_text, True)
    key = temp_key.lower()
    new_text = ""
    key_index = 0
    for i in text:
        if i.isalpha():
            new = ((ord(i)-(ord(key[key_index])))%26)+97
            if new > 122:
                new-=26
            elif new < 97:
                new += 26
            new_text += chr(new)
            key_index = (key_index+1)%len(key)
        else:
            new_text += " "
    return(new_text)
################################################################################


'''from cipher import remove_punct

def rail_encrypting(temp_text, key, plain):
    if plain == 1:
        text = temp_text
    elif plain == 2:
        text = remove_punct(temp_text, False)
    else:
        text = remove_punct(temp_text,True)
'''

def IOC(temp_text, length):
    """calculates the IOC of a text, with a given key length. The higher it is,
    the more likely it is that that key is correct"""
    text = remove_punct(temp_text, False)
    ioc = [0 for _ in range(length)]
    final = 0
    for k in range(length):
        text_chunk = text[k::length] #all chars from k to end with step length
        for i in range(26):
            count = 0
            for j in text_chunk:
                if j == chr(i+97):
                    count += 1
            ioc[k] += count*(count-1)
        ioc[k] = ioc[k]/(len(text_chunk)* (len(text_chunk)-1))
    total = sum(ioc)
    final = total/length
    return(final)

def ioc_graphics(totals):
    """draws out the IOC for the key lengths 1 to 20, to make it easier to spot
    patterns in the data. Basically just makes everything look pretty. \ u2500
    is just a nice unicode character.
    first draws out the IOC expected for standard English to compare the results
    to"""
    key_lengths = [totals[i] for i in range(26)]
    print("En: ", end = "")
    for _ in range(66):
        print("\u2500", end="")
    print()
    for i in range(26):
        print("\n{:2}: ".format(i+1), end = "")
        for j in range(key_lengths[i]):
            print("\u2500", end="" )

def ioc_execute(text):
    """turns the IOC value into an integer that can be drawn out, and repeats
    this 20 times, for each of the key lengths 1 to 20"""
    keys = [0 for _ in range(26)]
    for i in range(26):
        keys[i] = (int(IOC(text,i+1)*1000))
    ioc_graphics(keys)

def v_guess_length(text):
    keys = [0.0 for _ in range(26)]
    for i in range(26):
        keys[i] = (IOC(text,i+1))
    length = keys.index(max(keys)) + 1
    return(length)
################################################################################

def factors(temp_text):
    text = remove_punct(temp_text, False)
    factors = []
    length = len(text)
    for i in range(1, floor(sqrt(length))+ 1):
        if length % i == 0:
            factors.append([i, int(length/i)])
    return(factors)

def make_grid(temp_text, width, column):
    text = remove_punct(temp_text, False)
    columns = [[] for _ in range(width)]
    if column:
        for i in range(len(text)):
            try:
                columns[ i // ceil(len(text)/width) ].append(text[i])
            except(IndexError):
                continue
    else:
        for i in range(len(text)):
            columns[i%width].append(text[i])
    return(columns)

def print_grid(text):
    for i in range(len(text[0])):
        for j in range(len(text)):
            try:
                print(text[j][i], end = " ")
            except(IndexError):
                break
        print("")

def transpose_grid(columns, order):
    new_columns = []
    for i in range(len(order)):
        new_columns.append(columns[order.index(min(order))])
        order[order.index(min(order))] = len(order) + 1
        #print(new_columns[i])
    return(new_columns)

def plain_from_grid(text_list):
    plain = ""
    for i in range(len(text_list[0])):
        for j in range(len(text_list)):
            try:
                plain+= text_list[j][i]
            except (IndexError):
                continue
    return(plain)
################################################################################

def swap(text):
    new_text = ""
    for i in range(0, len(text)-1, 2):
        new_text += (text[i+1])
        new_text += (text[i])
    return(new_text)


def triple(text):
    total = 0
    for i in range(len(text) - 2):
        if text[i] == text[i+1] and text[i+1] == text[i+2]:
            total += 1
    return(total)

def common_tri(text):
    trigrams = []
    for i in range(len(text)-3):
        current_tri = text[i:i+3]
        if not current_tri in (i[0] for i in trigrams):
            total = 1
            for j in range(i+1, len(text)-2):
                if text[j:j+3] == current_tri:
                    total += 1
            if total >= 5:
                trigrams.append([current_tri, total])
    return(trigrams)

def sort_tri(trigrams):
    sorted_tri = sorted(trigrams, key=lambda x: x[1])
    return(sorted_tri[::-1])

def tri_freq_distance(text, trigram):
    distances = []
    for i in range(len(text) - 3):
        if text[i:i+3] == trigram:
            j = i+3
            while(True):
                if text[j:j+3] == trigram:
                    distances.append(j-i)
                    break
                elif j == len(text) - 2:
                    break
                else:
                    j += 1
    return(distances)

def write_to_list(text, length):
    thingy = []
    print(text)
    for i in range(0, len(text), length):
        thingy.append(text[i:i+length])
        print(text[i:i+length])
    return(thingy)

def base_to_dec(from_base, convert):
    dec, power = 0, 0
    for i in range(len(convert)):
        temp = ord(convert[-i-1])
        if temp >= 65 and temp <= 90:
            digit = temp-55
        elif temp >= 97 and temp <= 122:
            digit = temp+10+26-97
        else:
            digit = temp - ord("0")
        dec += digit* (from_base**power)
        power += 1
    return(dec)

#thing = write_to_list(file[0], 3)
#print(thing)
#letters = ""
#for i in range(len(thing)):
#    print(base_to_dec(3, thing[i]))
#    letters += chr(65+int(base_to_dec(3, thing[i])))
#print(letters)

def main():
    text_to_use = file[0]
    sub_text = ""
    t = 0
    temp_text = file[t]
    substitutions = []
    while True:
        action = input("\nCipher_Challenge|action >> ").lower().split()
        print()
        if not action:
            continue
        try:
            if action[0] == "w":
                f = open("/home/lena/Documents/cipher_write.txt", "w")
                if len(action) == 2 and action[1] == "upper":
                    f.write(temp_text.upper())
                else:
                    f.write(temp_text)
                f.close()
                with open("/home/lena/Documents/cipher_write.txt", "r") as temp_file:
                    file[1] = temp_file.read()
                print(file[1])

            if action[0] == "u":
                if action[1] == "0" or action[1] == "1":
                    t = int(action[1])
                    print(file[t])

            if action[0] == "h" or action[0] == "help":
                print(MENU)

            elif action[0] == "f" or action[0] == "frequency":
                frequency_graphics(frequency_nums(file[t]))
                print(frequency_order(file[t], 26))

            elif action[0] == "q" or action[0] == "quit":
                break

            elif action[0] == "p" or action[0] == "print":
                if len(action) == 1:
                    print(file[t])
                elif action[1] == "plain":
                    temp_text = remove_punct(file[t], False)
                    print(temp_text)
                elif action[1] == "space":
                    temp_text = remove_punct(file[t], True)
                    print(temp_text)

            elif action[0] == "c" or action[0]== "caesar":
                if len(action) == 1:
                    temp_text = vigenere(file[t], guess_vigenere(file[t], 1))
                    print(temp_text)
                elif action[1] == "plain":
                    temp_text = remove_punct(caesar(file[t], choose_key(frequency_order(file[t], 1)[0])), False)
                    print(temp_text)
                elif action[1].isalpha():
                    temp_text = caesar(file[t], (ord(action[1][1].lower()) - ord(action[1][0].lower()))%26)
                    print(temp_text)
                else:
                    temp_text = caesar(file[t], int(action[1]))
                    print(temp_text)

            elif action[0] == "s":
                sub_text = substitute(text_to_use, action[1].split(","))
                temp_text = sub_text
                for i in range(len(action[1].split(","))):
                    substitutions.append(action[1].split(",")[i])
                print(sub_text)

            elif action[0] == "sr":
                sub_text = sub_lower(text_to_use, action[1].split(","))
                temp_text = sub_text
                for i in range(len(substitutions)):
                    if substitutions[i][1] == action[1][0]:
                        pos = i
                        break
                substitutions[pos][1] = action[1][1]
                print(sub_text)

            elif action[0] == "sl":
                print(substitutions)

            elif action[0] == "ss" or action[0] == "save":
                if len(action) == 1:
                    text_to_use = sub_text
                    print(text_to_use)
                    if text_to_use == text_to_use.lower():
                        print("\nfinished")
                elif action[1] == "clear":
                    text_to_use = file[t]
                    print(text_to_use)

            elif action[0] == "at" or action[0] == "atbash":
                temp_text = atbash(file[t])
                print(temp_text)

            elif action[0] == "af" or action[0] == "affine":
                temp_text = affine_decrypt(file[t], affine_prob(file[t])[0], affine_prob(file[t])[1])
                print(temp_text)

            elif action[0] == "k":
                sub_text = substitute(text_to_use, keyword(file[t], action[1]))
                temp_text = sub_text
                print(sub_text)

            elif action[0] == "ioc":
                ioc_execute(file[t])

            elif action[0] == "v" or action[0] == "vigenere":
                if len(action) == 1:
                    temp_text = vigenere(file[t], guess_vigenere(file[t], v_guess_length(file[t])))
                    print(temp_text)
                elif action[1].isalpha():
                    temp_text = vigenere(file[t], action[1])
                    print(temp_text)
                else:
                    temp_text = guess_vigenere(file[t], int(action[1]))
                    print(temp_text)

            elif action[0] == "fb":
                typ_bigram_freq()
                print()
                check_freqs(file[t], True)

            elif action[0] == "t":
                tris = sort_tri(common_tri(file[t]))
                for i in range(len(tris)):
                    print(tris[i][0], end =" ")
                    print(tris[i][1])

            elif action[0] == "td":
                if len(action) == 1:
                    print(tri_freq_distance(file[t], sort_tri(common_tri(file[t]))[0][0]))
                else:
                    print(tri_freq_distance(file[t], action[1].upper()))

            elif action[0] == "l" or action[0] == "length":
                print(factors(file[t]))

            elif action[0] == "b" or action[0] == "backwards":
                temp_text = file[t][::-1]
                print(temp_text)

            elif action[0] == "g" or action[0] == "grid":
                if action[1] == "c":
                    print_grid(make_grid(file[t], int(action[2]), True))
                elif action[1] == "r":
                    print_grid(make_grid(file[t], int(action[2]), False))

            elif action[0] == "ct":
                if action[2].isnumeric():
                    if action[1] == "c":
                        temp_text = plain_from_grid(transpose_grid(make_grid(file[t], len(action[2]), True), list(map(int, action[2]))))
                        print(temp_text)
                    elif action[1] == "r":
                        temp_text = plain_from_grid(transpose_grid(make_grid(file[t], len(action[2]), False), list(map(int, action[2]))))
                        print(temp_text)
        except (ValueError):
            print("Value error")
#        except (IndexError):
#            print("Index error")

if __name__ == "__main__":
    main()
