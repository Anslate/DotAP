from PIL import Image,ImageDraw
if(__name__ == "__main__"):
    DotAP_text = open("./Debug/DotAP.txt","r")
    DotAP_text = DotAP_text.read()
    DotAP_command = DotAP_text.split("\n")
    header = DotAP_command[0].split(" ")
    Images = []
    ImagesD = []
    #头转为int
    for i in range(3):
        header[i] = int(header[i])
    #背景颜色
    backgcolor = header[3].split(",")
    for i in range(3):#背景颜色转为int
        backgcolor[i] = int(backgcolor[i])
    #创建Image对象
    for i in range(header[0]):
        Images.append(Image.new("RGB",(header[1],header[2]),tuple(backgcolor)))
        ImagesD.append(ImageDraw.Draw(Images[i],"RGB"))

    class basic():
        def __init__(self,position,fill_color,outline_color,width):
            #将坐标转为二维数组
            position=position.split(",")
            self.position=[]
            for i in range(0,len(position),2):
                self.position.append([int(position[i]),int(position[i+1])])
            #填充颜色的转换
            self.fill_color=[]
            fill_color=fill_color.split(",")
            for i in fill_color:
                self.fill_color.append(int(i))
            #轮廓颜色转换
            self.outline_color=[]
            outline_color=outline_color.split(",")
            for i in outline_color:
                self.outline_color.append(int(i))
            #线宽
            self.width = int(width)
        def show(self,startf,stopf):
            #坐标改元组
            position = []
            for i in self.position:
                position.append(tuple(i))
            #颜色改元组
            fill_color = tuple(self.fill_color)
            outline_color = tuple(self.outline_color)
            for i in range((stopf-startf)+1):
                ImagesD[startf-1+i].polygon(position,fill_color,outline_color,self.width)

    graph = {}
    for line in range(1,len(DotAP_command),1):
        command = DotAP_command[line].split(" ")
        if(command[0]=="create"):
            if(command[1]=="basic"):
                graph[command[2]] = basic(command[3],command[4],command[5],command[6])
            else:
                print("未知命令，在",line+1,"行，第 2 段")
        elif(command[0]=="show"):
            graph[command[1]].show(int(command[2]),int(command[3]))
        elif(command[0]=="move"):
            pass
        else:
            print("未知命令，在",line+1,"行，第 1 段")

    for i in Images:
        i.show()