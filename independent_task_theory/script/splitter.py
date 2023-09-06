
import csv
import os

file_path = 0
d_c=1
n_c=2
#f = open("1", "w+")


f = open("data_splitter_script.csv", "r")
file_row = list(csv.reader(f, delimiter=","))

def chunks(file_name, size):
    print("Function Size of File "+str(size)) 
    with open(file_name) as f:
        while content := f.read(size):
            yield content


if __name__ == '__main__':
  file_name_prev=""
  for i in range(0, len(file_row)): 
    file_name = file_row[i][file_path]
    
    d=file_row[i][d_c]
    n=file_row[i][n_c]
    #print(d)
    file_stats = os.stat(file_name)  
    t=file_stats.st_size 
    size=int(int(d)*t/int(n))
    #size=int(d)
    print(" main File Size in Bytes is "+str(size))    
    
    
    if file_name_prev!=file_row[i][file_path]:
     split_files = chunks(file_row[i][file_path], size)
     print("first "+" size "+str(size)+" "+str(split_files)) 
    else:
     size=size
     split_files = chunks(rest_file, size)
     print("second "+rest_file+" size "+str(size)+" "+str(split_files)) 
    
    flag=0
    for chunk in split_files:
       name, ext = os.path.splitext(file_name)
       if flag==0 :
        split_file_name=name+d+"_"+n+ext
        split_file_name=split_file_name.replace(" ", "")
        print(split_file_name) 
        f1 = open(split_file_name, "w+")
        print(flag)
        f1.write(chunk)
        f1.close()
        flag=1
       else:
        split_file_name=name+"_rest"+ext
        split_file_name=split_file_name.replace(" ", "")
        f2 = open(split_file_name, "w+")
        f2.write(chunk)
        print(flag)
        f2.close()
        rest_file=split_file_name
        rest_size=size
    file_name_prev=file_row[i][file_path]
    
    


  
