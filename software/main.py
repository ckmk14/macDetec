TEST = ['08:00:27:dd:50:c5',
        '08:00:27:3e:a0:1a',
        '00:1c:06:35:c0:7c',
        '00:01:23:2d:bd:7b',
        '00:30:de:0c:ae:68',
        '00:80:f4:0e:59:bc',
        '00:30:de:0c:aa:6c',
        '00:24:59:0a:58:b0',
        '84:ac:fb:00:05:e6',
        'e0:dc:a0:1c:35:4f',
        '00:a0:45:9d:42:54',
        '00:90:e8:56:78:5d',
        '00:30:de:41:b9:e6',
        '00:1c:06:35:c0:7b',
        '28:63:36:c6:cc:67',
        '28:63:36:c6:c7:d4',
        '00:90:e8:2a:e5:34',
        '00:01:23:2d:ba:a3',
        '00:80:f4:0e:58:89',
        'e0:dc:a0:1c:35:85',
        '84:ac:fb:00:05:e0']

from modules import an_database
from modules import an_mac

if __name__ == "__main__":
    OUILIST = an_database.search_dic("oui.txt")
    DEVLIST = an_database.get_device_list("../database/")

    result = an_mac.classify(TEST, OUILIST, DEVLIST)
    print(result)
