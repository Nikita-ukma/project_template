import pandas as pd

def read_from_console():
    """
    Function for reading text from the console.
    
    Returns:
        str: Text input from console
    """
    text = input("Enter your text: ")
    return text


def read_from_file(file_path):
    """
    Function for reading text from a file using Python's built-in
    capabilities.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: File contents
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"


def read_from_file_pandas(file_path):
    """
    Function for reading data from a file using the pandas library.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: String representation of the DataFrame
    """
    try:
        # Attempt to read the file - choosing method based on extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            # Default to csv
            df = pd.read_csv(file_path)
        
        return df.to_string()
    except Exception as e:
        return f"Error reading file with pandas: {str(e)}"