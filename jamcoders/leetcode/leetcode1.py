def check_keyboard_correct(words):
    def check_word(r, w):
        for char in w:
            if char not in r: 
                return False
        return True
        
    rows = [
        "qwertyuiop", "asdfghjkl", "zxcvbnm"
    ]
    
    ans = []
    
    for word in words:
        for row in rows:
            if check_word(row, word.lower()):
                ans.append(word)
                break
    return ans

def check_answers(their_fn, my_fn, questions):
    
    their_answers = [their_fn(i) for i in questions]
    correct_answers = [my_fn(i) for i in questions]

    for i in range(len(questions)):
        if their_answers[i] != correct_answers:
            print("Wrong answer!")
            print("The input:", questions[i])
            print("Your answer:", their_answers[i])
            print("Correct Answer:", correct_answers[i])
            return
    
    print("All test cases passed! Good job!")

def check_keyboard(fn):
    questions = [
        ["Hello","Alaska","Dad","Peace"],
        ["omk"],
        ["adsdf","sfd"]
    ]
    check_answers(fn, check_keyboard_correct, questions)


