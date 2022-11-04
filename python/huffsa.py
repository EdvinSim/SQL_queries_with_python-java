import psycopg2

# MERK: Må kjøres med Python 3

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
    while ch != "3":
        print("\n--[ HUFFSA ]--")
        print("Vennligst velg et alternativ:\n 1. Søk etter planet\n 2. Legg inn forsøksresultat\n 3. Avslutt")

        ch = input("Valg: ")

        if ch == "1":
            planet_sok(conn)
        elif ch == "2":
            legg_inn_resultat(conn)
        elif ch == "3":
            print("Hadet bra :)")
        else:
            print("\nUgyldig kommando!")

def planet_sok(conn: psycopg2):
    cur = conn.cursor()
    molekyl1 = input("Molekyl:")
    molekyl2 = input("Skriv et molekyl til eller trykk enter: ")
    sporring = f"SELECT DISTINCT p.navn, p.masse, s.masse , s.avstand, liv\
            FROM materie AS m\
                INNER JOIN planet AS p ON (m.planet = p.navn)\
                INNER JOIN stjerne AS s ON (p.stjerne = s.navn)\
            WHERE molekyl LIKE '%{molekyl1}%' AND molekyl LIKE '%{molekyl2}%'\
            ORDER BY p.navn;"

    cur.execute(sporring)

    for rad in cur.fetchall():
        if rad[4] == True:
            liv = "Ja"
        else:
            liv = "Nei"
        print(f"\n--PLANET--\nNavn: {rad[0]}\nPlanet-masse: {rad[1]}\
        \nStjerne-masse: {rad[2]}\nStjerne-distanse: {rad[3]}\nBekreftet liv: {liv}")

def legg_inn_resultat(conn):
    # TODO: Oppg 2
    return

if __name__ == "__main__":
    huffsa()
