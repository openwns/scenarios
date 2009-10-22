import scenarios.interfaces
from hexagonal import HexagonalPlacer
from circular import CircularPlacer

class NonePlacer(scenarios.interfaces.INodePlacer):

    def __init__(self):
        pass

    def setCenter(self, center):
        pass

    def getPositions(self):
        return []
