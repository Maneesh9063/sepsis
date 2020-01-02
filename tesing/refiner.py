import pandas as pd

fields =[]
rows =[]
filename= "d:/Sepsis/tesing" #'''"d:/Sepsis/tesing/merged.csv" '''
 

df1 = pd.read_csv(filename+"/1.psv",sep='|')
df2 = pd.read_csv(filename+"/2.psv",sep='|')
df3 = pd.read_csv(filename+"/3.psv",sep='|')
df4 = pd.read_csv(filename+"/4.psv",sep='|')
df5 = pd.read_csv(filename+"/5.psv",sep='|')
df6 = pd.read_csv(filename+"/6.psv",sep='|')
df7 = pd.read_csv(filename+"/7.psv",sep='|')
df8 = pd.read_csv(filename+"/8.psv",sep='|')
df9 = pd.read_csv(filename+"/9.psv",sep='|')


final_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9])

final_df = final_df[['SepsisLabel','HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN', 'Alkalinephos', 'Calcium', 
'Chloride', 'Creatinine', 'Bilirubin_direct', 'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium', 'Bilirubin_total', 'TroponinI', 'Hct', 'Hgb', 'PTT', 'WBC', 'Fibrinogen', 'Platelets', 'Age', 'Gender', 'Unit1', 'Unit2', 'HospAdmTime', 'ICULOS' ]]

print(final_df.head())

pd.DataFrame.to_csv(final_df, 'd:/Sepsis/tesing/merged.csv', sep=',', index=False)





# df = pd.read_csv(filename)
# print(df.isna().sum())
# print(df["SepsisLabel"].value_counts())
# print(df.dtypes)
