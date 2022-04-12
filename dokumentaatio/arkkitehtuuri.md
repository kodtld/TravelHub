```mermaid
 classDiagram
      
      HomeFrame  <|-- MainFrame
      

      HomeFrame : Syötä kaupunki  
      HomeFrame : GetGeoCode()

      class MainFrame{
  	  Syötekaupungin nimi
          GetGeoCode kutsun palauttamat kaupungit koordinaatit  
          GetWeather() Hakee kaupungin sään koordinaattien perusteella
	  Tulevaisuus() Tulevaisuudessa kutsuu muita funktioita/luokkia syötekaupungin nimellä
          }

```
Luokkakaavio toistaiseksi, ohjelmaa ei ole vielä jaettu erillisiin tiedostoihin joten luokkien nimet ja väliset suhteet tulevat varmasti kokemaan muutoksia sovelluksen edetessä.
Ideana on kuitenkin se että GetGeoCode funktion syötettä "kannetaan" mukana eri funktioiden välillä joita kutsutaan syötteellä.
