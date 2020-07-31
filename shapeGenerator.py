import maya.cmds as cmds

global sphereCountField
global sphereRadiusField


global cubeW
global cubeH
global cubeD
global cubeCount

# Takes the user input to set Cube dimensions.
def cubeFunction(args):
    w = cmds.floatField(cubeW, query=True, value=True)
    h = cmds.floatField(cubeH, query=True, value=True)
    d = cmds.floatField(cubeD, query=True, value=True)

# Takes the input for the number of Cubes to be created.
    numCubes = cmds.intField(cubeCount, query=True, value=True)

# Spaces out the Cubes on the Y-axis.
    for i in range(numCubes):

        cmds.polyCube(width=w, height=h, depth=d)
        cmds.move(0, 0, (i * h * 1.1))





# Creates a generic Wall prefab.
def wallFunction(args):
    cmds.polyCube(width = '1in', height = '8in', depth = '1ft')    



# Takes the user input to set Sphere radius, number of Spheres to be created, and space them out along the X-axis.
def sphereFunction(*args):
    global sphereCountField
    global sphereRadiusField

    numSpheres = cmds.intField(sphereCountField, query=True, value=True)
    myRadius = cmds.floatField(sphereRadiusField, query=True, value=True)

    for i in range(numSpheres):
        cmds.polySphere(radius=myRadius)
        cmds.move((i * myRadius * 2.2), 0, 0)




# Tabs created to help seperate each category.
class TabExample:

    def __init__(self):

        global sphereCountField
        global sphereRadiusField


        global cubeW
        global cubeH
        global cubeD
        global cubeCount



        self.win = cmds.window(title="Shape Generator", widthHeight=(500, 200))
        self.tabs = cmds.tabLayout()

        # Tab #1 with button and input layout for Cube
        firstTab = cmds.columnLayout()
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[firstTab, 'Cube'])

        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Width:")
        cubeW = cmds.floatField(minValue=.1)
        cmds.setParent("..")

        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Height:")
        cubeH = cmds.floatField(minValue=.1)
        cmds.setParent("..")

        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Depth:")
        cubeD = cmds.floatField(minValue=.1)
        cmds.setParent("..")

        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="How many Cubes would you like to create?:")
        cubeCount = cmds.intField(minValue=1)
        cmds.setParent("..")



        cmds.button(label="Make Cube", command=cubeFunction)
        cmds.setParent("..")

        # Tab #2 with button and input layout for Sphere
        newLayout = cmds.scrollLayout()
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[newLayout, 'Sphere'])
        cmds.columnLayout()


        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="How many Spheres would you like to create?")
        sphereCountField = cmds.intField(minValue=1)
        cmds.setParent("..")

        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="With a radius of:")
        sphereRadiusField = cmds.floatField(minValue=0.5)
        cmds.setParent("..")

        cmds.button(label="Make Spheres", command=sphereFunction)
        cmds.setParent("..")
        cmds.setParent("..")


        newLayout = cmds.scrollLayout()
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[newLayout, 'Wall'])
        cmds.columnLayout()

        # Tab #3 for creating a premade wall.
        cmds.button(label="Make a Wall", command=wallFunction)
        cmds.setParent("..")
        cmds.setParent("..")

        cmds.showWindow(self.win)

TabExample()
