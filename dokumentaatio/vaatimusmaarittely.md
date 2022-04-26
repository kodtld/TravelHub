# Vaatimusmäärittely

## Sovelluksen perusidea
Sovellus tarjoaa katsauksen käyttäjän valitsemaan matkustuskohteeseen. 
Tämä katsaus sisältää kohteen valuuttakurssin/muuntajan *TEHTY*, kohteen sää-ennusteen *TEHTY* tulevilta päiviltä, viimeisemmät uutiset kohteesta *TEHTY*,
sekä tiedot kohteen nähtävyyksistä *TEHTY*.

## Käyttöliittymäluonnos
Sovellus koostuu kahdesta näkymästä."TEHTY" Ensimmäisessä näkymässä valitaan matkustuskohde.
Toinen näkymä näyttää tiedot kohteesta, sekä sisältää linkkejä ulkoisiin lähteisiin.

![](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/kayttoliittyma_draft.png)

## Sovelluksen toiminnallisuus
Sovelluksen tämänhetkinen toiminnallisuus:
- Etusivu
  - Käyttäjä syöttää validin kohde-kaupungin."TEHTY"
  - Mikäli kohde ei ole validi, pyytää ohjelma uutta syötettä
- Sisältösivu
  - Käyttäjä voi syöttää arvoja valuuttamuuntajaan.
  - Käyttäjä näkee kohteen uutiset *TEHTY*, nähtävyydet*TEHTY* (alkuperäinen suunnitelma oli lennot, mutta sopivaa API:ta ei löytynyt) ,Valuuttamuuntajan *TEHTY* , sekä sään*TEHTY*. (Uutiset, sekä nähtävyydet sisältävät linkit ulkoisiin lähteisiin).
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
