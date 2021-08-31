import pandas as pd
import numpy as np

dfEm = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Empresas')
dfEn = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Entidades')
dfPol = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Politécnicos e Universidades')
dfMun = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Municipios')

dfEm["Localidade"] = dfEm["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfEn["Localidade"] = dfEn["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
#dfPol["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfMun["Localidade"] = dfMun["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

dfEm["Localidade"] = dfEm["Localidade"].str.lower()
dfEn["Localidade"]= dfEn["Localidade"].str.lower()
dfPol["Localidade"] = dfPol["Localidade"].str.lower()
dfMun["Localidade"] = dfMun["Localidade"].str.lower()

#Get File
dfloc = pd.read_csv("listamunicipios.csv")

#Selecionar e Renomear
dfloc = dfloc.iloc[:, [0, 2]]
headernames = ["Distrito", "Municipio"]
dfloc.columns = headernames

#Em string
dfloc.to_string()

##Normalizar e Lower
dfloc["Distrito"] = dfloc["Distrito"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfloc["Distrito"] = dfloc["Distrito"].str.lower()
dfloc["Municipio"] = dfloc["Municipio"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfloc["Municipio"] = dfloc["Municipio"].str.lower()


print("Len dfloc = " + str(len(dfloc["Municipio"])))
print("Len dfEm = " + str(len(dfEm["Localidade"])))
