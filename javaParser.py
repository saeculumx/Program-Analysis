import glob
import re
from tree_sitter import Language, Parser
from colorama import init as colorama_init
from colorama import Fore, Back, Style

from classBuilder import build
from colorPrint import colorPrint

paths = []
childList = []
filename = 0
b = build()


def auto():
    colorama_init()
    search()
    for p in paths:
        initiate(p)


def initiate(filepath):
    FILE = "./languages.so"  # the ./ is important
    Language.build_library(FILE, ["tree-sitter-java"])
    parser = Parser()
    parser.set_language(Language(FILE, "java"))
    with open(filepath, "rb") as f:
        tree = parser.parse(f.read())
    baseNode = tree.root_node

    file_name = re.search(r'[^/]+\.java$', filepath).group(0)
    file_name = re.sub(r'\.java$', '', file_name)

    i = 0
    imps = []
    funs = []
    colorPrint("--- " + file_name + " Base Node Structure---", Fore.BLUE)
    while i < baseNode.child_count:
        child = baseNode.children[i]
        childList.append(child)
        print(str(i) + " | " + child.type)
        i += 1

    for subChild in childList:
        match subChild.type:
            case "package_declaration":
                package = subChild.text.decode('utf-8')
                b._package = package
            case "import_declaration":
                i = 0
                while i < subChild.child_count:
                    c = subChild.children[i]
                    if c.type == "scoped_identifier":
                        importation = c.text.decode('utf-8')
                        imps.append(importation)
                        # colorPrint(importation, Fore.RED)
                    i += 1
                b._importation = imps
            case "class_declaration":
                i = 0
                while i < subChild.child_count:
                    c = subChild.children[i]
                    if c.type == "identifier" or c.type == "super_interfaces":
                        function = c.text.decode('utf-8')
                        funs.append(function)
                        # colorPrint(importation, Fore.RED)
                    i += 1
                b._function = funs
            case "line_comment":
                i = 0
            case "block_comment":
                i = 0
                # print("block_comment")
    b.output()


def search():
    for p in glob.glob(r"course-02242-examples/src/dependencies/java/dtu/deps/**/*.java", recursive=True):
        paths.append(p)
    colorPrint(__name__ + " >>>" + " Path Generated using glob, Total path: " + str(len(paths)), Fore.GREEN)
    colorPrint(__name__ + " >>> " + "Parser Initiated", Fore.GREEN)
    return paths
