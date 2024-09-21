import pandas as pd
import numpy as np

df = pd.read_csv("dadosmay.csv", delimiter=",", encoding="utf-8")



new_lines = []
visited = {}
keys = []
years = []
for i in range(len(df)):
    line = df.iloc[[i]]
    title = str(line["Title"].values[0])
    year = float(line["Year"].values[0])
    author = str(line["Authors"].values[0])
    if title in visited:
        continue
    if np.isnan(year):
        continue

    visited[title] = 1
    new_lines.append(line)
    print(year, title, author)
print(len(new_lines))



from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()



final_lines = []
i = 0

while i < len(new_lines):
    title = str(new_lines[i]["Title"].values[0])
    print(title)
    final_lines.append(new_lines[i])
    i = i + 1
    if i >= len(new_lines):
        break
    while similar(title, str(new_lines[i]["Title"].values[0])) > 0.7:
        i = i + 1
        if i >= len(new_lines):
            break
print(len(final_lines))


df_keys=list(df.keys())

final_df={k: [] for k in df_keys}
for l in final_lines:
    for k in df_keys:
        final_df[k].append(l[k].values[0])





pd.DataFrame(final_df).to_csv("rd_filtrado.csv", sep=",", encoding="utf-8", index=False)
