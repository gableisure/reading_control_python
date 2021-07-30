import globals

MODE = ''

# Read the file
def read():
    MODE = 'r'
    with open(globals.FILE_NAME, MODE, encoding='utf8') as db:
        print(db.read())

# Write in file
def write(str):
    MODE = 'a'
    with open(globals.FILE_NAME, MODE, encoding='utf8') as db:
        db.write(str)

# Count the number of records
def countLines():
    MODE = 'r'
    count = 0
    with open(globals.FILE_NAME, MODE, encoding='utf8') as db:
        lines = db.readlines()
        for line in lines:
            if not line.startswith('\n') and not line.startswith('D'):
                count += 1
        return count

# Suming the number of pages read
def sumPages():
    MODE = 'r'
    sum = 0
    with open(globals.FILE_NAME, MODE, encoding='utf8') as db:
        lines = db.readlines()
        for line in lines:
            if not line.startswith('\n') and not line.startswith('D'):
                if line[12] != '\n':
                    sum += int(line[11] + line[12])
                else:
                    sum += int(line[11])
        return sum

# Returns arithmetic average of pages read
def avgPages():
    MODE = 'r'
    avg = 0
    with open(globals.FILE_NAME, MODE, encoding='utf8') as db:
        lines = db.readlines()
        return sumPages() / countLines()