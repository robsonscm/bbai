import json

import mysql.connector
from mysql.connector import errorcode

from src.db import DbConnector


def report(start_date, end_date):
    try:
        db = DbConnector()

        qry = "select b.box_name, b.box_build_date, r.mac_addr, r.purchase_date, r.cond " \
              "from boxes b, rpis r " \
              "where r.box_name = b.box_name " \
              f"and r.purchase_date >= '{start_date}' " \
              f"and r.purchase_date <= '{end_date}' " \
              "order by b.box_name, r.purchase_date"

        data = db.execute(qry)
        #
        report = []
        boxes = sorted(set([item['box_name'] for item in data]))
        for box in boxes:
            new_item = dict({'RPi': []})
            for item in [x for x in data if x['box_name'] == box]:
                new_item.update({
                    'box name': item['box_name'],
                    'box build date': item['box_build_date']
                })
                new_item['RPi'].append({
                    'MAC address': item['mac_addr'],
                    "purchase data": item['purchase_date'],
                    "condition": item['cond']
                })
            report.append(new_item)
        print(json.dumps(report, sort_keys=True, indent=4, separators=(',', ': '), default=str))
        #
        db.cnx.close()
        #
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

