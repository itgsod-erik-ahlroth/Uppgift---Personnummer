# coding=utf-8

def valid_pnr(personnummer):
    """
    :param personnummer: "ÅÅMMDDXXYZ" in string
    :return: True or False
    """
    if isinstance(personnummer,int):
        personnummer = str(personnummer)
    if isinstance(personnummer, str):
        if len(personnummer) != 10:
            return False

        nummer = map(int,list(personnummer))

        vaxel = 2; tot = 0
        for sif in nummer:
            int(sif)
            if isinstance(sif,str):
                return True
            if sif * vaxel > 9:
                for val in map(int,list(str(sif*vaxel))):
                    tot += val
            else:
                tot += sif * vaxel
            if vaxel == 1:
                vaxel = 2
            elif vaxel == 2:
                vaxel = 1
        if tot% 10 == 0:
            return True
        else:
            return False

pernum = raw_input('Skriv personnummer')
if valid_pnr(pernum):
    print "Du har ett korrekt personnummer"
elif valid_pnr(pernum) == False:
    print "Du har ett felaktigt personnummer (?)"
else:
    "?????"