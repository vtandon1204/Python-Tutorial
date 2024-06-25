def addTwo(x):
    return x+2
def substractTwo(num):
    return num-2
def printString(string):
    print(string)
def accleration(mass,force):
    a=mass/force 
    return a
print(addTwo(4))
print(substractTwo(5))
print(accleration(4,2))

def calc_total(exp):
    total = 0
    for item in exp:
        total += item
    return total

vt_exp = [2100,200,2200]
sd_exp = [400,2400,700]

vt_total = calc_total(vt_exp)
sd_total = calc_total(sd_exp)

print("vt total expenses are",vt_total)
print("sd total expenses are",sd_total)