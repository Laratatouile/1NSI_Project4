import fonctions as fct


def affiche_console(trame:int) -> tuple:
    """ affiche simplement dans la console les informations relative a la trame GGA en entree """
    fct.logs("AFF_c", "INFO", "Debut de la recherche d'informations de la trame")
    trame = trame.split(",")

    heure = trame[1]
    latitude = trame[2]
    longitude = trame[4]
    precision_horizontale = trame[8]
    type_positionnement = trame[6]
    altitude = trame[9]
    nombre_satelites = trame[7]
    fct.logs("AFF_c", "INFO", "Fin de la recherche d'informations sur la trame")
    fct.logs("AFF_c", "INFO", "debut de l'affichage des données de la trame GGA dans la console")
    fct.logs("AFF_c", "INFO", "")
    fct.logs("AFF_c", "INFO", "Informations sur la trame GGA :")
    fct.logs("AFF_c", "INFO", "")
    fct.logs("AFF_c", "INFO", f"heure -> {heure[0:2]}h, {heure[2:4]}m, {heure[4:6]}s, {heure[7:10]}ms")
    fct.logs("AFF_c", "INFO", f"latitude -> {latitude[0:2]}° {latitude[2:4]}' {float('0.'+latitude[5:])*60}\" N")
    fct.logs("AFF_c", "INFO", f"longitude -> {longitude[1:3]}° {longitude[3:5]}' {float('0.'+longitude[6:])*60}\" E")
    fct.logs("AFF_c", "INFO", f"type de positionnement -> {'GPS' if type_positionnement == '1' else 'inconnu'}")
    fct.logs("AFF_c", "INFO", f"nombre de satelites -> {nombre_satelites}")
    fct.logs("AFF_c", "INFO", f"précision horizontale -> {precision_horizontale}m")
    fct.logs("AFF_c", "INFO", f"altitude -> {altitude}m")
    fct.logs("AFF_c", "INFO", "")
    fct.logs("AFF_c", "INFO", "Fin de l'affichage des données de la trame GGA")

    return heure, latitude, longitude, precision_horizontale, altitude