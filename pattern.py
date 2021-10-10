import xml.etree.ElementTree as et

# Classes and methods for In Stitches are defined here
class Chart:
    # Contains a 2d array of ChartSquare
    def __init__(self, file=None, path=None):
        if file == None or path == None:
            new(25, 25, "ffffff")
        else:
            openOXS(file, path)

    # Set attribute functions
    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setCopyright(self, info):
        self.copyright = info

    def setInstructions(self, info):
        self.instructions = info

    def setStitchesPerInch(self, spi):
        self.stitchesPerInch = spi

    # Create a new array of ChartSquare and set attributes to a default
    def new(self, stitchesW, stitchesH, backgroundColor):
        self.width = stitchesW
        self.height = stitchesH
        self.backgroundColor = backgroundColor

        setTitle("untitled")
        setAuthor("")
        setCopyright("")
        setInstructions("")
        setStitchesPerInch("")

    # Open a .oxs XLM file given that file and its path
    def openOXS(self, file, path):
        self.file = file
        self.path = path

    # Write to an existing .oxs XML file or create a new one
    def save(self):
        pass

    # Add rows and/or columns of ChartSquare to the 2d array
    def addStitches(self, stitchesW, stitchesH):
        pass

    # Remove rows and/or columns of ChartSquare from the 2d array
    def removeStitches(self, stitchesW, stitchesH):
        pass

    # Change the chart's fabric color stored in backgroundColor
    def changeBackground(self, color):
        self.backgroundColor = color

class ChartSquare:
    # Initialize the GridSquare object, each GridSquare has a Stitch
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        # An exclusive or relation exists between stitch and partStitch
        self.stitch = None
        self.partStitch = None

        # Set border color dependent upon GridSquare object position
        if self.x % 10 == 0:
            self.borderR = "757575"
        else:
            self.borderR = "c9c9c9"
        if self.x % 10 == 1:
            self.borderL = "757575"
        else:
            self.borderL = "c9c9c9"
        if self.y % 10 == 0:
            self.borderT = "757575"
        else:
            self.borderT = "c9c9c9"
        if self.y % 10 == 1:
            self.borderB = "757575"
        else:
            self.borderB = "c9c9c9"

    # Create a new stitch in the ChartSquare
    def newStitch(self, color="", type=""):
        if color != "":
            if type == "half":
                self.stitch = Stitch(half=color)
            else:
                self.stitch = Stitch(full=color)

            # Inforce xor relationship
            if self.partStitch != None:
                removePartStitch()
                
    # Create a new part stitch in the ChartSquare
    def newPartStitch(self, color="", type=""):
        if color != "":
            if type == "qIV":
                self.partStitch = PartStitch(quadIV=color)
            elif type == "qIII":
                self.partStitch = PartStitch(quadIII=color)
            elif type == "qII":
                self.partStitch = PartStitch(quadII=color)
            else:
                self.partStitch = PartStitch(quadI=color)

            # Infore xor relationship
            if self.sitich != None:
                removeStitch()

    def removeStitch(self):
        self.stitch = None

    def removePartStitch(self):
        self.partStitch = None

class Stitch:
    # Sets color of ChartSquare and/or half stitches, if applicable
    def __init__(self, full="", half=""):
        self.full = full
        self.half = half

    def setFull(self, color):
        self.full = color

    def setHalf(self, color):
        self.half = color

    def getFull(self):
        return self.full

    def getHalf(self):
        return self.half

    def delFull(self):
        self.full = None

    def delHalf(self):
        self.half = None

class PartStitch:
    # Sets colors of a quartered ChartSquare, if applicable
    # _____________
    #| qII  | qI   | This box represents a chart square, subdivided
    #|      |      | into four quadrants. Only qI and qII are
    #|-------------| needed for the .oxs format of a part stitch.
    #| qIII | qIV  | In other .oxs software qI and qII correspond
    #|      |      | to right and left while qIII and qIV are ignored.
    #|-------------|
    def __init__(self, quadI="", quadII="", quadIII="", quadIV=""):
        self.quadI = quadI
        self.quadII = quadII
        self.quadIII = quadIII
        self.quadIV = quadIV

    def setQuadI(self, quad):
        self.quadI = quad

    def setQuadII(self, quad):
        self.quadII = quad

    def setQuadIII(self, quad):
        self.quadIII = quad

    def setQuadIV(self, quad):
        self.quadIV = quad

    def getQuadI(self):
        return self.quadI

    def getQuadII(self):
        return self.quadII

    def getQuadIII(self):
        return self.quadIII

    def getQuadIV(self):
        return self.quadIV

class LineStitch:
    # Sets a line segment and its color, if applicable
    def __init__(self, x1=None, x2=None, y1=None, y2=None, color=None):
        self.start = (x1, y1)
        self.end = (x2, y2)
        self.color = color

    def setColor(self, color):
        self.color = color

    def setStart(self, x, y):
        self.start = (x, y)

    def setEnd(self, x, y):
        self.end = (x, y)

    def getColor(self):
        return self.color

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

class Floss:
    # Kinds of floss that may be put into a palette
    def __init__(self):
        pass

class Palette(Floss):
    # Floss colors being used in chart
    def __init__(self, colors=[]):
        self.colors = colors
