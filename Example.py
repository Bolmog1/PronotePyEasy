import pronotepy
import PronotePyEasy

etab = 'https://demo.index-education.net/pronote/eleve.html'  # Etablissement fictif de démonstration créer par PRONOTE
client = pronotepy.Client(etab,
                          username='demonstration',
                          password='pronotevs')

eleve = PronotePyEasy.Student(client)  # Connexion et récupération des données via les internets

print(eleve.next_homework())  # Renvoie le prochain devoir
print(eleve.homework())  # Renvoie tous les prochains devoir
print(eleve.homework(3))  # Renvoie les 3 prochains devoir (dans la limites des prochains devoirs)
print(eleve.average())  # Renvoie la moyenne général
print(eleve.informations_polls(83))  # Renvoie les 83 dernières informations/sondages (dans la limites des infos etc...)
print(eleve.absences())  # Renvoie toutes les dernières absences
print(eleve.grades())  # Renvoie toutes les dernières notes
