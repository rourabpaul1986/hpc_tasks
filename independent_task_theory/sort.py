import csv



def Sorted():
 ft = open("fitted.csv", "r+")
 shares = list(csv.reader(ft, delimiter=","))
 shares.sort(key=lambda x: float(x[len(shares)-3]))# the sum of weight location 3rd from last
 shares.reverse()
 with open('sorted_fitted.csv', 'w') as ft:
  write = csv.writer(ft)
  write.writerows(shares)
  
 nft = open("not_fitted.csv", "r+")
 shares = list(csv.reader(nft, delimiter=","))
 shares.sort(key=lambda x: float(x[len(shares)-3]))# the sum of weight location 3rd from last
 shares.reverse()
 with open('sorted_not_fitted.csv', 'w') as nft:
  write = csv.writer(nft)
  write.writerows(shares)
