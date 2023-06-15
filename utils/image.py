from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class ImageMan:
    def __init__(self, file_object: object) -> None:
        self._img = Image.open(file_object)
        self.file_path = f'./images/{file_object.name}'
        self._draw = ImageDraw.Draw(self._img)
        self.set_font()
    
    # TODO: デコレーター対応
    # def decorator_chk_font(self, func, *args, **kwargs):
    #     def _wrapper(*args, **kwargs):
    #         if self._font is None:
    #             self.set_font()
    #         func(*args, **kwargs)
    #     return _wrapper

    def save_img_file(self):
        self.img.save(self.file_path)

    def set_font(self, font_path='./fonts/Helvetica 400.ttf', size=50):
        self._font = ImageFont.truetype(font=font_path, size=size)

    @property
    def img(self):
        return self._img
    
    @property
    def draw(self):
        return self._draw
    
    @property
    def font(self):
        return self._font
    
    def get_textsize(self, caption: str):        
        w, h = self.draw.textsize(caption, font=self.font)
        return w, h

    def draw_rectangle(self, x: int, y: int, w: int, h: int, 
                       fill: str=None, outline: str=None, width: int=1):
        self.draw.rectangle([(x, y), (x+w, y+h)], 
                            fill=fill, outline=outline, width=width)

    def draw_text(self, x: int, y: int, caption: str, fill: str='white'):
        self.draw.text((x, y), caption, fill=fill, font=self.font)

