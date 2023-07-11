def staff_check_keyboard_correct(words):
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
        if their_answers[i] != correct_answers[i]:
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
    check_answers(fn, staff_check_keyboard_correct, questions)



def staff_unique_morse_codes_correct(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    s = set()
    
    for word in words:
        so_far = []
        for char in word:
            idx = ord(char) - ord('a')
            so_far.append(morse[idx])
        s.add(''.join(so_far))
    return len(s)


def check_morse_code(fn):
    questions = [
        ["gin","zen","gig","msg"],
        ["gin","zen","gig","msg", "dad", "mad", "pot", "bed", "car"],
        ["a"],
        []
    ]
    check_answers(fn, staff_unique_morse_codes_correct, questions)
    

def staff_print_vertically(s):
    words = s.split()
    max_length = max((len(i) for i in words))
    
    answer = [[] for _ in range(max_length)]
    
    for w in words:
        for i in range(len(w)):
            answer[i].append(w[i])
        
        
        for i in range(len(w), max_length):
            answer[i].append(' ')
    
    return [''.join(w).rstrip() for w in answer]
                
def check_print_vertical(fn):
    questions = [
        "HOW ARE YOU",
        "TO BE OR NOT TO BE",
        "CONTEST IS COMING"
    ]
    check_answers(fn, staff_print_vertically, questions)