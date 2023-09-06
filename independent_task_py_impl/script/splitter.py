import csv
import os

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


def split_file_by_sizes(input_file, directory, name, ext, output_prefix, split_sizes, d_list, n_list):
    with open(input_file, 'rb') as infile:
        for i, size in enumerate(split_sizes):
            data = infile.read(size)
            if not data:
                break
            output_file = f"{name}_{d_list[i]}_{n_list[i]}{ext}"
            with open(directory+"/"+output_file, 'wb') as outfile:
                outfile.write(data)



def store_rows_with_same_value(input_file, column_index, file_path):
    rows_by_value = {}

    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        #header = next(reader)  # Skip the header row
        for row in reader:
            value = row[column_index]
            ##################### remove previous splitted files ############################
            file_directory, file_name = separate_file_name_and_path(row[file_path])
            delete_files_except_one(file_directory, file_name)	
            #################################################################################
            if value not in rows_by_value:
                rows_by_value[value] = []
            rows_by_value[value].append(row)

    return rows_by_value

def extract_file_info(file_path):
    file_directory, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return file_directory, file_name, file_extension

#if __name__ == '__main__':
def Data_Splitter():
  file_name_prev=""
  file_path = 0
  d_c=1
  n_c=2
  
  
  
  input_csv_file = 'script/data_splitter_script.csv'
  column_index_to_check = 0  # Replace this with the index of the column you want to check

  result = store_rows_with_same_value(input_csv_file, column_index_to_check, file_path)

  # Print the rows with the same value in the specified column
  for value, rows in result.items():
    size_list = []
    d_list=[]
    n_list=[]
    #print(f"Rows with value '{value}':")
    for row in rows:
       d=row[d_c]
       n=row[n_c]
       file_stats = os.stat(row[file_path])  
       t=file_stats.st_size 
       size=int(int(d)*t/int(n))
       size_list.append(size)
       d_list.append(d.replace(" ", ""))
       n_list.append(n.replace(" ", ""))
    print(size_list)
    directory, name, ext = extract_file_info(row[file_path])
    #print(directory)
    #print(name)
    #print(ext)
    output_prefix = 'output_split'
    split_file_by_sizes(row[file_path], directory, name, ext, output_prefix, size_list, d_list, n_list)


