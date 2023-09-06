import csv
import math


def Task_Share_Cal(tasks, cu_column, data_column, period_column, tslr):
 print( "task share calculation started")
 f = open("task_shares.csv", "w+")
 f.write("Task ID, Varianets, Shares")
 f.write("\n")
 for i in range(1, len(tasks)):  #i iteration is started from 1 to skip the header
  #print(str(i))
  f.write(tasks[i][0]+","+tasks[i][cu_column]+",")
  for j in range(1, int(tasks[i][cu_column])+1): #5th column of tasks.csv represent number of Computation Unit
   e=float(tasks[i][data_column])/float(tasks[i][cu_column+j]) 
   w=e*tslr/float(tasks[i][period_column]) # weight calculation
   f.write(str(math.ceil(w))+",")
  f.write("\n")
 #f.close()
