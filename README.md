
# sisteme_recomandare-lab03
Am folosit scriptul recombee_items.py pentru a încărca cele 1303 laptopuri în Recombee, utilizând proprietățile definite la laboratorul 2.

Produsele au fost trimise în loturi de câte 100, folosind Batch și SetItemValues.
# sisteme_recomandare-lab02

## Dataset

Pentru acest laborator am ales un dataset cu laptopuri de pe Kaggle.

Link: https://www.kaggle.com/datasets/muhammetvarl/laptop-price

Dataset-ul contine **1303 laptopuri** si informatii despre producator, model, procesor, RAM, stocare, placa video, sistem de operare si pret.

## Proprietati Recombee

Am definit urmatoarele proprietati in Recombee:

| Proprietate | Tip | Descriere |
|---|---|---|
| Company | string | Producatorul laptopului |
| Product | string | Modelul laptopului |
| TypeName | string | Tipul laptopului (Notebook, Ultrabook etc.) |
| Inches | double | Dimensiunea ecranului in inch |
| ScreenResolution | string | Rezolutia ecranului |
| Cpu | string | Modelul procesorului |
| Ram | string | Capacitatea memoriei RAM |
| Memory | string | Tipul si capacitatea stocarii |
| Gpu | string | Modelul placii video |
| OpSys | string | Sistemul de operare |
| Weight | string | Greutatea laptopului |
| Price_euros | double | Pretul laptopului in euro |


## Rezultat

Am folosit scriptul `recombee_properties.py` pentru a citi dataset-ul si a crea proprietatile in Recombee.

Toate cele 12 proprietati au fost adaugate cu succes. Produsele nu au fost inca incarcate in Recombee.
