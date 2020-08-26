from neubanner import banner

import pprint

##############################################################################
##############################################################################

TERM = '202110'
STUDID = '001602220'

if banner.login():
    banner.termset(TERM)

    banner.idset(banner.getxyz_studid(STUDID))
    data = banner.studenttaddresses()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
else:
    print("Login Error!")
