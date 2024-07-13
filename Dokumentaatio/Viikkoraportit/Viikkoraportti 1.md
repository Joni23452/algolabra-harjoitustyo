# Viikkoraportti 1

## Mitä olen tehnyt tällä viikolla?

Olen valinnut harjoitustyön aiheen, tutkinut aihetta, alustanut projektin repositorion ja laatinut määrittelydokumentin. 

Aikaa käytetty tällä viikolla ~12h 

## Miten ohjelma on edistynyt?

En ole vielä aloittanut ohjelman luomista. 

## Mitä opin tällä viikolla / tänään?

Olen oppinut kuinka pelikartan proseduraalinen generointi voidaan käytännössä totetuttaa ja minkälaisia algoritmeja ja funktioita tässä voi hyödyntää. Olen myös saanut selville kuinka soluautomaatin voi käytännössä toteuttaa ja ymmärtänyt ainakin jossakin määrin teoriassa kuinka Perlin noise ja Fortunen algoritmi toimivat. 

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Fortunen algoritmin toteutus ja hyödyntäminen käytännössä on vielä hieman epäselvää. Pohdin olisiko sittenkin kannattavampaa jakaa kartta sektoreihin laskemalla jokaiselle kartan kohdalle etäisyydet kaikkiin sektoripisteisiin sillä sektoripisteitä kuitenkin ajattelen olevan hyvin vähän suhteessa kartan kokoon. Tai voisiko tässä laskea kerran yhden kohdan etäisyyden jokaiseen sektoripisteeseen ja pitää näitä etäisyyksiä muistissa ja seuraaville kohdille laskea vain etäisyydet edellisen pisteen lähimmille sektoreille? 

## Mitä teen seuraavaksi?

Laitan pystyyn ohjelmalle tavan graafisesti piirtää halutun kokoista karttaa ja asettaa kartalle kiveä/ilmaa ja aloitan kartan sektoreihin jaon toteuttamisen. Lisäksi haluaisin saada tavan liikuttaa karttaa nuolinäppäimistä ja zoomata karttaa lähemmäs/kauemmas. Grafiikoiden piirto pythonilla ei ole minulle kovin tuttua entuudestaan, joten ajattelin käyttää pygame kirjastoa tähän sillä sitä on käytetty aiemmilla kursseilla mutta olisiko ohjaajilla jotain muita kirjasto ehdotuksia tähän tarkoitukseen? 