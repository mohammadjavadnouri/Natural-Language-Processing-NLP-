input_word = input("Please write your sentence in the known BAAH BAAAH language:")
listed_input_word = list(input_word)

if listed_input_word[0] == 'B':
    for i in range(len(listed_input_word)):
        del listed_input_word[0]
        if listed_input_word[0] == 'A' :   
            print(listed_input_word)
        elif listed_input_word[0] == 'H':
            print(listed_input_word)
            if len(listed_input_word) != 1:
                print("You said something after H and this is out of law of this language.")
                break
            else:
                print("Correct language cause it began with B and finished with H and A in between.")
                break
        
else:
    print("This is not the correct language cause it either has not began with B or finished with H or A in between.")
