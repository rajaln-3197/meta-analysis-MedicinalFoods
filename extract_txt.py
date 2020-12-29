import csv
import pandas as pd
import os
herb_df = pd.read_csv('Medicinal Herb Articles.csv')

for i in range(0):
    abstract = herb_df.loc[i,'Abstract']
    os.chdir('D:\Grad\CSE 597 - 005\Project\Meta-Analysis_Research_Artciles-master\Data')
    if abstract:
        herb = herb_df.loc[i,'Herb']
        name = herb+'_'+str(i)+'.txt'
        g = open(name, "w", encoding='utf-8')
        g.write(str(abstract))
        g.close()

herbs = herb_df.loc[:,'Herb']

print(herbs.unique())
