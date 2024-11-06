# Sample Symbol Table (ST), Literal Table (LT), and Machine Operation Table (MOT)
ST = {
    "LOOP": [1, 100],
    "END": [2, 200]
}
LT = {
    "=5": [1, 500],
    "=1": [2, 1000]
}
MOT = {
    "ADD": "01",
    "SUB": "02",
    "MUL": "03",
    "DIV": "04",
    "LOAD": "05",
    "STORE": "06"
}

# Convert line to list
def convert_to_list(line):
    line = line.strip().replace('     ', '-').replace('   ', '-').split('-')
    if line[0][:2] == 'lc':
        line.pop(0)
    return line

# Convert list to machine code
def convert_to_machine(line):
    result = [line[0][5:7]] if line[0][1:3] in ['IS', 'DL'] else []
    if len(line) > 1 and line[1][0] == '(' and line[1][2] == ')':
        result.append('0' + line[1][1])
    if len(line) > 2:
        table = LT if line[-1][1] == 'L' else ST
        result.append(str([v[1] for k, v in table.items() if str(v[0]) == line[-1][4]][0]))
    return ' '.join(result + ['00', '000'][len(result):])

# Main execution
if __name__ == '__main__':
    with open('Outputs/IR.txt', 'r') as file:
        lines = file.readlines()

    code = [convert_to_machine(convert_to_list(line)) for line in lines if line[0][1:3] not in ['AD', 'DS']]

    with open('Outputs/target.txt', 'w') as file:
        file.write('\n'.join(code) + '\n')
