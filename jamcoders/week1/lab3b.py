# For answer checking without revealing the answer
def check_answers_with_num(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def create_check_answer(correct, num):
    def check_fn(ans):
        check_answers_with_num(ans, correct, num)
    return check_fn

check_answer_0_1 = create_check_answer('Hello JamCoders', '0.1')
check_answer_0_4 = create_check_answer('JamCoders', '0.4')

from colorama import Fore, Back, Style

ansi_color_characters = {
    "black": Fore.BLACK,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "green": Fore.GREEN,
    "grey": Fore.LIGHTBLACK_EX,
    "light_blue": Fore.LIGHTBLUE_EX,
    "light_cyan": Fore.LIGHTCYAN_EX,
    "light_green": Fore.LIGHTGREEN_EX,
    "light_magenta": Fore.LIGHTMAGENTA_EX,
    "light_red": Fore.LIGHTRED_EX,
    "light_white": Fore.LIGHTWHITE_EX,
    "light_yellow": Fore.LIGHTYELLOW_EX,
    "magenta": Fore.MAGENTA,
    "red": Fore.RED,
    "white": Fore.WHITE,
    "yellow": Fore.YELLOW,
}

def colored(string, color):
  assert color in ansi_color_characters, f"We don't have a color named '{color}'. Please use one of the following colot names: {list(ansi_color_characters.keys())}"
  ansi_char = ansi_color_characters[color]
  return ansi_char + string + Fore.RESET
