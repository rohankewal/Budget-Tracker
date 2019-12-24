def main():
    endProgram = 'no'
    integerchoice = 0
    totalBudget = int(raw_input('Enter your budget for the month and press enter:$'))
    while endProgram == 'no':
        print()
        print ('1-Add an Expense:')
        print ('2-Remove an Expense:')
        print ('3-Add Revenue:')
        print ('4-Remove Revenue:')
        print ('5-Check Budget Balance:')
        print ('6-Exit')
        print()
        choice = int(raw_input('Enter your selection: '))
        if choice == 1:
            totalBudget = addExpense (totalBudget)
        elif choice == 2:
            totalBudget = removeExpense(totalBudget)
        elif choice == 3:
            totalBudget = addRevenue(totalBudget)
        elif choice == 4:
            totalBudget = removeRevenue(totalBudget)
        elif choice == 5:
            print ('Your balance is',totalBudget)
        elif choice == 6:
            endProgram = 'yes'
            print ('Thank you for using my budget program, Goodbye')
        else:
            print('Invalid choice, please try another')

def addExpense(totalBudget):
    bill = int(raw_input('Enter the expense amount and press enter:'))
    manyBill = int(raw_input('Enter the frequency of the expense per month and press enter:'))
    totalBill = bill * manyBill
    totalBudget = totalBudget - totalBill
    checkBudget(totalBudget)
    return totalBudget

def removeExpense(totalBudget):
    lessBill = int(raw_input('Enter the amount to remove and press enter:'))
    manyLess = int(raw_input('Enter the frequency of the expense removal per month and press enter:'))
    totalLess = lessBill * manyLess
    if totalLess <= (totalBudget):
        totalBudget = totalBudget + totalLess
        checkBudget(totalBudget)
    else:
        print('*ERROR* re-check the amounts entered')
        return totalBudget

def addRevenue(totalBudget):
    income = int(raw_input('Enter the amount of additional income and press enter:'))
    totalBudget = totalBudget + income
    checkBudget(totalBudget)
    return totalBudget

def removeRevenue(totalBudget):
    lossIncome = int(raw_input('Enter the amount of income to be removed and press enter:'))
    totalBudget = totalBudget - lossIncome
    checkBudget(totalBudget)
    return totalBudget

def checkBudget(totalBudget):
    if totalBudget >= (0):
        print('The total remaining budget is:$' + totalBudget )
    else:
        print('You have exceeded the monthly budget')
        print('Re-evaluate your expenses and balance the budget')
        print('Current balance:', totalBudget)

main()

