#3-4.py

#本练习要求：定义一个类，完成指定功能。

class Student:  #定义一个学生类

    def __init__(self,name,num,chn,math,eng,phy,chem,bio):
        #定义构造函数
        self.name=name
        self.number=num
        self.chn=chn
        self.math=math
        self.eng=eng
        self.phy=phy
        self.chem=chem
        self.bio=bio

    #计算平均分（请自行补充完整）
    def aver_score(self):
        total = self.chn + self.math + self.eng + self.phy + self.chem + self.bio
        total = float(total)
        score = total/6
        return score

    #计算等级（请自行补充完整）
    def aver_grade(self):
        #若平均分在90~100，则为A
        if self.aver_score()>=90 and self.aver_score()<=100:
            grade="A"
        elif self.aver_score()>=80:
            grade = "B"
        elif self.aver_score()>=70:
            grade = "C"
        elif self.aver_score()>=60:
            grade = "D"
        else:
            grade = "F"
        return grade
	
    #按照格式输出学生信息（请自行补充完整）
    def print_student(self):
        print(self.name,"(学号：",self.number,") ","语",self.chn," 数",self.math," 英",self.eng," 物",self.phy," 化",self.chem," 生",self.bio," 平均分",self.aver_score()," 等级",self.aver_grade())
        

#测试开始（请自行补充完整）
if __name__=="__main__":
    #采用列表保存类的实例
    Stu_List=[]
    stu1=Student("A","201601",85,93,95,80,89,90)
    stu2=Student("B","201602",90,95,83,72,95,96)
    stu3=Student("C","201603",82,88,90,90,93,86)
    stu4=Student("D","201604",87,86,93,84,76,90)
    stu5=Student("E","201605",79,99,80,84,86,76)
    stu6=Student("F","201606",83,76,83,65,67,70)
    stu7=Student("G","201607",93,84,97,76,78,65)
    stu8=Student("H","201608",65,92,90,95,96,94)
    stu9=Student("I","201609",88,90,91,93,89,97)
    stu10=Student("J","201610",92,91,96,96,97,93)
    Stu_List.append(stu1)
    Stu_List.append(stu2)
    Stu_List.append(stu3)
    Stu_List.append(stu4)
    Stu_List.append(stu5)
    Stu_List.append(stu6)
    Stu_List.append(stu7)
    Stu_List.append(stu8)
    Stu_List.append(stu9)
    Stu_List.append(stu10)
    for item in Stu_List:
        item.print_student()