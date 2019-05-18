from PIL import Image, ImageDraw


class LineGraph:
    def __init__(self, width = 100, height = 100, interx = 1, intery = 1, stx = 0, sty = 0, thk = 3):
        self.w = width
        self.h = height
        self.intx = interx
        self.inty = intery
        self.stx = stx
        self.sty = sty
        self.thk = thk

    def create(self):
        try:
            self.img
        except:
            self.im = Image.new("RGB", (self.w, self.h), "white")
            self.img = self.im.load()

    def draw(self, op = "x", dic = {}, color = "black"):
        points = [None] * self.w
        draw = ImageDraw.Draw(self.im)
        for a in range(self.w):
            x = (a*self.intx) + self.stx
            dic.update({'x': x})
            b = eval(op, dic)
            y = round((b/self.inty) - self.sty)
            points[a] = (a, y)
        for l in points:
            try:
                draw.line((l, last), color, self.thk)
                print("drawing line", self.thk, last)
            except:
                pass
            last = l

    def save(self, out = "img.png", flip = True):
        if flip == False:
            final = self.im
        else:
            final = self.im.transpose(Image.FLIP_TOP_BOTTOM)
        final.save(out)

    def graph(self, fun = "x", dict = {}, color = "black", width = 100, height = 100, interx = 1, intery = 1, stx = 0, sty = 0, thk = 3, out = "img.png", flip = True):
        self.w = width
        self.h = height
        self.intx = interx
        self.inty = intery
        self.stx = stx
        self.sty = sty
        self.thk = thk
        self.create()
        self.draw(fun, dict, color)
        self.save(out, flip)