MOT = {'STOP': '00', 'ADD': '01', 'SUB': '02', 'MULT': '03', 'MOVER': '04',
       'MOVEM': '05', 'COMP': '06', 'BC': '07', 'DIV': '08', 'READ': '09',
       'PRINT': '10', 'START': '01', 'END': '02', 'ORIGIN': '03', 'LTORG': '05',
       'DS': '01', 'DC': '02', 'AREG,': '01', 'BREG,': '02', 'EQ': '01'}

ST = []
LT = []
code = []
# Function to classify words based on their type
def classy(word):
    if word in MOT:  # Check if the word is in the Machine Operation Table (MOT)
        # Check for different types of assembler directives and instructions
        if word in ['START', 'END', 'ORIGIN', 'LTORG']:
            return 'AD'  # Assembler Directive
        elif word in ['DS', 'DC']:
            return 'DL'  # Declarative Statement
        elif word in ['AREG,', 'BREG,']:
            return 'RG'  # Register
        else:
            return 'IS'  # Imperative Statement
    return 'None'  # Return 'None' if the word is not recognized

# Function to read a file and return its lines
def read_file(file_path):
    try:
        with open(file_path, 'r') as source:  # Open the file in read mode
            return source.readlines()  # Read all lines from the file and return as a list
    except FileNotFoundError:  # Handle the case where the file is not found
        print('File Not found. Create a source.txt first.')
        return None  # Return None if the file is not found

def pass1():
    ST_index, LT_index, address = 0, 0, 0  # Initialize indices and address counter
    if lines[0].strip().upper().split()[0] == 'START':
        address = int(lines[0].strip().split()[1])  # Set starting address if START directive is found
        lines = lines[1:]  # Skip the START line for further processing
    
    for line in lines:  # Iterate over each line in the source code
        words = line.strip().split()  # Split the line into words
        for word in words:  # Process each word in the line
            word = word.upper()  # Convert word to uppercase
            if word.startswith('='):  # Check if the word is a literal
                LT.append((LT_index, word, address))  # Add literal to literal table with current address
                LT_index += 1  # Increment literal table index
            elif classy(word) == 'None':  # Check if the word is a label (not in MOT)
                if not any(sym[1] == word for sym in ST):  # Avoid duplicate symbols in symbol table
                    ST.append((ST_index, word, address))  # Add symbol to symbol table with current address
                    ST_index += 1  # Increment symbol table index
        address += 1  # Increment address counter for the next line
    
    print('Literal Table:', LT)  # Print the literal table for verification
    print('Symbol Table:', ST)  # Print the symbol table for verification
    

def intermediate(lines):
    for line in lines:  # Iterate over each line in the source code
        entry = []  # Initialize an empty entry for the intermediate code
        words = line.strip().split()  # Split the line into words
        for word in words:  # Process each word in the line
            word = word.upper()  # Convert word to uppercase
            if classy(word) != 'None':  # If the word is recognized (directive/instruction)
                entry.append((classy(word), MOT[word]))  # Add the word's classification and machine code to the entry
            elif word.startswith('='):  # If the word is a literal
                index = next((i for i, lt in enumerate(LT) if lt[1] == word), -1)  # Find the index of the literal in the literal table
                entry.append(('L', index))  # Add the literal with its index to the entry
            else:  # If the word is a label (symbol)
                index = next((i for i, st in enumerate(ST) if st[1] == word), -1)  # Find the index of the symbol in the symbol table
                entry.append(('S', index))  # Add the symbol with its index to the entry
        code.append(entry)  # Append the entry to the intermediate code list
    
    print("\nIntermediate Code:")  # Print the generated intermediate code
    for entry in code:  # Iterate over the intermediate code entries
        print(entry)  # Print each entry


file_path = 'source.txt'
lines = read_file(file_path)
if lines:
    pass1(lines)
    intermediate(lines)