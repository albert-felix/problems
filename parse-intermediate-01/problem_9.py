import os
import pandas as pd


folder = '/SVC_files'
result = folder+'/'+'result.xls'
writer = pd.ExcelWriter(result)

file_num = 1
sheet_num = 1

for filename in os.listdir(folder):
    if file_num ==1:
        firstFile = pd.read_fwf(folder+'/'+filename, skiprows=25, names=[0,1,2])
        firstFile[3] = firstFile[2].str.split(" ").str[-1]
        firstFile[2] = firstFile[2].str.split(" ").str[0]
        file_num += 1
    else:
        currentFile = pd.read_fwf(folder+'/'+filename, skiprows=25, names=[0,1,2])
        currentFile[3] = currentFile[2].str.split(" ").str[-1]
        currentFile[2] = currentFile[2].str.split(" ").str[0]
        firstFile = firstFile.append(currentFile,ignore_index=True)
        file_num += 1
    if file_num == 11:
        firstFile.to_excel(writer,sheet_name=f"sheet_{sheet_num}")
        sheet_num += 1
        file_num = 1
if file_num != 1:
    firstFile.to_excel(writer,sheet_name=f"sheet_{sheet_num}")
writer.save()
