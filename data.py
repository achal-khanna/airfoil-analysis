import os
import csv
import pandas as pd

directory_path = 'Data'
df = pd.DataFrame(columns=['Thickness', 'Reynolds', 'Mach', 'alpha', 'CL', 'CD'])

for folder in sorted(os.listdir(directory_path)):
    folder_path = os.path.join(directory_path, folder)
    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)

        thickness = float(item[5:9])
        reynolds = float(item[15:19])
        mach = float(item[22:24])
        new_row2 = [thickness, reynolds, mach]

        with open(item_path, 'r') as file:
            reader = csv.reader(file)

            new_row1 = []
            for i in range(10):
                next(reader)
            for row in reader:
                if len(row) != 0: 
                    new_row1 = row[:3]
                    new_row1 = new_row2 + new_row1

                    df.loc[len(df)] = new_row1

df.to_csv('full.csv', index = False)



        
    
