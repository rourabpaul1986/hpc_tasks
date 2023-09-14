import csv



def Sorted():
 ft = open("temp/fitted.csv", "r+")
 shares = list(csv.reader(ft, delimiter=","))
 shares.sort(key=lambda x: float(x[len(shares)-1]))# the sum of power location 1st from last
 #shares.reverse()
 with open('temp/sorted_fitted.csv', 'w') as ft:
  write = csv.writer(ft)
  write.writerows(shares)
  
 nft = open("temp/not_fitted.csv", "r+")
 shares = list(csv.reader(nft, delimiter=","))
 shares.sort(key=lambda x: float(x[len(shares)-1]))# the sum of power location 1st from last
 #shares.reverse()
 with open('temp/sorted_not_fitted.csv', 'w') as nft:
  write = csv.writer(nft)
  write.writerows(shares)
