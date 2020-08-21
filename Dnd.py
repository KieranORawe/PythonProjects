import math

str = 10
dex = 10
con = 10
wis = 10
int = 10
cha = 10

str_mod = math.floor((str-10)/2)
dex_mod = math.floor((dex-10)/2)
con_mod = math.floor((con-10)/2)
wis_mod = math.floor((wis-10)/2)
int_mod = math.floor((int-10)/2)
cha_mod = math.floor((cha-10)/2)

stats = {"str":str,"dex":dex,"con":con,"wis":wis,"int":int,"cha":cha}
stats_mod = {"str":str_mod,"dex":dex_mod,"con":con_mod,"wis":wis_mod,"int":int_mod,"cha":cha_mod}

for i in stats:
    print(i,stats[i],stats_mod[i])
