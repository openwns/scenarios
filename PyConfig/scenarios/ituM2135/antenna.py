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

import rise.Antenna
import scenarios.antenna.isotropic
import scenarios.interfaces

class IndoorHotspotAntennaCreator(scenarios.antenna.IsotropicAntennaCreator):

    def __init__(self):
        scenarios.antenna.IsotropicAntennaCreator.__init__(self, [0.0, 0.0, 6.0])

    def create(self):
        antenna = scenarios.antenna.IsotropicAntennaCreator.create(self)
        return antenna

class UrbanMicroAntennaCreator(scenarios.interfaces.IAntennaCreator):

    def __init__(self, azimuth):
        self.azimuth = azimuth

    def create(self):
        # Downtilt 12 degrees (in rise up is 0 degree horizontal is 90 degree)
        downtilt = (12.0 + 90.0)/360.0 * 2 * 3.14159265

        antenna = rise.Antenna.ITU("17.0 dB", [0.0, 0.0, 10.0], self.azimuth, downtilt)
        antenna.drawAntennaPattern = False
        return antenna

class UrbanMacroAntennaCreator(scenarios.interfaces.IAntennaCreator):

    def __init__(self, azimuth):
        self.azimuth = azimuth

    def create(self):
        # Downtilt 12 degrees (in rise up is 0 degree horizontal is 90 degree)
        downtilt = (12.0 + 90.0)/360.0 * 2 * 3.14159265

        antenna = rise.Antenna.ITU("17.0 dB", [0.0, 0.0, 25.0], self.azimuth, downtilt)
        antenna.drawAntennaPattern = False
        return antenna

class RuralMacroAntennaCreator(scenarios.interfaces.IAntennaCreator):

    def __init__(self, azimuth):
        self.azimuth = azimuth

    def create(self):
        # Downtilt 12 degrees (in rise up is 0 degree horizontal is 90 degree)
        downtilt = (6.0 + 90.0)/360.0 * 2 * 3.14159265

        antenna = rise.Antenna.ITU("17.0 dB", [0.0, 0.0, 35.0], self.azimuth, downtilt)
        antenna.drawAntennaPattern = False
        return antenna

SuburbanMacroAntennaCreator = RuralMacroAntennaCreator
