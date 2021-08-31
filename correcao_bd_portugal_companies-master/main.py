import pandas as pd
import numpy as np

dfEm = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Empresas')
dfEn = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Entidades')
dfPol = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Politécnicos e Universidades')
dfMun = pd.read_excel("Base_de_Dados_Empresas_Entidades.xlsx", sheet_name='Municipios')

# Retirar espaço em branco antes e depois das str
dfEm.Localidade = dfEm.Localidade.str.strip()
dfEn.columns = dfEn.columns.str.strip()
dfPol.columns = dfPol.columns.str.strip()
dfMun.columns = dfMun.columns.str.strip()

# Tirar NAN dos E-mails


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

# Passar listas para o DF original
dfEm["Distrito"] = dfEmDist
dfEm["Municipio"] = dfEmMun

# REMOVER NAN's no FINAL
print("Len dfloc = " + str(len(dfloc["Municipio"])))
print("Len dfEm = " + str(len(dfEm["Localidade"])))
