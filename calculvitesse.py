def calcul_vitesse_en_metre_par_seconde_unefois(distance,temps):
    return (distance/temps)


def calcul_temps_en_seconde(fps,nbframe):
    return (nbframe/fps)


def calcul_vitesse_en_metre_par_seconde_moyenne(distance,fps,nbframes):
    vitesses = []
    for i in nbframes:
        temps = calcul_temps_en_seconde(fps,i)
        vitesses.append(calcul_vitesse_en_metre_par_seconde_unefois(distance,temps))
    return (sum(vitesses)/len(vitesses))


def calcul_vitesse_en_metre_par_seconde_max(distance,fps,nbframes):
    vitesses = []
    for i in nbframes:
        temps = calcul_temps_en_seconde(fps,i)
        vitesses.append(calcul_vitesse_en_metre_par_seconde_unefois(distance,temps))
    return (max(vitesses))
