#!/usr/bin/env python3
import pymysql
import xlwt
import time

# 连接上数据库并且，设置光标
# ebhs_table_point是一个全局变量，指向table数据的表
def connect_database():
    global ebhs_database
    ebhs_database = pymysql.connect(host="127.0.0.1", user="root", password="asdfghjkl;'", database="Ebbinghaus",
                                    charset="utf8")
    global ebhs_table_point
    ebhs_table_point = ebhs_database.cursor(cursor=pymysql.cursors.DictCursor)
    pass


# 关闭数据库
def close_database():
    ebhs_table_point.close()
    ebhs_database.close()


# 在每次复习的时候都需要增加一列
def add_column():
    connect_database()  # 连接数据库,获得光标
    width = 0  # 定义宽度
    row_affetch = ebhs_table_point.execute('select * from Ebbinghaus')  # 获取行数
    all = ebhs_table_point.fetchone()  # 获取第一行的内容
    print("获取" + str(row_affetch) + "条内容")
    # 得到列数，也就是宽度
    for i in all:
        len(i)
        width += 1
    # 由宽度得到要添加的行的名称
    log = "log" + str(int(width) - 2)
    # 设计SQL语言，添加一行
    sql = "alter table Ebbinghaus add column {} varchar(45)".format(log)
    # 执行SQL语句
    ebhs_table_point.execute(sql)
    # 提交数据库
    ebhs_database.commit()


# 将数据库里面的内容转化成xls
# ebhs_database
# ebhs_table_point
def mysql_xls():
    # 新建的工作簿 Ebbinghaus_workbook
    Ebbinghaus_workbook = xlwt.Workbook()
    # 新建表格Ebbinghaus_workbook_sheet
    Ebbinghaus_workbook_sheet = Ebbinghaus_workbook.add_sheet('ebhs')
    # 给Excel文件开头
    Ebbinghaus_workbook_sheet.write(0, 0, "id")
    Ebbinghaus_workbook_sheet.write(0, 1, "content")
    Ebbinghaus_workbook_sheet.write(0, 2, "stage")
    for i in range(1, 101):
        Ebbinghaus_workbook_sheet.write(0, i + 2, "log{}".format(i))

    # 连接数据库
    connect_database()

    # 获取列数，也就是宽度
    row_affetch = ebhs_table_point.execute('select * from Ebbinghaus')
    print("获取" + str(row_affetch) + "条记录")
    # 获取整个数据库里面的内容
    all = ebhs_table_point.fetchall()
    # 循环，分别写入Excel文件中
    # 记录坐标的编号r，d
    d = 1
    for element in all:
        r = 0
        for key in element:
            Ebbinghaus_workbook_sheet.write(d, r, "{}".format(element[key]))
            r += 1
        d += 1
    Ebbinghaus_workbook.save("/Users/stevenjobs/Downloads/ebhs.xls")


# 第一次学习的内容，进行插入
# ebhs_database
# ebhs_table_point
def new_content():
    # 获取整个要记录的信息
    connect_database()
    ##
    print("#########################################################################")
    print("#\t\t\t\t\t\t\t\t\t#")
    content = input(
        "#\t新学习的内容是什么 \tor \t\t退出？\t\t\t#\t\t\t\t\n#\t\t\t\t\t\t\t\t\t#\n#########################################################################\n:")
    if content == "退出":
        return
    ebhs_table_point.execute('select * from Ebbinghaus')
    all = ebhs_table_point.fetchall()
    length = len(all)
    for i in range(length):
        if all[i]["content"] == content:
            ##
            print(
                "#################################\n#\t\t\t\t#\n#\t信息重复_请重新输入\t#\n#\t\t\t\t#\n#################################")
            close_database()
            return
    ebhs_table_point.close()
    connect_database()
    first_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log = first_time
    stage = 1

    rows = ebhs_table_point.execute('select * from Ebbinghaus')
    id = str(rows + 1)
    # SQL语言,进行插入
    # 先进行判断这个表格有多少列
    # 如果新的内容不够行数，就补上空
    one = ebhs_table_point.fetchone()
    width = len(one)
    if width > 4:
        sql_1 = '''("{}", "{}", "{}", "{}"'''.format(id, content, stage, log)
        for i in range(2, width - 2):
            sql_1 = sql_1 + ''',"NULL"'''
        sql = '''insert into Ebbinghaus values ''' + sql_1 + ")"
        ebhs_table_point.execute(sql)
    elif width == 4:
        sql_1 = '''("{}", "{}", "{}", "{}")'''.format(id, content, stage, log)
        sql = '''insert into Ebbinghaus values ''' + sql_1 + ")"
        ebhs_table_point.execute(sql)
    else:
        ##
        print("#########################\n#\t\t\t#\n#\t请检查MySQL\t#\n#\t\t\t#\n#########################")
    ebhs_database.commit()


