# Import functions from input.py and output.py
from app.io.input import read_from_console, read_from_file, read_from_file_pandas
from app.io.output import write_to_console, write_to_file

def main():
    """
    Main function that calls the imported input and output functions.
    """
    # Output file path
    output_file = "output_results.txt"

    # 1. Read from console
    console_text = read_from_console()
    write_to_console("\nText from console:")
    write_to_console(console_text)
    
    # 2. Read from file using built-in Python
    file_text = read_from_file("sample_file.txt")
    write_to_console("\nText from file (built-in Python):")
    write_to_console(file_text)
    
    # 3. Read from file using pandas
    pandas_text = read_from_file_pandas("sample_data.csv")
    write_to_console("\nData from file (pandas):")
    write_to_console(pandas_text)
    
    # Write all results to file
    all_results = f"""
RESULTS:

1. Text from console:
{console_text}

2. Text from file (built-in Python):
{file_text}

3. Data from file (pandas):
{pandas_text}
"""
    
    write_to_file(output_file, all_results)
    write_to_console(f"\nAll results have been saved to '{output_file}'")


if __name__ == "__main__":
    main()