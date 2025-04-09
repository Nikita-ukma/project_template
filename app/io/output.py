def write_to_console(text):
    """
    Function for outputting text to the console.
    
    Args:
        text (str): Text to be displayed in the console
    """
    print(text)


def write_to_file(file_path, text):
    """
    Function for writing text to a file using Python's built-in
    capabilities.
    
    Args:
        file_path (str): Path to the file
        text (str): Text content to write to the file
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

