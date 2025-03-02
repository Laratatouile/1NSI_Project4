import fonctions as fct
import carte
import affichage_console as aff_c



class fcts():
    def brut_decimal(donnee:float) -> float:
        """ transforme les données brutes de la trame en données utilisables en decimales"""
        return float(donnee[0:2]) + float(donnee[2:])/60







fct.logs("Main", "INFO", "Demarrage du programme")

trame = "$GNGGA,192459.000,4816.7752,N,00525.9807,E,1,20,0.68,323.9,M,47.7,M,,*7B"
fct.logs("Main", "INFO", f"la trame a traiter est : \"{trame}\"")


# affiche les informations dans la console
fct.logs("Main", "INFO", "Lancement du script de traitement de la trame GGA")
heure, latitude, longitude, precision_horizontale, altitude = aff_c.affiche_console(trame)
fct.logs("Main", "INFO", "Le script de traitement de la trame GGA c'est termine")

fct.logs("Main", "INFO", "Lancement du script de la creation de la carte avec les informations de la trame")
# cree la carte a afficher
latitude, longitude = fcts.brut_decimal(latitude), fcts.brut_decimal(longitude)

carte.cree_carte([latitude, longitude], [[1, [latitude, longitude], "slt"], [2, [latitude, longitude], precision_horizontale]])