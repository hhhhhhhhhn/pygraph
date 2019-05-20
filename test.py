import math
from graph import LineGraph
from scatter import ScatterPlot

gg = LineGraph()
gg.graph(color = "red", fun = "sin(x)", dict={"sin":math.sin}, intery=0.005, interx=0.02, height=1000, width= 1000, thk= 3, stx = 0,sty= -1.5)
gg.graph(color = "blue", fun = "sin(x)", dict={"sin":math.sin}, intery=0.005, interx=0.02, height=1000, width= 1000, thk= 3, stx = 3.14,sty= -1.5)
gg.graph(color = "black", fun = "sin(x)", dict={"sin":math.sin}, intery=0.005, interx=0.02, height=1000, width= 1000, thk= 3, stx = 6.28,sty= -1.5)


ss = ScatterPlot()
ss.graph(interx=10, intery=10, height= 1000, width= 1000,scatter=[(3,5),(50,30),(5,3)], color = "blue", rad= 10)
ss.graph(interx=10, intery=10, height= 1000, width= 1000,scatter=[(20,50),(20,100),(70,32)], color = "red", rad= 10)
