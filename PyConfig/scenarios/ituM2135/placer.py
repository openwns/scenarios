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

class UrbanMacroBSPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self, numberOfCircles):
        self.placer = scenarios.placer.HexagonalPlacer(numberOfCircles, interSiteDistance = 500.0)

    def setCenter(self, position):
        self.placer.setCenter(position)

    def getPositions(self):
        return self.placer.getPositions()
