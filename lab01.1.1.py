#overlap appointments

date1 = int(input("which hour starts first date? : "))
dateend1 = int(input("which hour ends first date? : "))
date2 = int(input("which hour start second date? : "))
dateend2 = int(input("which hour end second date? :"))

if date1 > date2:
    s = date1
else:
    s = date2
if dateend1 > dateend2:
    e = dateend1
else:
    e = dateend2

if s < e:
    print("the appointmenrs overlap")
else:
    print("the appointments dont overlap")

