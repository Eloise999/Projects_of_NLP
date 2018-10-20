import random
import time
import os
import pandas as pd
import csv


def get_douban_id(douban_id_info_directory):
    files = os.listdir(douban_id_info_directory)#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表

    for file in files:
        file_name = os.path.join(douban_id_info_directory, file)#获取文件路径
        contents = pd.read_csv(file_name).iterrows()
        for c in contents:
            yield c[1].douban_id


def random_sleep():
    random_sleep_time = random.randint(80, 200) / 100
    time.sleep(random_sleep_time)


def csv_saver(file, columns):
    need_column = not os.path.isfile(file)#os.path.isfile(绝对路径)表示,是否存在此"绝对路径".
    #csvfile = open(file, 'a+', newline='')
    csvfile = open(file, 'a+')
    spamwrite = csv.writer(csvfile)
    if need_column:
        spamwrite.writerow(columns)

    def _save(row):
        spamwrite.writerow(list(row))

    return _save


if __name__ == '__main__':
    for ii, id in enumerate(get_douban_id('movie_info/movies_id')):
        print(id)
        if ii > 5: break
