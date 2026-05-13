# 作者: 苏尛鱼
# 2026年05月13日13时33分52秒
# xxx@qq.com
"""
保存学生类的信息
"""
class Student():
    def __init__(self,name,gender,age,phone,desc):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.desc=desc
    def __str__(self):
        return f"name:{self.name},gender:{self.gender},age:{self.age},phone:{self.phone},desc:{self.desc}"

if __name__ == '__main__':
    student=Student("Jack","man",18,"1234566","傻逼")
    print(student)