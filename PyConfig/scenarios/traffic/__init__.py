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

import openwns.simulator
import constanze.traffic
import scenarios.binding
class CBR:

    def __init__(self, offset, trafficRate, packetSize, loggerRetriever = lambda node: node.logger):
        self.offset = offset
        self.trafficRate = trafficRate
        self.packetSize = packetSize
        self.loggerRetriever = loggerRetriever

    def create(self, node):
        return constanze.traffic.CBR0(offset = self.offset,
                                      throughput = self.trafficRate,
                                      packetSize = self.packetSize,
                                      parentLogger = self.loggerRetriever(node))

class VoIP:

    def __init__(self, offset, loggerRetriever = lambda node: node.logger):
        self.offset = offset
        self.loggerRetriever = loggerRetriever

    def create(self, node):
        return constanze.traffic.VoIP(offset = self.offset,
                                      parentLogger = self.loggerRetriever(node))

def addTraffic(bindingCreator,loadCreator, direction="UL"):
    ueNodes = openwns.simulator.getSimulator().simulationModel.getNodesByType("UE")

    for ue in ueNodes:
        if direction=="UL":
            ue.addTraffic(bindingCreator.create(ue), loadCreator.create(ue))
        if direction == "DL":
            rang = openwns.simulator.getSimulator().simulationModel.getNodesByType("RANG")[0]

            rang.addTraffic(bindingCreator.createDL(ue), loadCreator.create(rang))
