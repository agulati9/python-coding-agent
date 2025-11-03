import os

def write_file(working_directory, file_path, content):
    """
    Function that can write to and overwrite a file. It writes the content to the file and returns a success message.

    Args:
        working_directory: The base working directory (security boundary)
        file_path: The path to the file to write to (can be relative to working_directory)
        content: The content to write to the file
    """

    # Resolve absolute paths for security boundary and target file
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Restrict access to files within the working directory only
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Validate that the resolved target path is a file
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" is not a file'