# sisteme_recomandare-lab02

# Lab 02 – Recommender Systems

## Dataset

Pentru acest laborator am ales un dataset cu laptopuri de pe Kaggle.

Link: https://www.kaggle.com/datasets/muhammetvarl/laptop-price

Dataset-ul contine **1303 laptopuri** si informatii despre producator, model, procesor, RAM, stocare, placa video, sistem de operare si pret.

## Proprietati Recombee

Am definit urmatoarele proprietati in Recombee:

| Proprietate | Tip |
|---|---|
| Company | string |
| Product | string |
| TypeName | string |
| Inches | double |
| ScreenResolution | string |
| Cpu | string |
| Ram | string |
| Memory | string |
| Gpu | string |
| OpSys | string |
| Weight | string |
| Price_euros | double |

## Rezultat

Am folosit scriptul `recombee_properties.py` pentru a citi dataset-ul si a crea proprietatile in Recombee.

Toate cele 12 proprietati au fost adaugate cu succes. Produsele nu au fost inca incarcate in Recombee.
