import math
from graph import LineGraph

gg = LineGraph()
gg.graph(color = "red", fun = "sin(x)", dict={"sin":math.sin}, intery=0.005, interx=0.02, height=1000, width= 1000, thk= 3, stx = 0.5,sty= -500)
