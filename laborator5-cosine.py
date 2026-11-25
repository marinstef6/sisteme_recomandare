import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Citirea dataset-ului
df = pd.read_csv("laptop_price.csv", encoding="latin1")

print("Numar laptopuri:", len(df))
print("Coloane:", df.columns.tolist())
# Crearea descrierilor laptopurilor
columns = [
    "Company",
    "Product",
    "TypeName",
    "Inches",
    "ScreenResolution",
    "Cpu",
    "Ram",
    "Memory",
    "Gpu",
    "OpSys"
]

df["description"] = df[columns].astype(str).agg(" ".join, axis=1)

print("\nPrima descriere:")
print(df["description"].iloc[0])
# Preprocesarea descrierilor
df["description"] = df["description"].str.lower()
df["description"] = df["description"].str.replace(
    r"\s+", " ", regex=True
).str.strip()

print("\nDescriere dupa preprocesare:")
print(df["description"].iloc[0])
# Vectorizarea descrierilor
vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(df["description"])

print("\nDimensiune matrice TF-IDF:", tfidf_matrix.shape)
print("Numar termeni unici:", len(vectorizer.vocabulary_))
# Calcularea matricei de similaritate
similarity_matrix = cosine_similarity(tfidf_matrix)

print("\nDimensiune matrice Cosine Similarity:")
print(similarity_matrix.shape)

print("\nPrimele 5 randuri si 5 coloane:")
print(similarity_matrix[:5, :5])
# Identificarea laptopurilor similare
index = 0

scores = similarity_matrix[index]

# Sortarea scorurilor in ordine descrescatoare
sorted_indices = np.argsort(scores)[::-1]

print("\nLaptop de referinta:")
print(df["description"].iloc[index])

print("\nTop 5 laptopuri similare:")

count = 0

for i in sorted_indices:
    # Excludem laptopul comparat cu el insusi
    if i == index:
        continue

    print("\nLaptop:", df["Company"].iloc[i],
          df["Product"].iloc[i])

    print("ID:", df["laptop_ID"].iloc[i])
    print("Descriere:", df["description"].iloc[i])
    print("Cosine Similarity:", round(scores[i], 6))

    count += 1

    if count == 5:
        break
    
# Salvarea matricei de similaritate
similarity_df = pd.DataFrame(
    similarity_matrix,
    index=df["laptop_ID"],
    columns=df["laptop_ID"]
)

similarity_df.to_csv(
    "similarity_matrix.csv",
    float_format="%.6f"
)

print("\nMatricea de similaritate a fost salvata.")
