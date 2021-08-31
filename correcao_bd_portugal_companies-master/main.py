import pandas as pd
import numpy as np

dfEm = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Empresas')
dfEn = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Entidades')
dfPol = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Politécnicos e Universidades')
dfMun = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Municipios')

# Remover Nan's
for x in dfEm.columns:
    x = str(x)
    dfEm[x] = dfEm[x].fillna("")

for x in dfEn.columns:
    x = str(x)
    dfEn[x] = dfEn[x].fillna("")

for x in dfMun.columns:
    x = str(x)
    dfMun[x] = dfMun[x].fillna("")

for x in dfPol.columns:
    x = str(x)
    dfPol[x] = dfPol[x].fillna("")

# Retirar espaço em branco antes e depois das str
for x in dfEm.columns:
    if dfEm[x].dtypes == str:
        x = str(x)
        dfEm[x] = dfEm[x].str.strip()
    if dfEm[x].dtypes == object:
        x = str(x)
        dfEm[x] = dfEm[x].astype(str).replace('\.0', '', regex=True)

for x in dfEn.columns:
    if dfEn[x].dtypes == str:
        x = str(x)
        dfEn[x] = dfEn[x].str.strip()
    if dfEn[x].dtypes == object:
        x = str(x)
        dfEn[x] = dfEn[x].astype(str).replace('\.0', '', regex=True)

for x in dfMun.columns:
    if dfMun[x].dtypes == str:
        x = str(x)
        dfMun[x] = dfMun[x].str.strip()
    if dfMun[x].dtypes == object:
        x = str(x)
        dfMun[x] = dfMun[x].astype(str).replace('\.0', '', regex=True)

for x in dfPol.columns:
    if dfPol[x].dtypes == str:
        x = str(x)
        dfPol[x] = dfPol[x].str.strip()
    if dfPol[x].dtypes == object:
        x = str(x)
        dfPol[x] = dfPol[x].astype(str).replace('\.0', '', regex=True)

# Normalizar e tirar acentos
dfEm["Localidade"] = dfEm["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfEn["Localidade"] = dfEn["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
# dfPol["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfMun["Localidade"] = dfMun["Localidade"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# Meter tudo em minúsculas
dfEm["Localidade"] = dfEm["Localidade"].str.lower()
dfEn["Localidade"] = dfEn["Localidade"].str.lower()
dfPol["Localidade"] = dfPol["Localidade"].str.lower()
dfMun["Localidade"] = dfMun["Localidade"].str.lower()

# Get File
dfloc = pd.read_csv("listamunicipios.csv")

# Selecionar e Renomear
dfloc = dfloc.iloc[:, [0, 2]]
headernames = ["Distrito", "Municipio"]
dfloc.columns = headernames

# Em string
dfloc.to_string()

##Normalizar e Lower
dfloc["Distrito"] = dfloc["Distrito"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfloc["Distrito"] = dfloc["Distrito"].str.lower()
dfloc["Municipio"] = dfloc["Municipio"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
dfloc["Municipio"] = dfloc["Municipio"].str.replace("-", " ")
dfloc["Municipio"] = dfloc["Municipio"].str.lower()

# Criar Listas para itenerar
dfEmMun = dfEm.Localidade.values.tolist()
dfEmDist = dfEm.Localidade.values.tolist()

dfEnMun = dfEn.Localidade.values.tolist()
dfEnDist = dfEn.Localidade.values.tolist()

dfPolMun = dfPol.Localidade.values.tolist()
dfPolDist = dfPol.Localidade.values.tolist()

dfMunDist = dfMun.Localidade.values.tolist()
dfMunMun = dfMun.Localidade.values.tolist()

dfloclist = dfloc.values.tolist()

# Corrigir uns valores da Lista de Municipios

for y in dfloclist:
    if y[1] == "lisbon":
        y[1] = "lisboa"

    if y[0] == "lisbon":
        y[0] = "lisboa"

    if y[1] == "azores":
        y[1] = "acores"

    if y[0] == "azores":
        y[0] = "acores"


# Funções
def pesquisa_municipios(x):
    for y in range(len(dfloclist)):

        if str(dfloclist[y][1]) in str(x):
            x = str(dfloclist[y][1])

    return x


def pesquisa_distrito(x):
    for y in range(len(dfloclist)):

        if str(dfloclist[y][1]) in str(x):
            x = str(dfloclist[y][0])

    return x


# ativar funções que procurar nomes de distritos e localidades dentro de listas
for x in range(len(dfEmMun)):
    dfEmMun[x] = pesquisa_municipios(dfEmMun[x])

for x in range(len(dfEmDist)):
    dfEmDist[x] = pesquisa_distrito(dfEmDist[x])

for x in range(len(dfEnMun)):
    dfEnMun[x] = pesquisa_municipios(dfEnMun[x])

for x in range(len(dfEnDist)):
    dfEnDist[x] = pesquisa_distrito(dfEnDist[x])

for x in range(len(dfPolMun)):
    dfPolMun[x] = pesquisa_municipios(dfPolMun[x])

for x in range(len(dfPolDist)):
    dfPolDist[x] = pesquisa_distrito(dfPolDist[x])

for x in range(len(dfMunMun)):
    dfMunMun[x] = pesquisa_municipios(dfMunMun[x])

for x in range(len(dfMunDist)):
    dfMunDist[x] = pesquisa_distrito(dfMunDist[x])

# Passar listas para o DF original
dfEm["Distrito"] = dfEmDist
dfEm["Municipio"] = dfEmMun

dfEn["Distrito"] = dfEnDist
dfEn["Municipio"] = dfEnMun

dfPol["Distrito"] = dfPolDist
dfPol["Municipio"] = dfPolMun

dfMun["Distrito"] = dfMunDist
dfMun["Municipio"] = dfMunMun

# Save Excels
dfEm.to_excel("dfEm.xlsx")
dfEn.to_excel("dfEn.xlsx")
dfMun.to_excel("dfMun.xlsx")
dfPol.to_excel("dfPol.xlsx")