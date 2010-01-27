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

import scenarios.placer
import unittest

# WARNING: This is a statistic test. There is always a probability it could fail! We tolerate 10% error
# If you are sure everything is still OK: Increase "count"
class RectangularAreaPlacerTest(unittest.TestCase):

    count = 5E5

    def setUp(self):
        self.placer = scenarios.placer.RectangularAreaPlacer(int(self.count), 10, 10)
        
    def testMeanVar(self):
        pos = self.placer.getPositions()
        
        sum_x = 0
        sum_y = 0
        for p in pos:
          sum_x = sum_x + p.x
          sum_y = sum_y + p.y
          
        meanX = sum_x / self.count
        meanY = sum_y / self.count  
          
        self.assertAlmostEqual(meanX, 0.0, 1)
        self.assertAlmostEqual(meanY, 0.0, 1)
          