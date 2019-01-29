
from menu import show_menu
from student_info import *

def main():
    infos = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            # 显示学生信息:
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student(infos)
        elif s =='5':
            infos = sorted(infos,key=lambda d:d.get_score(),reverse=True)  #
            output_student(infos)

        elif s == '6':
            infos = sorted(infos,key=lambda d:d.get_score())
            output_student(infos)
        elif s == '7':
            infos = sorted(infos,key=lambda d:d.get_age(),reverse=True)
            output_student(infos)
        elif s == '8':
            infos = sorted(infos,key=lambda d:d.get_age())
            output_student(infos)
        elif s == 'q':
            break
        elif s == '9':
            
            infos = read_from_file()
        elif s == '10':
            save_to_file(infos)
        else:
            print("您输错了")

main()











