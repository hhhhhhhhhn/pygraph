from PIL import Image, ImageDraw


class ScatterPlot:
    def __init__(self, height=100, width=100, interx=1, intery=1, stx=0, sty=0):
        self.h = height
        self.w = width
        self.intx = interx
        self.inty = intery
        self.stx = stx
        self.sty = sty

    def create(self):
        try:
            self.img
        except:
            self.im = Image.new("RGB", (self.w, self.h), "white")
            self.img = self.im.load()

    def draw(self, scatter=[(50,50)], color="black", rad = 2):
        draw = ImageDraw.Draw(self.im)
        points = scatter
        count = 0
        print(scatter)
        for a in scatter:
            q = int(a[0])
            w = int(a[1])
            x = ((q - self.stx) * self.intx) + (self.intx / 2)
            y = ((w - self.sty) * self.inty) + (self.inty / 2)
            points[count] = (x,y)
            count = count + 1
        for l in points:
            print("Drawing point ", l[0], l[1])
            try:
                draw.ellipse((l[0] - rad, l[1] - rad, l[0] + rad, l[1] + rad), fill=color)
            except:
                pass


    def save(self, out="scatter.png", flip=True):
        if flip == False:
            final = self.im
        else:
            final = self.im.transpose(Image.FLIP_TOP_BOTTOM)
        final.save(out)

    def graph(self, scatter=[(50,50)], color="black", rad = 2, width = 100, height = 100, interx = 1, intery = 1, stx = 0, sty = 0, out = "scatter.png", flip = True):
        self.w = width
        self.h = height
        self.intx = interx
        self.inty = intery
        self.stx = stx
        self.sty = sty
        self.create()
        self.draw(scatter, color, rad)
        self.save(out, flip)
