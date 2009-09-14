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
import openwns.geometry.position
import math

class HexagonalPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self, numberOfCircles, radius, rotate = 0.0):
        """ 
        @type  numberOfCircles: int
        @param numberOfCircles: The number of circles around the center cell

        @type  radius: float
        @param radius: The cell radius is in Meters [m]

        @type  rotate: float
        @param rotate: Rotate the final result by rotate in radiant [0..2pi]
        """
        assert numberOfCircles >= 0
        assert radius > 0
        assert 0 <= rotate <= 2.0*math.pi # rotates the final result by corrAngle

        self.numberOfCircles = numberOfCircles
        self.radius = radius
        self.rotate = rotate

    def _transformHexCoordinates(self, i, j, gridDistance):
        return openwns.geometry.position.Vector(math.sqrt(3)/2.0*j,float(i)+0.5*float(j))*gridDistance

    def getPositions(self):
        center = openwns.geometry.position.Position(x = 0.0, y = 0.0, z = 0.0)
        posList = [center] # central BS position

        for circle in xrange(1, self.numberOfCircles +1): #  xrange(numberOfCircles)=0..numberOfCircles-1
            i=circle; j=0 # start vector
            di=-1
            dj=1 # delta vector
            for edge in xrange(6): # 0..5
                for way in xrange(circle):
                    v = self._transformHexCoordinates(i,j, self.radius)
                    p = v.turn2D(self.rotate).toPosition()

                    posList.append(p)

                    i=i+di; j=j+dj

                # turn delta vector by 60 degrees right
                odi=di; odj=dj
                di=-odj
                dj=odi+odj

        return posList
