import sys
def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# def main(input_file="input.txt", output_file="output.txt"):
#     """Main function to process a text file."""
#     text = read_file(input_file)
#     if text:
#         results = process_text(text)
#         if results:
#             success = write_results(results, output_file)
#             if success:
#                 print(f"Processing complete. Results written to {output_file}")
#                 return True
    
#     print("Processing failed.")
#     return False

def main(input_file="input.txt", output_file="output.txt"):
    print("Welcome to the Python Text Processor!")
    print(f"Current input file: {input_file}")

    # Check if the script is being run in an interactive environment
    if sys.stdin.isatty():  # Only true if running in terminal
        choice = input("Do you want to edit the input file content? (y/n): ").strip().lower()
        if choice == 'y':
            new_content = []
            print("Enter the new content line by line (type 'DONE' to finish):")
            while True:
                line = input()
                if line.strip().upper() == 'DONE':
                    break
                new_content.append(line)
            try:
                with open(input_file, 'w') as f:
                    f.write('\n'.join(new_content))
                print("Input file updated successfully.")
            except Exception as e:
                print(f"Error updating file: {e}")
                return False
    else:
        print("Non-interactive mode detected. Skipping input prompts...")

    # Continue processing
    text = read_file(input_file)
    if text:
        results = process_text(text)
        if results:
            success = write_results(results, output_file)
            if success:
                print(f"Processing complete. Results written to {output_file}")
                return True
    print("Processing failed.")
    return False

if __name__ == "__main__":
    main()
