import csv

def count_csv_rows(file_path):
    row_count = 0

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            row_count += 1

    return row_count



def fetch_csv_row(file_path, row_number):
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        if row_number < 1 or row_number > len(rows):
            return None  # Invalid row number
        else:
            return rows[row_number - 1]


#etw defines how far work is done in current fpga
def fpga(tasks, sti, stw, task_int, task_length, tcfg, tslr, ii_column):
   #f = open("tasks.csv", "r")
   #task_set = list(csv.reader(f, delimiter=","))
   task_set=tasks
   #print(task[4][2])
   start=0
   end=0
   eti=0
   etw=0
   rc=tslr
   
   for i in range(sti, task_length): # for a single task
      start=end
      end=(end+int(task_int[i])+tcfg)-stw
      #stw=0
      if end>tslr:
        end=tslr
      for j in range(start, end): # for a single task
         #print("start : "+str(start))
         #print("end : "+str(end))
         if(j>=start) and j<(start+tcfg):
           print("t"+str(j)+"-> Task"+str(i)+" Tcfg.."+str(task_int[i]))
         elif(j>=start+tcfg) and j<(end):
           #print("t"+str(j)+"T : "+str(i)+"rc :"+str(rc))
           print("t"+str(j)+"-> Task"+str(i)+" Running")
      rc1=rc
      rc=rc-task_int[i]-tcfg+stw;
      stw1=stw
      stw=0
      #print(rc)
      if rc<=tcfg and rc>=0 or rc<=int(task_set[i+1][ii_column]) and rc>=0 :
        eti=i+1
        etw=0
        break
      if rc<0:
        eti=i
        etw=rc1-tcfg+stw1
        break        
      

        
   return eti, etw 

def Power_Opt(tasks, tcfg, tslr,nf, length, ii_column):
 r=0
 rank_1=0
 f = open("sorted_fitted.csv", "r")
 task_share = list(csv.reader(f, delimiter=","))
 task_int = [[] for _ in range(len(task_share))] 
 for k in range(0, len(task_share)):
  task_int[k] = [int(float(num)) for num in task_share[k]]

  sti=0
  stw=0
  for i in range(0, nf): # for nf FPGAs
    print("*********FPGA"+str(i)+"***********")
    sti, stw=fpga(tasks, int(sti), int(stw), task_int[k], length, tcfg, tslr, ii_column)
    if sti==0 and stw==0:
     if rank_1==0 :
       rank_1=k
     print("***************************")
     print("Number of FPGA Required to Map Given Tasks Set "+str(i+1) )
     print("***************************")
     break
    elif sti-stw!=0 and i==nf-1: 
     print("*********Task Rejected***********")
     r=r+1
    else:
     print("Next Task : T"+str(sti))
     print("Completion of T"+str(sti)+" in Current FPGA : "+str(stw))
 #print("number of rejected task "+str(r))
 


 not_fit = "not_fitted.csv" 
 fit = "fitted.csv"  
 nf = count_csv_rows(not_fit)
 fit = count_csv_rows(fit)
 print("Number of Not Fitted Task", nf+r)
 print("Number of Fitted Task", fit-r)
 print("The Row Index of Selected Low Power Task", rank_1)
 

 file_path = "sorted_fitted.csv"  # Replace with the path to your CSV file
 row_number = rank_1  # Replace with the desired row number

 row = fetch_csv_row(file_path, row_number)
 print("The Most Low power task set is", row[:length])
 ##########################################################

 return row[:length]
 
