#!/usr/bin/env python
MAX_DISTANCE = int("FFFFFF", 16)


def classify(MACLIST, OUILIST, DEVLIST):
    result = dict.fromkeys(MACLIST)
    for address in MACLIST:
        result[address] = dict.fromkeys(['oui', 'product', 'vendor', 'likelihood'])
        # Mac Distance FFFFFF is the a vendor group
        min_mac_distance = int("FFFFFF", 16)
        min_mac_product = ""
        min_mac_vendor = ""
        p_mac = address[0:2] + address[3:5] + address[6:8]
        for ouientry in OUILIST:
            for ouikey, ouivalue in ouientry.items():
                if ouikey == "oui":
                    if ouivalue == p_mac.upper():
                        result[address]['oui'] = ouientry.get('company')
                        for refdev in DEVLIST:
                            for devkey, devvalue in refdev.items():
                                if devkey == "mac":
                                    devvalue = devvalue.replace(":", "")
                                    pcapvalue = address.replace(":", "")
                                    mac_distance = int(devvalue, 16) - int(pcapvalue, 16)
                                    if min_mac_distance > abs(mac_distance):
                                        min_mac_distance = abs(mac_distance)
                                        min_mac_product = refdev.get('product')
                                        min_mac_vendor = refdev.get('vendor')
                        result[address]['product'] = min_mac_product
                        result[address]['vendor'] = min_mac_vendor
                        result[address]['likelihood'] = (MAX_DISTANCE - min_mac_distance) / MAX_DISTANCE
    return result
