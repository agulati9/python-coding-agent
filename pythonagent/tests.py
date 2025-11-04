from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    # #Test get_files_info function
    # working_dir = "calculator"
    # root_contents = get_files_info(working_dir, ".")
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "../")
    # print(pkg_contents)

    # # Test get_file_content function
    # working_dir = "calculator"
    # file_content = get_file_content(working_dir, "lorem_ipsum.txt")
    # print(file_content)

    # # Test get_file_content function
    # working_dir = "calculator"
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "/bin/cat"))
    # print(get_file_content(working_dir, "pkg/does_not_exist.py"))

    # Test write_file function
    working_dir = "calculator"
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

main()