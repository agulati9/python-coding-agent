from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

    # Test get_file_content function
    working_dir = "calculator"
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "/bin/cat"))
    print(get_file_content(working_dir, "pkg/does_not_exist.py"))

main()