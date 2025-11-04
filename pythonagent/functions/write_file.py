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
    
    # Create the directory if it doesn't exist
    target_dir = os.path.dirname(target_path)
    if target_dir and not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    
    # Write the file content
    try:
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to "{file_path}": {e}'
