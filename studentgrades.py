from neubanner import banner

import pprint

##############################################################################
##############################################################################

if banner.login():
    banner.termset('202110')

    # known crn
    sections = [ { 'crn' : '15177', 'section' : '02'}, { 'crn' : '13902', 'section' : '03'} ]

    for section in sections:
        print(section['crn'])
        banner.crnset(section['crn'])
        for student in banner.summaryclasslist():
            print(student["name_lastfirst"])
            banner.idset(banner.getxyz_studid(student["nuid"]))
            termsdata = banner.studenttranscript()["terms"]
            for term_data in termsdata:
                if term_data["term"] == "Fall 2020 Semester":
                    for course in term_data["courses"]: 
                        if course["course"] == "4500":
                            print(course["grade"])
                    
else:
    print("Login Error!")
