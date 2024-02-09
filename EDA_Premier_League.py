# Loading libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import matplotlib.pyplot as plt
import pandas as pd
import scipy as s
import seaborn as sns

# From the IPython.display package, import display and Markdown
from IPython.display import display, Markdown

from tkinter import filedialog
# Mostrar el diálogo para abrir un archivo.
filename = filedialog.askopenfilename()
# Imprimir la ruta del archivo seleccionado por el usuario.
print(filename)

Main_dir = r"E:\Data Science\Data Science Projects\04_Python_Interview_Test/"
os.chdir(Main_dir)
Folder_names = ['csv files','image files','text files']
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
EPL = pd.read_csv(filename)
os.chdir(Main_dir)

EPL.info()
EPL.head()

os.chdir(Folder_names[0])
EPL[['Season','Team','Pos','Pts','GF','GD','Qualification or relegation']].to_csv('EPL_Condensated.csv',index=False)
EPL_Condensed = EPL[['Season','Team','Pos','Pts','GF','GD','Qualification or relegation']]
os.chdir(Main_dir)

EPL['Qualified'] = EPL['Qualification or relegation'].str.split(expand=True).iloc[:,0]
EPL['Qualified'] = EPL['Qualified'].str.replace('Qualification','Yes').str.replace('Not','-')
A = EPL['Qualification or relegation'].str.split(expand=True).iloc[:,[3,4]]
EPL['Competition'] = A[3] + ' ' + A[4]
EPL['Competition'] = EPL['Competition'].fillna('-')
# B = EPL['Qualification or relegation'].str.split(expand=True).iloc[:,5:].fillna('')
# C = []
# for x in range(0,B.shape[0]):
#     for y in range(0,B.shape[1]):
#         C.append(B.iloc[x,y])
# EPL['Ranking']

EPL.drop('Qualification or relegation',axis=1,inplace=True)

def update_result(x):
    if 'Champions League' in x:
        x = 'Champions'
    elif 'Intertoto' in x or 'UEFA' in x:
        x = 'Europa'
    elif 'Football' in x:
        x = '2nd Division'
    else:
        x = '-'
    return x

EPL_Condensed = EPL_Condensed.rename(columns={'Qualification or relegation': 'Result'})
EPL_Condensed['Result'] = EPL_Condensed['Result'].apply(update_result)
print(EPL_Condensed['Result'].value_counts())

Champions_Qual = EPL_Condensed[EPL_Condensed['Result'] == 'Champions']
Champions_Qual = EPL_Condensed[EPL_Condensed.Result == 'Champions']

Champions_Qual_Stats = Champions_Qual\
                        .groupby('Season')\
                        .agg({'Pos':'max','Pts':'min','GD':'min'})
print(Champions_Qual_Stats)
Champions_Qual_Stats.describe()

UEFA_Qual = EPL_Condensed[EPL_Condensed['Result'] == 'Europa']
UEFA_Qual = EPL_Condensed[EPL_Condensed.Result == 'Europa']

UEFA_Qual_Stats = UEFA_Qual\
                  .groupby('Season')\
                  .agg({'Pos':'max','Pts':'min','GD':'min'})
print(UEFA_Qual_Stats)
UEFA_Qual_Stats.describe()

######### PLOTTING #########
EPL_winners = EPL_Condensed[EPL_Condensed['Pos'] == 1]
EPL_winners = EPL_winners.reset_index(drop=True)

relegation_zone = EPL_Condensed[EPL_Condensed['Pos'] == 18]
relegation_zone = relegation_zone.reset_index(drop=True)

plt.figure(figsize=(12,6))
sns.lineplot(x='Season', y='Pts', data=EPL_winners, marker='o', color='#38003c', label='winner')
sns.lineplot(x='Season', y='Pts', data=relegation_zone, marker='o', color='#e90052', label='relegation')
plt.xticks(rotation=90)
plt.title('Points of EPL Winners & Relegated Teams')
plt.xlabel('Season')
plt.ylabel('Points')
plt.show()

print(EPL_winners.Pts.sub(relegation_zone.Pts).mean())
print(EPL_winners.Pts.corr(relegation_zone.Pts))
# Correlación negativa signifca que cuando uno lo hace muy bien, el otro suele hacerlo mal.

team_counts = EPL_Condensed['Team'].value_counts()
team_counts = team_counts.reset_index()

euro_ids = EPL_Condensed['Result'].isin(['Europa','Champions League'])
euro_ids = EPL_Condensed.Result.isin(['Europa','Champions League'])
euro_year_counts = EPL_Condensed[euro_ids].Team.value_counts()
euro_year_counts = EPL_Condensed[euro_ids]['Team'].value_counts()
euro_year_counts = euro_year_counts.reset_index()

plt.figure(figsize=(12,6))
sns.barplot(team_counts,x='Team',y='count',color='#38003c')
plt.ylabel('Years in EPL')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(data=euro_year_counts,x='Team',y='count', color='#e90052', label='Years in Europe')
plt.ylabel('Years in European Competitions')
plt.xticks(rotation=90)
plt.yticks(range(0,23,1))
plt.show()

# ===================================================================
chelsea = EPL_Condensed[EPL_Condensed.Team == 'Chelsea']

# Set figure size
plt.figure(figsize=(12, 6))

ax = sns.lineplot(x='Season', y='GD', data=chelsea, label='Goal Diff.', marker='o')
ax2 = ax.twinx()
sns.lineplot(x='Season', y='Pts', data=chelsea, label='Points', ax=ax2, marker='o', color='green')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax.legend(lines + lines2, labels + labels2, loc='upper left')
ax2.get_legend().remove()
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title("Chelsea GD and Pts per season")
plt.show()
































