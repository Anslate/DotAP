#运行时会跳出一次未知命令,这是正常现象,是我偷懒在处理普通命令时没有跳过文件头,把文件头认为普通命令处理从而导致的未知
from re import S
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
    image_draw.append(ImageDraw.Draw(image[i]))#转换为ImageDraw对象,存储在image_draw列表中,每一项为1帧

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
    def move(self,step,x2,y2):
        x_step=(x2-self.x)/step#每帧移动步长
        y_step=(y2-self.y)/step
        for i in range(1,step+1,1):#人从1开始数
            image_draw[self.frame].point((self.x+x_step*i,self.y+y_step*i),self.color)
            self.frame += 1#绘制完成之后将待绘制帧移到下一位
        self.x = x2#移动完毕后将点坐标重新赋值
        self.y = y2

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
        elif(command[1]=="move"):
            objects[command[0]].move(int(command[2]),int(command[3]),int(command[4]))
        else:
            print("未知命令")

for i in image:
    i.show()