import pandas as pd
df = pd.read_csv("youtube/GBvideos.csv")

# ilk 10 kaydı yazdırma.
result = df.head(10)

# 5 ile 20 arasındaki kayıtların ilk 5 kaydı yazdır.
result = df[5:20].head(5)

# youtubede bulunan column isimleri ve sayısını yazdır.
result = df.columns
result = len(df.columns)

# 'comments_disabled', 'ratings_disabled' bu iki column bilgisini sildir.
df = df.drop(["comments_disabled", "ratings_disabled"], axis=1)
result = df

# Beğenme(like) ve beğenmeme(dislikes) sayılarının ortalaması bul.
result = df["likes"].mean()
result = df["dislikes"].mean()

# ilk 50 videonun like ve dislike kolunlarını yazdır.
result = df.head(50)[["likes", "dislikes"]]

# En çok görüntülenen video hangisdir?
result = df[df["views"].max() == df["views"]]

# En fazla görüntülenen ilk 5 video
result = df.sort_values("views", ascending=False).head(5)

# kategoriye göre beğeni ortalamalarını sırala yazdır.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# kategoriye göre yorum sayılarını yukarıdan aşağıya sıralama.
result = df.groupby("category_id").sum().sort_values(
    "comment_count", ascending=False)["comment_count"]

# kategoride kaç video var?
result = df["category_id"].value_counts()

print(result)


# En popüler videoları yazdır.

def enpopuler(youtube):
    likelist = list(youtube["likes"])
    dislilelist = list(youtube["dislikes"])
    print(likelist, dislilelist)


enpopuler(df)
