#-*- coding:utf-8 -*-

from PIL import Image
import argparse

class ImageHandler(object):
    def __init__(self, src_image, output='output.txt'):
        im = Image.open(src_image)
        self.__src_image = im.resize((int(im.width/10),int(im.height/10)), Image.NEAREST)
        self.__ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.__output = output
    def get_char(self,r,g,b,alpha = 256):
        if alpha == 0:
            return ' '
        length = len(self.__ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1)/length
        return self.__ascii_char[int(gray/unit)]

    def output(self):
        txt = ""
        for i in range(self.__src_image.height):
            for j in range(self.__src_image.width):
                txt += self.get_char(*self.__src_image.getpixel((j,i)))
            txt += '\n'
        #字符画输出到文件
        with open(self.__output,'w') as f:
            f.write(txt)

def main(args):
    if args.output:
        im = ImageHandler(args.file, args.output)
    else:
        im = ImageHandler(args.file)
    im.output()
if __name__ == '__main__':
    #命令行输入参数处理
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='图片文件', action="store", required=True)     #输入文件
    parser.add_argument('-o', '--output', help='输出文件', action="store")   #输出文件

    #获取参数
    main(parser.parse_args())