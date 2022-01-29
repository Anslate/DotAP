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

#接下来开始绘制
count = -1 #此变量用来进行如下循环的计数
for command in DotAP_list:
    if(count == -1):#跳过第一次循环
        count += 1
        continue
    command = command.split(" ")#将DotAP语句储存于命令(command)
    #区分静止与否
    if(command[0] == "still"):
        if(command[1] == "point"):#绘制点(point)
            for i in range(int(command[3])):#帧持续长度,偷个小懒用i表示了,因为DotAP中开始帧1帧表示为1而不是编程中常用的0,所以下方还要减去1
                image_draw[int(command[2])+i-1].point((int(command[4]),int(command[5])), int(command[6]))
        elif(command[1] == "rectangle"):#绘制矩形(retangle)
            for i in range(int(command[3])):
                image_draw[int(command[2])+i-1].rectangle((int(command[4]),int(command[5]),int(command[6]),int(command[7])), int(command[10]), int(command[9]), int(command[8]))
        else:
            print("未知命令，在第",str(count+2),"行，第 2 项")
            break
    elif(command[0] == "move"):
        if(command[3] == "1"):
            print("运动图形持续帧数不能为1，在",str(count+2),"行")
            break
        if(command[1] == "point"):#绘制动点(point)
            step_x = (int(command[6]) - int(command[4]))/(int(command[3])-1)#计算x轴每次移动步长
            step_y = (int(command[7]) - int(command[5]))/(int(command[3])-1)#计算y轴每次移动步长
            for i in range(int(command[3])):#同上
                image_draw[int(command[2])+i-1].point((int(command[4])+step_x*i,int(command[5])+step_y*i), int(command[8]))
        elif(command[1] == "rectangle"):
            step_x1 = (int(command[8]) - int(command[4]))/(int(command[3])-1)
            step_y1 = (int(command[9]) - int(command[5]))/(int(command[3])-1)
            step_x2 = (int(command[10]) - int(command[6]))/(int(command[3])-1)
            step_y2 = (int(command[11]) - int(command[7]))/(int(command[3])-1)
            for i in range(int(command[3])):
                image_draw[int(command[2])+i-1].rectangle((int(command[4])+step_x1*i,int(command[5])+step_y1*i,int(command[6])+step_x2*i,int(command[7])+step_y2*i), int(command[14]), int(command[13]), int(command[12]))
        else:
            print("未知命令，在第",str(count+2),"行，第 2 项")
            break
    else:
        print("未知命令，在第",str(count+2)," 行，第 1 项")
    count+=1

for i in image:
    i.show()
    pass