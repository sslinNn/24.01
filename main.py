import pandas as pd
import numpy as np


# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

# ptd1 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_01.csv')
# ptd2 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_02.csv')
# ptd3 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_03.csv')
# ptd4 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_04.csv')
# ptd5 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_05.csv')
# ptd6 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_06.csv')
# ptd7 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_07.csv')
# ptd8 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_08.csv')
# ptd9 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_09.csv')
# ptd10 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_10.csv')
# ptd11 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_11.csv')
# ptd12 = pd.read_csv('C:/Users/slinm/Desktop/tatatata/datasets/part_12.csv')
#
#
# ptd1_9 = pd.concat([ptd1, ptd9], ignore_index=True)
# ptd2_11 = pd.concat([ptd2, ptd11], ignore_index=True)
# ptd3_8 = pd.concat([ptd3, ptd8], ignore_index=True)
# ptd4_7 = pd.concat([ptd4, ptd7], ignore_index=True)
# ptd5_12 = pd.concat([ptd5, ptd12], ignore_index=True)
# ptd6_10 = pd.concat([ptd6, ptd10], ignore_index=True)
#
# df1 = ptd1_9.merge(ptd2_11, left_on='ID', right_on='ID')
# df1 = df1.merge(ptd3_8, left_on='ID', right_on='ID')
# df1 = df1.merge(ptd4_7, left_on='ID', right_on='ID')
# df1 = df1.merge(ptd5_12, left_on='ID', right_on='ID')
# df1 = df1.merge(ptd6_10, left_on='ID', right_on='ID')
# df1 = df1.sort_values(by = 'ID')
# df1 = df1.drop_duplicates(keep= False)
#
# df1.to_csv('dataframe')


df=pd.read_csv('dataframe')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# dfInfo = df.info(verbose=True) # Команда, которая поможет вам выявить, какие же поля являются текстовыми.
# print(df.APP_CAR.unique()) # Команда, позволяющая посмотреть список уникальных значений в столбце
# array([nan, 'PRIVATE', 'STATE'], dtype=object)
# list(df.APP_COMP_TYPE.unique()) # Она же, только представленная в виде списка.
# df5.APP_COMP_TYPE.replace('state','гос',inplace=True) #Команда, которая позволяет заменить значения в столбце на другие значения

#2
for i in range(116):
    if df.iloc[:, i].dtypes == object:
        df.iloc[:, i] = df.iloc[:, i].str.lower()
        print(list(df.iloc[:, i].unique()))
# #3
# d = 0
# for i in range(116):
#     if df.iloc[:, i].dtypes == object:
#         if df.iloc[:, i].name != 'CLNT_JOB_POSITION':
#             d += 1
#             df.iloc[:, i].replace('mother', 'мать', inplace=True)
#             df.iloc[:, i].replace('brother', 'брат', inplace=True)
#             df.iloc[:, i].replace('friend', 'друг', inplace=True)
#             df.iloc[:, i].replace('sister', 'сестра', inplace=True)
#             df.iloc[:, i].replace('daughter', 'дочь', inplace=True)
#             df.iloc[:, i].replace('son', 'сын', inplace=True)
#             df.iloc[:, i].replace('father', 'отец', inplace=True)
#             # print(d, ' - ', list(df.iloc[:, i].unique()))
#
# #4
# for i in range(116):
#     if df.iloc[:, i].dtypes == object:
#         df.iloc[:, i].replace(' ', np.NaN, inplace=True)
#         # print(list(df.iloc[:, i].unique()))
#
# #5
# for i in range(116):
#     if df.iloc[:, i].dtypes == object:
#         if df.iloc[:, i].name != 'PACK':
#             try:
#                 df.iloc[:, i] = df.iloc[:, i].astype(float)
#             except ValueError:
#                 pass
#
#
# #6


