def get_files_info(working_directory, directory="."):
    '''
    The directory parameter should be treated as a relative path within the working_directory. Use os.path.join(working_directory, directory) to create the full path, then validate it stays within the working directory boundaries.

    If the full path is not within the working directory, raise a ValueError with a descriptive message.

    '''
   