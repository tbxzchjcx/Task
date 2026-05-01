# 学生信息列表（内存存储，程序关闭即消失）
students = []

def add_student(name, score):
    """添加一个学生"""
    students.append({"name": name, "score": score})
    print(f"已添加学生：{name}，成绩：{score}")

def show_all_students():
    """展示所有学生信息"""
    if not students:
        print("暂无学生信息。")
        return
    print("\n当前学生列表：")
    for i, stu in enumerate(students, 1):
        print(f"{i}. 姓名：{stu['name']}，成绩：{stu['score']}")

def calculate_average():
    """计算并返回平均分"""
    if not students:
        return 0
    total = sum(stu["score"] for stu in students)
    return total / len(students)