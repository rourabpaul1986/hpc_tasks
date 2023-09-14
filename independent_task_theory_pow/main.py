import csv
import matplotlib.pyplot as plt
from task_share import *
from task_fit_check import *
from task_set_gen import *
from task_set_pow_gen import *
from sort import *
from power_opt1 import *
from fpga_script import *
import itertools


input_tasks="task_sets/tasks1.csv"
tslr=60 # given time slice
nf=4 # number of FPGA
tcfg=6 # bit file configuration time
cu_column=10
data_column=9
ii_column=8
period_column=7
host_com_column=6
host_loc_column=5
in_data_com_column=4
in_data_loc_column=3
xclbin_com_column=2
xclbin_loc_column=1
task_name_column=0
max_cu=4
power_column=cu_column+max_cu
#*****************************open input task files************************************
file = open(input_tasks, "r")
tasks = list(csv.reader(file, delimiter=","))
file.close()
#*******************task parameter calculation******************************************
Task_Share_Cal(tasks, cu_column, data_column, period_column, tslr, max_cu)
#************************initial task fit checking***************************************
Task_Set_Gen(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu)
Task_Set_Pow_Gen(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu)
Task_Fit_Check(nf, tcfg, tslr, tasks, power_column, cu_column, max_cu)
#**************descending order sorting based on total weight of of task****************
Sorted() 
#**********************find task most fitted task set***************************
print(len(tasks)-1)
task=Power_Opt(tasks, tcfg, tslr, nf,len(tasks)-1, ii_column)
#task=[48, 9, 48, 32, 24, 24]
#task=[24, 12, 12, 48, 48, 48]
print("The low power task set is"+str(task))

float_list = [float(num) for num in task]
task_int = [int(num) for num in float_list]

print(task_int)
fpga_script(tasks, tcfg, tslr, nf, task_int, len(task_int), task_name_column, data_column, period_column, cu_column, xclbin_loc_column, xclbin_com_column, in_data_com_column, in_data_loc_column, host_loc_column, host_com_column, ii_column)
