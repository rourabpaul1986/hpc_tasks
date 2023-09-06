import csv
import itertools


def Task_Fit_Check(nf, tcfg, tslr):
 f = open("task_shares.csv", "r")
 nft = open("not_fitted.csv", "w+")
 ft = open("fitted.csv", "w+")
 shares = list(csv.reader(f, delimiter=","))
 #print(shares[1])
 for i in range(1, len(shares)):  #the first row is skipped because it is headed
  shares[i]=shares[i][2:-1]
 print(shares)
 i=0
 for combination in itertools.product(*shares[1:]):
  i=i+1
  out = []
  #print(str(i))  
  for item in combination:
    out.append(float(item)) 
  #print(out) 
  Sum = sum(out)
  workload=Sum*100/(tslr*nf)
  #len(shares)-1 is number of task
  avg_task_wt=Sum/(tslr*(len(shares)-1))
# minimum requirement to fit tasks
  if Sum > nf*tslr- len(shares)*tcfg :
   nft.write(str(out)[1:-1]+", "+str(Sum)+", "+str(workload)+", "+str(avg_task_wt))
   #nft.write(str(out)[1:-1]+", "+str(Sum))
   nft.write("\n")
  else :
   ft.write(str(out)[1:-1]+", "+str(Sum)+", "+str(workload)+", "+str(avg_task_wt))
   #ft.write(str(out)[1:-1]+", "+str(Sum))
   ft.write("\n")
  #print(Sum)
 f.close()
