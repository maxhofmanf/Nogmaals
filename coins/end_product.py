# name of student: max hofman
# number of student: 99068182
# purpose of program: om te laten zien 
# function of program:
# structure of program: 




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
# comment on code below: 
    if coinValue == 500:
      vijfhonkwart =nrCoinsReturned
      vijfhonkwart =str(vijfhonkwart)
      print("je hebt " + vijfhonkwart + " cent van 500")
      coinValue = 300
    elif coinValue == 300:
      driehonkwart =nrCoinsReturned
      driehonkwart =str(driehonkwart)
      print("je hebt " + driehonkwart + " cent van 300")
      coinValue = 200
    elif coinValue == 200:
      tweehonkwart =nrCoinsReturned
      tweehonkwart =str(tweehonkwart)
      print("je hebt " + tweehonkwart + " cent van 200")
      coinValue = 50
    elif coinValue == 50:
      vijftigkwart =nrCoinsReturned
      vijftigkwart =str("je hebt " + vijftigkwart + " cent van 50")
      coinValue = 20
    elif coinValue == 20:
      twintigkwart=nrCoinsReturned
      twintigkwart=str(twintigkwart)
      print("je hebt " + twintigkwart " cent van 20")
      coinValue = 10
    elif coinValue == 10:
      tienkwart=nrCoinsReturned
      tienkwart=str(tienkwart)
      print("je hebt" + tienkwart + " cent van 10")
      coinValue = 5
    elif coinValue == 5:
      vijfkwart=nrCoinsReturned
      vijfkwart+str(vijfkwart)
      print("je hebt" + vijfkwart + " cent van 5")
      coinValue = 2
    elif coinValue == 2:
      tweekwart=nrCoinsReturned
      coinValue = 1
    else:
    
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print("done")
