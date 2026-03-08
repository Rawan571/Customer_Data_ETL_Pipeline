# create hardcoded CSV data and write it to a file

csv_data="""TransactionID,CustomerID,TransactionDate,TransactionAmount,TransactionType
1,c001,2024-01-15,250.00,purchase
2,c002,2023-11-20,150.00,purchase
3,c003,2022-07-30,-75.00,refund
4,c004,2024-03-05,,purchase
5,c005,2024-06-22,500.00,purchase
"""

# Writing the hardcoded CSV data to a file

with open('customer_transaction.csv','w') as f:
    f.write(csv_data)


import pandas as pd
df = pd.read_csv('customer_transaction.csv')
df


# Filter for rows which have TransactionType as 'purchase'

df = df[df['TransactionType']=='purchase']


# Filtering those rows which has positive and not null TransactionAmount

df = df[df['TransactionAmount'].notnull() & (df['TransactionAmount'].notnull() > 0)]
df


# Converting TransactionDate values to date tybe

df['TransactionDate']=pd.to_datetime(df['TransactionDate'])
df['TransactionDate']


# TransactionAmount for each CustomerID

summary_df = df.groupby('CustomerID')['TransactionAmount'].sum().reset_index()
df

summary_df


# Loading

# Saving the final dataframe into a csv in a local machine

summary_df = summary_df.to_csv('customer_purchase_summary.csv')
