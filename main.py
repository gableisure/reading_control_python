import db
import methods as mtd
import globals

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
    print('Total pages: ', globals.TOTAL_PAGES)
    print('Pages read: ', db.sumPages())
    print(f'Reading percentage: {round(mtd.getReadPercentage(db.sumPages(), globals.TOTAL_PAGES), 2)} %')
    print('Reading average: ', round(db.avgPages(), 2))
    print("\n****************************************************************\n")

# Method to receive an option
def receiveOption():
    print("\n********************* Book Reading Control *********************")
    print("\n1 - Dashboard\n"
          "2 - Record reading\n"
          "3 - Exit\n")
    option = input("Enter an option: ")
    validatedOption = mtd.validateOption(option)
    if validatedOption:
        option = int(option)
        processOption(option)
    else:
        print("\nInvalid option!")
        receiveOption()

# Method to receive a record
def receiveRecord():
    date = input("\nDate (dd/mm/yyyy): ")
    isValidate = mtd.validateDate(date)
    while isValidate != True:
        print("\nInvalid date. Type again.")
        date = input("Date (dd/mm/yyyy): ")
        isValidate = mtd.validateDate(date)
    pages = input("Pages: ")
    isInt = mtd.isInt(pages)
    if isInt:
        readRecord = date + '\t' + pages + "\n"
        db.write(readRecord)
    else:
        while isInt != True:
            print("\nInvalid number of pages. Type again.")
            pages = input("Pages: ")
            isInt = mtd.isInt(pages)
        readRecord = date + '\t' + pages + "\n"
        db.write(readRecord)

main()

