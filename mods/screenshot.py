from PIL import ImageGrab
import io


class SCREENSHOT:

    SC_DATA = b""
    
    def __init__(self):
        self.generate()
    
    def generate(self):
        img = ImageGrab.grab()
        with io.BytesIO() as output:
            img.save(output, format='PNG')
            self.SC_DATA = output.getvalue()
    
    def get_data(self):
        return self.SC_DATA
