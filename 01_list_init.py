## SEZNAMY - LISTS ##

# 01 - INICIALIZACE


def prazdny_seznam():
# Prazdny seznam
    seznam = []
    print(seznam)

prazdny_seznam()

# Seznam obsahujici nejake hodnoty

seznam_jmen = ['Jana','Lenka','Petra','Hanka']
#print(seznam_jmen)



def vypis_jmen(jmena):
# Vypsani hodnot pomoci for cyklu
    for jmeno in seznam_jmen:
        print(jmeno)

#vypis_jmen(seznam_jmen)

# UKOL 01: Vytvor seznam něčeho, co máš rád/a a vytiskni seznam)





# Seznamy muzou obsahovat ruzne datove typy, je to heterogenni datova struktura

def vytvor_typove_nesourody_seznam(polozka):
    typove_nesourody_seznam = ['Je', True, 'ze', 'je', 'dnes', polozka, ['. rijna', 2018,'?']]
    return typove_nesourody_seznam

#print(vytvor_typove_nesourody_seznam(30))
