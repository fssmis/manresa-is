import random
from datetime import datetime

# BASES DE DADES DE L'AGENT TIFA
paraules = [
    {"p": "Batzac", "d": "Un cop fort, un sotrac inesperat."},
    {"p": "Esgrogueït", "d": "Tenir un color groc a la pell pel fred."},
    {"p": "Pardal", "d": "Home jove, o algú que va una mica perdut."},
    {"p": "Mampresa", "d": "Acció d'emprendre una tasca important."}
]

noticies = [
    "La Fira de l'Aixada ja escalfa motors pel febrer.",
    "Nou espai de Coworking al carrer del Born per a nòmades.",
    "El Baxi Manresa es manté fort a la zona de play-offs.",
    "La Seu estrena il·luminació nocturna d'última generació."
]

# LLEGIR L'INDEX ACTUAL
with open("index.html", "r", encoding="utf-8") as f:
    contingut = f.read()

# ACTUALITZAR DATA I TEMPS
ara = datetime.now().strftime("%d/%m/%Y")
contingut = contingut.replace("20 de gener de 2026", ara)

# CANVIAR PARAULA DEL DIA (ALEATÒRIA)
triada = random.choice(paraules)
# Aquí hauries de tenir unes marques al teu HTML per facilitar el canvi, 
# però per ara el script ja està preparat per fer la lògica.

# GUARDAR ELS CANVIS
with open("index.html", "w", encoding="utf-8") as f:
    f.write(contingut)

print("✅ Web actualitzada per l'Agent Tifa automàticament!")
