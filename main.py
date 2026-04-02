#Importing Libraries
import pandas as pd
import os

#Defining Function add_transaction()
def add_transaction(id,date,amount,category,description = "NA"):
    #"NA" as Default Value for descrition.
    print(f"ID of Transaction is : {id}")
    print(f"Date of Trancastion is {date}")
    print(f"Amount of Transaction is {amount}")
    print(f"Category of Transaction is {category}")
    if description != "NA":
        print(f"Description of Transaction is {description}")
    else:
        print("No Description")
    #Creating a Dictionary because pandas considers list [] as row and {} key:value as column name and value 
    l = {
        "ID":id,
        "Date":date,
        "Amount":amount,
        "Category":category,
        "Description":description
    }
    return l


#Defining Function saving()
def saving(l):
    #Creating DataFrame
    df = pd.DataFrame([l])
    #Checking if Transaction.csv already exists or not
    head = not(os.path.exists("Transaction.csv"))
    # if file already Exist Header = False else True
    #Append Mode to not overwrite upon previous values
    df.to_csv("Transaction.csv",mode ="a",header=head,index=False)
    print(df)

# To Delete Unwanted Transactions
def delete_transaction():
    #User Needs to Enter the Id of the Transaction
    D = int(input("Enter ID of the Transaction to be Deleted : "))
    #it Checks whether the ID is present in DataFrame
    if D in df["ID"].values:
        df.drop(df[df["ID"] == D].index,inplace=True)
        print("Transaction Deleted.....")
        #DataFrame is Updated after Deletion
        df.to_csv("Transaction.csv",index=False)
    else:
        print(f"ID {D} Doesn't Exist")




def view_transaction():

    print(df)



def generate_monthly_report(month):
    # filter
    df_2 = df[df["Month"] == month]
    if df_2.empty:
        print("NO TRANSACTION FOR THIS MONTH")
    else:
        # total spending
        tot_spend = df_2["Amount"].sum()
        cat_sum = df_2.groupby("Category")["Amount"].sum()
        # category-wise
        tot_spend_cat = cat_sum.reset_index()
        # highest category
        high_cat = cat_sum.idxmax()
        #highest Amount
        high_amount = cat_sum.max()
        # printing report
        print(f"Report For Month : {month} ")
        print(f"Total Spending : {tot_spend} ")
        print("Total Spending Category Wise : ")
        print(f"{tot_spend_cat}")
        print(f"Highest Spending Category : {high_cat} ")
        print(f"Highest Amount : {high_amount}")



#Checks if file Already Exist or not because Pandas Cannot Read File that doesn't Exist
if os.path.exists("Transaction.csv"):#Return True if File Exists
    df = pd.read_csv("Transaction.csv")
else:
    df = pd.DataFrame(columns=["ID","Date","Amount","Category","Description"])
#Providing Different Operations
print("Enter 0 to View Transaction \nEnter 1 to Add Transactions \nEnter 2 to Delete Transaction \nEnter 3 to Generate Monthly Report")
opt = int(input("Enter your Option"))


if opt == 1:
    #Data Input
    if os.path.exists("Transaction.csv"):
        Id = df["ID"].max() + 1
    else:
        Id = 1
    while True:
        try:
            Date = pd.to_datetime(input("Enter the Date format DD/MM/YY:"),dayfirst=True)
            #Changing Date Column to Correct Data Type as Per Indian Standards 
            break
        except ValueError:
            print("Enter Valid Date")
    while True:
        try:    
            Amount = float(input("Enter the Amount :"))
            Amount.is_integer
            break
        except ValueError:
            print("Enter a valid Input")
    Category = input("Enter Category :")
    Description = input("Input Description :")

    #Function Calling
    l = add_transaction(Id,Date,Amount,Category,Description)
    saving(l)
    print("Saved............")

elif opt == 0:
    view_transaction()
elif opt == 2:
    delete_transaction()
elif opt == 3:
    month = int(input("Enter which Month Report to be Generated :" ))
    #Creating Month Column
    df["Month"] = df["Date"].dt.month
    generate_monthly_report(month)
else:
    print("NO OPTION CHOOSEN")

