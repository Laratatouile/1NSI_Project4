import folium
import fonctions as fct


def cree_carte(localisation:list[longitude:float, latitude:float], dessins:list[objects:list[chose:int, position:list[longitude:float, latitude:float], param:float or str]]=None) -> None:
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
        carte = folium.map(location=localisation)
        if dessins:
            for objects in dessins:
                if objects[0] == 1:
                   folium.Circle(location=object[1], radius=objects[2]).add_to(carte)
                elif objects[0] == 2:
                    folium.Marker(location=objects[1], popup=objects[2]).add_to(carte)
    except Exception as e:
        fct.logs("Carte", "ERROR", f"La carte n'a pas pu être générée Erreur : {e}")

    return None