import os

##  address
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(os.path.dirname(current_file_path))
data_dir_name = "src"
data_file_name = "items.csv"
data_file_dir = os.path.join(current_file_dir, data_dir_name)
data_file_path = os.path.join(data_file_dir, data_file_name)
