

partysize= int(input("How many mates- inlcuding yourself- are having a pint?"))
pintprice= float(input("How much are you paying per pint?"))
tax= (1+(float(input("Enter the tax surcharge as a decimal, if any. If none, put 0."))))
tip= (1+(float(input("Enter either the service charge or how much you plan on tipping as a decimal. If nothing, put 0."))))
totalpints= (partysize**2)
#each person buys a drink for the table including themselves, thus the exponent

total_amount= (totalpints*pintprice*tax*tip)
total_perperson=(total_amount)/partysize
print('\nTotal amount of bill = %f' %total_amount)
print('\nTotal amount each person pays = %f' %total_perperson)