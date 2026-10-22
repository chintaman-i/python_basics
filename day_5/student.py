students={101:{"Name":"aditi","scores":[100,90,22]},
          102:{"Name":"sam","scores":[10,90,22]},
          103:{"Name":"ram","scores":[70,90,22]},
          104:{"Name":"ham","scores":[80,90,22]}}

for sid,deatails in students.items():
    avg=sum(deatails["scores"])/len(deatails["scores"])
    deatails["average"]=avg
    deatails["passed"]=avg>=30

    print("students who passed")

    for sid,deatails in students.items():
        if deatails["passed"]:
            print(deatails["Name"])

    #20