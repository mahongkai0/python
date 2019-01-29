import menu 
import student_info as info

while True:

    print("+---------------------------------------+")
    print("| 1) 添加学生信息                        |")
    print("| 2)显示学生信息                         |")
    print("| 3)删除学生信息                         |")
    print("| 4)修改学生成绩                         |")
    print("| 5) 按学生成绩高~低显示学生信息         |")
    print("| 6) 按学生成绩低~高显示学生信息         |")
    print("| 7) 按学生年龄高~低显示学生信息         |")
    print("| 8) 按学生年龄低~高显示学生信息         |")
    print("| q)退出                                 |")
    print("+--------------------------------------- |")
    bianhao = str(input("请亲输入编号："))

    if bianhao == '1':
        L=info.tianjia()
    elif bianhao == '2':
        menu.xianshi(L)

    elif bianhao == '3':
        info.shanchu(L)

    elif bianhao == '4':
        info.xiugai(L)
    elif bianhao == "q":
        break
    elif bianhao == "6":
        info.show_info(L)
    elif bianhao == "5":
        info.sortgao(L)
    elif bianhao == "8":
        info.age_di(L)
    elif bianhao == "7":
        info.age_gao(L)
    else:
        print("您输错了，请重新输入")





