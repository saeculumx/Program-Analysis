from colorama import Fore

from colorPrint import colorPrint


class build:
    def __init__(self, package="", importation="", variable="", function=""):
        self._package = package
        self._importation = importation
        self._variable = variable
        self._function = function

    def output(self):
        colorPrint(
            self._package + " / " + str(self._importation) + " / " + self._variable + " / " + str(self._function),
            Fore.RED)
