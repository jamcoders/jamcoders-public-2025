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

def staff_integer_to_words(num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n//10-2]] + words(n%10)
        if n < 1000:
            return [to19[n//100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n//1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'

def check_integer_to_words(fn):
    questions = [
        123,
        12345,
        1234567
    ]
    check_answers(fn, staff_integer_to_words, questions)