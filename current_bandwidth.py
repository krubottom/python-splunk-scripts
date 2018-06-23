from snmp_helper import snmp_get_oid,snmp_extract
from time import sleep
import datetime

COMMUNITY_STRING = 'public'
SNMP_PORT = 161
a_device = ('192.168.1.1', COMMUNITY_STRING, SNMP_PORT)

def get_bandwidth(delay):
    snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.2.2.1.10.4', display_errors=True)

    first_data = snmp_extract(snmp_data)

    sleep(delay)

    snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.2.2.1.10.4', display_errors=True)

    second_data = snmp_extract(snmp_data)

    bps = ((float(second_data) - float(first_data))*8)/delay
    
    mbps = bps/1024/1024
    
    mbps = round(mbps,2)

    return mbps


print get_bandwidth(30)