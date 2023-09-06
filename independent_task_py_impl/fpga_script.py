import csv
import os
import subprocess # to change permission of files


def delete_files_starting_with(directory_path, prefix):
    files = os.listdir(directory_path)
    for file in files:
        if file.startswith(prefix):
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)

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
def fpga(tasks, nf, file_fpga, file_fpga_py, file_data, sti, stw, task_int, task_length, tcfg, tslr, task_name_column, data_column, period_column, cu_column, xclbin_loc_column, xclbin_com_column, in_data_com_column, in_data_loc_column, host_loc_column, host_com_column, time_scale):
   start=0
   end=0
   eti=0
   etw=0
   rc=tslr
   xclbin_flag=0
   #f = open("tasks.csv", "r")
   #task = list(csv.reader(f, delimiter=","))
   task=tasks
   #print(task[1][1])
   for i in range(sti, task_length): # for a single task
      start=end
      end=(end+int(task_int[i])+tcfg)-stw
      if end>tslr:
        end=tslr
      for j in range(start, end): # for a single task
         if(j>=start) and j<(start+tcfg):
           #*************************to count number of CU**************************
           data=task[i+1][data_column]
           p=task[i+1][period_column]
           w=task_int[i]
           x=(int(data)*tslr)/(int(p)*w)
           for n in range(1, int(task[i+1][cu_column])+1):
               if x==float(task[i+1][cu_column+n]):
                   cu=n
                   break
           #************************************************************************* 
           xcl_loc=task[i+1][xclbin_loc_column]
           xcl_com=task[i+1][xclbin_com_column]  
           data_loc=task[i+1][in_data_loc_column]
           data_com=task[i+1][in_data_com_column] 
           host_loc=task[i+1][host_loc_column]
           host_com=task[i+1][host_com_column]
           if   host_com:
              host_com="\""+host_com+"\","
           if   xcl_com:
              xcl_com="\""+xcl_com+"\","  
           if   data_com:
              data_com="\""+data_com+"\","               
           split_data_name = os.path.splitext(data_loc)  #split input file name and its extension. its required to split and renamimng of input file
           print("t"+str(j)+"-> Task"+str(i)+" Tcfg.."+str(n)+"cu_t"+str(i)+"cu.xclbin")
           if xclbin_flag==0:
            xclbin_flag=1
            data_size=str(end-start-tcfg)+"_"+str(w)
            xclbin_name=str(n)+"CU_"+str(task[i+1][task_name_column])+".xclbin"
            host_name=str(n)+"CU_"+str(task[i+1][task_name_column])
            if(end-start-tcfg==w):
             #file_fpga.write("\n"+host_com+" ./"+host_loc+host_name+" "+xcl_com+" ./"+xcl_loc+xclbin_name+" "+data_com+" "+split_data_name[0]+split_data_name[1]+" -id "+str(nf))
             file_fpga_py.write("\nargs=["+host_com+" \"./"+host_loc+host_name+"\", "+xcl_com+" \"./"+xcl_loc+xclbin_name+"\", "+data_com+" \""+split_data_name[0]+split_data_name[1]+"\", \"-id\" ,\""+str(nf)+"\"]\n")
             file_fpga_py.write("subprocess.call(args)\n")
             #file_fpga_py.write("\n"+host_com+" ./"+host_loc+host_name+" "+xcl_com+" ./"+xcl_loc+xclbin_name+" "+data_com+" "+split_data_name[0]+split_data_name[1]+" -id "+str(nf))
            else:
             file_fpga_py.write("\nargs=["+host_com+" \"./"+host_loc+host_name+"\", "+xcl_com+" \"./"+xcl_loc+xclbin_name+"\", "+data_com+" \""+split_data_name[0]+"_"+str(data_size)+split_data_name[1]+"\", \"-id\" ,\""+str(nf)+"\"]\n")
             file_fpga_py.write("subprocess.call(args)\n")
             #file_data.write(split_data_name[0]+split_data_name[1]+", "+str(end-start-tcfg)+", "+str(w)+", "+task[i+1][data_column]+"\n")
             #file_fpga.write("\n"+host_com+" ./"+host_loc+host_name+" "+xcl_com+" ./"+xcl_loc+xclbin_name+" "+data_com+" "+split_data_name[0]+"_"+str(data_size)+split_data_name[1]+" -id "+str(nf))
         elif(j>=start+tcfg) and j<(end):
           xclbin_flag=0
           print("t"+str(j)+"-> Task"+str(i)+" Running")
           file_fpga_py.write("\ntime.sleep("+str(time_scale)+")")
      rc1=rc
      rc=rc-task_int[i]-tcfg+stw;
      stw1=stw
      stw=0
      #print(rc)
      if rc<=tcfg and rc>=0:
        eti=i+1
        etw=0
        break
      if rc<0:
        eti=i
        etw=rc1-tcfg+stw1
        break        
      

        
   return eti, etw 

def fpga_script(tasks, tcfg, tslr, nf, task_int, length, task_name_column, data_column, period_column, cu_column, xclbin_loc_column, xclbin_com_column, in_data_com_column, in_data_loc_column, host_loc_column, host_com_column, time_scale):

  sti=0
  stw=0
  file_data = open("script/data_splitter_script.csv", "w+")
  #********************* to delete previous script*********************
  directory_path="script"
  prefix_to_delete="fpga"
  delete_files_starting_with(directory_path, prefix_to_delete)
  #********************************************************************
  for i in range(0, nf): # for nf FPGAs
    file_fpga = open("script/fpga%s" %i, "w+")
    file_fpga_py = open("script/fpga%s.py" %i, "w+")
    file_fpga_py.write("import subprocess\nimport time\n")
    subprocess.call(['chmod', '0770', "script/fpga"+str(i)])
    print("*********FPGA"+str(i)+"***********")
    sti, stw=fpga(tasks, i, file_fpga, file_fpga_py,file_data, int(sti), int(stw), task_int, length, tcfg, tslr, task_name_column, data_column, period_column, cu_column, xclbin_loc_column, xclbin_com_column, in_data_com_column, in_data_loc_column, host_loc_column, host_com_column, time_scale)
    if sti==0 and stw==0:
     print("***************************")
     print("Number of FPGA Required to Map Given Tasks Set "+str(i+1) )
     print("***************************")
     break
  file_fpga.close()   
  file_fpga_py.close() 

 


 
