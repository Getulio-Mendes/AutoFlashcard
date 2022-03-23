import pandas as pd
import dicParse
import genDeck

with open("./Word List/Mandarin-Wiktionary.html",'r',encoding="utf-8") as file:
    dfs = pd.read_html(file.read())

df = pd.concat(dfs)
df.drop(columns=['Traditional', 0,1,2],inplace=True)
df.dropna(inplace=True)

# Query dictionary and place the definiton on the row
for x in df.index:
    definiton = dicParse.getDicDef(df.at[x,"Simplified"])
    df.at[x,"Meaning"] = definiton

genDeck.generatePkg(df)
