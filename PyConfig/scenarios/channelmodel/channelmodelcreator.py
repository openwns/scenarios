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
import rise.scenario.Propagation
from rise.scenario import Shadowing
from rise.scenario import FastFading

defaultPairs = [("AP","AP"),("AP","FRS"),("AP","UT"),
                   ("UT","UT"),("UT","FRS"),("UT","AP"),
                   ("FRS","FRS"),("FRS","AP"),("FRS","UT"),("DropIn","DropIn")]

class ChannelModelConfiguration():
    
    def __init__(self, transceiverPair, channelmodel):
        self.transceiverPair = transceiverPair
        self.channelmodel = channelmodel

class SingleChannelModelCreator(scenarios.interfaces.IChannelModelCreator):
    
    def __init__(self, transceiverPairs, pathloss = None, shadowing = Shadowing.No(), fastFading = FastFading.No()):
        self.transceiverPairs = transceiverPairs
        self.pathloss = pathloss
        self.shadowing = shadowing
        self.fastFading = fastFading
        
    def create(self):
        channelmodelConfigurations = []
        for pair in self.transceiverPairs:
            channelmodel = rise.scenario.Propagation.Configuration(self.pathloss, self.shadowing, self.fastFading)
            channelmodelConfiguration = ChannelModelConfiguration(pair, channelmodel)
            channelmodelConfigurations.append(channelmodelConfiguration)
        return channelmodelConfigurations


class PerPairChannelModelCreator(scenarios.interfaces.IChannelModelCreator):
    
    def __init__(self, channelmodelConfigurations):
        self.channelmodelConfigurations = channelmodelConfigurations
        
    def create(self):
        return self.channelmodelConfigurations

