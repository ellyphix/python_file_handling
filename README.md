**File Reader & Modifier – Python Project**

This Python script reads a text file and writes a modified version of it to a new file. It includes a menu with different ways to modify the content, and features robust error handling for a smooth user experience.

## 🔧 Features

- ✅ User input for filename
- ✅ Multiple content modification options:
  - Reverse lines
  - Remove extra whitespace
  - Capitalize sentences
  - Number each line
- ✅ Error handling for:
  - File not found
  - Permission denied
  - Directory instead of file
  - File decode issues (non-text)
  - Keyboard interrupt (Ctrl+C)

## 🧪 How to Use

1. Run the script using Python 3:
   ```bash
   python file_modifier.py
2. Enter the name of the file you want to read (must be in the same directory or provide full path).
3. Choose a modification option when prompted.
4. The modified content will be saved as modified_<filename>.
