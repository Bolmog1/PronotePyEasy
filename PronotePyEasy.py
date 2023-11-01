import datetime
import pronotepy


class Student:
    def __init__(self, client: pronotepy.Client):
        self.client = client

    def next_homework(self):
        """Renvoie le prochain devoirs.[Nom de la Matière (str)/ Description (str)/ deadline (date)/ Fait (bool)]"""
        homeworks = self.client.homework(datetime.date.today())
        last_homeworks = homeworks[0]
        return [last_homeworks.subject.name, last_homeworks.description, last_homeworks.date.replace(),
                last_homeworks.done]

    def homework(self, x: int = None):
        """Renvoie les x prochain devoirs.[Nom de la Matière (str)/ Description (str)/ deadline (date)/ Fait (bool)]"""
        homeworks = self.client.homework(datetime.date.today())
        if x is None:  # Garde fou, éviter les erreur.
            x = len(homeworks)
        elif type(x) is not None and x > len(homeworks):
            x = len(homeworks)
        result = homeworks[:x]
        return [[i.subject.name, i.description, i.date.replace(), i.done] for i in result]

    def average(self):
        """Renvoie la moyenne sur le trimestre (float) ou None si aucune note"""
        moyennes_notes = self.client.current_period.averages
        student_average = []
        for average in moyennes_notes:
            student_average.append(float(average.student.replace(',', '.')))  # Reformate les données
        global_average = None
        if len(student_average) > 0:  # Garde fou, évite division par 0
            global_average = round(sum(student_average) / len(student_average), 2)  # Calcul la moyenne
        return global_average

    def informations_polls(self, x: int = None):
        """Renvoie les X dernières informations et sondage [Titre (str)/ Auteur (str)/ Contenue(str)/ Date(date)/
        lu (bool)]"""
        infos = self.client.information_and_surveys()
        if x is None:  # Garde fou, évite les erreurs.
            x = len(infos)
        elif type(x) is not None and x > len(infos):
            x = len(infos)
        result = infos[:x]
        return [[i.title, i.author, i.content, i.creation_date, i.read] for i in result]

    def absences(self, x: int = None):
        """Renvoie les X dernières absence [Nombre d'heure (str)/ Raison (list[str])/ Justifié(bool)]"""
        absences = self.client.current_period.absences
        if x is None:  # Garde fou, évite les erreurs.
            x = len(absences)
        elif type(x) is not None and x > len(absences):
            x = len(absences)
        result = absences[:x]
        return [[a.hours, a.reasons, a.justified] for a in result]
