import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Restrict access to files within the working directory only
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot run "{file_path}" as it is outside the permitted working directory'
    
    # Validate that the resolved target path is a file
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" is not a file'
    
    # Validate that the resolved target path is a Python file
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        # Run the Python file with the given arguments (30s timeout)
        completed_process = subprocess.run(
            ["python", target_path, *args], 
            cwd=working_directory,
            timeout=30
        )
        return f'Successfully ran "{file_path}" with arguments {args}'
    except subprocess.TimeoutExpired:
        return f'Error: "{file_path}" execution timed out after 30 seconds'
    except Exception as e:
        return f'Error running "{file_path}": {e}'