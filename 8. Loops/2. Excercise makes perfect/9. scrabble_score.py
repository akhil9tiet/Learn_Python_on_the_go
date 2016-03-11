"""Create a scrabble where all  the alphabets have a score. We display the sum of score."

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    word.lower()
    print word
    acore = 0
    
    for m in word :
        print m, "<---lopp"
        if m not in score:
            m = m.lower()
            print m, "<---in if"
        acore = acore + score[m]
    return acore
        
print scrabble_score("DuNe")