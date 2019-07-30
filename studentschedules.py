
from neubanner import banner

import collections

##############################################################################
##############################################################################

_DAYS = collections.OrderedDict()
_DAYS["M"] = "Monday"
_DAYS["T"] = "Tuesday"
_DAYS["W"] = "Wednesday"
_DAYS["R"] = "Thursday"
_DAYS["F"] = "Friday"

def _demo_time_to_index(t, start):
	hrm,ampm = t.split(" ")
	hr,m = (int(x) for x in hrm.split(":"))
	isam = ampm=="am"

	index = hr
	if isam is False and hr < 12:
		index += 12

	index *= 10
	if m > 30:
		index += 5

	if start:
		if m == 30:
			index += 5

	if not start:
		if m == 0:
			index -= 5

	return index

def _demo_studentschedule(schedule, xyz, days):
	for entry in schedule:
		for meeting in entry["meetings"]:
			for day in meeting["days"]:
				for tf in range(_demo_time_to_index(meeting["times"][0], True), _demo_time_to_index(meeting["times"][1], False)+1, 5):
					if tf>=80 and tf<200:
						days[day][tf].add(xyz)


def _demo_day(d):
	return "h" if d == "R" else d.lower()

def _demo_time(t):
	return ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"][t-1]

def _demo_schedulelatex(days, people):
	for day,schedule in days.items():
		for slot,attendees in schedule.items():
			count = len(attendees)
			if count > 0:
				color = "class"
				if count >= people/2.:
					color = "office" # red
				elif count >= people/4.:
					color = "away" # yellow
				print("\\slot{}{{{}}}{{\\tc{}{}{}}}{{{}}}{{1}}".format(color, _demo_day(day), _demo_time(slot//10 if slot <= 120 else (slot - 120)//10), "am" if slot < 120 else "pm", "H" if (slot // 5) % 2 == 1 else "",count))

def demoschedules(crns=[], nuids=[]):
	days = {d:{t:set() for t in range(80, 200, 5)} for d in _DAYS.keys()}

	done = set()

	for crn in crns:
		print("== {} ==".format(crn))

		banner.crnset(crn)
		summary = banner.summaryclasslist()

		for student in summary:
			if student['xyz'] not in done:
				done.add(student['xyz'])
				print(student['name_lastfirst'])
				banner.idset(student['xyz'])
				_demo_studentschedule(banner.studentschedule(), student['xyz'], days)

	if nuids:
		print("== {} ==".format('NUIDs'))
		for student in nuids:
			xyz = banner.getxyz_studid(student)
			if xyz not in done:
				done.add(xyz)
				print(student)
				banner.idset(xyz)
				_demo_studentschedule(banner.studentschedule(), xyz, days)

	_demo_schedulelatex(days, len(done))

##############################################################################
##############################################################################

if banner.login():
	banner.termset("202010")

	codes = banner.searchcodes()

	# X's instructor code
	def find_instructor(iname):
		global codes

		iname = iname.lower()
		for icode,instr in codes['sel_instr'].items():
			if iname in instr.lower():
				return icode

	sections = banner.sectionsearch(instructor=[find_instructor('Derbinsky')], subject=['CS', 'DS', 'CY'])
	demoschedules(crns=(s['crn'] for s in sections))

	# sections = banner.sectionsearch(subject=['CS'], coursenum='2500')
	# demoschedules(crns=(s['crn'] for s in sections if s['crn'] != '10461'))

	# demoschedules(crns='10460 11286'.split())
	# demoschedules(nuids = "001203533 001481520".split())

else:
	print("Login Error!")
