import pandas as pd

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
        # print report
        print(f"Report For Month : {month} ")
        print(f"Total Spending : {tot_spend} ")
        print("Total Spending Category Wise : ")
        print(f"{tot_spend_cat}")
        print(f"Highest Spending Category : {high_cat} ")
        print(f"Highest Amount : {high_amount}")

df = pd.read_csv("Transaction.csv")
df["Date"] = pd.to_datetime(df["Date"],dayfirst=True)
df["Month"] = df["Date"].dt.month

month = int(input("Enter which Month Report to be Generated :" ))
generate_monthly_report(month)