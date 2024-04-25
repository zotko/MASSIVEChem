
#importing packages
import matplotlib.pyplot as plt
import pandas as pd





# Lecture du fichier texte
with open('abundance.txt', 'r', encoding='ISO-8859-1') as file:
    # Sauter la première ligne
    next(file)
    lines = file.readlines()

# Initialisation des listes pour stocker les valeurs des colonnes
colonne1 = []
colonne2 = []
colonne3 = []


# Parcours des lignes et extraction des valeurs
for line in lines:
    values = line.split()  # Séparation des valeurs par espace

    # Vérifier si la ligne contient le nombre attendu de valeurs
    if len(values) >= 6:
        # Remplacement des virgules par des points pour les décimales et conversion en float
        colonne1.append(values[0])
        colonne2.append(float(values[1]))
        colonne3.append(float(values[2]))



data = {
    'Gauge Pressure [Bar]': colonne1,
    'Flow rate H2 [L/min]': colonne2,
    'Voltage [V]': pd.to_numeric(colonne3),
    'Current [A]': pd.to_numeric(colonne4),
    'Power [W]': colonne5,
    'Temp [°C]': colonne6
}

# Création du DataFrame
DF = pd.DataFrame(data2)