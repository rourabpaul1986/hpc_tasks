import csv
import itertools


def Task_Set_Gen(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu):

 f = open("temp/task_shares.csv", "r")
 tb = open("temp/task_comb.csv", "w+")
 shares = list(csv.reader(f, delimiter=","))
 #print(shares[1])
 for i in range(1, len(shares)):  #the first row is skipped because it is headed
  shares[i]=shares[i][2:-1]#share started from 2nd column
 print(shares)
 i=0
 for combination in itertools.product(*shares[1:]):
  i=i+1
  out = []
  #print(str(i))  
  for item in combination:
    out.append(float(item)) 
  #print(out[0]) 
  Sum = sum(out)
  workload=Sum*100/(tslr*nf)
  #len(shares)-1 is number of task
  avg_task_wt=Sum/(tslr*(len(shares)-1))
  
  tb.write(str(out)[1:-1]+", "+str(Sum)+", "+str(workload)+", "+str(avg_task_wt))
  #nft.write(str(out)[1:-1]+", "+str(Sum))
  tb.write("\n")
 f.close()
