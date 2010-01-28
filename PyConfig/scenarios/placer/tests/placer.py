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
import math
# WARNING: This is a statistic test. There is always a probability it could fail! We tolerate 10% error
# If you are sure everything is still OK: Increase "count"
class RectangularAreaPlacerTest(unittest.TestCase):

    count = 5E5

    def setUp(self):
        self.placer = scenarios.placer.RectangularAreaPlacer(int(self.count), 100, 100)
        
    def testMeanVar(self):
        pos = self.placer.getPositions()
        
        sum_x = 0
        sum_y = 0
        for p in pos:
          sum_x = sum_x + p.x
          sum_y = sum_y + p.y
          
        meanX = sum_x / self.count
        meanY = sum_y / self.count  
          
        #self.assertAlmostEqual(meanX, 0.0, 1)
        #self.assertAlmostEqual(meanY, 0.0, 1)
        assert(abs(meanX) < 1)
        assert(abs(meanY) < 1)

        sum_x2 = 0
        sum_y2 = 0
        for p in pos:
            sum_x2 = sum_x2 + (p.x - meanX) * (p.x - meanX)
            sum_y2 = sum_y2 + (p.y - meanY) * (p.y - meanY)
        
        varX = sum_x2 / (self.count - 1)
        varY = sum_y2 / (self.count - 1)

        #self.assertAlmostEqual(varX, 834.0, 4)
        #self.assertAlmostEqual(varY, 834.0, 1)
        assert(abs(varX- 834.0)<4)
        assert(abs(varY- 834.0)<4)



class HexagonalAreaPlacerTest(unittest.TestCase):

    count = 5E5

    def setUp(self):
        self.placer = scenarios.placer.HexagonalAreaPlacer(int(self.count), 100)
        
    def testMeanVar(self):
        pos = self.placer.getPositions()
        
        sum_x = 0
        sum_y = 0
        for p in pos:
          sum_x = sum_x + p.x
          sum_y = sum_y + p.y
          
        meanX = sum_x / self.count
        meanY = sum_y / self.count  
          
        assert(abs(meanX-1000.0) < 1)
        assert(abs(meanY-1000.0) < 1)

        sum_x2 = 0
        sum_y2 = 0
        for p in pos:
            sum_x2 = sum_x2 + (p.x - meanX) * (p.x - meanX)
            sum_y2 = sum_y2 + (p.y - meanY) * (p.y - meanY)
        
        varX = sum_x2 / (self.count - 1)
        varY = sum_y2 / (self.count - 1)

        assert(abs(varX- 694.0)<3)
        assert(abs(varY- 694.0)<3)
