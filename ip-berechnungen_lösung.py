
"""
Das Programm soll eine IPv4-Adresse einlesen und auf Korrektheit überprüfen.
Anschließend bestimmt das Programm den Adresstyp (Netzwerkadresse, Host-Adresse,
Broadcastadresse) und berechnet die Netzwerk- und Broadcastadresse des einge-
gebenen Netzwerks.

Mögliche Erweiterungen:
Eine mögliche Erweiterung wäre die Berücksichtigung von IPv6-Adressen.

Hilfen:
 * Handbuch zur mitgelieferten Bibliothek "ipaddress" [1]

Quellen:
[1] https://docs.python.org/3/library/ipaddress.html#ip-network-definitions

"""


import ipaddress


try:
    eingabe = input('Bitte IPv4-Adresse eingeben (z.B. 1.2.3.4/25): ')
    adresse, subnetzmaske = eingabe.split('/')
except ValueError as e:
    print('Die IPv4-Adresse ist unvollständig oder es fehlt die Subnetzmaske (z.B. /24)!')
    exit()

try:
    # erzeuge Objekte für die Adresse selbst und das Netzwerk, in dem sie sich befindet
    netzwerk = ipaddress.ip_network(eingabe, strict=False)
    adresse = ipaddress.ip_address(adresse)
except ValueError as e:
    # gib Fehlermeldung aus, wenn die IP-Adressen ungültig oder fehlerhaft sind
    print('Ungültige IPv4-Adresse, bitte noch einmal versuchen!')

# betimme Netzwerk- und Broadcast-Adresse des Netzwerks und vergleiche mit gegebener Adresse
if adresse == netzwerk.broadcast_address:
    print('Die Adresse ist eine Broadcastadresse!')
elif adresse == netzwerk.network_address:
    print('Die Adresse ist eine Netzwerkadresse!')
else:
    print('Die Adresse ist eine Host-Adresse!')

ausgabe = 'Das Netzwerk beginnt bei {} und endet bei {} und besitzt {} Hostadressen.'
print(ausgabe.format(netzwerk.network_address, netzwerk.broadcast_address, len(list(netzwerk.hosts()))))
