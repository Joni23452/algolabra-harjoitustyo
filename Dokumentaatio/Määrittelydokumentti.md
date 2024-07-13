# Määrittelydokumentti
Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT) 

Projektin dokumentaatio on suomeksi. 

Tämä harjoitustyö toteutetaan Pythonilla, enkä hallitse muita ohjelmointikieliä vertaisarviointeja varten. 

Työssä toteutan ohjelman, jolla generoidaan 2D-kartalle erilaisia luolastoja peliä varten. Kartta koostuu kivestä sekä tyhjästä tilasta ja pelissä pelaaja pystyisi kaivamaan kiveä kulkeakseen luolastojen välillä (Harjoitustyö keskittyy kuitenkin vain kartan luomiseen). Kartta jaetaan sektoreihin ja eri sektoreilla luolastoa voidaan generoida eri tavoin, esimerkiksi jollain sektorilla kiveä on tiheästi ja jollain tyhjää tilaa runsaasti.

Kartan jaon sektoreihin ajattelin toteuttaa Voronoi diagrammina käyttäen Fortunen algoritmia ja luolaston generointiin eli kiven ja ilman sijoitteluun ajattelin käyttää erilaisia algoritmeja/funktioita kuten soluautomaatteja, Perlin noisea ja/tai Simplex noisea. Tavoitteena on saada generoitua monipuolista luolastoa, ratkaistaan siis ongelma kuinka saadaan generoitua monipuolinen 2-ulotteinen luolastokartta. 

Aluksi ajattelin toteuttaa ohjelman luomaan vain annetun kokoisen kartan, eli syötteenä ohjelmalla olisi kartan koko (x,y), josta luodaan karttaa kuvaava matriisi. Tätä matriisia iteroidaan kunnes kartta on generoitu. Mikäli onnistuu, ohjelmaa voisi laajentaa luomaan luolastoa loputtomasti pelaajan liikkumisen mukaan jolloin tätä syötettä ei tarvita. Lisäksi syötteenä voisi olla siemenluku jolla alustetaan satunnaislukugeneraattori, jolloin samalla syötteellä saadaan aina sama kartta.

Algoritmin aikavaativuus suhteessa generoidun kartan kokoon. Aluksi kartan jako sektoreihin Fortunen algoritmilla vie aikaa O(n log n) jonka jälkeen kartan jokaiselle pisteelle tehdään jonkin verran operaatioita jotka hyödyntävät vain muutamia läheisiä pisteitä mikä vie aikaa luokkaa O(n). Koskaan ei pitäisi tarvita yhtä pistettä varten hyödyntää koko karttaa! Tavoitteena siis aikavaativuudelle O(n log n).

Harjoitustyön ydin on luonnolliselta vaikuttavaa ja monipuolista maastoa generoivan algoritmin toteutus. 


## Viitteet

https://en.wikipedia.org/wiki/Voronoi_diagram

https://en.wikipedia.org/wiki/Fortune%27s_algorithm

https://fi.wikipedia.org/wiki/Soluautomaatti

https://en.wikipedia.org/wiki/Perlin_noise

https://en.wikipedia.org/wiki/Simplex_noise