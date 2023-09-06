
import csv
import os


def process_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Initialize the new_data list with the header and add the 'NewColumn' header
    new_data = [data[0] + ['1']]

    # Process the data rows to add the new column values
    for i in range(1, len(data) - 1):
        prev_value = data[i-1][0]
        current_value = data[i][0]
        next_value = data[i+1][0]

        new_column_value = 0

        if current_value != prev_value :
            new_column_value = 1
        elif current_value == prev_value == next_value:
            new_column_value = 2
        else:
            new_column_value = 3

        new_row = data[i] + [new_column_value]
        new_data.append(new_row)

    # Add the last row with 'NewColumn' value as 3
    new_data.append(data[-1] + [3])
    

    # Write the new_data to the output CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_data)


def separate_file_name_and_path(file_path):
    file_name = os.path.basename(file_path)
    file_directory = os.path.dirname(file_path)
    return file_directory, file_name

def delete_files_except_one(directory, file_to_keep):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename != file_to_keep and os.path.isfile(file_path):
            os.remove(file_path)
            #print(f"Deleted file: {filename}")




def chunks(file_name, size):
    #print("Function Size of File "+str(size)) 
    with open(file_name, encoding='ISO 8859-1') as f:
        while content := f.read(size):
            yield content



def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None




if __name__ == '__main__':
  file_name_prev=""
  file_path = 0
  d_c=1
  n_c=2
  ########################## tag rows ####################################
  input_csv_file = 'data_splitter_script.csv'
  output_csv_file = "data_splitter_script_tagged.csv"
  f0 = open(output_csv_file, "w+")
  process_csv(input_csv_file, output_csv_file)
  ##############################################################
  f = open("data_splitter_script_tagged.csv", "r")
  file_row = list(csv.reader(f, delimiter=","))
  

  ##################### remove previous splitted files ############################
  for i in range(0, len(file_row)): 						  #
   directory_path=file_row[i][file_path]					  #
   file_directory, file_name = separate_file_name_and_path(directory_path)	  #
   delete_files_except_one(file_directory, file_name)				  #	
  #################################################################################

  j=1
  same_file=0
  for i in range(0, len(file_row)): 
    file_name = file_row[i][file_path]
    file_stats = os.stat(file_name)  
    t=file_stats.st_size 
    print(file_name+" main File Size in Bytes is "+str(t)) 
    name, ext = os.path.splitext(file_name)
    d=file_row[i][d_c]
    n=file_row[i][n_c]
 
    ################################# name of first chunk ##########################
    split_file_name1=name+d+"_"+n+ext
    split_file_name1=split_file_name1.replace(" ", "")
    f1 = open(split_file_name1, "a+")
    #################################################################################
    
    ############################### name of second chunk ############################
    split_file_name2=name+"_rest"+ext
    split_file_name2=split_file_name2.replace(" ", "")
    f2 = open(split_file_name2, "a+")
    #################################################################################

    
    #size=int(d)
      
    
    
    #if file_name_prev!=file_row[i][file_path]:
    if file_row[i][-1]=="1":
     size=int(int(d)*t/int(n))
     split_files = chunks(file_row[i][file_path], int(size))
     print(str(j)+"th chunk of "+file_name+" size :"+str(size)) 
    elif file_row[i][-1]=="2":
     size=int(int(d)*t/int(n))
     split_files = chunks(rest_file, size)
     print(str(j)+"th chunk of "+file_name+" size :"+str(size))
    else:
     split_files = chunks(rest_file, rest_size)
     print(str(j)+"th chunk of "+file_name+" size :"+str(rest_size))
    
    flag=0
    for chunk in split_files:
       
       if flag==0 :
        #print(flag)
        f1.write(chunk)
        #f1.close()
        flag=1
       else:
        f2.write(chunk)
        #print(flag)
        #f2.close()

    #rest_size=t-size
    j=j+1
    file_name_prev=file_row[i][file_path]
    f2.close()
    f1.close()
    rest_file=split_file_name2
    rest_size = get_file_size(rest_file)  
    print(rest_file)
    print("rest size is: "+str(rest_size))
    
    


  
