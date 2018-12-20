# coding=utf-8

a = 1
def NOchangeValue(a):
    a = a + 1
    return a
NOchangeValue(a)
print a


def MenCopy():
    data_1 = []
    json_data = {
            'x':'',
            'y':'',
            'z':'',
        }
    all_info = [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}]
    for test_infos in all_info:
        # json_data = json_data.copy()
        json_data['x'] = test_infos.get('a')
        json_data['y'] = test_infos.get('b')
        json_data['z'] = test_infos.get('c')
        data_1.append(json_data)
    print data_1