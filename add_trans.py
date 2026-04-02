#Importing Libraries
import pandas as pd
import os

#Defining Function add_transaction()
def add_transaction(date,amount,category,description = "NA"):
    #"NA" as Default Value for descrition.
    print(f"Date of Trancastion is {date}")
    print(f"Amount of Transaction is {amount}")
    print(f"Category of Transaction is {category}")
    if description != "NA":
        print(f"Description of Transaction is {description}")
    else:
        print("No Description")
    #Creating a Dictionary because pandas considers list [] as row and {} key:value as column name and value 
    l = {
        "Date":date,
        "Amount":amount,
        "Category":category,
        "Descrition":description
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


#Data Input
Date = input("Enter the Date :")
Amount = input("Enter the Amount :")
Category = input("Enter Category :")
Description = input("Input Description :")

#Function Calling
l = add_transaction(Date,Amount,Category,Description)
saving(l)
print("Saved............")
