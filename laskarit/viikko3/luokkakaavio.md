```mermaid
 classDiagram
      Pelilauta -- Pelaaja
      Noppa  <|-- Pelaaja
      Ruutu  <|-- Menevankilaan
      Ruutu  <|-- Aloitusruutu
      Ruutu  <|-- Vankila
      Ruutu  <|-- Sattuma/Yhteismaa
      Ruutu  <|-- Asema
      Ruutu  <|-- Katu
      Ruutu  <|-- Pelaaja
      Ruutu -- Pelilauta
      Kiinteistö -- Katu
      Pelaaja -- Pelinappula
      Ruutu <.. Pelinappula
      Sattumakortti -- Sattuma  

      Pelilauta : Pelaajien määrä  

      class Pelaaja{
          Pelinappula
          Rahat
          Omistetut kiinteistöt  
          Onko vankilassa
          Nopan tulos
          
          Kaupanteko pelaajan kanssa()
          Osta kiinteistö()
          Maksa vuokra()
          Nosta kortti()
          Maksa vankilamaksu()  
      }

      class Pelinappula{
          Hahmo
          Ruutu johon sijoitettu
      }

      class Noppa{
          Heitto(anna numero)
      }

      class Ruutu{
          Nimi
          Seuraava ruutu
          Onko kiinteistö
          Onko vapaa
          Sijainti laudalla
          Toiminto
      }

      class Menevankilaan{
          Lähetä pelaaja vankilaan()
      }
      class Vankila{
          Vapautumismaksun hinta
      }
      class Aloitusruutu{
          Anna pelaajalle rahaa()
      }
      class Sattuma/Yhteismaa{
          Anna kortti()
      }

      class Sattumakortti{
          Sattuma
      }

      class Asema{
          Onko myyty
          Omistava pelaaja
      }

      class Katu{
          Kadunnimi
          Kadun väri
          Kiinteistöt kadulla
          Kiinteistön omistaja
      }

      class Kiinteistö{
          Nimi
          Väri
          Onko myyty
          Hinta
          Vuokran määrä
          Omistaja
      }
```
