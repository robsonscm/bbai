import mysql.connector
import os
from mysql.connector import errorcode

from src.db import DbConnector


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


def load(files):
    try:
        db = DbConnector()
        for file in files:
            print("=================================")
            print(f"===> Start processing file {file}")
            print("=================================")
            f = open(file, 'r')
            count = 0
            for line in f:
                try:
                    count += 1
                    split_line = line.strip().split(',')
                    #
                    box_name = split_line[0:2][0]
                    box_build_date = split_line[0:2][1]
                    rpi_list = list(divide_chunks(split_line[2:], 3))
                    #
                    add_box = f"insert into boxes (box_name, box_build_date) values ('{box_name}', '{box_build_date}')"
                    db.execute(add_box)
                    #
                    for rpi in rpi_list:
                        mac_addr = rpi[0]
                        purchase_date = rpi[1]
                        cond = rpi[2]
                        add_rpi = "insert into rpis (mac_addr, purchase_date, cond, box_name) " \
                                  f"values ('{mac_addr}', '{purchase_date}', '{cond}', '{box_name}')"
                        db.execute(add_rpi)
                    #
                    db.cnx.commit()
                    print(f"Line {count} - Imported!")
                except mysql.connector.Error as err:
                    db.cnx.rollback()
                    print(f"Line {count} - Error: {err}")
            #
            f.close()
            print("==================================")
            print(f"===> Finish processing file {file}")
            print("==================================\n\n")
        db.cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
