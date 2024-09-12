import ast

def check_syntax(file_path):
    try:
        # Read the script from the file
        with open(file_path, 'r') as file:
            script = file.read()

        # Parse the script to check for syntax errors
        ast.parse(script, file_path)
        print("Accepted: The script has no syntax errors.")

        # If no syntax errors, execute the script
        print("Executing the script now...\n")
        exec(script)
    
    except SyntaxError as e:
        # Extract and print error details
        print(f"Rejected: Syntax error detected.")
        print(f"File: {e.filename}")
        print(f"Line: {e.lineno}")
        print(f"Error: {e.msg}")
        # Optionally, show the problematic line
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Code: {lines[e.lineno - 1].strip()}")
    
    except Exception as e:
        # Catch other exceptions (e.g., runtime errors during parsing or execution)
        print(f"Rejected: An error occurred during execution.")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Example usage:
    file_path = 'example.py'
    check_syntax(file_path)
