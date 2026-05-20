# 作者: 苏尛鱼
# 2026年05月13日13时34分04秒
# xxx@qq.com
import json
import time

from pandas.io.sas.sas_constants import sas_server_type_length

from student import Student
class StudentCMS:
    def __init__(self):
        self.student_list = [
            Student("Jack","man",18,"1234566","傻逼"),
            Student("Tom","woman",18,"1234566","傻逼"),
            Student("Mike","man",18,"1234566","傻逼"),
            Student("Mary","woman",18,"1234566","傻逼"),
            Student("Lucy","woman",18,"1234566","傻逼"),
            Student("Lily","woman",18,"1234566","傻逼"),
            Student("Mike","man",18,"1234566","傻逼")
        ]
    @staticmethod
    def show_menu():
        print("*" * 23)
        print("\t1. 添加学生信息")
        print("\t2. 删除学生信息")
        print("\t3. 修改学生信息")
        print("\t4. 查询学生信息")
        print("\t5. 显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0. 退出系统")
        print("*" * 23)
        print("请输入您要操作的编号:",end="")

    def add_student(self):
        name=input("请输入要添加的学生姓名:")
        gender=input("请输入要添加的学生性别:")
        age=input("请输入要添加的学生年龄:")
        phone=input("请输入要添加的学生手机:")
        desc=input("请输入要添加的学生描述:")
        student=Student(name,gender,age,phone,desc)
        self.student_list.append(student)
        print("学生信息添加成功！\n")

    def delete_student(self):
        name=input("请输入要删除的学生姓名:")
        for i in self.student_list:
            if i.name==name:
                self.student_list.remove(i)
                print(f"{name}同学的信息删除成功！\n")
                break
        else:
            print(f"没有找到{name}同学，无法删除！\n")


    def modify_student(self):
        # 修改学生的信息
        name=input("请输入要修改的学生的姓名：")
        for stu in self.student_list:
            if stu.name==name:
                stu.gender=input("请输入修改的性别：")
                stu.age=input("请输入要修改的年龄：")
                stu.phone=input("请输入要修改的电话号码：")
                stu.desc=input("请输入要修改的描述：")
                print(f"{name}同学的信息修改成功！\n")
                break
        else:
            print(f"没有找到{name}同学，无法修改！\n")

    def search_student(self):
        name=input("请输入要查询的学生的姓名：")
        for stu in self.student_list:
            if name==stu.name:
                print(stu)
                print(f"{name}同学的信息查询成功！\n")
                break
        else:
            print(f"没有找到{name}同学，无法查找！\n")

    def show_all_student(self):
        if len(self.student_list)==0:
            print("没有学生信息，请添加后查询！\n")
        else:
            for i in self.student_list:
                print(i)
            print()

    def save_student(self):
        with open("stu_file.txt", "w", encoding="utf-8") as stu_f:
            stu_dict=[stu.__dict__ for stu in self.student_list ]
            json.dump(stu_dict,stu_f,ensure_ascii=False)
    def load_student(self):
        try:
            with open("stu_file.txt", "r", encoding="utf-8") as stu_f:
                stu_list=json.load(stu_f)
                self.student_list=[Student(**stu) for stu in stu_list ]
        except:
            stu_f=open("stu_file.txt", "w", encoding="utf-8")



    def start(self):
        self.load_student()
        while True:
            time.sleep(1)
            StudentCMS.show_menu()
            choice = input()
            if choice == "1":
                # 添加学生信息
                # print("添加学生信息")
                self.add_student()
            elif choice == "2":
                # 删除学生信息
                # print("删除学生信息\n")
                self.delete_student()
            elif choice == "3":
                # 修改学生信息
                # print("修改学生信息\n")
                self.modify_student()
            elif choice == "4":
                # 查询学生信息
                # print("查询学生信息\n")
                self.search_student()
            elif choice == "5":
                # 显示所有学生信息
                # print("显示所有学生信息\n")
                self.show_all_student()
            elif choice == "6":
                print("保存学生信息\n")
                self.save_student()
                print("保存学生信息成功！\n")
            elif choice == "0":
                print("确认要退出系统吗？(Y/N)->")
                exit_choice = input()
                if exit_choice == "Y" or exit_choice == "y":
                    self.save_student()
                    print("欢迎下次再来")
                    exit()
            else:
                print("输入错误，请重新输入")
if __name__ == '__main__':
    # studentCMS=StudentCMS()
    # studentCMS.start()
    import os
    print(os.getcwd())
