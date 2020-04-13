##
# Student: Jael Dubey & Robel Teklehaimanot
# Date   : 11.04.2020
# Title  : Lab 2 - Simple Cube
# File   : SimpleCube.py
##

import vtk

# Create the VTK datasets
points = vtk.vtkPoints()
polys = vtk.vtkCellArray()
scalars = vtk.vtkFloatArray()
cube = vtk.vtkPolyData()

# The coordinates for a cube centred in 0, 0, 0
x = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5),
     (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)]

# Points for cube with quadrilatere
pts = [(3, 2, 1, 0), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]

# Points for cube with triangle
# pts = [(3, 2, 0), (2, 1, 0), (4, 5, 7), (5, 6, 7), (0, 1, 4), (1, 5, 4), (1, 2, 5), (2, 6, 5), (2, 3, 6),
#               (3, 7, 6), (3, 0, 7), (0, 4, 7)]

# Points for cube with triangle strip
# pts = [(1, 0, 2, 3, 7, 0, 4, 1, 5, 2, 6, 7, 5, 4)]

for i in range(8):
    points.InsertPoint(i, x[i])
for i in range(len(pts)):
    polys.InsertNextCell(len(pts[i]), pts[i])
for i in range(8):
    scalars.InsertTuple1(i, i)

cube.SetPoints(points)

# Change if you make a cube with triangle strip
cube.SetPolys(polys)
#cube.SetStrips(polys)

cube.GetPointData().SetScalars(scalars)

# Write .vtk file
file = vtk.vtkPolyDataWriter()
file.SetInputData(cube)
file.SetFileName("cube.vtk")
file.Write()

# Read the file
reader = vtk.vtkPolyDataReader()
reader.SetFileName("cube.vtk")
reader.Update()

# Map the file
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetScalarRange(0, 7)
cubeMapper.SetInputConnection(reader.GetOutputPort())

# Create actor
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)

# Check the faces side
# cubeActor.GetProperty().BackfaceCullingOn()
# cubeActor.GetProperty().FrontfaceCullingOn()

# Create the Renderer and assign actors to it. A renderer is like a
# viewport. It is part or all of a window on the screen and it is responsible
# for drawing the actors it has.  We also set the background color here.
#
ren1 = vtk.vtkRenderer()
ren1.AddActor(cubeActor)
ren1.SetBackground(0.1, 0.1, 0.1)

#
# Finally we create the render window which will show up on the screen
# We put our renderer into the render window using AddRenderer. We also
# set the size to be 300 pixels by 300.
#
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

#
# The vtkRenderWindowInteractor class watches for events (e.g., keypress,
# mouse) in the vtkRenderWindow. These events are translated into
# event invocations that VTK understands (see VTK/Common/vtkCommand.h
# for all events that VTK processes). Then observers of these VTK
# events can process them as appropriate.
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#
# By default the vtkRenderWindowInteractor instantiates an instance
# of vtkInteractorStyle. vtkInteractorStyle translates a set of events
# it observes into operations on the camera, actors, and/or properties
# in the vtkRenderWindow associated with the vtkRenderWinodwInteractor.
# Here we specify a particular interactor style.
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

#
# Unlike the previous scripts where we performed some operations and then
# exited, here we leave an event loop running. The user can use the mouse
# and keyboard to perform the operations on the scene according to the
# current interaction style.
#

#
# Initialize and start the event loop. Once the render window appears, mouse
# in the window to move the camera. The Start() method executes an event
# loop which listens to user mouse and keyboard events. Note that keypress-e
# exits the event loop. (Look in vtkInteractorStyle.h for a summary of events, or
# the appropriate Doxygen documentation.)
#
iren.Initialize()
iren.Start()
