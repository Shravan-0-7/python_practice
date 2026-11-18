students={
    101:{"Name":"Aditi","Scores":[78,85,90]},
    102:{"Name":"Rahul","Scores":[45,60,50]},
    103:{"Name":"Sneha","Scores":[90,88,95]},
    104:{"Name":"Karan","Scores":[55,72,68]},
    105:{"Name":"Priya","Scores":[49,51,47]}
}

for sid,details in students.items():
    avg= sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg>=50

print("Students Who Passed: ")
for sid,details in students.items():
    if details["Passed"]==True:
        print(details["Name"])