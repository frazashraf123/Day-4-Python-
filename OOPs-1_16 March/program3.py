#Q2
def speciality(med_list,med_spec):
    max_visit=0
    P=med_list.count('P')
    O=med_list.count('O')
    E=med_list.count('E')
    if P>E and P>O:
        sp = med_spec['P']
    elif E>O:
        sp = med_spec['E']
    else:
        sp=med_spec['O']
    return sp
p_list=[301,'P',302,'P',305,'P',401,'P',656,'E']
d={"P":"Pediatrics","O":"Orthopeics","E":"ENT"}
sp=speciality(p_list,d)
print(sp)

p_list="301,'P',302,'P',305,'P',401,'P',656,'E'"
print((p_list).split(","))

