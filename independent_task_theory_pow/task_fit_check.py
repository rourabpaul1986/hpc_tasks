import csv
import itertools


def Task_Fit_Check(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu):

 f = open("temp/task_comb.csv", "r")
 pf = open("temp/task_pow_comb.csv", "r")
 nft = open("temp/not_fitted.csv", "w+")
 ft = open("temp/fitted.csv", "w+")
 shares = list(csv.reader(f, delimiter=","))
 power = list(csv.reader(pf, delimiter=","))
 
 for i in range(0, len(shares)):  
  s=str(shares[i])
  #print(s)
  cleaned_s = s.replace("'", "")
  #print(cleaned_s)
  if float(shares[i][len(tasks)-1]) > nf*tslr- len(tasks)*tcfg:#-1 because task input has header row
   nft.write(cleaned_s[1:-1]+", "+str(power[i][len(tasks)-1]))
   nft.write("\n")
  else : 
   ft.write(cleaned_s[1:-1]+", "+str(power[i][len(tasks)-1]))
   ft.write("\n")
   
 f.close()
 ft.close()
 nft.close()

