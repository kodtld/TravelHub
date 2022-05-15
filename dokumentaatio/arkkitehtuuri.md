# Sovellusarkkitehtuuri

## Rakenne

**UI** vastaa käyttöliittymästä, se sisältää myös kutsut **Logic** pakkaukseen, joka vastaa API kutsuista, sekä muista sovelluslogiikan operaatioista.
**Logic** pakkaus käyttää hyväkseen **Data Files** pakkauksen sisältämiä tiedostoja, jossa säilytetään tietoa valuuttakursseista, sekä tietoa viimeisen kutsun päivämäärästä.
Saatuaan palautuksen **Logic** pakkaukselta, **UI** kutsuu **API Format** pakkausta, joka vastaa API kutsujen palautteen asettelusta yms.

![](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pack.png)

## Käyttöliittymä

Käyttöliittymä sisältää kaksi näkymää, ensimmäisessä näkymässä syötetään kohdekaupunki, toisessa ns. "päänäkymässä" on tiedot kohteesta. Päänäkymä sisältää myös linkkejä ulkoisiin lähteisiin.

## Sovelluslogiikka

Sovelluksen toiminta perustuu kahden UI tiedoston lähettämiin kutsuihin. Home UI kutsuu HomeLogic tiedostoa saadakseen kohdekaupungin korkeus ja leveyspiirit, mikäli HomeLogic API kutsu epäonnistuu, pyydetään käyttäjältä uutta syötettä. Mikäli kutsu on suotuisa, antaa HomeUI palautuksen HUBUI:lle tätä kutsuessaan.

HUBUI taas kutsuu HUBLogic tiedostoa, joka vastaa HUB sivun API kutsuita ja muusta logiikasta. HUBLogic hakee tarpeelliset tiedot API kutsuilla ja palauttaa ne HUBUI tiedostolle. Valuuttakurssien kohdalla suoritetaan ensin kutsu cur_code_by_a2.txt tiedostoon, joka palauttaa kohdemaan valuuttakoodin HomeLogic(get_geocode) funktion palauttaman maakoodin pohjalta. Kun valuuttakoodi on haettu, suoritetaan tarkistus viimeisen API kutsun päivämäärästä.

Mikäli viimeinen valuuttakutsu on yli päivän vanha, lähetetään uusi API kutsu, jonka palautus kirjoitetaan kyseisen päivämäärän kanssa latest_cur.txt tiedostoon. Tämän jälkeen lates_cur.txt tiedostosta haetaan kohdemaan valuutakurssi Euroon nähden, jonka jälkeen se palautetaan HUBUI:lle.

Kun tarpeelliset kutsut on suoritettu ja tiedot saatu HUBLogic:ilta, HUBUI kutsuu FormatAPI pakkauksen sisältämiä tiedostoja, jotka vastaavat aihekohtaisesti API vastausten lopullisesta asettelusta, fonttikoosta yms. käyttöliittymän ulkoasuun liittyvistä tekijöistä. 

Alla ohjelman kutsulogiikka kokonaisuudessaan:


```mermaid
 classDiagram
      
      Index  -- MainFrame
      MainFrame <|-- HomeUI
      HomeLogic <|-- HomeUI
      HomeUI <|-- HubUI
      HubLogic <|-- HubUI
      HubLogic -- Latest_cur_txt
      HubLogic -- Cur_code_by_a2_txt
      HubUI ..	HomeUI
      HubUI <|-- FormatWeather
      HubUI <|-- FormatNews
      HubUI <|-- FormatAttractions
      HubUI <|-- FormatCurrency

       
      Index : LoadMainframe()

      class MainFrame{
  	  Init tkinter()
         Load home_ui()
         }

      class HomeUI{
           tk.root
  	  Init home_ui()
         Place home_ui()
         call_get_geo_code(from home_logic, pass root)
         }

      class HomeLogic{
          
  	     get_geo_code(turns homeUI entry into latitude and logitude code)
            call_load_hub_UI()
          
         }

      class HubUI{
           tk.root
           cityname
           country
           latitude
           longitude

  	     load_hub_UI(hub_root)
            call_get_weather(root,lat,long)
            call_get_news(root,cityname)
            call_return_to_home_ui(from hub_logic)
            call_format_weather(root,got_weather)
            call_format_news(root,got_news)
            call_format_currency(root,amount,country,currency_name,currency_code)
            call_format_attractions(root,got_attractions)
            return_to_home_ui()
         }

      class HubLogic{

          get_weather(root,lat,long)
  	  get_news(root,cityname)
          get_currency()
	  get_attractions()
	  Write and read files()  
          
         }

      class FormatWeather{
           hub_root
           got_weather

          format_weather_from_lat_lon()
          load_formatted_response_to_root()
          
         }

      class FormatNews{
           hub_root
           got_news

          format_news_from_city()
          load_formatted_response_to_root()
          
         }


      class FormatCurrency{
           hub_root
           currency info

          format_currency_data()
          load_formatted_response_to_root()
          check_for_last_request()
         }


      class FormatAttractions{
           hub_root
           got_attractions

          format_attractions_for_city()
          load_formatted_response_to_root()

         }

     
      class Latest_cur_txt{
           Date of last request
	   Exchange rate of euro --> all currencies

         }

      class Cur_code_by_a2_txt{
           Holds information of currency name
	   Information of currency code by country code

         }
```

