import colorama
from colorama import Fore, Back

def cm():
    colorama.init()

    return (Back.GREEN + Fore.YELLOW + 'Желтый текст на зеленом фоне')


