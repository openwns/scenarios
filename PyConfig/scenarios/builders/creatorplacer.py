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

    def __init__(self, bsCreator, bsPlacer, bsAntennaCreator, utCreator, utPlacer, channelmodelCreator):
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


        if openwns.simulator.getSimulator() is None:
            print "Creating new Simulator"
            newSimulator = openwns.simulator.OpenWNS()
            newSimulator.simulationModel = openwns.node.NodeSimulationModel()
            openwns.simulator.setSimulator(newSimulator)

        from ofdmaphy.OFDMAPhy import OFDMASystem

        ofdmaPhySystem = OFDMASystem('ofdma')
        openwns.simulator.getSimulator().modules.ofdmaPhy.systems.append(ofdmaPhySystem)

        self.bsCreator = bsCreator
        self.bsPlacer = bsPlacer
        self.bsAntennaCreator = bsAntennaCreator
        self.utCreator = utCreator
        self.utPlacer = utPlacer
        self.channelmodelCreator = channelmodelCreator

        self.bsNodes = []
        self.utNodes = []

        self._createBaseStations()
        self._createUserTerminals()

    def _createBaseStations(self):
        channelmodelConfigurations = self.channelmodelCreator.create()
        for antenna in self.bsAntennaCreator.create():

            self.bsPositions = self.bsPlacer.getPositions()

            ### Set isCenter to True for first BS sectors
            isCenter = True
            for currentPosition in self.bsPositions:
                bsNode = self.bsCreator.create()
                assert isinstance(bsNode, scenarios.interfaces.INode)
                bsNode.setProperty("isCenter", isCenter)
                bsNode.setPosition(currentPosition)
                bsNode.setAntenna(antenna)
                bsNode.setChannelModel(channelmodelConfigurations)
                openwns.simulator.getSimulator().simulationModel.nodes.append(bsNode)
                self.bsNodes.append(bsNode)

                ### Set isCenter to False for the following BS sectors
                if isCenter == True:
                    isCenter = False

    def _createUserTerminals(self):
        channelmodelConfigurations = self.channelmodelCreator.create()
        self.utPositions = []
        if self.utPlacer.perBS == True:
            for bs in self.bsNodes:
                # We only translate by the x,y coordinates. The height is not altered
                offset = openwns.geometry.position.Position(bs.getPosition().x, bs.getPosition().y, 0.0)
                self.utPlacer.setCenter(offset)
                for currentPosition in self.utPlacer.getPositions():
                    utNode = self.utCreator.create()
                    assert isinstance(utNode, scenarios.interfaces.INode)
                    utNode.setPosition(currentPosition)
                    utNode.setProperty("BS", bs)
                    self.utNodes.append(utNode)
        else:
            self.utPlacer.setCenter(self.bsPlacer.center)
            for currentPosition in self.utPlacer.getPositions():
                utNode = self.utCreator.create()
                assert isinstance(utNode, scenarios.interfaces.INode)
                utNode.setPosition(currentPosition)
                self.utNodes.append(utNode)

        self.utPlacer.setCenter(self.bsPositions[0])
        print "Position of first (center) BS is x: ", self.bsPositions[0].x," y: ", self.bsPositions[0].y
        for utNode in self.utNodes:
            utNode.setProperty("isCenter", self.utPlacer.isInside(currentPosition))
            utNode.setChannelModel(channelmodelConfigurations)
            openwns.simulator.getSimulator().simulationModel.nodes.append(utNode)

