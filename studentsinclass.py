from neubanner import banner

import pprint

##############################################################################
##############################################################################

banner.login()
banner.termset('201830')

codes = None

# X's instructor code
def find_instructor(iname):
	global codes
	if codes is None:
		codes = banner.searchcodes()

	iname = iname.lower()
	for icode,instr in codes['sel_instr'].items():
		if iname in instr.lower():
			return icode

def csvout(*args):
	return ",".join(['"{}"'.format(a) for a in args])

pp = pprint.PrettyPrinter(indent=4)

# find by course
sections = banner.sectionsearch(coursenum='2500', subject=['CS'])

# find by instructor
# sections = banner.sectionsearch(instructor=[find_instructor('Derbinsky')], subject=['%', '%'])

# pp.pprint(sections)

for section in sections:
	banner.crnset(section['crn'])
	for student in banner.summaryclasslist():
		# no e-mail (fast!)
		print(csvout(section["section"], student["name_lastfirst"], student["nuid"], "Withdraw" not in student["regstatus"]))

		# with e-mail (per-student request)
		# banner.idset(student["xyz"])
		# print(csvout(section["section"], student["name_lastfirst"], student["nuid"], banner.studentemail()))
