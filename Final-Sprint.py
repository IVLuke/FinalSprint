# Final Sprint Project 2
# Authors: Cameron D'Amico, Jordon Kelloway, Luke Jones, Nathan Green
# Date Submitted: August 19th, 2022

import datetime
import FormatValues as FV
import math

# Functions

def QuitProgram():
    # prints the quit message for the program
    print("You have quit the program!")

def ComingSoon():
    # prints coming soon for options that didn't need to be coded
    print("Coming soon!!!")

def AnyKey():
    # function that calls for an input to end the program
    print()
    Ending = input("Enter any key to continue")
    print()
    return Ending

def ProfitListing():
    # Accumulators

    RevenueCTR = 0
    ExpenseCTR = 0
    RevenueACC = 0
    ExpenseACC = 0

    # Header

    print()
    print("HAB TAXI SERVICES")
    print("COMPANY PROFIT LISTING")
    print("FOR THE MONTH OF APRIL")
    print("----------------------")
    print()
    print("TRANSACTION DRIVER  TRANSACTION")
    print("DATE        NUMBER  DESCRIPTION         SUBTOTAL   HST      TOTAL")
    print("=" * 68)

    # Loop For First Table

    f = open('Revenue.dat', 'r')
    for ProfitListing in f:
        ProfitLine = ProfitListing.split(",")

        TransDate = ProfitLine[1].strip()
        TransDescription = ProfitLine[2].strip()
        DriverNo = ProfitLine[3].strip()
        TransAmt = float(ProfitLine[4].strip())
        HST = float(ProfitLine[5].strip())
        TotalTrans = float(ProfitLine[6].strip())

        print(
            f"{TransDate}  {DriverNo:<4s}    {TransDescription:<18s}  {FV.FDollar2(TransAmt):>7s}   {FV.FDollar2(HST):>7s}  {FV.FDollar2(TotalTrans):>9s}")
        RevenueCTR += 1
        RevenueACC += TotalTrans
    f.close()

    # Header #2
    print("=" * 68)
    print(f"REVENUE LISTINGS: {RevenueCTR}          TOTAL REVENUE FOR THE MONTH: {FV.FDollar2(RevenueACC)}")
    print()

    print("INVOICE     DRIVER   ITEM          ITEM                     INVOICE")
    print("DATE        NUMBER   DESCRIPTION   QTY   SUBTOTAL  HST      TOTAL")
    print("=" * 68)

    # Loop For 2nd Table

    f = open('Expenses.dat', 'r')
    for ExpenseListing in f:
        ExpenseLine = ExpenseListing.split(",")

        InvoiceDate = ExpenseLine[1].strip()
        DriverNo = ExpenseLine[2].strip()
        ItemDescription = ExpenseLine[4].strip()
        ItemQty = int(ExpenseLine[6].strip())
        SubTotal = float(ExpenseLine[7].strip())
        HST = float(ExpenseLine[8].strip())
        InvoiceTotal = float(ExpenseLine[9].strip())
        print(
            f"{InvoiceDate}  {DriverNo:<4s}     {ItemDescription:<12s}  {ItemQty:<3d}  {FV.FDollar2(SubTotal):>9s}  {FV.FDollar2(HST):>7s} {FV.FDollar2(InvoiceTotal):>9s}")

        ExpenseCTR += 1
        ExpenseACC += InvoiceTotal
    f.close()

    # Calculations

    ProfitLoss = RevenueACC - ExpenseACC

    # Final Print Statements

    print("=" * 68)
    print(f"EXPENSE LISTINGS: {ExpenseCTR}        TOTAL EXPENSES FOR THE MONTH: {FV.FDollar2(ExpenseACC):>10s}              ")
    print()
    print(f"                            PROFIT LOSS FOR THE MONTH:    {FV.FDollar2(ProfitLoss):>10s}")
    print("                            (PROFIT LOSS IS REVENUE - EXPENSES) ")

# Loop for the menu
while True:

    print("HAB Taxi Services")
    print("Company Service System")
    print()
    print("1. Enter a New Employee (Driver). ")
    print("2. Enter Company Revenues.        ")
    print("3. Enter Company Expenses.        ")
    print("4. Track Car Rentals.             ")
    print("5. Record Employee Payment.       ")
    print("6. Print Company Profit Listing.  ")
    print("7. Print Driver Financial Listing.")
    print("8. Quit Program.                  ")
    print()

    # Input + Verification for the main loop
    while True:
        try:
            Choice = int(input("  Enter choice (1-8): "))
            print()
        except:
            print("  Error -  enter a valid integer between 1-8")
            continue
        else:
            if Choice < 1 or Choice > 8:
                print("  Error -  enter a valid integer between 1-8")
                continue
        break

    if Choice == 1:
        AnyKey()
    elif Choice == 2:
        ComingSoon()
        AnyKey()
    elif Choice == 3:
        ComingSoon()
        AnyKey()
    elif Choice == 4:
        ComingSoon()
        AnyKey()
    elif Choice == 5:
        ComingSoon()
        AnyKey()
    elif Choice == 6:
        ProfitListing()
        AnyKey()
    elif Choice == 7:
        AnyKey()
    elif Choice == 8:
        QuitProgram()
        break
