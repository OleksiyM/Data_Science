import os
import zipfile
import pandas as pd
import shutil

filename = 'data/homework.zip'

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall('')
print(f'zipfile {filename} extracted')

df_list = []

for dir_name in os.listdir('data'):
    if not os.path.isdir(f'data/{dir_name}'):
        continue
    else:
        print(f'Working with dir: {dir_name}')
        for file_name in os.listdir(f'data/{dir_name}'):
            if file_name.endswith('.csv'):
                df_csv = pd.read_csv(f'data/{dir_name}/{file_name}')
                df_csv['action'] = dir_name
                df_list.append(df_csv)
        shutil.rmtree(f'data/{dir_name}')

# os.rmdir('data') # remove the directory in Colab
df = pd.concat(df_list, ignore_index=True)
# df.to_csv('df.csv', index=False) # save the df to a csv file in Colab
df.to_csv('data/df.csv', index=False)
print('df created and saved to df.csv')

