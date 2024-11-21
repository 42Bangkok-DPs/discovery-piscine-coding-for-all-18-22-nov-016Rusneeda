from checkmate import checkmate
import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error : file '{file_path}' not found.\n"
    except Exception as e:
        return f"Error : unable to read file '{file_path}' . reason: {e}\n"

def main():
    
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <file1> <file2> ...')
        sys.exit(1)

    for file_path in sys.argv[1:]:
        board = read_file(file_path)
        checkmate(board)


if __name__ == "__main__":
    main()