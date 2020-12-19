from PIL.ImageQt import ImageQt
from PIL import Image

class ImageParser():
    def __init__(self, size):
        self.images = [Image.new("RGBA", (1, 1)) for i in range(size)]

    def importImage(self, id, filename):
        self.images[id] = Image.open(filename)

    def resizeImage(self, id, width, height):
        self.images[id] = self.images[id].resize((width, height),
                                                 resample=Image.BICUBIC,
                                                 box=(0, 0, self.images[id].width, self.images[id].height))

    def qtImage(self, id):
        return ImageQt(self.images[id])
