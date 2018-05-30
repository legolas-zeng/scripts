# coding=utf-8

def ten_sixteen(rang):
    tar = hex(rang)
    return tar

def Joining(R,G,B):
    R = ten_sixteen(R)[2:4]
    G = ten_sixteen(G)[2:4]
    B = ten_sixteen(B)[2:4]
    req = "#"+R+G+B
    return req

#print Joining(255,125,123)
import re
import string

def toRgb(tmp):
    opt = re.findall(r'(.{2})', tmp)  # 将字符串两两分割
    strs = ""  # 用以存放最后结果
    for i in range(0, len(opt)):  # for循环，遍历分割后的字符串列表
        strs += str(int(opt[i], 16)) + ","  # 将结果拼接成12，12，12格式
    print("转换后的RGB数值为：")
    print(strs[0:-1])  # 输出最后结果，末尾的","不打印


def toHex(tmp):
    rgb = tmp.split(",")
    strs = "#"
    for j in range(0, len(rgb)):
        num = string.atoi(rgb[j])
        strs += str(hex(num))[-2:]  # 每次转换之后只取0x7b的后两位，拼接到strs中
    print("转换后的16进制值为：")
    print(strs)


def main():
    inColor = raw_input("输入颜色值")
    if (len(inColor) <= 11):

        if (inColor.index(",") >= 0):
            tmp = inColor
            toHex(tmp)
        elif (inColor[0] == "#"):  # 如果首字母#则代表输入为16进制字符串
            tmp = inColor[1:]  # 取出第一个至最后一个字符
            toRgb(tmp)
    else:
        print("请输入正确的数值！如\"#777bbb\"或\"123,123,123\"")


main()


