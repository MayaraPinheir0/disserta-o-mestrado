from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"palavras.csv", delimiter=';', encoding="utf-8")

comment_words = ""
stopwords = set(STOPWORDS)
for val, c in zip(df.keyword, df.freq):
    for i in range(c):
        if type(val) is str:
            comment_words += " " + val.lower() + " "

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="white",
    stopwords=stopwords,
    min_font_size=10,
    colormap="Blues",
).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
