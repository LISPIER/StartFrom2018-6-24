# 2018-6-24
# 杨辉三角形
# 按q退出，任意键显示下一行
# 不断打印杨辉三角形的每一行直到结束
from typing import List, Any, Union


def main():
    historyLines = []  # 用于存储已经打印过的行
    currentLine = []  # 当前行
    nextLine = []  # 下一行

    while True:
        if True:  # 主逻辑开始
            if historyLines == []:  # 如果当前历史行为空，则进行初始化，此处划线不用管
                currentLine.append(1)
                nextLine.append(currentLine[0])
                nextLine.append(currentLine[-1])
            else:  # 其他情况下则继续下去
                nextLine.append(currentLine[0])  # 任何情况下，下一行的第一个数字都与上一行的第一个数字相同
                for i in range(0, len(currentLine)-1):
                    nextLine.append(currentLine[i]+currentLine[i+1])
                nextLine.append(currentLine[-1])
            # 收尾
            historyLines.append(currentLine)
            for i in currentLine:
                print(i, end=" ")  # end="" 可以用空字符串取代换行，为了方便查看输出，所以结尾改成了空格
            currentLine = nextLine
            nextLine = []


if __name__=='__main__':
    main()