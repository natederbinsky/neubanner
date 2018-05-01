from neubanner import banner

import pprint

##############################################################################
##############################################################################

TERM = '201910'
STUDID = '001602220'

banner.login()
banner.termset(TERM)

banner.idset(banner.getxyz_studid(STUDID))
data = banner.studenttranscript()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
