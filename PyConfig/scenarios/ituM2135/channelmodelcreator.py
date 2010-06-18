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
import rise.scenario
import scenarios.channelmodel
import rise.scenario.Pathloss
from rise.scenario import Shadowing
from rise.scenario import FastFading

class IndoorHotspotChannelModelCreator(scenarios.channelmodel.ChannelModelCreator):
    
    def __init__(self):
        scenarios.channelmodel.ChannelModelCreator.__init__(self, rise.scenario.Pathloss.ITUInH(), Shadowing.No(), FastFading.No())

class UrbanMicroChannelModelCreator(scenarios.channelmodel.ChannelModelCreator):
    
    def __init__(self):
        scenarios.channelmodel.ChannelModelCreator.__init__(self, rise.scenario.Pathloss.ITUUMi(), Shadowing.No(), FastFading.No())

class UrbanMacroChannelModelCreator(scenarios.channelmodel.ChannelModelCreator):
    
    def __init__(self):
        scenarios.channelmodel.ChannelModelCreator.__init__(self, rise.scenario.Pathloss.ITUUMa(), Shadowing.No(), FastFading.No())

class RuralMacroChannelModelCreator(scenarios.channelmodel.ChannelModelCreator):
    
    def __init__(self):
        scenarios.channelmodel.ChannelModelCreator.__init__(self, rise.scenario.Pathloss.ITURMa(), Shadowing.No(), FastFading.No())

class SuburbanMacroChannelModelCreator(scenarios.channelmodel.ChannelModelCreator):
    
    def __init__(self):
        scenarios.channelmodel.ChannelModelCreator.__init__(self, rise.scenario.Pathloss.ITUSMa(), Shadowing.No(), FastFading.No())