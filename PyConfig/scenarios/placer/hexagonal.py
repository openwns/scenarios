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
import math,random

class HexagonalPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self, numberOfCircles, interSiteDistance, rotate = 0.0):
        """ 
        @type  numberOfCircles: int
        @param numberOfCircles: The number of circles around the center cell

        @type  interSiteDistance: float
        @param interSiteDistance: The cell interSiteDistance is in Meters [m]

        @type  rotate: float
        @param rotate: Rotate the final result by rotate in radiant [0..2pi]
        """
        assert numberOfCircles >= 0
        assert interSiteDistance > 0
        assert 0 <= rotate <= 2.0*math.pi # rotates the final result by corrAngle

        self.numberOfCircles = numberOfCircles
        self.interSiteDistance = interSiteDistance

        self.rotate = rotate

        self.center = openwns.geometry.position.Position(x = 1000.0, y = 1000.0, z = 0.0)

    def setCenter(self, center):
        self.center = center

    def _transformHexCoordinates(self, i, j, gridDistance):
        return openwns.geometry.position.Vector(math.sqrt(3)/2.0*j,float(i)+0.5*float(j), 0.0)*gridDistance

    def getPositions(self):
        centralBSPosition = openwns.geometry.position.Position(x = 0.0, y = 0.0, z = 0.0)
        posList = [centralBSPosition] # central BS position

        for circle in xrange(1, self.numberOfCircles +1): #  xrange(numberOfCircles)=0..numberOfCircles-1
            i=circle; j=0 # start vector
            di=-1
            dj=1 # delta vector
            for edge in xrange(6): # 0..5
                for way in xrange(circle):
                    v = self._transformHexCoordinates(i,j, self.interSiteDistance)
                    p = v.turn2D(self.rotate).toPosition()

                    posList.append(p)

                    i=i+di; j=j+dj

                # turn delta vector by 60 degrees right
                odi=di; odj=dj
                di=-odj
                dj=odi+odj

        return [pos + self.center for pos in posList]



def isInHexagon(position, radius, center, corrAngle = 0.0):
    """ returns true if position is located within hexagon boundaries.
        Can be used to correct random placement of UTs within circle!=hexagon
    """
    assert 0 <= corrAngle <= 2.0*math.pi   # rotates hexagon by corrAngle. 0=radius to the right, flat top
    #print "isInHexagon([%s],%d,[%s],%f) ?"%(position.toString(),radius,center.toString(),corrAngle)
    vector = (position-center)/radius      # from center to position; normalized
    length = vector.length2D()
    cos30deg = 0.86602540378443865         # =cos(30deg)=sin(60deg)
    if length>1.0:
        return False
    if length<cos30deg:
        return True
    angle  = vector.angle2D()-corrAngle    # 0=right; pi/2=up; pi=left; -pi/2=down
    angleReduced = angle % (math.pi/3.0)   # in [0..60deg]
    x = length*math.cos(angleReduced)
    y = length*math.sin(angleReduced)
    maxy = (1.0-x)*2.0*cos30deg
    isIn = (y<=maxy)
    #print "isInHexagon([%s],%d,[%s],%f): v=%s, l=%.3f a=%.3fdeg =>%s"%(position.toString(),radius,center.toString(),corrAngle,vector.toString(3),length,angleReduced*180/math.pi,isIn)
    return isIn

def createAreaScanMobility(steps, radius, minDistance, center, corrAngle):
    import rise.Mobility
    from scenarios.placer.circular import isInCircle
    mobility = None
    radius = radius * 2 / math.sqrt(3)
    xMin = center.x - radius
    yMin = center.y - radius

    stepSize = 2.0 * radius / float(steps)

    for x in xrange(steps + 1):
        for y in xrange(steps + 1):
            pos = openwns.geometry.position.Position(xMin + x * stepSize, yMin + y * stepSize, 0.0)
            if isInHexagon(pos, radius, center, corrAngle) and not isInCircle(pos, minDistance, center):
                if mobility is None:
                    mobility = rise.Mobility.EventList(pos)
                else:
                    mobility.addWaypoint(0.01 * (x+1) * (y+1), pos)
    return mobility
                
                
                
class HexagonalAreaPlacer(scenarios.interfaces.INodePlacer):

    def __init__(self, numberOfNodes, interSiteDistance, rotate = 0.0):
        """ 
        @type  numberOfCircles: int
        @param numberOfCircles: The number of circles around the center cell

        @type  interSiteDistance: float
        @param interSiteDistance: The cell interSiteDistance is in Meters [m]

        @type  rotate: float
        @param rotate: Rotate the final result by rotate in radiant [0..2pi]
        """
        assert numberOfNodes >= 0
        assert interSiteDistance > 0
        assert 0 <= rotate <= 2.0*math.pi # rotates the final result by corrAngle

        #self.numberOfCircles = numberOfCircles
        self.interSiteDistance = interSiteDistance
        self.numberOfNodes = numberOfNodes
        self.rotate = rotate

        self.center = openwns.geometry.position.Position(x = 1000.0 , y = 1000.0, z = 0.0)

    def setCenter(self, center):
        self.center = center

    def _transformHexCoordinates(self, i, j, gridDistance):
        return openwns.geometry.position.Vector(math.sqrt(3)/2.0*j,float(i)+0.5*float(j), 0.0)*gridDistance

    def getPositions(self):
        #centralBSPosition = openwns.geometry.position.Position(x = 0.0, y = 0.0, z = 0.0)
        #posList = [centralBSPosition] # central BS position

        positions = []
        #for s in xrange(self.numberOfNodes):
            #temp_angle = random.random() * math.pi/3.0;
            #i =  random.random() * self.interSiteDistance/(2.0 * math.cos(temp_angle - math.pi/6.0));
            #angle = float(int(random.random()*6.0)) * math.pi/3.0 + temp_angle;
            #v = openwns.geometry.position.Vector(x = i * math.cos(angle), y = i * math.sin(angle) , z = 0.0)
            #p = v.turn2D(self.rotate).toPosition()
            #positions.append(p)
        
        stationcounter = 0
        while stationcounter < self.numberOfNodes:
            x = random.random() * self.interSiteDistance * 2.0 / math.sqrt(3) - self.interSiteDistance / math.sqrt(3)
            y = random.random() * self.interSiteDistance * 2.0 / math.sqrt(3) - self.interSiteDistance / math.sqrt(3)
            ptemp =  openwns.geometry.position.Position(x=x, y=y, z=0.0)
            #print "position.x= %f, y=%f,interSiteDistance=%d",x,y,self.interSiteDistance
            if isInHexagon(position=ptemp, radius=self.interSiteDistance / math.sqrt(3), center=openwns.geometry.position.Position(0.0,0.0,0.0), corrAngle = self.rotate) == True:
                v = openwns.geometry.position.Vector(x = x, y = y , z = 0.0)
                p = v.turn2D(self.rotate).toPosition()
                positions.append(p)
                stationcounter=stationcounter +1
                
            else:
                pass



        return [pos + self.center for pos in positions]