## Tiedon tallennus

API tietokantojen lisäksi ohjelma hyödyntää kahta sisäistä tekstitiedostoihin tallennettua tietokantaa.

### latest_cur.txt

Sisältää tiedon viimeisestä suoritetusta API kutsusta formaatissa:

```
Latest_request,DD-MM-YYYY 
``` 

Sekä viimeisen suoritetun kutsun palautuksen, joka sisältää valuuttakoodit ja niiden suhteen Euron hintaan formaatissa:

```
AED,3.823892
AFN,91.614523
ALL,120.608353
...
```
### cur_code_by_a2.txt

Sisältää maiden virallisen nimen, a2 koodin (kaksinumeroinen maakoodi joka vastaa HomeLogicin palauttamaa maakoodia, ja jonka avulla kyseisen maan valuuttakoodi saadaan), maan valuutan nimen, sekä maan valuuttakoodin formaatissa:

```
Afghanistan,AF,Afghani,AFN	
Albania,AL,Lek,ALL
Algeria,DZ,Algerian Dinar,DZD
...
```
## Ohjelman toiminnallisuus

Ohjelman toiminnallisuus sekvenssikaavioin kuvattuna:

### Take me there!

Etusivun syötekenttään kirjoitetun kohteen tiedot haetaan seuraavalla tavalla:

```mermaid
sequenceDiagram
  actor User
  participant Home_UI
  participant Home_Logic
  participant Hub_UI
  participant Hub_Logic
  participant Format_Weather
  participant Format_News
  participant Format_Currency
  participant Format_Attractions
  participant latest_cur.txt
  participant cur_code_by_a2.txt
  User->>Home_UI: Type location and press "Take me there!" button.
  Home_UI->>Home_Logic: get_geocode(city name)
  Home_Logic-->>Home_UI: latitude, longitude, cityname, country
  Home_UI->>Home_UI: load_home_ui()
  Home_UI->>Hub_UI: load_hub_ui(latitude, longitude, cityname, country)
  Hub_UI->>Hub_Logic: get_weather(latitude, longitude)
  Hub_Logic-->>Hub_UI: weather_data
  Hub_UI->>Format_Weather: format_weather(weather_data)

  Hub_UI->>Hub_Logic: get_news(cityname)
  Hub_Logic-->>Hub_UI: news_data
  Hub_UI->>Format_News: format_news(news_data)

  Hub_UI->>Hub_Logic: setup_currency_code(country)
  Hub_Logic->>cur_code_by_a2.txt: a2 country code
  cur_code_by_a2.txt-->>Hub_Logic: country, currency_name, currency_code
  Hub_Logic-->>Hub_UI: coutry, currency_name, currency_code
  Hub_UI->>Hub_Logic: check_currency()
  Hub_Logic->>lates_cur.txt: datetime current date, currency_code
  latest_cur.txt-->>Hub_Logic: currency_code, exchange_rate
  Hub_Logic-->>Hub_UI: latest_cur.txt
  Hub_UI->Hub_Logic: get_currency(amount, country, currency_name, currency_code)
  Hub_Logic-->>Hub_UI: exchange_rate
  Hub_UI->>Format_Currency: format_currency(country, currency_name, amount, exhange_rate)

  Hub_UI->>Hub_Logic: get_attractions(latitude, longitude, cityname)
  Hub_Logic-->>Hub_UI: attractions_data
  Hub_UI->>Format_Attractions: format_attractions(attractions_data)

```

### Return

Kun HUB sivulla painetaan "return" painiketta, latautuu etusivu takaisin seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant Hub_UI
  participant Home_UI

  User->>Hub_UI: Press "return" button.
  Hub_UI->>Hub_UI: self.load_back()
  Hub_UI->>Home_UI: home_ui.place_ui()
  Home_UI->>Home_UI: load_home_ui()
```
