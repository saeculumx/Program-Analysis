def load(filename):
    wordlist = []
    for line in open(filename):
        li = line.strip()
        if not li.startswith("//") | li.startswith("/*"):
            a = line.rstrip()
            wordlist.append(a)
    return wordlist
