# Calculates the reading percentage
getReadPercentage = lambda pagesRead, totalPages: (pagesRead * 100) / totalPages

# Validate the date for the format dd/mm/yyyy
def validateDate(date):
    print(date.split('/'))
    if date[2] != '/' or date[5] != '/':
        return False
    dateUnits = date.split('/')
    for date in dateUnits:
        if int(date) != int:
            print("errado!")
    print(len(dateUnits))
    # if
    #     date.split('/')
    #     # print(date.split('/'))