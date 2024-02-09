# Loading libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

Main_dir = r"E:\Data Science\Data Science Projects\04_Python_Interview_Test/"
os.chdir(Main_dir)

Folder_names = ['csv files','image files','text files']
for x in range(0,len(Folder_names)):
    if not os.path.exists(Main_dir + Folder_names[x]):
        # os.makedirs(Main_dir + Folder_names[x])
        os.makedirs(Folder_names[x])

File_names_main = os.listdir(Main_dir)
for file in File_names_main:
    if ".csv" in file and not os.path.exists("csv files/"+file):
        shutil.move(file,"csv files/"+file)
    if ".jpg" in file and not os.path.exists("image files/"+file):
        shutil.move(file,"image files/"+file)
    if ".txt" in file and not os.path.exists("text files/"+file):
        shutil.move(file,"text files/"+file)

os.chdir(Folder_names[0])
Current_folder = os.getcwd()
print("Current folder: ",Current_folder)

File_names = os.listdir(Current_folder)
audible_uncleaned = "" # To remove the false erros in the script

for filenames in File_names:
    # print(filenames)
    # print(os.path.join(Current_folder,filenames))
    Delimiter = filenames.find('.')
    Name_var = filenames[:Delimiter]

    Load_ans = input(f"Do you want to load this file? [y/n]\n{filenames}\n")
    if Load_ans == 'y':
        Sentence = Name_var + " = pd.read_csv(filenames)"
        exec(Sentence)
    elif Load_ans == 'n':
        continue

audible_uncleaned.info()
audible_uncleaned.head()

# cadena = '["Hola","buenos","dias"]'
# lista = eval(cadena)
# import ast
# lista = ast.literal_eval(cadena)
# frase = " ".join(lista)
# cadena = str(lista)

# for dirname, _, filenames in os.walk(Current_folder):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

os.chdir(Main_dir)

# Cleaning data to better understanding
audible_uncleaned['author'] = audible_uncleaned['author'].str.replace('Writtenby:','')
audible_uncleaned['narrator'] = audible_uncleaned['narrator'].str.replace('Narratedby:','')

audible_uncleaned['stars'].sample()
audible_uncleaned['stars'].unique()

Not_rate = audible_uncleaned.query("stars == 'Not rated yet'")
audible_uncleaned.stars.value_counts()

audible_uncleaned['stars'] = audible_uncleaned['stars'].str.replace('Not rated yet','NaN')

# audible_uncleaned['n_rating'] = audible_uncleaned['stars'].str.extract('([0-1000]*)')
# audible_uncleaned['stars'].str.slice(0,9)
# audible_uncleaned['stars'].str.replace('out of 5 stars','').str.replace('ratings','')

audible_uncleaned['rating_stars'] = audible_uncleaned['stars'].str.split(expand=True)\
                                    .iloc[:,0].astype(float)
audible_uncleaned['n_rating'] = audible_uncleaned['stars'].str.split(expand=True)\
                                .iloc[:,4].str.replace('stars','').str.replace(',','').astype(float)
audible_uncleaned['n_rating'].max()

audible_uncleaned.drop('stars',axis=1,inplace=True)

audible_uncleaned['price'] = audible_uncleaned['price'].str.replace('Free','0')\
                            .str.replace(',','').astype(float)
audible_uncleaned['rating_stars'].unique()
audible_uncleaned['rating_stars'] = audible_uncleaned['rating_stars'].astype("category")
audible_uncleaned['releasedate'] = pd.to_datetime(audible_uncleaned['releasedate'])

audible_uncleaned['time'] = audible_uncleaned['time'].str.replace('hrs','hr')\
                            .str.replace('mins','min').str.replace('Less than 1 minute','1 min')
audible_uncleaned['hours'] = audible_uncleaned['time'].str.split(expand=True)\
                            .iloc[:,0].astype(int)
audible_uncleaned['mins'] = audible_uncleaned['time'].str.split(expand=True)\
                            .iloc[:,3].fillna(0).astype(int)
audible_uncleaned.drop('time',axis=1,inplace=True)

audible_uncleaned['time_mins'] = audible_uncleaned['hours']*60 + audible_uncleaned['mins']

audible_uncleaned['price'].describe()
audible_uncleaned['rating_stars'].describe()
audible_uncleaned['n_rating'].describe()
audible_uncleaned['time_mins'].describe()

audible_uncleaned.describe(exclude=[np.number])

audible_uncleaned['price'] = audible_uncleaned['price']*0.012

# audible_uncleaned['language'].map(lambda x: x.lower())
audible_uncleaned['language'] = audible_uncleaned['language'].str.lower()

audible_uncleaned['name'].duplicated().sum()
subset_cols = audible_uncleaned[['releasedate','name','author','narrator','time_mins','price']]
subset_cols.info()
subset_cols.duplicated()
subset_cols.drop_duplicates(keep='last')

audible_uncleaned.isna().sum()

os.chdir(Folder_names[0])
audible_uncleaned.to_csv('File_Cleaned.csv',index=False)
os.chdir(Main_dir)

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,4,5,6]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
df.loc['G1'].loc[1]
df.index.names = ['Grupo','Número']

# EJEMPLOS ÚTILES EN DATAFRAMES (PANDAS):
ecom[ecom['Job'] == 'Lawyer'].index
len(ecom[ecom['Job'] == 'Lawyer'].index)
ecom[ecom['Job'] == 'Lawyer'].count()
ecom[ecom['Job'] == 'Lawyer'].value_counts()
ecom[ecom['Job'] == 'Lawyer'].unique()
ecom[ecom['Job'] == 'Lawyer'].nunique()
ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25').count()
ecom['Email'].split('@')[1]
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts()













