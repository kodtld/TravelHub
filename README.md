# TravelHUB
Sovellus tarjoaa katsauksen käyttäjän valitsemaan matkustuskohteeseen. Tämä katsaus sisältää kohteen valuuttakurssin/muuntajan, kohteen sää-ennusteen tulevilta päiviltä, viimeisemmät uutiset kohteesta, sekä ajankohtaiset tiedot lentojen hinnoista kohteeseen.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivi

### Asennus

 Sovelluksen käynnistämistä varten tarvittavat riippuvuudet asennetaan komennolla:

```bash
poetry install
```

### Suorita ohjelma

```bash
poetry run invoke start
```
### Ohjelman testaus

Allaolevan komennon syötettyäsi ohjelma käynnistää itsensä uuteen ikkunaan, voit vain sulkea avatun ikkunan heti sen auettua, niin testit suoritetaan automaattisesti.

```bash
poetry run invoke test
```
### Testikattavuusraportti

```bash
poetry run invoke coverage-report
```
Raportti löytyy htmlcov-hakemistosta.

### Pylint testaus

Pylint testauksen voi ajaa komennolla:
```bash
poetry run invoke lint
```
