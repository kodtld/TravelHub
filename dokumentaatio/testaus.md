# Testaus

Sovellukselle on kirjoitettu automaattiset testit sekä home_logic-, että hub_logic luokille.

Todellisuudessa home_logic luokan **get_geo_code()** funktion testaaminen on ainoa suorituksen kannalta merkittävä testi, sillä sen hyväksymällä/palauttamalla arvolla on mahdollista suorittaa loput API kutsut.

Tästä huolimatta myös hub_logic luokan funktioille on kirjoitettu validin ja epävalidin syötteen testit. 

## Home_Logic

Home logic luokalla on vain yksi testattava funktio, **get_geo_code()** joka hakee käyttäjän syötteen perusteella kohdekaupunkia vastaavat leveys ja korkeuspiirit, sekä maan nimen.
Toimintaa on testattu sekä validilla että virheellisellä syötteellä.

## Hub_Logic

Hub logic luokan kaikille API kutsuille on kirjoitettu testit jotka kokeilevat kutsujen palautusarvoja niin valideilla, kuin epävalideilla syötteillä.

## Kattavuus

Testien haaraumakattavuus (poislukien UI:sta vastaavat luokat) on 82%, kattavuuden olisi saanut korkeammaksi, jos hub_logic luokan tekstitiedostoihin kirjoittavia funktioita olisi myös testattu.

