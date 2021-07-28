import re

# Calculates the reading percentage
getReadPercentage = lambda pagesRead, totalPages: (pagesRead * 100) / totalPages

# Validates the data type of the number of pages entered
def isInt(quantityPages):
    while True:
        try:
            int(quantityPages)
            return True
        except ValueError or TypeError:
            return False

# Method to validate user option
def validateOption(option):
    while True:
        try:
            op = int(option)
            if op < 1 or op > 3:
                return False
            return True
        except ValueError or TypeError:
            return False

# Method to validate date
def validateDate(date):
    all = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", date)
    if len(all) == 0:
        return False
    return True
