import re
from area import area
def chickID(idcard):
    if(len(idcard)!=18):
        print("身份证位数错误")
    elif(idcard[:6] not in area):
        print("身份证地区非法")
    else:
        s=int(idcard[0])*7+int(idcard[1])*9+int(idcard[2])*10+int(idcard[3])*5+int(idcard[4])*8+int(idcard[5])*4\
        +int(idcard[6])*2+int(idcard[7])*1+int(idcard[8])*6+int(idcard[9])*3+int(idcard[10])*7+int(idcard[11])*9\
        +int(idcard[12])*10+int(idcard[13])*5+int(idcard[14])*8+int(idcard[15])*4+int(idcard[16])*2
        y=s%11
        j='10x98765432'
        if(j[y]!=idcard[17]):
            print('身份证校验码错误')
        else:
            sfz=re.search(r'([0-9]{6})([1-2][0-9]{3})([0-1][0-9])([0-3][0-9])([0-9]{3})([0-9Xx])',idcard)
            print('地区:',area[sfz.group(1)])   
            print('生日:',sfz.group(2),'年',sfz.group(3),'月',sfz.group(4),'日')
            if(int(sfz.group(5))%2==0):
                print('性别：女')
            else:
                print('性别：男')
                
print("请输入身份证号：")
idcard=input()
chickID(idcard)
print()


