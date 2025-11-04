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
    # Convert working_directory to absolute path to use as security boundary
    abs_working_dir = os.path.abspath(working_directory)
    # Join working_directory with file_path and convert to absolute path
    # This handles both relative paths (e.g., "file.txt") and nested paths (e.g., "pkg/file.txt")
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security check: Restrict access to files within the working directory only
    # Ensure the target file path is within the working directory to prevent directory traversal attacks
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Create parent directory if it doesn't exist
    # Extract the parent directory from the file path (e.g., "pkg" from "pkg/file.txt")
    target_dir = os.path.dirname(target_path)
    # Only create directory if:
    # 1. target_dir is not empty (file is in a subdirectory, not root)
    # 2. The directory doesn't already exist
    if target_dir and not os.path.exists(target_dir):
        # Create all necessary parent directories (e.g., "a/b/c" if needed)
        # exist_ok=True prevents errors if directory was created by another process
        os.makedirs(target_dir, exist_ok=True)
    
    # Write the file content
    # Open file in write mode ("w") which will create the file if it doesn't exist,
    # or overwrite it if it does exist
    try:
        with open(target_path, "w") as f:
            f.write(content)
        # Return success message with character count
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        # Return error message if file writing fails (e.g., permission denied, disk full)
        return f'Error writing to "{file_path}": {e}'
