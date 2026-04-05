import sys
expenses=[]
def add_expense():
    try:
        amount=float(input("Enter the amount"))
        category=input("Enter the category: Food,Travel,Books,Health,House Maintainence,Unexpected Expenses(Fine)")
        mandatory=input("Was the above expense mandatory or simply by choice,enter 'Yes' if yes else enter 'No'")
        description=input("Details Of Expense")
        expense={
            "amount":amount,
            "category":category,
            "mandatory":mandatory,
            "description":description

        }
        expenses.append(expense)
    except ValueError:
        print("Enter appropriate details!!!")

def view_expense():
    if not expenses:
        print("No expenses found")
        return
    else:
        print("========Expense List======")
        for i,exp in enumerate(expenses,start=1):
            print(f"{i}. Rs.,{exp['amount']} | {exp['category']} | {exp['mandatory']} |{exp['description']}")
        print()


def del_expense():
    view_expense()
    if not expenses:
        print("No expenses found")
        return
    try:
        x=int(input("Enter the expense number to be deleted"))-1
        if((x>=0) and (x<len(expenses))):
            removed=expenses.pop(x)
            print("======Expense Deleted Successfully======")
    except ValueError:
        print("Enter Expense Number Properly!!!")

def check_exp():
    mandatory_exp=0
    over_exp=0
    view_expense()
    if not expenses:
        print("No expense found")
        return
   
    for i in expenses:
        if(i["mandatory"]=="Yes"):
            mandatory_exp=mandatory_exp+i["amount"]
        else:
            over_exp=over_exp+i["amount"]
    
    print("=======Mandatory Expenses========\n")
    # for i in expenses:
        # if(expenses["mandatory"]=="Yes"):
            # print(f"{i+1}. { expenses['amount']} | {expenses['category']}| {expenses['descrption']}")
    for i,exp in enumerate(expenses,start=1):
        if(exp['mandatory']=='Yes'):
            print(f"{i}. Rs.,{exp['amount']} | {exp['category']} | {exp['mandatory']} |{exp['description']}")
    print()
    
    print()
    print("====Total Mandatory Expense=====\n")    
    print(mandatory_exp)
    print("==================================\n")

    print("=======Overhead Expenses========")
    for i,exp in enumerate(expenses,start=1):
        if(exp['mandatory']=='No'):
            print(f"{i}. Rs.,{exp['amount']} | {exp['category']} | {exp['mandatory']} |{exp['description']}")
    print()
    print("====Total Overhead Expense=====\n")    
    print(over_exp)
          

    


def total_expense():
    
    total=sum(i["amount"] for i in expenses)
    print("=========Total Expense=========\n")
    print(f"Total Revenue  Rs.{total}")

             



def menu():
    while (True):
        print("=====Expense Tracker=====")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. To exit !!")
        print("=========================")
        x=int(input("Enter your input "))
        if (x==1):
            add_expense()
        elif(x==2):
            view_expense()
        elif(x==3):
            del_expense()
        elif(x==4):
            total_expense()
            check_exp()
        elif(x==5):
            print("Thanks for using Expensify!!")
            sys.exit()
        else:
            print("Enter valid option!!")


menu()