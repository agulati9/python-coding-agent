import os

def get_file_content(working_directory, file_path):
    """
    Function that can get the content of a file. It reads the content of the file and returns it as a string.

    Args:
        working_directory: The base working directory (security boundary)
        file_path: The path to the file to read (can be relative to working_directory)

    Returns:
        The content of the file as a string, or an error message if something goes wrong
    """

    # Resolve absolute paths for security boundary and target file
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Restrict access to files within the working directory only
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Validate that the resolved target path is a file
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" is not a file'
    
    # Read up to MAX_CHARS to avoid overly large outputs
    MAX_CHARS = 10000
    try:
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        # Indicate truncation if file is larger than MAX_CHARS
        try:
            is_truncated = os.path.getsize(target_path) > MAX_CHARS
        except Exception:
            is_truncated = False
        if is_truncated:
            return file_content_string + f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters.]"
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
