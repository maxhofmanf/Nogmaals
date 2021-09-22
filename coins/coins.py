# name of student: max hofman
# number of student: 9908281
# purpose of program: to show coin value
# function of program: when you type a coinvalue it shows how many coins you need to return
# structure of program:  i dont understand this question

toPay = int(float(input('Amount to pay: '))* 100) #
payed = int(float(input('Payed amount: ')) * 100) #
change = payed - toPay #

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: i added         to the code
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
    
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')