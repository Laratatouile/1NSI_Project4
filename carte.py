import folium
import fonctions as fct


def cree_carte(localisation:list[float, float], dessins:list) -> None:
    """
    cree une carte avec la localisation et des objects:
    - La localisation est une liste avec la longitude et la latitude

    Pour les objects:
    - une liste des objects a placer

    Les objects en eux memes:
    - Le type de l'object
    - Une localisation sur la carte
    - Les parametres

    Les parametres:
    1 -> Un texte si l'object est un marqueur
    2 -> Un rayon float en metres pour les cercles
    """
    fct.logs("Carte", "INFO", "demarrage de la génération de la carte")
    try:
        fct.logs("Carte", "INFO", "Creation de la carte")
        carte = folium.Map(location=localisation)
        if dessins:
            for objects in dessins:
                if objects[0] == 2:
                    fct.logs("Carte", "INFO", f"Ajout d'un marqueur texte aux coordonees {objects[1]}")
                    folium.Circle(location=objects[1], radius=objects[2]).add_to(carte)
                elif objects[0] == 1:
                    fct.logs("Carte", "INFO", f"Ajout d'un marqueur cercle aux coordonees {objects[1]}")
                    folium.Marker(location=objects[1], popup=objects[2]).add_to(carte)
        fct.logs("Carte", "INFO", "Sauvegarde de la carte")
        carte.save("Ma carte.html")
        fct.logs("Carte", "INFO", "La carte a ete sauvegardee arret du module")
    except Exception as e:
        fct.logs("Carte", "ERROR", f"La carte n'a pas pu être générée Erreur : {e}")

    return None