# 返回一个整型的数字
def calculation(record_time_str):
    now_time_list = []
    record_time_list = []
    now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
    now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
    now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
    now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
    now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
    now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
               now_time_list[3] * 60 + now_time_list[4]

    record_time_list.append(int(record_time_str[0:4]))
    record_time_list.append(int(record_time_str[5:7]))
    record_time_list.append(int(record_time_str[8:10]))
    record_time_list.append(int(record_time_str[11:13]))
    record_time_list.append(int(record_time_str[14:16]))
    record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
        2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]
    ans = now_time - record_time
    return ans


# 把需要复习的内容显示在屏幕上
# ebhs_database
# ebhs_table_point
def display():
    print("#########################")
    print("\n")
    connect_database()
    ebhs_table_point.execute('select * from Ebbinghaus')
    all = ebhs_table_point.fetchall()
    # 遍历列表中所有的字典,每一个字典里面就是一条记录
    for element in all:
        # 遍历字典里面所有的键,键就是行向的项目
        record_time_str = ""
        for key in element:
            # 找到项目是“stage”的项目
            if key == "stage":
                # 判断键“stage”值里面的值是不是1


                #找到阶段一
                if int(element[key]) == 1:
                    # 如果是stage = 1 就遍历最后一个log
                    # element就是一个字典
                    list_str = []
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 5:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段二
                elif int(element[key]) == 2:
                    list_str = []
                    # 如果是stage = 2 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 30:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段三
                elif int(element[key]) == 3:
                    list_str = []
                    # 如果是stage = 3 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 12 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段四
                elif int(element[key]) == 4:
                    list_str = []
                    # 如果是stage = 4 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 24 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段5
                elif int(element[key]) == 5:
                    list_str = []
                    # 如果是stage = 2 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 2 * 24 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段6
                elif int(element[key]) == 6:
                    list_str = []
                    # 如果是stage = 2 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 4 * 24 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")


                #找到阶段7
                elif int(element[key]) == 7:
                    list_str = []
                    # 如果是stage = 2 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if key_time.find("log") + 1:
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 7 * 24 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")

                #找到阶段8
                elif int(element[key]) == 8:
                    list_str = []
                    # 如果是stage = 2 就遍历最后一个log
                    for key_time in element:
                        # 找到log* 不停的刷新record_time_str
                        if (key_time.find("log") + 1):
                            list_str.append(element[key_time])
                            if element[key_time] is None:
                                break
                            elif element[key_time] == "NULL":
                                break
                    record_time_str = list_str[-2]
                    ####
                    if calculation(record_time_str) >= 15 * 24 * 60:
                        for c in element:
                            if c == "content":
                                print(element[c])
                                print("#########################")
                                print("\n")
                else:
                    ##
                    print("#########################\n#\t\t\t#\n#\tlevel Error\t#\n#\t\t\t#\n#########################")


# 复习
# 增加一条学习记录，增加在内容的最后面
# ebhs_database
# ebhs_table_point
def review():
    # 获取复习的内容
    display()
    ##
    print("#################################################")
    print("#\t\t\t\t\t\t#")
    content_input = input(
        "#\t复习的内容 \tor\t 退出？\t\t#\n#\t\t\t\t\t\t#\n#################################################\n:")
    connect_database()
    ebhs_table_point.execute('select * from Ebbinghaus')
    # 获得一个列表，里面装字典，每一条字典都是一个行记录
    all = ebhs_table_point.fetchall()
    # 得到记录的数目
    length = len(all)
    # 循环所有的记录，一次一次的开始
    for i in range(length):
        # 如果第找到的这一纪录的content是输入的内容
        if all[i]["content"] == content_input:
            # 得到这条记录的stage->compare
            compare = int(all[i]["stage"])
            # 得到整个记录的长度
            width = len(all[i])
            # 补上差的列数
            while (compare + 4) > width:
                add_column()
                width += 1
            new_stage = str(all[i]["stage"])
            SQL = '''update Ebbinghaus set stage = "{}" where content = "{}"'''.format(str(int(new_stage) + 1),
                                                                                       content_input)
            ebhs_table_point.execute(SQL)
            log_puls = 0
            # 循环的所有的行数
            for n in range(length):
                # 如果找到了这一行
                if all[n]["content"] == content_input:
                    list_log = []
                    for m in all[n]:
                        list_log.append(m)
                        log_puls = len(list_log) - 3
                        if all[n][m] is None:
                            break
                        elif all[n][m] == "NULL":
                            break
            time_p = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            SQL_1 = '''update Ebbinghaus set log{} = "{}" where content = "{}"'''.format(log_puls, time_p,
                                                                                         content_input)
            ebhs_table_point.execute(SQL_1)
            ebhs_database.commit()
            print("复习记录完成")
            print("复习的内容是" + content_input)


