import os


def get_files_info(working_directory, directory="."):
    """
    
     function that can get the contents of a directory. It lists all files and directories in the specified directory with their sizes.
    
    Args:
        working_directory: The base working directory (security boundary)
        directory: The relative directory path to list (default: current directory ".")
    
    Returns:
        A formatted string with file information, or an error message if something goes wrong
    """
    # Convert working directory to absolute path for comparison
    abs_working_dir = os.path.abspath(working_directory)
    
    # Join the working directory with the target directory and convert to absolute path
    # This handles relative paths like ".." or "subfolder" correctly
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    
    # Restriction to prevent LLM from accessing files outside the working directory
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Validate that the target path is actually a directory, not a file
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        # List to store information about each file/directory found
        files_info = []
        
        # Loop through each item (file or directory) in the target directory
        for filename in os.listdir(target_dir):
            # Build the full path to the current item
            filepath = os.path.join(target_dir, filename)
            
            # Initialize file_size (will be updated if it's a file)
            file_size = 0
            
            # Check if the current item is a directory (True) or a file (False)
            is_dir = os.path.isdir(filepath)
            
            # Get the size of the file in bytes
            # Note: This might fail for directories, which is caught by the exception handler
            file_size = os.path.getsize(filepath)
            
            # Add formatted information about this file/directory to our list
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        
        # Join all file info strings with newlines to create the final output
        return "\n".join(files_info)
    except Exception as e:
        # Catch any errors (e.g., permission issues, directory size calculation errors)
        return f"Error listing files: {e}"
