##Varible
WithBal = int(input("How much do you want to withdraw: "))
MaxWithdrawLimit = 23000
Thousand = 10
FiveHundred = 20
Hundred = 30
WithdrawThousand = 0
WithdrawFiveHundred = 0
WithdrawHundred = 0

##WithBalCheck if it True
WithBalCheck = WithBal/100
if WithBalCheck % 1 == 0:
    WithBalCheck = int(WithBalCheck)
else:
    WithBalCheck = float(WithBalCheck)
CheckResault = isinstance(WithBalCheck, int)
##Debug WithBalCheck
#print(WithBalCheck)
#print(CheckResault)
if WithBal <= MaxWithdrawLimit and CheckResault == True:
    while True:
        if WithBal >= 1000 and Thousand !=0:
            WithBal = WithBal-1000
            WithdrawThousand = WithdrawThousand+1
            Thousand = Thousand-1
        else:
            break
    while True:
        if WithBal >= 500 and FiveHundred !=0:
            WithBal = WithBal-500
            WithdrawFiveHundred = WithdrawFiveHundred+1
            FiveHundred = FiveHundred-1
        else:
            break
    while True:
        if WithBal >= 100 and Hundred !=0:
            WithBal = WithBal-100
            WithdrawHundred = WithdrawHundred+1
            Hundred = Hundred-1
        else:
            break
    print("WithdrawThousand: ", WithdrawThousand)
    print("WithdrawFiveHundred: ", WithdrawFiveHundred)
    print("WithdrawHundred: ", WithdrawHundred)
else:
    print("Can't withdraw")