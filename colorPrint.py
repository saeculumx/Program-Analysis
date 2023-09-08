from colorama import Fore, Style


def colorPrint(content, color=Fore.WHITE):
    print(color + str(content))
    print(Style.RESET_ALL)
