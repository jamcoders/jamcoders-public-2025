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