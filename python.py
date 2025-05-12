import re

def read_and_write_file():
    try:
        filename = input("Enter the filename to read from: ")

        # Try reading the file with proper encoding
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()

        print("\nChoose how to modify the content:")
        print("1. Reverse lines")
        print("2. Remove extra whitespace")
        print("3. Capitalize sentences")
        print("4. Number each line")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            modified_content = ''.join(reversed(content))

        elif choice == '2':
            modified_content = ''.join(line.strip() + '\n' for line in content if line.strip())

        elif choice == '3':
            full_text = ''.join(content)
            sentences = re.split(r'(?<=[.!?]) +', full_text)
            modified_content = ' '.join(sentence.capitalize() for sentence in sentences)

        elif choice == '4':
            modified_content = ''.join(f"{i+1}: {line}" for i, line in enumerate(content))

        else:
            print("❌ Invalid choice.")
            return

        new_filename = f"modified_{filename}"
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)

        print(f"\n✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: Permission denied. You do not have the required access rights.")
    except IsADirectoryError:
        print("❌ Error: Expected a file but got a directory.")
    except UnicodeDecodeError:
        print("❌ Error: Cannot decode the file. It may not be a plain text file.")
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user.")
    except IOError:
        print("❌ Error: File could not be read or written.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the program
read_and_write_file()
