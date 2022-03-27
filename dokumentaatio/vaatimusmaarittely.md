# Vaatimusmäärittely

## Sovelluksen perusidea
Sovellus tarjoaa katsauksen käyttäjän valitsemaan matkustuskohteeseen. 
Tämä katsaus sisältää kohteen valuuttakurssin/muuntajan, kohteen sää-ennusteen tulevilta päiviltä, viimeisemmät uutiset kohteesta,
sekä ajankohtaiset tiedot lentojen hinnoista kohteeseen.

## Käyttöliittymäluonnos
Sovellus koostuu kahdesta näkymästä. Ensimmäisessä näkymässä valitaan matkustuskohde, sekä matkan ajankohta (jos tiedossa).
Toinen näkymä näyttää tiedot kohteesta, sekä sisältää linkkejä ulkoisiin lähteisiin.

KUVA TÄHÄN

## Sovelluksen toiminnallisuus
Sovelluksen tämänhetkinen toiminnallisuus:
- Etusivu
  - Käyttäjä syöttää validin kohde-kaupungin.
  - Käyttäjä valitsee joko lähto-, ja paluupäivämäärän, tai valitsee tehdä haun ilman tarkkaa päivämäärää.
- Sisältösivu
  - Käyttäjä voi syöttää arvoja valuuttamuuntajaan.
  - Käyttäjä näkee kohteen uutiset, lennot, sekä sään. (Uutiset, sekä lennot sisältävät linkit ulkoisiin lähteisiin).
  - Sisältösivulta pääsee "return" painikkeella takaisin etusivulle.

## Jatkokehitysideoita
Sovelluksen toiminta perustuu eri API rajapintojen höydyntämiseen. Tämänhetkinen versio rakentuu näiden ilmaisversiohin,
joissa toiminnallisuus/ominaisuudet ovat rajattuja. Tulevaisuudessa ohjelman toimintaa voisi laajentaa monin tavoin.

- Historiallisen säädatan näyttäminen esim. edellisen vuoden vastaavien päivien säästä.
- Lisätä maakohtaiset uutislähteet, sen sijaan että hakee vain suurimpien englanninkielisten uutislähteiden julkaisut.
- Lisätä kohteen suositut ja vapaat hotellit/AirBnb:t valituille päiville.
- Mahdollisuus vertailla matkakohteita keskenään.
- Näkymä joka näyttää hyödylliset "peruslauseet" kohdemaan kielellä.
- Museo, ravintola, tapahtuma, jne. suositukset kohteesta.
- Yms. Jatkokehitysmahdollisuudet ovat melkein rajattomat. Kehityksen suuntana olisi näyttää mahdollisimman tarkka ja ajankohtainen "ote" kohteen tämänhetkisestä tilasta ja elämästä.
