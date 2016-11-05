#3-1.py
#本练习要求：计算每门课程的最高分、最低分和算术平均分

#本程序无输入

#处理过程
#将10名同学语文、数学、英语、物理、化学、生物的成绩储存在对应列表Chinese、Math、English、Physics、Chemistry、Biology中
Chinese = [85, 90, 82, 87, 79, 83, 93, 65, 88, 92]
Math = [93, 95, 88, 86, 99, 76, 84, 92, 90, 91]
English = [95, 83, 90, 93, 80, 83, 97, 90, 91, 96]
Physics = [80, 72, 90, 84, 84, 65, 76, 95, 93, 96]
chemistry = [89, 95, 93, 76, 86, 67, 78, 96, 89, 97]
Biology = [90, 96, 86, 90, 76, 70, 65, 94, 97, 93]

#输出过程
#输出每门课程的算术平均分、最高分和最低分
print("语文平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(Chinese)/len(Chinese),max(Chinese),min(Chinese)))
print("数学平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(Math)/len(Math),max(Math),min(Math)))
print("英语平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(English)/len(English),max(English),min(English)))
print("物理平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(Physics)/len(Physics),max(Physics),min(Physics)))
print("化学平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(chemistry)/len(chemistry),max(chemistry),min(chemistry)))
print("生物平均成绩:%.2f分，最高分: %d分，最低分: %d分" %(sum(Biology)/len(Biology),max(Biology),min(Biology)))