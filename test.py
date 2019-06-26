import sqlite3
import sys

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect('./resume.db')
db.row_factory = dict_factory
# classes = db.execute("SELECT * FROM Classes").fetchall()

# for c in classes:
#     print(c)


# print("\n\nALL UPPER LEVEL CLASSES \n")

# classes = db.execute("SELECT * FROM Classes WHERE Code LIKE '__3%' OR Code LIKE '__4%'").fetchall()

# for c in classes:
#     print(c)


# print("\n Is CS-y\n ")
# classes = db.execute("SELECT * FROM Classes WHERE IsCSy=1").fetchall()

# l="Relevent Courses: "
# for c in classes:
#     l=l+c["Name"]+", "

# l=l[:-2]

# print(l)


# lang = db.execute("SELECT Name FROM Skills WHERE Rating>1 AND (Type='Language' OR Type='Framework') ").fetchall()
# print(lang)

# misc = db.execute("SELECT NAME FROM Skills WHERE Rating>1 AND NOT (Type='Language' OR Type='Framework') ").fetchall()
# print(misc)



def print_preamble():

    print("\\documentclass[letterpaper,11pt]{article}\n%-----------------------------------------------------------\n%Margin setup\n\n\\setlength{\\voffset}{0.1in}\n\\setlength{\\paperwidth}{8.5in}\n\\setlength{\\paperheight}{11in}\n\\setlength{\\headheight}{0in}\n\\setlength{\\headsep}{0in}\n\\setlength{\\textheight}{11in}\n\\setlength{\\textheight}{9.5in}\n\\setlength{\\topmargin}{-0.25in}\n\\setlength{\\textwidth}{7in}\n\\setlength{\\topskip}{0in}\n\\setlength{\\oddsidemargin}{-0.25in}\n\\setlength{\\evensidemargin}{-0.25in}\n%-----------------------------------------------------------")
    print("\n\\usepackage{tcolorbox}\n%\\usepackage{fullpage}\n%\\usepackage{shading}\n%\\textheight=9.0in\n\\pagestyle{empty}\n\\raggedbottom\n\\raggedright\n\\setlength{\\tabcolsep}{0in}\n\n%-----------------------------------------------------------\n%Custom commands\n\\definecolor{yeetGreen}{HTML}{C1FFC4}")
    print("\n\\newtcolorbox{trixiematel}[1][]\n{\n    colframe=blue!50!black, colback=lightgray,\n  #1,\n}\n\\newcommand{\\resitem}[1]{\\item #1 \\vspace{-2pt}}\n\\newcommand{\\resheading}[1]{ \\begin{trixiematel}\\textbf{#1}\\end{trixiematel}}\n\\newcommand{\\ressubheading}[4]{\n\\begin{tabular*}{6.5in}{l@{\\extracolsep{\\fill}}r}\n                \\textbf{#1} & #2 \\\\\n                \\textit{#3} & \\textit{#4} \\\\\n\\end{tabular*}\\vspace{2pt}}")
    print("\n\\newcommand{\\Heading}[5]{\n    \\begin{tabular*}{7in}{l@{\\extracolsep{\\fill}}r}\n        \\textbf{\\Large #1}  & #2\\\\\n        #3 & #4 \\\\\n        & #5 \\\\\n        \\end{tabular*}}\n%-----------------------------------------------------------")

    print("\n\n\\begin{document}")


def print_header():
    head=db.execute("SELECT * FROM Personal").fetchall()[0]

    print("\\Heading{"+str(head["FirstName"])+" "+str(head["LastName"])+"}{"+str(head["PhoneNumber"])+"}{"+str(head["ProfessionalEmail"])+"}{"+str(head["PersonalURL"])+"}{"+str(head["GithubURL"])+"}")
    print("\vspace{0.1in}")

def print_education():
    edustring="\\reshading{Education}\n\\begin{description}\n"
    edus=db.execute("SELECT * FROM Education").fetchall()
    for edu in edus:
        edustring=edustring+"\\item\n\\ressubheading{"+str(edu["School"])+"}{"+str(edu["Location"])+"}{"+str(edu["Degree"])+"}{"+str(edu["Started"])+" - "+str(edu["Completed"])+"} \n\n\n"
        
        edustring+="Relevant Courses: "
        classes=db.execute("SELECT * FROM Classes WHERE IsCSy=1").fetchall()
        for c in classes:
            edustring+=c["Name"]+", "
        edustring=edustring[:-2]+"\n\n"

    edustring+="\\end{description}"
    print(edustring)

print_education()


