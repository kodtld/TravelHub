```mermaid
 classDiagram
      
      Index  -- MainFrame
      MainFrame -- HomeUI
      HomeUI <|-- HomeLogic
      HomeLogic <|-- HubUI
      HubUI <|-- HubLogic
      HubLogic <|-- FormatWeather
      HubLogic <|-- FormatNews

       
      Index : LoadMainframe()

      class MainFrame{
  	  Init tkinter()
         Load home_ui()
         }

      class HomeUI{
  	  Init home_ui()
         Place home_ui()
         call_get_geo_code(from home_logic, pass root)
         }

      class HomeLogic{
           root
  	     get_geo_code(turns homeUI entry into latitude and logitude code)
            call_load_hub_UI()
          
         }

      class HubUI{
           root
           cityname
           country
           latitude
           longitude

  	     load_hub_UI()
            call_get_weather(root,lat,long)
            call_get_news(root,cityname)
          
         }

      class HubLogic{
           root

          get_weather(root,lat,long)
  	     get_news(root,cityname)
            
            call_format_weather(root,got_weather)
            call_format_news(root,got_news)
          
         }

      class FormatWeather{
           root
           got_weather

          format_weather_from_lat_lon()
          load_formatted_response_to_root()
          
         }

      class FormatNews{
           root
           got_news

          format_news_from_city()
          load_formatted_response_to_root()
          
         }

```
Luokkakaavio toistaiseksi, ohjelmaa ei ole vielä jaettu erillisiin tiedostoihin joten luokkien nimet ja väliset suhteet tulevat varmasti kokemaan muutoksia sovelluksen edetessä.
Ideana on kuitenkin se että GetGeoCode funktion syötettä "kannetaan" mukana eri funktioiden välillä joita kutsutaan syötteellä.
