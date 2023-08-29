# This is a sample Python script.
import glob

import load

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
root = r"course-02242-examples/src/dependencies/java/dtu/deps"
paths = []
if __name__ == '__main__':
    i = 0
    for p in glob.glob(r"course-02242-examples/src/dependencies/java/dtu/deps/**/*.java", recursive=True):
        paths.append(p)
    for path in paths:
        full = []
        word = load.load(path)
        for w in word:
            # print("\n" + w)
            full.append(w)
        print(full)
        with open(str(i) + ".txt", "w") as f:
            f.write(str(full))
        i = i + 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
