from datetime import datetime
from json import load, dump

### ___ affichage dans la comsole simplifié ___ ###
class logs:
    """ affichage dans les logs """
    def __init__(self, Loader, Gravity, Text, ErrorCode=1):
        """ Loader, gravité, texte, code d'erreur si il y en a un """
        decalage_max_texte, LenSpace = 20, ""
        if len(Loader) + len(Gravity) < decalage_max_texte:
            Space = decalage_max_texte - (len(Loader) + len(Gravity))
            for i in range(Space):
                LenSpace += " "
        if Gravity == "FATAL" :
            LenSpace += "  "
            self._ErrorExit(ErrorCode, Text, LenSpace, Loader)
        else :
            self._log(Loader, Gravity, LenSpace, Text)

    def _log(self, Loader, Gravity, LenSpace, Text):
        print("[",str(datetime.now())[11:-7],"] [",Loader,"/",Gravity.upper(),"]",LenSpace," :",Text)


    def _ErrorExit(self, ErrorCode, ErrorText, LenSpace, Loader):
        exit(str("[ "+str(datetime.now())[11:-7]+" ] [ "+Loader+" / FATAL ]"+LenSpace+" : Code d'erreur "+str(ErrorCode)+" : "+ErrorText))




### ___ getion des fichiers ___ ###
class Json:
    """
    Class qui permet de sauvegarder et de charger des dictionnaires python avec la librairie json
    avec les fonctions "Read" et "Save"
    """
    def Read(file:str) -> dict or None:
        """
        chargement du fichier a ouvrir et retour sous forme de dictionnaire
        Si data renvoie data
        Sinon renvoie None
        """
        try:
            data = load(open(file, "r"))
            logs("JsonReader", "INFO", "Le fichier a été lu")
        except Exception as e:
            logs("JsonReader", "FATAL", "Le fichier n'a pas pu être lu : "+str(e), 2)
            return None
        return data

    def Save(data:dict, file:str) -> bool:
        """
        sauvegarde du dictionnaire dans le fichier donné
        Si sauvegardé renvoie True
        Sinon renvoie False
        """
        try:
            dump(data, open(file, "w"))
            logs("JsonReader", "INFO", "Le fichier a été enregistré")
        except Exception as e:
            logs("JsonReader", "FATAL", "Le fichier n'a pas pu être enregistré : "+str(e), 2)
            return False

        return True
