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
            print("\nHadet bra :)")
        else:
            print("\nUgyldig kommando!")


def planet_sok(conn: psycopg2):
    print("--[ PLANET-SØK ]--")
    cur = conn.cursor()
    molekyl1 = input("Molekyl:")
    molekyl2 = input("Skriv et molekyl til eller trykk enter: ")

        #Hvis det bare skrives et molekyl.
    if molekyl2 == "":
        molekyl2 = molekyl1


    sporring = f"SELECT p.navn, p.masse, s.masse , s.avstand, liv\
            FROM (\
                SELECT DISTINCT planet\
                FROM materie\
                WHERE molekyl LIKE '{molekyl1}'\
                ) AS m1\
                \
                INNER JOIN (\
                SELECT DISTINCT planet\
                FROM materie\
                WHERE molekyl LIKE '{molekyl2}'\
                ) AS m2 USING (planet)\
                \
                INNER JOIN planet as p ON (m2.planet = p.navn)\
                INNER JOIN stjerne AS s ON (p.stjerne = s.navn)\
            ORDER BY s.avstand;"

    cur.execute(sporring)

    for rad in cur.fetchall():
        if rad[4] == True:
            liv = "Ja"
        else:
            liv = "Nei"
        print(f"\n--PLANET--\nNavn: {rad[0]}\nPlanet-masse: {rad[1]}\
        \nStjerne-masse: {rad[2]}\nStjerne-distanse: {rad[3]}\nBekreftet liv: {liv}")

    cur.close()


#Antar at bruker alltid skriver gyldige verdier i alle feltene.
def legg_inn_resultat(conn):
    print("--[ LEGG INN RESULTAT ]--")

    planetnavn = input("Planetnavn: ")

    skummel = input("Skummel j/n: ")
    if skummel == "j":
        skummel = True
    elif skummel == "n":
        skummel = False

    intelligent = input("Intelligent j/n: ")
    if intelligent == "j":
        intelligent = True
    elif intelligent == "n":
        intelligent = False

    beskrivelse = input("Beskrivelse: ")

    cur = conn.cursor()
    sporring = f"UPDATE planet\
                SET skummel = {skummel}, intelligent = {intelligent}, beskrivelse = '{beskrivelse}'\
                WHERE navn = '{planetnavn}'"

    cur.execute(sporring)
    conn.commit()

    oppdatert = f"SELECT * FROM planet WHERE navn = '{planetnavn}'"
    cur.execute(oppdatert)
    for rad in cur.fetchall():
        print(f"\n--OPPDATERT--\nNavn: {rad[0]}\nLiv: {rad[4]}\nSkummel: {rad[5]}\nIntelligent: {rad[6]}\nBeskrivelse: {rad[7]}")

    cur.close()


if __name__ == "__main__":
    huffsa()






"""
Sporring for oppgave 1.

SELECT p.navn, p.masse, s.masse , s.avstand, liv
            FROM (
                SELECT DISTINCT planet
                FROM materie
                WHERE molekyl LIKE 'C2H2'
                ) AS m1

                INNER JOIN
                (
                SELECT DISTINCT planet
                FROM materie
                WHERE molekyl LIKE 'K'
                ) AS m2 USING (planet)

                INNER JOIN planet as p ON (m2.planet = p.navn)
                INNER JOIN stjerne AS s ON (p.stjerne = s.navn)
            ORDER BY s.avstand;
"""
