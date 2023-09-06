import csv
#import matplotlib.pyplot as plt
from task_share import *
from task_fit_check import *
from sort import *
from power_opt import *
from fpga_script import *
from script.splitter import *
from run_fpga import *
import subprocess
import itertools
#import pyxrt
from utils_binding import *
import os
import sys
import uuid
import re
import pyopencl as cl

import json




#********************parameters***************************************************
input_tasks="task_sets/tasks2.csv"
time_scale=0.001 #in milli second
tslr=600 # given time slice
nf=2 # number of FPGA
tcfg=21 # bit file configuration time
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
#*****************************open input task files************************************
#****************************c++ test*****************************************

print(subprocess.run(["./xilinx_platform", ""]))

#***************************************************************************************
#print(subprocess.run(['xilinx_platform'], shell=True))
file = open(input_tasks, "r")
tasks = list(csv.reader(file, delimiter=","))
file.close()
#*******************task parameter calculation******************************************
Task_Share_Cal(tasks, cu_column, data_column, period_column, tslr)#calculate weight based on (e*tslr)/p and e=total data/throughput
#************************initial task fit checking***************************************
Task_Fit_Check(nf, tcfg, tslr)
#**************descending order sorting based on total weight of of task****************
Sorted() 
#**********************find task most fitted task set***************************
print(len(tasks)-1)
task=Power_Opt(tasks, tcfg, tslr,nf,len(tasks)-1, ii_column)

#print("The low power task set is"+str(task))

float_list = [float(num) for num in task]
task_int = [int(num) for num in float_list]

print(task_int)
fpga_script(tasks, tcfg, tslr, nf, task_int, len(task_int), task_name_column, data_column, period_column, cu_column, xclbin_loc_column, xclbin_com_column, in_data_com_column, in_data_loc_column, host_loc_column, host_com_column, time_scale)

Data_Splitter()
run_fpga(nf)


