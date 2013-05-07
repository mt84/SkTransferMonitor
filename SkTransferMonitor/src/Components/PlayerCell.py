'''
Created on Apr 30, 2013

@author: MT
'''
    
class PlayerCell(object):
    """Represent player shown on transfer list page."""
    def __init__(self, ID, skillStamina, skillPace, skillTechnique, skillPassing, skillKeeper, skillDefending, skillPlaymaking, skillScoring, endOfBidding, price):
        '''
        Constructor
        '''
        self._ID = ID
        self._skillStamina = skillStamina
        self._skillPace = skillPace
        self._skillTechnique = skillTechnique
        self._skillPassing = skillPassing
        self._skillKeeper = skillKeeper
        self._skillDefending = skillDefending
        self._skillPlaymaking = skillPlaymaking
        self._skillScoring = skillScoring
        self._endOfBidding = endOfBidding
        self._price = price
        
    @property
    def ID(self):
        return self._ID
    @property
    def skillStamina(self):
        return self._skillStamina
    @property
    def skillPace(self):
        return self._skillPace
    @property
    def skillTechnique(self):
        return self._skillTechnique
    @property
    def skillPassing(self):
        return self._skillPassing
    @property
    def skillKeeper(self):
        return self._skillKeeper
    @property
    def skillDefending(self):
        return self._skillDefending
    @property
    def skillPlaymaking(self):
        return self._skillPlaymaking
    @property
    def skillScoring(self):
        return self._skillScoring
    @property
    def endOfBidding(self):
        return self._endOfBidding
    @endOfBidding.setter
    def endOfBidding(self, value):
        self._endOfBidding = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value