import pymysql


def menu():
    print("1. 打印所有学生的姓名、各科成绩")
    print("2. 根据姓名查询指定学生的各科成绩")
    print("3. 添加新的学生的考试信息")
    print("4. 根据姓名删除指定学生的考试成绩")
    print("5. 输出成绩总分前3名的学生姓名、各科成绩、总分数")
    print("6. 退出系统")


def main():
    while True:
        menu()
        conn = pymysql.connect(host="127.0.0.1", user="root", password="mysql", database="kaoshi", port=3306)
        cursor = conn.cursor()
        num = input("请输入要执行的操作:")
        if num == "1":
            sql = "select * from students;"
            cursor.execute(sql)
            print(cursor.fetchall())
        elif num == "2":
            name = input("请输入要查询的学生姓名")
            sql = f"select * from students where name = '{name}'"
            cursor.execute(sql)
            print(cursor.fetchone())
        elif num == "3":
            name = input("请输入要添加的学生姓名")
            chinese = int(input("请输入语文成绩"))
            english = int(input("请输入英语成绩"))
            math = int(input("请输入数学成绩"))
            try:
                sql = f"insert into students(name, chinese, english, math) values('{name}', {chinese}, {english}, {math})"
                cursor.execute(sql)
            except Exception as e:
                print(e)
                print("输入有误")
            conn.commit()
            print("添加成功")
        elif num == "4":
            name = input("请输入要删除的学生姓名")
            try:
                sql = f"delete from students where name = '{name}';"
                cursor.execute(sql)
            except Exception as e:
                print("输入姓名有误")
            conn.commit()
            print("删除成功")
        elif num == "5":
            try:
                sql = "select name, chinese, english, math, (chinese + english + math) as sorce from students order by sorce desc limit 3;"
                cursor.execute(sql)
            except Exception as e:
                print("输入有误, 请重新输入")
            print(cursor.fetchall())
        elif num == "6":
            cursor.close()
            conn.close()
            break
        else:
            print("输入错误,请重新输入")


if __name__ == '__main__':
    main()

print("这是pycharm的一句话")
