import json
import argparse
import sys

def readAndDo(path, doFunc):
    f = open(path, 'r', encoding='utf-8')
    for _, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        doFunc(obj)

def filterFrom(path, substring):
    def fFrom(obj):
        del obj['trace']
        del obj['referer']
        del obj['version']

        fromVal = obj.get('from')
        # 只有当from存在且为字符串且包含目标子串时才保留
        if obj['msg'] == 'Settlement' and substring in fromVal:
            del obj['msg']
            del obj['from']
            print(obj)
    readAndDo(path, fFrom)

def getUidHistory(path, uid):
    global day
    day = 1
    def fUid(obj):
        if obj['uin'] == uid:
            global day
            print('day' + str(day) + ' ' + obj['ext1'])
            if obj['msg'] == 'Settlement':
                print(obj['@timestamp'])
                day += 1
    readAndDo(path, fUid)

if __name__ == '__main__':
    filterFrom('11.10全字段.ndjson', 'sagi.anucs.online')
    # getUidHistory('11.10全字段.ndjson', '1762754691311')