from PIL import Image

class Parse():

    def __init__(self, path, width=160, height=40):
        self._path = path
        self._width = width
        self._height = height
        self._text = ""

    def to_ascii_char(self, r, g, b):
        """ 将 RGB 转为灰度值，并且返回该灰度值对应的字符标记 """
        # 存储用于显示图片的字符种类。list 的最后一个元素是空格，表示将使用空格来代替原图片中灰度值最高的像素点
        # （在灰度图像中，灰度值最高为 255，代表白色，最低为 0，代表黑色）。
        ascii_char = list(r"$kB%8&WM#*oa&**@qwmZO0QLCJUYXzcvun<rjft/\|()1{}[]?-_+~<>i!lI;:,\ ^`'. ")
        # RGB 转为灰度值计算公式
        gray = int((19595 * r + 38469 * g + 7474 * b) >> 16)
        # ascii_char 中的一个字符所能表示的灰度值区间
        unit = 256.0 / len(ascii_char)
        return ascii_char[int(gray / unit)]

    def output(self):
        """ 输出结果 """
        image = Image.open(self._path)
        image = image.resize((self._width, self._height), Image.NEAREST)
        for h in range(self._height):
            for w in range(self._width):
                # [:3]表示取前三个值 R G B
                self._text += self.to_ascii_char(*image.getpixel((w, h))[:3])
            self._text += '\n'
        return self._text

    def save(self):
        """ 保存文件到本地 """
        with open("parse.txt", 'w') as f:
            f.write(self._text)

if __name__ == "__main__":
    parse = Parse("images\we.jpg")
    print("\n>> 你会挽着我的衣袖 我会把手揣进裤兜")
    print(parse.output())
