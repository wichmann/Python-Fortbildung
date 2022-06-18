
"""
„Heiligabend, die Familie hat sich angekündigt. Du fragst deinen Mitbewohner am
Frühstückstisch nach der Uhrzeit, um feststellen zu können, wann das Chaos über
dich hereinbrechen wird.

Da du deinem Mitbewohner dieses Jahr nichts zu Weihnachten schenkst und er
irgendwie beleidigt ist, antwortet er so: "Wenn du einfach ein Viertel der Zeit
seit Mitternacht bis jetzt zur halben Zeit von jetzt bis Mitternacht
hinzufügst, dann hast du die genaue Uhrzeit."

Grinsend geht er weg und lässt dich mit dem Frühstückstisch abräumen alleine.
Wie spät ist es denn nun?“ [1]

Hilfen
 * Tutorial zur Bibliothek sympy

Quellen
[1] http://www.getdigital.de/community/raetsel/getdigital-adventsraetsel-2014.html
[2] https://docs.sympy.org/latest/tutorial/intro.html

"""

from sympy import *

stunde, minute = symbols('stunde minute')

aussage = (stunde*60+minute) / 4 + ((24-stunde)*60+(60-minute)) / 2

eq1 = Eq(aussage, stunde*60+minute)
eq2 = Eq(minute, 4)

r = linsolve([eq1, eq2], [stunde, minute])
for x in r:
    for y in x:
        print(N(y))
