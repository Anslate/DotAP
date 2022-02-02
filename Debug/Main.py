#运行时会跳出一次未知命令,这是正常现象,是我偷懒在处理普通命令时没有跳过文件头,把文件头认为普通命令处理从而导致的未知
from PIL import Image,ImageDraw
image = []
image_draw = []

DotAP_file = open("./DotAP.txt", "r", encoding="utf-8")#读取文件
DotAP_file = DotAP_file.read()#还是读取
DotAP_list = DotAP_file.split("\n")#以换行进行分割

Header = DotAP_list[0].split(" ")#处理文件头
#根据 帧数，文件头 进行场景创建
for i in range(int(Header[0])):
    image.append(Image.new("L", (int(Header[1]),int(Header[2])), int(Header[3])))#创建场景
    image_draw.append(ImageDraw.Draw(image[i]))#转换为ImageDraw对象

class point:
    def __init__(self,start_frame,x,y,color):
        self.frame = start_frame-1#这个frame是待绘制的帧，此帧还没绘制！！！减1是因为计算机从0开始数而人类从1开始数
        self.x = x
        self.y = y
        self.color = color
    def still(self,frames):#frames是帧数，注意单复数
        for i in range(frames):
            image_draw[self.frame].point((self.x,self.y), self.color)
            self.frame += 1#绘制完成之后将待绘制帧移到下一位
    def move(self,x2,y2,step):
        pass

objects = {}
for command in DotAP_list:
    command = command.split(" ")
    if(command[0] == "create"):#由于Python不支持switch...case语句,于是用if...elif...else取代
        if(command[1] == "point"):
            objects[command[2]] = point(int(command[3]), int(command[4]), int(command[5]), int(command[6]))
        else:
            print("未知命令")
    else:
        if(command[1]=="still"):
            objects[command[0]].still(int(command[2]))
        else:
            print("未知命令")

for i in image:
    i.show()