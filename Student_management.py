def show_menu():
    print("===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 显示所有学生")
    print("3. 计算平均分")
    print("4. 退出系统")

def main():
    while True:
        show_menu()
        choice = input("请输入操作编号：")
        if choice == "1":
            print("功能开发中...")
        elif choice == "2":
            print("功能开发中...")
        elif choice == "3":
            print("功能开发中...")
        elif choice == "4":
            print("感谢使用，再见！")
            break
        else:
            print("输入有误，请重新选择。")

if __name__ == "__main__":
    main()