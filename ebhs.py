#!/usr/bin/env python3
import time
import os
import sys

lines_read = []
dic_date = {}


# 读文本,并且放入dic_date = {} 中
def read_file_date():
    read_file = open("/Users/stevenjobs/Downloads/Ebbinghaus.txt".encode("UTF-8"), 'rb')
    read_file.readline()
    lines = read_file.readlines()
    for line in lines:
        part = line.split()
        dic_date[str(part[0].decode("UTF-8")) + " " + str(part[1].decode("UTF-8"))] = [str(part[2].decode("UTF-8")),
                                                                                       str(part[3].decode("UTF-8"))]
    read_file.close()


# 进行显示
def display():
    # content表示的是   字典-列表组合中的列表     content[1]就是表示后面的等级
    # list_content 同上也是一样的意思
    # stage_total 就是遍历所有的等级，把所有的等级都存放在列表中
    stage_total = []
    for key in dic_date:
        list_content = dic_date[key]
        stage_total.append(list_content[1])

    for key in dic_date:
        now_time_list = []
        record_time_list = []
        content = dic_date[key]

        if int(content[1]) == 1:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 5:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 2:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 30:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 3:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 12 * 60:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 4:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 24 * 60:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 5:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 2 * 24 * 60:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 6:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 4 * 24 * 60:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 7:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 7 * 24 * 60:
                remind = dic_date[key]
                print(remind[0])
        elif int(content[1]) == 8:
            now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            now_time_list.append(int(now_time_str[0:4]))  # year  list[0]
            now_time_list.append(int(now_time_str[5:7]))  # month  list[1]
            now_time_list.append(int(now_time_str[8:10]))  # day  list[2]
            now_time_list.append(int(now_time_str[11:13]))  # hour  list[3]
            now_time_list.append(int(now_time_str[14:16]))  # Minute  list[4]
            now_time = now_time_list[0] * 365 * 24 * 60 + now_time_list[1] * 30 * 24 * 60 + now_time_list[2] * 24 * 60 + \
                       now_time_list[3] * 60 + now_time_list[4]

            record_time_list.append(int(key[0:4]))
            record_time_list.append(int(key[5:7]))
            record_time_list.append(int(key[8:10]))
            record_time_list.append(int(key[11:13]))
            record_time_list.append(int(key[14:16]))
            record_time = record_time_list[0] * 365 * 24 * 60 + record_time_list[1] * 30 * 24 * 60 + record_time_list[
                2] * 24 * 60 + record_time_list[3] * 60 + record_time_list[4]

            if now_time - record_time >= 15 * 24 * 60:
                remind = dic_date[key]
                print(remind[0])
        else:
            print("level Error")


# 插入数据的函数
def input_date():
    record = []
    record_str = ''
    date_content = input("学习的章节\n")
    print("新学习的内容是\t" + date_content + "\n")
    now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    record_str = '\t'.join([now_time_str, date_content, record_str, str("1")])
    record.append('\n' + record_str)
    write_file = open("/Users/stevenjobs/Downloads/Ebbinghaus.txt", 'a')
    write_file.writelines(record)
    write_file.close()


def delete_file():
    # 判断文件是否存在
    if os.path.exists("/Users/stevenjobs/Downloads/Ebbinghaus.txt"):
        os.remove("/Users/stevenjobs/Downloads/Ebbinghaus.txt")
        print("重置成功\n")
    else:
        print("要重置的文件不存在！\n")


def review():
    remake_list = ["时间\t"+"\t", "内容\t"+"\t", "阶段\n"]
    review_date = input("复习的内容")
    read_file_date()
    for key in dic_date:
        if review_date == str(dic_date[key][0]):
            remake_stage_str = dic_date[key][1]
            remake_stage_int = int(remake_stage_str)
            remake_stage_int += 1
            dic_date[key][1] = str(remake_stage_int)
            if remake_stage_int >= 8:
                dic_date[key][1] = '8'
            break
        else:
            print("\n请核实再输入\n")
            break

    list_time = list(dic_date)
    list_value = list(dic_date.values())
    txt_high = len(list_time)
    for i in range(txt_high):
        remake_list.append(list_time[i] + "\t")
        remake_list.append(list_value[i][0] + "\t")
        remake_list.append(list_value[i][1] + "\n")
    delete_file()
    write_file = open("/Users/stevenjobs/Downloads/Ebbinghaus.txt", 'w')
    write_file.writelines(remake_list)
    write_file.close()


def main():
    while True:
        keyboard = input("##新章节##" + "\n" + "##查看##" + "\n" + "##复习完成##\n" + "##退出##\n" + "\n" + "你想做点什么?\n")
        if str(keyboard) == "新章节":
            input_date()
        elif str(keyboard) == "查看":
            read_file_date()
            print("\n")
            print("\n")
            display()
            print("\n")
            print("\n")
        elif str(keyboard) == "复习完成":
            review()
        elif str(keyboard) == "退出":
            sys.exit(0)
        else:
            print("\n" + "你怕是输入错误了")


if __name__ == '__main__':
    main()

