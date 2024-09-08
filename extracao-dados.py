import pandas as pd
df = pd.read_csv("tabela_verdade.csv", delimiter=";")
columns = [
    "palavras-chaves",
    "jornal/editora",
    "pais dos autores",
    "instituição dos autores",
    "autores",
    "ano",
]
for column in columns:
    W = set()
    count = {}

    for _kws in df[column]:
        if type(_kws) is int:
            kws = _kws
        else:
            kws = _kws.replace(",", ".")

        for w in kws.split(".") if type(kws) is str else [kws]:
            k = w if type(w) is int else w.strip()

            if k in count.keys():
                count[k] = count[k] + 1
            else:
                count[k] = 1
            W.add(k)
    count = dict(sorted(count.items(), key=lambda item: -item[1]))

    ks = [k for k in count.keys()]
    c = [count[k] for k in count.keys()]

    r = pd.DataFrame({column: ks, "ocorrencias": c})
    r.to_csv(f"ranking_{column.replace('/','_')}.csv")
