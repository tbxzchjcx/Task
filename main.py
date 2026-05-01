def show_menu():
    print("===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 显示所有学生")
    print("3. 计算平均分")
    print("4. 退出系统")
import Student_management as sm
def main():
    while True:
        show_menu()
        choice = input("请输入操作编号：")
        if choice == "1":
            name = input("请输入学生姓名：")
            try:
                score = float(input("请输入学生成绩："))
            except ValueError:
                print("成绩必须为数字！")
                continue
            sm.add_student(name, score)
        elif choice == "2":
            sm.show_all_students()
        elif choice == "3":
            avg = sm.calculate_average()
            print(f"当前学生平均分：{avg:.2f}")
        elif choice == "4":
            print("感谢使用，再见！")
            break
        else:
            print("输入有误，请重新选择。")

if __name__ == "__main__":
    main()