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

import openwns.simulator
import openwns.node

class CreatorPlacerBuilder(object):
    """
    A scenario that consists of a single cell and an arbitrary number of user
    terminals
    """

    def __init__(self, bsCreator, bsPlacer, utCreator, utPlacer):
        """
        Initialize the scenario

        @type  bsCreator: scenarios.interfaces.INodeCreator
        @param bsCreator: The creation strategy for the base station
        @type  bsPlacer: scenarios.interfaces.INodeCPlacer
        @param bsPlacer: The placement strategy for the base stations
        @type  utCreator: scenarios.interfaces.INodeCreator
        @param utCreator: The creation strategy for the user terminals
        @type  utPlacer: scenarios.interfaces.INodeCPlacer
        @param utPlacer: The placement strategy for the user terminals
        """

        assert isinstance(bsCreator, scenarios.interfaces.INodeCreator)
        assert isinstance(bsPlacer, scenarios.interfaces.INodePlacer)
        assert isinstance(utCreator, scenarios.interfaces.INodeCreator)
        assert isinstance(utPlacer, scenarios.interfaces.INodePlacer)

        newSimulator = openwns.simulator.OpenWNS()
        newSimulator.simulationModel = openwns.node.NodeSimulationModel()
        openwns.simulator.setSimulator(newSimulator)

        self.bsCreator = bsCreator
        self.bsPlacer = bsPlacer
        self.utCreator = utCreator
        self.utPlacer = utPlacer

        self.bsNodes = []
        self.utNodes = []

        self._createBaseStations()
        self._createUserTerminals()

    def _createBaseStations(self):
        self.bsPositions = self.bsPlacer.getPositions()

        for currentPosition in self.bsPositions:
            bsNode = self.bsCreator.create()
            assert isinstance(bsNode, scenarios.interfaces.INode)
            bsNode.setPosition(currentPosition)
            openwns.simulator.getSimulator().simulationModel.nodes.append(bsNode)
            self.bsNodes.append(bsNode)

    def _createUserTerminals(self):
        self.utPositions = []
        for bsPosition in self.bsPositions:
            self.utPlacer.setCenter(bsPosition)
            self.utPositions += self.utPlacer.getPositions()

        for currentPosition in self.utPositions:
            utNode = self.utCreator.create()
            assert isinstance(utNode, scenarios.interfaces.INode)
            utNode.setPosition(currentPosition)
            openwns.simulator.getSimulator().simulationModel.nodes.append(utNode)
            self.utNodes.append(utNode)
