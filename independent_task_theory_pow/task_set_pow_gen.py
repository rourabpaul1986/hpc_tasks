import csv
import itertools


def Task_Set_Pow_Gen(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu):
 ############power calculation###############
 power = [None for _ in range(len(tasks))]
 for i in range(1, len(tasks)): 
  back=int(tasks[i][cu_column])-max_cu
  if back==0:
   power[i]=tasks[i][power_column+1:]
  else:
   power[i]=tasks[i][power_column+1:back] 
 print(power)
 ##########################################
 tpb = open("temp/task_pow_comb.csv", "w+")
 i=0
 for combination in itertools.product(*power[1:]):
  i=i+1
  out = []
  #print(str(i))  
  for item in combination:
    out.append(float(item)) 
  #print(out[0]) 
  Sum = sum(out)
 
  tpb.write(str(out)[1:-1]+", "+str(Sum))
  tpb.write("\n")
 tpb.close()
