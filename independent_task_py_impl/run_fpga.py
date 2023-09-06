import multiprocessing
import subprocess
from datetime import datetime


def watchdog():
  watch = datetime.now()
  #print("hour ", watch.hour)
  #print("minute ", watch.minute)
  #print("second ", watch.second)
  #print("milli second ", watch.millisecond)
  return watch

def spawn(nf):
  print("FPGA:"+str(nf)+" tasks started")
  start=watchdog()
  #print(subprocess.run(["script/fpga"+str(nf)], shell=True))
  subprocess.run(["python", "script/fpga"+str(nf)+".py"])
  end=watchdog()
  time_dif = end - start
  print("FPGA:"+str(nf)+" tasks completed")
  print("************************************************************")
  print("FPGA"+str(nf)+" Start Time (HH:MM:SS:MSMSMS):"+str(start.hour)+":"+str(start.minute)+":"+str(start.second)+":"+str(int(start.microsecond/1000)))
  print("FPGA"+str(nf)+" End Time (HH:MM:SS:MSMSMS):"+str(end.hour)+":"+str(end.minute)+":"+str(end.second)+":"+str(int(end.microsecond/1000)))
  print("FPGA"+str(nf)+" Time Requirement (ms):"+ str(time_dif.total_seconds()*1000))
  print("************************************************************")
  #print("minute ", watch.minute)
  #print("second ", watch.second)
  #print("milli second ", watch.millisecond)
  
  

def run_fpga(nf):
  ##print(subprocess.run(['xilinx_platform'], shell=True))
  for i in range(nf):
    p = multiprocessing.Process(target=spawn, args=(i,))
    p.start()
  p.join() # this line allows you to wait for processes
