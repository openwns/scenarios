import scenarios.interfaces
from hexagonal import HexagonalPlacer
from circular import CircularPlacer
from hexagonal import HexagonalAreaPlacer
from circular import CircularAreaPlacer
from rectangular import RectangularPlacer
from rectangular import RectangularAreaPlacer

class NonePlacer(scenarios.interfaces.INodePlacer):

    def __init__(self):
        pass

    def setCenter(self, center):
        pass

    def getPositions(self):
        return []
