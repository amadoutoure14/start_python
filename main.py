import datetime
class Agent:
    def __init__(self, nom, poste, heure):
        self.nom = nom
        self.poste = poste
        self.heure = heure

Agents = []

def create_agent():
    nom = input("Tapez votre nom complet : ")
    poste = input("Tapez votre poste : ")
    heure_actuelle = datetime.datetime.now()
    heure = heure_actuelle.strftime("%H:%M:%S")
    return nom, poste, heure

def get_current_time():
    heure_actuelle = datetime.datetime.now()
    année_actuelle = heure_actuelle.year
    mois_actuelle = heure_actuelle.month
    jour_en_cours = heure_actuelle.day
    heure_reference = datetime.datetime(year=année_actuelle, month=mois_actuelle, day=jour_en_cours, hour=7, minute=45, second=0)
    heure_ref = heure_reference.strftime("%H:%M:%S")

    while True:
        nom, poste, heure = create_agent()
        l_agent = Agent(nom, poste, heure)
        if l_agent.heure > heure_ref:
            print("Dommage vous êtes en retard")
        else:
            print("Félicitation, vous êtes à l\'heure continue ainsi!")
        Agents.append(l_agent)

        cont = input("Voulez-vous ajouter un autre agent ? (oui/non) : ")
        if cont.lower() == "oui":
            get_current_time()
        elif cont.lower() == "non":
            admin = input("Saisir l\'identifiant admin : ")
            mdp = input("Saisir le mot de passe : ")
            if admin.lower() == "admin" and mdp.lower() == "admin":
                break

    print("Liste des agents enregistrés :")
    for agent in Agents:
        print("************************************************************************************************")
        print("Nom :", agent.nom)
        print("Poste :", agent.poste)
        print("Heure :", agent.heure)
        print("************************************************************************************************")
get_current_time()
