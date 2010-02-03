###############################################################################
# This file is part of openWNS (open Wireless Network Simulator)
# _____________________________________________________________________________
#
# Copyright (C) 2004-2007
# Chair of Communication Networks (ComNets)
# Kopernikusstr. 16, D-52074 Aachen, Germany
# phone: ++49-241-80-27910,
# fax: ++49-241-80-22242
# email: info@openwns.org
# www: http://www.openwns.org
# _____________________________________________________________________________
#
# openWNS is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation;
#
# openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import scenarios.interfaces
import scenarios.placer
import openwns.geometry.position

class IndoorHotspotBSPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self):
        self.center = openwns.geometry.position.Position(1000.0, 1000.0, 0.0)

    def setCenter(self, position):
        self.center = position

    def getPositions(self):
        leftStation = openwns.geometry.position.Position(-30.0, 0.0, 0.0)
        rightStation = openwns.geometry.position.Position(30.0, 0.0, 0.0)
        return [self.center + leftStation, self.center + rightStation]

class IndoorHotspotUEPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes
        self.placer = scenarios.placer.RectangularAreaPlacer(numberOfNodes, w=60.0, h=50.0)

    def setCenter(self, position):
        self.placer.setCenter(position)

    def getPositions(self):
        return self.placer.getPositions()



class UrbanMicroBSPlacer(scenarios.placer.HexagonalPlacer):

    def __init__(self, numberOfCircles):
        super(UrbanMicroBSPlacer,self).__init__(numberOfCircles, interSiteDistance = 200.0)


class UrbanMicroUEPlacer(scenarios.placer.HexagonalAreaPlacer):

    def __init__(self, numberOfNodes):
        super(UrbanMicroUEPlacer,self).__init__(numberOfNodes, interSiteDistance = 200.0)


class UrbanMacroBSPlacer(scenarios.placer.HexagonalPlacer):

    def __init__(self, numberOfCircles):
        super(UrbanMacroBSPlacer,self).__init__(numberOfCircles, interSiteDistance = 500.0)


class UrbanMacroUEPlacer(scenarios.placer.HexagonalAreaPlacer):

    def __init__(self, numberOfNodes):
        super(UrbanMacroUEPlacer,self).__init__(numberOfNodes, interSiteDistance = 500.0)


class RuralMacroBSPlacer(scenarios.placer.HexagonalPlacer):

    def __init__(self, numberOfCircles):
        super(RuralMacroBSPlacer,self).__init__(numberOfCircles, interSiteDistance = 1732.0)
        self.setCenter(openwns.geometry.position.Position(5000.0, 5000.0, 0.0))


class RuralMacroUEPlacer(scenarios.placer.HexagonalAreaPlacer):

    def __init__(self, numberOfNodes):
        super(RuralMacroUEPlacer,self).__init__(numberOfNodes, interSiteDistance = 1732.0)
        self.setCenter(openwns.geometry.position.Position(5000.0, 5000.0, 0.0))


class SuburbanMacroBSPlacer(scenarios.placer.HexagonalPlacer):

    def __init__(self, numberOfCircles):
        super(SuburbanMacroBSPlacer,self).__init__(numberOfCircles, interSiteDistance = 1299.0)
        self.setCenter(openwns.geometry.position.Position(5000.0, 5000.0, 0.0))


class SuburbanMacroUEPlacer(scenarios.placer.HexagonalAreaPlacer):

    def __init__(self, numberOfNodes):
        super(SuburbanMacroUEPlacer,self).__init__(numberOfNodes, interSiteDistance = 1299.0)
        self.setCenter(openwns.geometry.position.Position(5000.0, 5000.0, 0.0))
