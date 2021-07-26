"""
TODO: implementar método para validar a entrada de dados (date, pages) - Implementando
"""

import db
import methods as mtd

# Constants
TOTAL_PAGES = 237

# Method main
def main():
    receiveOption()

# Process the menu option
def processOption(option):
    if(option == 1):
        dashboard()
        db.read()
    elif(option == 2):
        receiveRecord()
        print("\nSaved reading!")
    else:
        print("\nFinished program...")
        exit()
    receiveOption()

# Display the dashboard
def dashboard():
    print("\nDashboard ******************************************************")
    print('\nRecords: ', db.countLines())
    print('Total pages: ', TOTAL_PAGES)
    print('Pages read: ', db.sumPages())
    print(f'Reading percentage: {round(mtd.getReadPercentage(db.sumPages(), TOTAL_PAGES), 2)} %')
    print('Reading average: ', round(db.avgPages(), 2))
    print("\n****************************************************************\n")

# Method to receive an option
def receiveOption():
    print("\n********************* Book Reading Control *********************")
    print("\n1 - Dashboard\n"
          "2 - Record reading\n"
          "3 - Exit\n")
    option = int(input("Enter an option: "))
    validateOption(option)

# Method to validate user option
def validateOption(option):
    while option < 1 or option > 3:
        print("Invalid option!\n")
        option = int(input("Enter an option: "))
    processOption(option)

# Method to receive a record
def receiveRecord():
    date = input("\nDate: ")
    mtd.validateDate(date)
    pages = input("Pages: ")
    readRecord = date + '\t' + pages + "\n"
    db.write(readRecord)

main()

