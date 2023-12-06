# Boucle de 1 à 3
for i in range(1, 4):
    # Créer le nom de la variable
    nom_variable = f"var{i}"
    
    # Définir la variable globale avec la valeur correspondante
    globals()[nom_variable] = i

print(var1)  # Affiche 1
print(var2)  # Affiche 2
print(var3)  # Affiche 3
