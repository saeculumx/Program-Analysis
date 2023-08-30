import re
import os
from typing import List


def modify_path(path, num_elements_to_remove, file_extension):
    # Split the path into parts
    parts = path.split(os.path.sep)

    # Remove the specified number of elements from the beginning
    remaining_parts = parts[num_elements_to_remove:]

    # Remove file extension and join parts with dots
    modified_path = ".".join(remaining_parts).replace(file_extension, "").replace(os.path.sep, ".")

    return modified_path
# the class represent a java file
class JavaFile:
    def __init__(self) -> None:
        self.id = ""  # the identification of the java file, e,g. dtu.deps.tricky.Example
        self.file_name = ""  # the name of the java file, e.g. Example
        self.own_class_list = []  # the classes owned by the file, e.g. ["Tricky"]
        self.total_str = ""  # the string containing all the text in the file
        self.package_name = "" # the name of the package the file belonging to

    def load_file(self, file_path: str) -> None:
        """
        load text of the java file into 'total_str'
        """
        tmp_file = open(file_path, "r")

        # read all the lines in the file
        str_list = tmp_file.readlines()
        for line in str_list:
            self.total_str += line  # add each line to 'total_str'
        self.file_name = modify_path(file_path,4,".java")
        # print(self.file_name)
        tmp_file.close()
        return self.file_name
    
    def remove_regex(self, reg_pattern: str) -> None:
        """
        remove the strings matching the reg_pattern in 'total_str'
        """
        # replace the matched strings with empty string, i.e. remove all the comments
        self.total_str = re.sub(reg_pattern, "", self.total_str)

    def remove_comment(self) -> None:
        """
        remove the comments in the 'total_str'
        """
        regex_pattern = "\/\/.*|\/\*(.|\n)*?\*\/" # the regular expression for comment
        
        # replace the comments with empty string, i.e. remove all the comments
        self.remove_regex(regex_pattern)

    def remove_string(self) -> None:
        """
        remove the strings in the 'total_str'
        """
        regex_pattern = "\"\"\"\n(.|\n)*?\"\"\"" # the regular expression for string blockhh
        self.remove_regex(regex_pattern) # remove string block
        
        regex_pattern = "\".*?\"" # the regular expression for one-line string
        self.remove_regex(regex_pattern) # remove one-line string
    
    def get_package_name(self) -> None:
        """
        get the package_name from the 'total_str'
        """
        regex_pattern = "package\s+[\w.]+" # the regular expression for package
        match_result: re.Match = re.search(regex_pattern, self.total_str) # search the package name

        if match_result == None:
            raise Exception(f"Can't find package name in {self.file_name}")
        
        # get the name of the package
        match_string: str = match_result.group()
        self.package_name = match_string.split(" ")[-1]
        # print(self.package_name)

    def get_id_and_package(self) -> None:
        """
        get the package_name and id of the java file
        """
        self.get_package_name()
        # get the file name from self.file_name
        dot_location = self.file_name.rfind(".")
        file_name = self.file_name[dot_location + 1:]
        self.id = self.package_name + "." + file_name
        # print(self.id)
    
    def get_own_class_list(self) -> None:
        """
        get the owned class list of the java file
        """
        regex_pattern = "public\s+class\s+[\w.]+" # the regular expression for public class
        match_results: List[re.Match] = re.findall(regex_pattern, self.total_str)
        
        # get the name of the class
        for result in match_results:
            self.own_class_list.append(result.split(" ")[-1])
        print(self.own_class_list)


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
        filename = tmp_java_file.load_file(file_path)
        tmp_java_file.remove_comment()
        tmp_java_file.remove_string()
        # tmp_java_file.get_package_name()
        tmp_java_file.get_id_and_package()
        tmp_java_file.get_own_class_list()

        # print(root_directory_path, file_path)
        # print(tmp_java_file.total_str) # print the text in the file
        with open(filename + ".txt", "w") as f:
            f.write(tmp_java_file.total_str)

