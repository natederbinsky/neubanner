from neubanner import banner

import pprint

##############################################################################
##############################################################################

banner.login()
banner.termset('201830')

codes = banner.searchcodes()

# X's instructor code
def find_instructor(iname):
	global codes

	iname = iname.lower()
	for icode,instr in codes['sel_instr'].items():
		if iname in instr.lower():
			return icode

pp = pprint.PrettyPrinter(indent=4)

# find by course
sections = banner.sectionsearch(coursenum='2500', subject=['CS'])

# find by instructor
# sections = banner.sectionsearch(instructor=[find_instructor('Derbinsky')], subject=['%', '%'])

pp.pprint(sections)

for section in sections:
	banner.crnset(section['crn'])
	for student in banner.summaryclasslist():
		print("\"{}\",\"{}\",\"{}\"".format(section["section"], student["name_lastfirst"], student["nuid"]))
