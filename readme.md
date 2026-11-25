**Calculul Cosine Similarity**

Pentru acest laborator am utilizat dataset-ul laptop_price.csv, care contine 1303 de laptopuri.

Am creat campul description prin concatenarea caracteristicilor fiecarui laptop. Pentru preprocesarea textului am transformat literele in lowercase si am eliminat spatiile suplimentare si stopwords. Am pastrat numerele deoarece acestea reprezinta specificatii tehnice importante.

Am utilizat TfidfVectorizer pentru vectorizarea descrierilor si cosine_similarity pentru calcularea scorurilor de similaritate.

**Rezultate obtinute:**
- Numar laptopuri: 1303
- Numar termeni unici: 928
- Dimensiune matrice TF-IDF: 1303 x 928
- Dimensiune matrice Cosine Similarity: 1303 x 1303

**Exemplu de doua produse asemanatoare:**

Laptop 1 (ID: 1):
Apple MacBook Pro, 13.3 inch, Intel Core i5 2.3GHz, 8GB RAM, 128GB SSD, Intel Iris Plus Graphics 640, macOS.

Laptop 2 (ID: 16):
Apple MacBook Pro, 13.3 inch, Intel Core i5 2.3GHz, 8GB RAM, 256GB SSD, Intel Iris Plus Graphics 640, macOS.

Cosine Similarity: 0.981962

Scorul ridicat de similaritate este justificat deoarece cele doua laptopuri au aproape aceleasi caracteristici tehnice. Singura diferenta dintre descrierile acestora este capacitatea de stocare, primul laptop avand un SSD de 128GB, iar al doilea un SSD de 256GB.

Matricea de similaritate a fost salvata in fisierul similarity_matrix.csv.