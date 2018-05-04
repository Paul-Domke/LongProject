UCS_TIME_CHOICES = (
	("", ("-------")),
	("MWF8", ("MWF 8:00 - 8:50 AM")),
	("MWF9", ("MWF 9:00 - 9:50 AM")),
	("MWF10", ("MWF 10:00 - 10:50 AM")),
	("MWF11", ("MWF 11:00 - 11:50 AM")),
    ("MLAB", ("Mon Lab/Studio 12:30 - 5:00 PM")),
    ("MSEM", ("Mon Seminar 2:00 - 4:50 PM")),
	("MR121", ("MR 12:30 - 1:50 PM")),
	("MR23", ("MR 2:00 - 3:20 PM")),
	("MR34", ("MR 3:30 - 4:50 PM")),
	("MW78", ("MW 7:00 - 8:20 PM")),
    ("M79", ("Mon 7:00 - 9:50 PM")),
	("TR910", ("TR 9:00 - 10:20 AM")),
	("TR1011", ("TR 10:30 - 11:50 AM")),
    ("TLAB", ("Tues Lab/Studio 1:00 - 5:20 AM")),
    ("TSEM", ("Tues Seminar 2:30 - 5:20 AM")),
	("TF12", ("TF 1:00 - 2:20 PM")),
    ("TF23", ("TF 2:30 - 3:50 PM")),
    ("TF45", ("TF 4:00 - 5:20 PM")),
    ("WSEM", ("Wed 12:30 - 3:20 PM")),
    ("W79", ("Wed 7:00 - 9:50 PM")),
    ("RLAB", ("Thurs Lab/Studio 1:00 - 5:20 PM")),
    ("RSEM", ("Thurs Seminar 2:30 - 5:20 PM")),
    ("FLAB", ("Fri Lab/Studio 1:00 - 5:20 PM")),
	("FSEM", ("Fri Seminar 2:30 - 5:20 PM"))
     )

ROOM_CHOICES = (
	("", ("-------")),
	("HNS 114",("HNS 114")),
	("HNS 108",("HNS 108")),
	("HNS 106",("HNS 106")),
	("HNS E167/168",("HNS E167/168")),
	("HNS E169",("HNS E169")),
	("HNS E170",("HNS E170")),
	("LBR 156",("LBR 156")),
	("LBR 209",("LBR 209")),
	("LBR 248",("LBR 248")),
	("LBR 259",("LBR 259")),
	("LBR 252",("LBR 252")),
	("HCL 8",("HCL 8")),
	("HCL 7",("HCL 7")),
	("Palmer 211",("Palmer 211")),
	("Palmer 213",("Palmer 213")),
	("MBR 100",("MBR 100")),
	("MBR 113",("MBR 113")),
	("ACE 102",("ACE 102")),
	("ACE 112",("ACE 112")),
	("ACE 113",("ACE 113")),
	("ACE 115",("ACE 115")),
	("ACE 201",("ACE 201")),
	("ACE 210",("ACE 210")),
	("ACE 211",("ACE 211")),
	("ACE 217",("ACE 217")),
	("ACE 218",("ACE 218")),
	("ACE 228",("ACE 228")),
	("ACE 237",("ACE 237")),
	("ACE 239",("ACE 239")),
	("ACE 327",("ACE 327")),
	("ACE 329",("ACE 329")),
	("CH 214",("CH 214")),
	("Bon",("Bon")),
	("Bon Class",("Bon Class")),
	("COH 120",("COH 120")),
	("CGR 103",("CGR 103")),
	)

LEVEL_CHOICES = (
	("Introductory", ("Introductory")),
	("Intermediate", ("Intermediate")),
	("Advanced", ("Advanced")),
	)

DEPT_CHOICES = (
	("", ("-------")),
	("Anthropology", ("Anthropology")),
    ("Art", ("Art")),
    ("Art History", ("Art History")),
    ("Biology", ("Biology")),
    ("Chemistry", ("Chemistry")),
    ("Computer Science", ("Computer Science")),
    ("Economics", ("Economics")),
    ("Environmental Studies", ("Environmental Studies")),
    ("Gender Studies", ("Gender Studies")),
    ("Geography", ("Geography")),
    ("History", ("History")),
    ("Interdivisional", ("Interdivisional")),
    ("Languages", ("Languages")),
    ("Literature", ("Literature")),
    ("Mathematics", ("Mathematics")),
    ("Music", ("Music")),
    ("Philosophy", ("Philosophy")),
    ("Physics", ("Physics")),
    ("Political Science", ("Political Science")),
    ("Psychology", ("Psychology")),
    ("Religion", ("Religion")),
    ("Sociology", ("Sociology")),
    ("Statistics", ("Statistics")),
    ("Theater", ("Theater")),
    ("Writing", ("Writing")),
	)

TERM_CHOICES = (
	("", ("-----")),
	("Full Term", ("Full Term")),
	("Mod 1", ("Mod 1")),
	("Mod 2", ("Mod 2")), 
	("Full Term Mod Credit", ("Full Term Mod Credit"))
	)

EQUIP_CHOICES = (
	("Whiteboards",("Whiteboards")),
	("Blackboards",("Blackboards")),
	("Projector",("Projector")),
	("Chemistry Lab",("Chemistry Lab")),
	("Biology Lab",("Biology Lab")),
	("Art Studio",("Art Studio")),
	("Computers",("Computers")),
	)

LAC_CHOICES = (
	("Yes", ("Yes")),
	("No", ("No")),
	)

GENDER_CHOICES = (
	("Yes", ("Yes")),
	("No", ("No")),
	)

INTER_CHOICES = (
	("Yes", ("Yes")),
	("No", ("No")),
	)