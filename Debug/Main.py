#这是我自己用的工具，纠错聊胜于无！
from turtle import width
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

    def list_change(stri):#字符逗号分割的字符串改成整形数组
        lis = []
        stri = stri.split(",")
        for i in stri:
            lis.append(int(i))
        return lis


    class basic():#标准图形至少三个坐标，少于三个的需转换为其他图形
        def __init__(self,position,fill_color,outline_color,width):
            self.position=position
            self.fill_color=list_change(fill_color)
            self.outline_color=list_change(outline_color)
            self.width = int(width)
        def show(self,startf,stopf):
            #Image库只接受元组，但图形动起来时数据肯定会变，所以就在这改元组了（毕竟都用Py了，慢点就慢点）
            #坐标改元组
            position = []
            for i in self.position:
                position.append(tuple(i))
            #颜色改元组
            fill_color = tuple(self.fill_color)
            outline_color = tuple(self.outline_color)
            for i in range(stopf-startf+1):
                ImagesD[startf-1+i].polygon(position,fill_color,outline_color,self.width)

    class line():#标准线段至少两个坐标，少于两个的需转换为其他图形
        def __init__(self,position,outline_color,width):
            self.position = position
            self.outline_color=list_change(outline_color)
            self.width = int(width)
        def show(self,startf,stopf):
            #改元组
            position = []
            for i in self.position:
                position.append(tuple(i))
            outline_color = tuple(self.outline_color)
            for i in range(stopf-startf+1):
                ImagesD[startf-1+i].line(position,outline_color,self.width)


    class point():
        pass

    graph = {}
    for lines in range(1,len(DotAP_command),1):
        command = DotAP_command[lines].split(" ")
        if(command[0]=="create"):
            if(command[1]=="basic"):
                #将坐标转为二维数组，position是一维数组，position_list是二维数组
                position=command[3].split(",")
                position_list=[]
                for i in range(0,len(position),2):
                    position_list.append([int(position[i]),int(position[i+1])])
                #转换为图形对象
                #大于等于3个坐标的是basic标准图形  
                #2个是线段，1个是点，此时填充颜色作废 
                if(len(position_list)>2):#三个坐标
                    graph[command[2]] = basic(position_list,command[4],command[5],command[6])
                elif(len(position_list)==2):#两个坐标
                    graph[command[2]] = line(position_list,command[5],command[6])
                else:#1个坐标或负个坐标(虽然不可能，但万一有时能防报错)，如果是0个坐标那直接未知命令了
                    pass
            elif(command[1]=="line"):
                #将坐标转为二维数组，position是一维数组，position_list是二维数组
                position=command[3].split(",")
                position_list=[]
                for i in range(0,len(position),2):
                    position_list.append([int(position[i]),int(position[i+1])])
                graph[command[2]] = line(position_list,command[4],command[5])
            else:
                print("未知命令，在",lines+1,"行，第 2 段")
        elif(command[0]=="show"):
            graph[command[1]].show(int(command[2]),int(command[3]))
        elif(command[0]=="move"):
            pass
        else:
            print("未知命令，在",lines+1,"行，第 1 段")

    for i in Images:
        i.show()