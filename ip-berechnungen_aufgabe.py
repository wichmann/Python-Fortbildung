
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


eingabe = input('Bitte IPv4-Adresse eingeben (z.B. 1.2.3.4/25): ')
adresse, subnetzmaske = eingabe.split('/')

adresse = ipaddress.ip_address(adresse)
