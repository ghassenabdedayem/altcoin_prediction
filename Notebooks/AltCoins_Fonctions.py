#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

def Create_Df_Test(df, val_pred, val_exp, nb_day):
    df2 = pd.DataFrame()
    df2['Date'] = df['GOLD_Time']
    
    # On récupère les colonnes à prédire
    for col_pred in val_pred:
        df2[col_pred] = df[col_pred]
    
    # Pour chacune des colonnes indicatives, on va récupérer les n-nb_day valeurs
    for col_exp in val_exp:
        for ii in range(nb_day):
            nb_col = ii+1
            new_col = col_exp + '_' + str(nb_col)
            df2[new_col] = 0.0
            for jj in range(len(df)):
                if ((jj+ii+1) >= len(df)):
                    df2[new_col].values[jj] = 'Nan'
                else:
                    df2[new_col].values[jj] = df[col_exp].values[jj+ii+1]
        
    return df2



def Create_Df_Test_dec(df, val_pred, val_exp, nb_day, nb_decal):
    df2 = pd.DataFrame()
    df2['Date'] = df['GOLD_Time']
    
    # On récupère les colonnes à prédire
    for col_pred in val_pred:
        df2[col_pred] = df[col_pred]
    
    # Pour chacune des colonnes indicatives, on va récupérer les n-nb_day valeurs
    for col_exp in val_exp:
        for ii in range(nb_decal-1, nb_day):
            nb_col = ii+1
            new_col = col_exp + '_' + str(nb_col)
            df2[new_col] = 0.0
            for jj in range(len(df)):
                if ((jj+ii+1) >= len(df)):
                    df2[new_col].values[jj] = 'Nan'
                else:
                    df2[new_col].values[jj] = df[col_exp].values[jj+ii+1]
        
    return df2


# Creation d'un DataFrame à l'aide d'une liste de colonnes existantes
def Creation_Df_From_ListCol(df, liste_col):
    df2 = pd.DataFrame()
    
    df2['Date'] = df['GOLD_Time']
    for col in liste_col:
        df2[col] = df[col]
        
    return df2



# Creation d'un DataFrame à l'aide d'une liste de trigrammes (récupère toutes les colonnes associées au trigramme)
def Creation_Df_From_ListTrigramme(df, liste_tri):
    df2 = pd.DataFrame()
    
    df2['Date'] = df['GOLD_Time']
    for col in liste_tri:
        for col_ref in df.columns:
            if (col == col_ref[:len(col)]):
                df2[col_ref] = df[col_ref]
        
    return df2


# Fonction pour extraire des données dans le dataset entre 2 dates
def extraction_part_dataset(df, date_debut, date_fin):
    df2 = df[(df['GOLD_Time'] >= date_debut) & (df['GOLD_Time'] <= date_fin)]
    return df2

