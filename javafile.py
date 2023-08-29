import re

# the class represent a java file
class JavaFile:
    def __init__(self) -> None:
        self.id = ""  # the idenfication of the java file, e,g. dtu.deps.tricky.Example
        self.file_name = ""  # the name of the java file, e.g. Example
        self.own_class_list = []  # the classes owned by the file, e.g. ["Tricky"]
        self.total_str = ""  # the string containing all the text in the file

    def load_file(self, file_path: str) -> None:
        """
        load text of the java file into 'total_str'
        """
        tmp_file = open(file_path, "r")

        # read all the lines in the file
        str_list = tmp_file.readlines()
        for line in str_list:
            self.total_str += line  # add each line to 'total_str'

        tmp_file.close()
    
    def remove_comment(self) -> None:
        """
        remove the comment in the 'total_str'
        """
        regex_pattern = "\/\/.*|\/\*(.|\n)*?\*\/" # the regular expression for comment
        
        # replace the comments with empty string, i.e. remove all the comments
        self.total_str = re.sub(regex_pattern, "", self.total_str)


# test code
if __name__ == "__main__":
    import glob

    root_directory_path = "course-02242-examples"
    file_paths = []
    # find all the files ending with '.java'
    for file_path in glob.glob("./" + root_directory_path + "/**/*.java", recursive=True):
        file_paths.append(file_path)
    
    for file_path in file_paths:
        tmp_java_file = JavaFile()
        tmp_java_file.load_file(file_path)

        tmp_java_file.remove_comment()

        print(tmp_java_file.total_str) # print the text in the file

