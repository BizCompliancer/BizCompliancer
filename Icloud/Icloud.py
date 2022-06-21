import pyicloud
from shutil import copyfileobj
import sys
sys.path.append("../..")
from PythonCore.scripts.nord_script import NordScript

api = pyicloud.PyiCloudService("sd7079269117@gmail.com")
#

nord_vpn = NordScript("biz_complaincer")

nord_vpn.connect("no")

nord_vpn.disconnect()

# with open('test.txt', 'rb') as file_in:
#     api.drive['testing'].upload(file_in)
file = 'test.txt'
with open('test.txt', stream=True) as response:
    with open('test.txt', 'wb') as file_out:
        copyfileobj(response.raw, file_out)
