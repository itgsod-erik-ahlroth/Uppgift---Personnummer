# coding=utf-8
def generate_pnr(dd, mm, ar, kon, ort):
    regionstart = {'Stockholm': 00, 'Kristianstad': 35, 'Kopparberg': 71,
                   'Uppsala': 14, 'Malmöhus': 39, 'Gävleborg': 74,
                   'Södermanland': 16, 'Halland': 46, 'Västernorrland': 78,
                   'Östergötland': 19, 'Västra Götaland': 48, 'Jämtland': 82,
                   'Jönköping': 24, 'Älvsborg': 55, 'Västerbotten': 85,
                   'Kronoberg': 27, 'Skaraborg': 59, 'Norrbotten': 89,
                   'Kalmar': 29, 'Värmland': 62,
                   'Gotland': 32, 'Örebro': 65,
                   'Blekinge': 33, 'Västmanland': 69}

    regionend = {'Stockholm': 13, 'Kristianstad': 38, 'Kopparberg': 73,
                 'Uppsala': 15, 'Malmöhus': 45, 'Gävleborg': 77,
                 'Södermanland': 18, 'Halland': 47, 'Västernorrland': 81,
                 'Östergötland': 23, 'Västra Götaland': 54, 'Jämtland': 84,
                 'Jönköping': 26, 'Älvsborg': 58, 'Västerbotten': 88,
                 'Kronoberg': 28, 'Skaraborg': 61, 'Norrbotten': 92,
                 'Kalmar': 31, 'Värmland': 64,
                 'Gotland': 32, 'Örebro': 68,
                 'Blekinge': 34, 'Västmanland': 70}
    out_pnr = []
    basetot = 0
    M = [1, 3, 5, 7, 9]
    F = [2, 4, 6, 8]

    def twolong(num):
        tal = 0
        for val in map(int, list(str(num))):
            tal += val
        return tal

    def add2(num, listadd):
        if isinstance(num, int):
            num = str(num)
        loop = 1
        for numb in num.split():
            numb = int(numb)
            if loop == 1:
                listadd += numb * loop
                loop = 2
            else:
                listadd += numb * loop
                loop = 1

    def numcheck(manad, dag, kontroll, region, konet, andra):
        temptot = andra
        add2(manad, temptot)
        add2(dag, temptot)
        add2(region, temptot)
        temptot += konet * 2
        temptot += kontroll
        if temptot % 10 == 0:
            return True
        else:
            return False

    def testcheck(manad, dag, kontroll, region, konet, andra):
        temptot = andra
        add2(manad, temptot)
        add2(dag, temptot)
        add2(region, temptot)
        temptot += konet * 2
        temptot += kontroll
        return temptot

    def finnum(num):
        if isinstance(num, str):
            int(num)
        if num < 10:
            num = '0%i' % (num)
        else:
            num = str(num)
        return num

    def manaddagrange():
        for manad in range(1, 12 + 1):
            if manad == 2:
                if ar % 4 == 0:
                    maxdag = 29
                else:
                    maxdag = 28
            elif manad == 4 or 6 or 9 or 11:
                maxdag = 30
            else:
                maxdag = 31
            for dag in range(1, maxdag + 1):
                for kontroll in range(0, 9 + 1):
                    for region in range(regionstart[ort], regionend[ort]):
                        if kon == 'M':
                            for konet in M:
                                if numcheck(manad, dag, kontroll, region, konet, basetot):
                                    outsak = '%s%s%s-%s%s%s' % (
                                        finnum(ar), finnum(manad), finnum(dag), finnum(region), konet, kontroll)
                                    out_pnr.append(outsak)
                        else:
                            for konet in F:
                                if numcheck(manad, dag, kontroll, region, konet, basetot):
                                    outsak = '%s%s%s-%s%s%s' % (
                                        finnum(ar), finnum(manad), finnum(dag), finnum(region), konet, kontroll)
                                    out_pnr.append(outsak)

    def easycreate():
        for kontroll in range(0, 9 + 1):
            for region in range(regionstart[ort], regionend[ort]):
                if kon == 'M':
                    for konet in M:
                        if numcheck(mm, dd, kontroll, region, konet, basetot):
                            outsak = '%s%s%s-%s%s%s' % (
                                finnum(ar), finnum(mm), finnum(dd), finnum(region), konet, kontroll)
                            out_pnr.append(outsak)
                else:
                    for konet in F:
                        if numcheck(mm, dd, kontroll, region, konet, basetot):
                            outsak = '%s%s%s-%s%s%s' % (
                                finnum(ar), finnum(mm), finnum(dd), finnum(region), konet, kontroll)
                            out_pnr.append(outsak)
        return out_pnr

    if isinstance(ar, int):
        basetot += twolong(ar)
        return easycreate()


for personnummer in generate_pnr(19, 4, 68, 'F', 'Gävleborg'):
    print personnummer