##
# 更改其中可能错误的部分
# ebhs_database
# ebhs_table_point
def renew():
    ##
    print("\n")
    print("#################################")
    print("#\t\t\t\t#")
    print("#\tid或内容任意一个\t#")
    print("#\t\t\t\t#")
    key = input("#\t请输入你想修改内容\t#\n#\t\t\t\t#\n#################################\n:")
    connect_database()
    ebhs_table_point.execute("select * from Ebbinghaus")
    all = ebhs_table_point.fetchall()
    # 遍历所有的列表内容，i为字典
    g = 0
    for i in all:
        # 找到我们要的这一行字典，内容
        if str(i["content"]) == key:
            # 获得我们最后的结果
            new = input("\n更改之后的内容\n")
            # 如果输入过小，就说明可能是修改id
            if len(new) <= 4:
                # 获取原来值
                con = all[g]["content"]
                # 执行
                SQL = '''update Ebbinghaus set stage = "{}" where content = "{}"'''.format(str(new), con)
                ebhs_table_point.execute(SQL)
                ebhs_database.commit()
                print("#########################\n#\t\t\t#\n#\t更改成功\t#\n#\t\t\t#\n#########################")
                return
            # 输入的不短，就可能是修改能容
            elif len(new) >= 4:
                idd = all[g]["id"]
                SQL = '''update Ebbinghaus set content = "{}" where id = "{}"'''.format(str(new), idd)
                ebhs_table_point.execute(SQL)
                ebhs_database.commit()
                print("#########################\n#\t\t\t#\n#\t更改成功\t#\n#\t\t\t#\n#########################")
                return
        elif str(i["id"]) == key:
            # 获得我们最后的结果
            new = input("\n更改之后的内容\n")
            # 如果输入过小，就说明可能是修改id
            if len(new) <= 4:
                # 获取原来值
                con = all[g]["content"]
                # 执行
                SQL = '''update Ebbinghaus set stage = "{}" where content = "{}"'''.format(str(new), con)
                ebhs_table_point.execute(SQL)
                ebhs_database.commit()
                print("#########################\n#\t\t\t#\n#\t更改成功\t#\n#\t\t\t#\n#########################")
                return
            # 输入的不短，就可能是修改能容
            elif len(new) >= 4:
                idd = all[g]["id"]
                SQL = '''update Ebbinghaus set content = "{}" where id = "{}"'''.format(str(new), idd)
                ebhs_table_point.execute(SQL)
                ebhs_database.commit()
                print("#########################\n#\t\t\t#\n#\t更改成功\t#\n#\t\t\t#\n#########################")
                return 
        g += 1
    print("#########################\n#\t\t\t#\n#\t更改失败\t#\n#\t\t\t#\n#########################")


def main():
    while True:
        ##
        print("#########################")
        print("#\t\t\t#")
        print("#\t 1.新章节\t#")
        print("#\t 2.查看\t\t#")
        print("#\t 3.复习完成\t#")
        print("#\t 4.更改\t\t#")
        print("#\t\t\t#")
        print("#\t 5.退出\t\t#")
        print("#\t\t\t#")
        print("#########################")

        key = input("\n你想做点什么\n:")
        if key == "新章节":
            new_content()
            mysql_xls()
            close_database()
        elif key == "1":
            new_content()
            mysql_xls()
            close_database()
        elif key == "查看":
            display()
            mysql_xls()
            close_database()
        elif key == "2":
            display()
            mysql_xls()
            close_database()
        elif key == "复习完成":
            review()
            mysql_xls()
            close_database()
        elif key == "3":
            review()
            mysql_xls()
            close_database()
        elif key == "更改":
            renew()
            mysql_xls()
            close_database()
        elif key == "4":
            renew()
            mysql_xls()
            close_database()
        elif key == "退出":
            exit()
        elif key == "5":
            exit()
        else:
            ##
            print("#########################\n#\t\t\t#\n#\t输入错误\t#\n#\t\t\t#\n#########################")


main()
