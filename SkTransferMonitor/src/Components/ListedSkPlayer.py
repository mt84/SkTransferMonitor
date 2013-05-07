'''
Created on Apr 28, 2013

@author: MT
'''
from ..Components.PlayerCell import PlayerCell

class ListedSkPlayer(PlayerCell):
    """Represent transfer-listed SK player."""

    def __init__(self, name, surname, countryID, age, height, weight, BMI, teamID, youthTeamID, value, wage, cards, goals, assists, matches, ntCards, ntGoals, ntAssists, ntMatches, injuryDays, national, skillForm, skillExperience, skillTeamwork, skillDiscipline, *args):
        '''
        Constructor
        '''
        super(ListedSkPlayer, self).__init__(*args)
        self._name = name
        self._surname = surname
        self._countryID = countryID
        self._age = age
        self._height = height
        self._weight = weight
        self._BMI = BMI
        self._teamID = teamID
        self._youthTeamID = youthTeamID
        self._value = value
        self._wage = wage
        self._cards = cards
        self._goals = goals
        self._assists = assists
        self._matches = matches
        self._ntCards = ntCards
        self._ntGoals = ntGoals
        self._ntAssists = ntAssists
        self._ntMatches = ntMatches
        self._injuryDays = injuryDays
        self._national = national
        self._skillForm = skillForm
        self._skillExperience = skillExperience
        self._skillTeamwork = skillTeamwork
        self._skillDiscipline = skillDiscipline
        
    @property
    def name(self):
        return self._name
    @property
    def surname(self):
        return self._surname
    @property
    def countryID(self):
        return self._countryID
    @property
    def age(self):
        return self._age
    @property
    def height(self):
        return self._height
    @property
    def weight(self):
        return self._weight
    @property
    def BMI(self):
        return self._BMI
    @property
    def teamID(self):
        return self._teamID
    @property
    def youthTeamID(self):
        return self._youthTeamID
    @property
    def value(self):
        return self._value
    @property
    def wage(self):
        return self._wage
    @property
    def cards(self):
        return self._cards
    @property
    def goals(self):
        return self._goals
    @property
    def assists(self):
        return self._assists
    @property
    def matches(self):
        return self._matches
    @property
    def ntCards(self):
        return self._ntCards
    @property
    def ntGoals(self):
        return self._ntGoals
    @property
    def ntAssists(self):
        return self._ntAssists
    @property
    def ntMatches(self):
        return self._ntMatches
    @property
    def injuryDays(self):
        return self._injuryDays
    @property
    def national(self):
        return self._national
    @property
    def skillForm(self):
        return self._skillForm
    @property
    def skillExperience(self):
        return self._skillExperience
    @property
    def skillTeamwork(self):
        return self._skillTeamwork
    @property
    def skillDiscipline(self):
        return self._skillDiscipline