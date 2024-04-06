ram_bank_balance=100000
ram_loan=500000

lakshman_bank_balance=2000000
lakshman_loan=1000000

net_worth=ram_bank_balance+lakshman_bank_balance
net_liability=ram_loan+lakshman_loan

final_value=net_worth-net_liability
print("so, the family has",final_value)

if ram_bank_balance < ram_loan:
    print("Ram needs to repay the loan or increase bank balance.")
else:
    print("Ram has enough balance to pay off the loan.")



