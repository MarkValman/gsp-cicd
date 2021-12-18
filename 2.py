# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def split(word):
    return [char for char in word]

def choose_one_letter_to_delete(S):
    unique_letters = set(split(S))
    letter_counter = {}
    for letter in unique_letters:
        letter_counter[letter] = S.count(letter)
    flipped = {}
    for key, value in letter_counter.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    letter_to_delete = ''
    for key, values in flipped.items():
        if len(values) > 1:
            letter_to_delete = values[0]
    return letter_to_delete
    


def solution(S):
    there_are_letters_to_delete = True
    counter = 0
    while (there_are_letters_to_delete):
        print(S)
        letter_to_delete = choose_one_letter_to_delete(S)
        if(letter_to_delete != ''):
            S = S.replace(letter_to_delete,"",1)
            counter += 1
        else:
           there_are_letters_to_delete = False
    return counter
    
    
# print(solution("ccaaffddecee"))
# choose_one_letter_to_delete("helloworld")