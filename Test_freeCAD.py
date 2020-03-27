FREECADPATH = r"C:\Program Files\FreeCAD 0.18\bin"
FREECADPATHLIB = r"C:\Program Files\FreeCAD 0.18\lib"
import sys
import sys
sys.path.append(FREECADPATH)

try:
    import FreeCAD
except ValueError:
    print("test")



sys.path.append(FREECADPATHLIB)

try:
    from Sketcher import *
    from Part import *
except ValueError:
    print("test")



