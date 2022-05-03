## Viikko 3

- Etusivulle lisätty entrybox käyttäjän syötteelle
- Etusivulla oleva painike käynnistaa Geocoding APIn, joka hakee syötettä vastaavat koordinaatit myöhemmin lisättävää Weather API:ta varten
- Automaattiset testit lisätty validille ja invalidille syötteelle
- Ohjelmalla ei vielä visuaalista feedbäkkiä syötteen oikeudesta

## Viikko 4

- Ohjelmaan lisätty ensimmäinen lopullinen toiminnallisuus, joka palauttaa hakukohteen seuraavien päivien sään
- Kotinäyttö siirretty luokkaan HomeFrame ja päänäyttö rakennettu luokkaan MainFrame
- Sovelluslogiikan ja UI:n jakaminen erillisiin tiedostoihin on osoittautunut erittäin haasteellisesksi joten toistaiseksi sovellus on edelleen kokonaisuudessaan main.py tiedostossa (korjataan mahdollisimman pian)
- Epävalidille syötteelle lisätty visuaalinen feedback
- Pylint otettu käyttöön

## Viikko 5

- Lisätty News_Api joka hakee kohteen uutiset, ja näyttää ne käyttäjälle
- Ohjelma toiminta hajautettu erillisiin tiedostoihin
- Sovelluksen rakenne muuttunut huomattavasti:
- UI elementit "ui" kansiossa
- Sovelluslogiikka "logic" kansiossa
- API kutsujen formatointi/järjestys "api_format" kansiossa

## Viikko 5 (toinen vaihe)

- Lisätty Currency_Api joka hakee kohteen valuutan ja muuntaa sen suhteessa euroihin
- Lisätty tiedosto johon tallennetaan päiväkohtaisesti kaikki valuuttakurssit euroon suhteutettuna
- Alkuperäisen suunnitelmaan tehty muutos:
- Lentojen hakeminen osoittautui ilmaisten API:den läpi mahdottomaksi
- Lentojen hakeminen korvattu kohteen suosittujen nähtävyyksien haulla
- Nähtävyyksien hakeminen lisätty Attractions_Api:n muodossa 

## Viikko 6

- Koodin rakennetta muokattu oleellisesti jotta testien kirjoittaminen on päästy aloittamaan
- Format_Weather ja Format_News, Format_Attractions luokkien sisältö vähentynyt yli sadalla rivillä
- Käyttöliittymän ja UI:n erottelu entistä paremmassa vaiheessa
- Ensimmäiset testit lisätty
- Kutsumarakenne muuttunut, pian logiikka täysin erillään UI:sta
- Get_News formatointia hieman kehitetty jotta pidemmät uutiset mahtuvat ruudulle paremmin
- Format_Currency osalta eroteltu UI ja logiikka (tästä aiheutui ongelma, jossa valuuttamuunnoksen haku uudestaan ei onnistu)((korjataan mahdollisimman pian))
