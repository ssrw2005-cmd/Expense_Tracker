import pandas as pd
def delete_transaction():
    D = int(input("Enter ID of the Transaction to be Deleted : "))
    if D in df.index:
        df.drop(index=D,inplace=True)
        print("Transaction Deleted.....")
        df.to_csv("Transaction.csv")
    else:
        print(f"ID {D} Doesn't Exist")




def view_transaction():

    print(df)




df = pd.read_csv("Transaction.csv")
print("Enter 1 to view Transactions or 2 to Delete Transaction")
opt = int(input("Enter your Option"))

if opt == 1:
    view_transaction()
elif opt == 2:
    delete_transaction()
else:
    print("NO OPTION CHOOSEN")