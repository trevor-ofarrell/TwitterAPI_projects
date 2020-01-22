#!/usr/bin/python3
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df=pd.read_csv(r"/home/oem/twitterbot/twitter_analytics/tweet_activity_metrics_trevorthegnar_20191226_20200123_en.csv",encoding="latin-1")
comment_words = ' '
#stopwords = set(STOPWORDS)
print(vars(df))
print(df)
for val in df["Tweet text"]:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
for words in tokens:
    comment_words = comment_words + words + ' '

wordcloud=WordCloud(width=1000,height=1000, background_color='blue', min_font_size=10).generate(comment_words)

plt.figure(figsize=(9,9),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
