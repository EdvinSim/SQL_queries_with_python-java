import psycopg2

# MERK: Må kjøres med Python 3
#Oppdatert TODO fjern

user = 'edvinas' # Sett inn ditt UiO-brukernavn ("_priv" blir lagt til under)
pwd = 'avahreeW2e' # Sett inn passordet for _priv-brukeren du fikk i en mail

connection = \
    "dbname='" + user + "' " +  \
    "user='" + user + "_priv' " + \
    "port='5432' " +  \
    "host='dbpg-ifi-kurs03.uio.no' " + \
    "password='" + pwd + "'"

def huffsa():
    conn = psycopg2.connect(connection)
    
    ch = 0
    while (ch != 3):
        print("--[ HUFFSA ]--")
        print("Vennligst velg et alternativ:\n 1. Søk etter planet\n 2. Legg inn forsøksresultat\n 3. Avslutt")
        ch = int(input("Valg: "))

        if (ch == 1):
            planet_sok(conn)
        elif (ch == 2):
            legg_inn_resultat(conn)
    
def planet_sok(conn):
    # TODO: Oppg 1
    return

def legg_inn_resultat(conn):
    # TODO: Oppg 2
    return

if __name__ == "__main__":
    huffsa()
