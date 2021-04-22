from kivy.app import App
from kivy.lang.builder import Builder
import json
import time
from kivy.core.window import Window
import requests
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen,WipeTransition
import webbrowser
from kivy.animation import Animation
from kivy.uix.button import Button


Builder.load_file('main.kv')
class P(Screen):
    pass
class Z(Screen):
    pass
class MenuScreen(Screen):

    def donate(self):
        webbrowser.open_new_tab("https://www.pmcares.gov.in/en/web/contribution/donate_india")
    def join(self):
        webbrowser.open_new_tab("https://t.me/MyGovCoronaNewsdesk")
    pass
class IndiaResult(Screen):

    def india(self):

        try:
            url = "https://covid-19-india-data-by-zt.p.rapidapi.com/GetIndiaTotalCounts"

            headers = {
            'x-rapidapi-host': "covid-19-india-data-by-zt.p.rapidapi.com",
            'x-rapidapi-key': "3ae1125923msha231c2e1fc6c41ep14814cjsnfe458e46c62f"
            }
            time.sleep(1)
            response = requests.request("GET", url, headers=headers)
            x = response.text
            parsed = json.loads(x)
            g = parsed['data']
            print(parsed)
            CONFIRMED = g[0]['confirmed']
            RECOVERED = g[0]['recovered']
            DEATHS = g[0]['deaths']


            self.add_widget(Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/color][/b]",pos=(-120,120), markup=True,text_size=(self.width,None)))
            self.add_widget(Label(text=str(CONFIRMED), pos=(200, 120), markup=True,text_size=(self.width,None)))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 60), markup=True,text_size=(self.width,None)))
            self.add_widget(Label(text=str(RECOVERED), pos=(200, 60), markup=True,text_size=(self.width,None)))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 0), markup=True,text_size=(self.width,None)))
            self.add_widget(Label(text=str(DEATHS), pos=(200, 0), markup=True,text_size=(self.width,None)))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class StateWise(Screen):
    def statewise(self):
        try :

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            print(p)
            parsed = json.loads(p)
            print(parsed)

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            g = parsed['statewise'][1]['active']
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Result(Screen):
    def worldtotal(self):
        try :
            url = "https://api.covid19api.com/summary"
            time.sleep(1)
            response = requests.get(url)
            x = response.text
            parsed = json.loads(x)
            g = parsed['Global']
            print(parsed)
            TOTAL = g['TotalConfirmed']
            RECOVERED = g['TotalRecovered']
            DEATHS = g['TotalDeaths']
            self.add_widget(Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/color][/b]", pos=(-120, 120),markup=True))
            self.add_widget(Label(text=str(TOTAL), pos=(200, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 60),markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(200, 60), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 0),markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(200, 0), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

        pass
class Assam(Screen):
    def assam(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][22]['active']
            CONFIRMED = parsed['statewise'][22]['confirmed']
            DEATHS = parsed['statewise'][22]['deaths']
            RECOVERED = parsed['statewise'][22]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160),markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160),markup=True))
            self.add_widget(Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120),markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80),markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80),markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40),markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40),markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()


    pass
class Haryana(Screen):
    def haryana(self):
        try :
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][16]['active']
            CONFIRMED = parsed['statewise'][16]['confirmed']
            DEATHS = parsed['statewise'][16]['deaths']
            RECOVERED = parsed['statewise'][16]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()


    pass
class Rajasthan(Screen):
    def rajasthan(self):
        try :
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][5]['active']
            CONFIRMED = parsed['statewise'][5]['confirmed']
            DEATHS = parsed['statewise'][5]['deaths']
            RECOVERED = parsed['statewise'][5]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Andaman(Screen):
    def andaman(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][24]['active']
            CONFIRMED = parsed['statewise'][24]['confirmed']
            DEATHS = parsed['statewise'][24]['deaths']
            RECOVERED = parsed['statewise'][24]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Bihar(Screen):
    def bihar(self):
        try :
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][14]['active']
            CONFIRMED = parsed['statewise'][14]['confirmed']
            DEATHS = parsed['statewise'][14]['deaths']
            RECOVERED = parsed['statewise'][14]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Goa(Screen):
    def goa(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][28]['active']
            CONFIRMED = parsed['statewise'][28]['confirmed']
            DEATHS = parsed['statewise'][28]['deaths']
            RECOVERED = parsed['statewise'][28]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Chattisgarh(Screen):
    def chattisgarh(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][23]['active']
            CONFIRMED = parsed['statewise'][23]['confirmed']
            DEATHS = parsed['statewise'][23]['deaths']
            RECOVERED = parsed['statewise'][23]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Himachal(Screen):
    def himachal(self):
        try:

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][21]['active']
            CONFIRMED = parsed['statewise'][21]['confirmed']
            DEATHS = parsed['statewise'][21]['deaths']
            RECOVERED = parsed['statewise'][21]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()

        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Jharkhand(Screen):
    def jharkhand(self):
        try:

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][18]['active']
            CONFIRMED = parsed['statewise'][18]['confirmed']
            DEATHS = parsed['statewise'][18]['deaths']
            RECOVERED = parsed['statewise'][18]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Kerala(Screen):
    def kerala(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][13]['active']
            CONFIRMED = parsed['statewise'][13]['confirmed']
            DEATHS = parsed['statewise'][13]['deaths']
            RECOVERED = parsed['statewise'][13]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Manipur(Screen):
    def manipur(self):
        try:

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][29]['active']
            CONFIRMED = parsed['statewise'][29]['confirmed']
            DEATHS = parsed['statewise'][29]['deaths']
            RECOVERED = parsed['statewise'][29]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Mizoram(Screen):
    def mizoram(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][31]['active']
            CONFIRMED = parsed['statewise'][31]['confirmed']
            DEATHS = parsed['statewise'][31]['deaths']
            RECOVERED = parsed['statewise'][31]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Puducherry(Screen):
    def puducherry(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][27]['active']
            CONFIRMED = parsed['statewise'][27]['confirmed']
            DEATHS = parsed['statewise'][27]['deaths']
            RECOVERED = parsed['statewise'][27]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Tamilnadu(Screen):
    def tamilnadu(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][6]['active']
            CONFIRMED = parsed['statewise'][6]['confirmed']
            DEATHS = parsed['statewise'][6]['deaths']
            RECOVERED = parsed['statewise'][6]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Tripura(Screen):
    def tripura(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][30]['active']
            CONFIRMED = parsed['statewise'][30]['confirmed']
            DEATHS = parsed['statewise'][30]['deaths']
            RECOVERED = parsed['statewise'][30]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Uttarakhand(Screen):
    def uttarakhand(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][20]['active']
            CONFIRMED = parsed['statewise'][20]['confirmed']
            DEATHS = parsed['statewise'][20]['deaths']
            RECOVERED = parsed['statewise'][20]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Andhra(Screen):
    def andhra(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][8]['active']
            CONFIRMED = parsed['statewise'][8]['confirmed']
            DEATHS = parsed['statewise'][8]['deaths']
            RECOVERED = parsed['statewise'][8]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Maharastra(Screen):
    def maharastra(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][1]['active']
            CONFIRMED = parsed['statewise'][1]['confirmed']
            DEATHS = parsed['statewise'][1]['deaths']
            RECOVERED = parsed['statewise'][1]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Madhya(Screen):
    def madhya(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][4]['active']
            CONFIRMED = parsed['statewise'][4]['confirmed']
            DEATHS = parsed['statewise'][4]['deaths']
            RECOVERED = parsed['statewise'][4]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Arunachal(Screen):
    def arunachal(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][32]['active']
            CONFIRMED = parsed['statewise'][32]['confirmed']
            DEATHS = parsed['statewise'][32]['deaths']
            RECOVERED = parsed['statewise'][32]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Chandigarh(Screen):
    def chandigarh(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][19]['active']
            CONFIRMED = parsed['statewise'][19]['confirmed']
            DEATHS = parsed['statewise'][19]['deaths']
            RECOVERED = parsed['statewise'][19]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Delhi(Screen):
    def delhi(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][3]['active']
            CONFIRMED = parsed['statewise'][3]['confirmed']
            DEATHS = parsed['statewise'][3]['deaths']
            RECOVERED = parsed['statewise'][3]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Gujrat(Screen):
    def gujrat(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][2]['active']
            CONFIRMED = parsed['statewise'][2]['confirmed']
            DEATHS = parsed['statewise'][2]['deaths']
            RECOVERED = parsed['statewise'][2]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass

class Jammu(Screen):
    def jammu(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][11]['active']
            CONFIRMED = parsed['statewise'][11]['confirmed']
            DEATHS = parsed['statewise'][11]['deaths']
            RECOVERED = parsed['statewise'][11]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Karnataka(Screen):
    def karnataka(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][12]['active']
            CONFIRMED = parsed['statewise'][12]['confirmed']
            DEATHS = parsed['statewise'][12]['deaths']
            RECOVERED = parsed['statewise'][12]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Ladakh(Screen):
    def ladakh(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][25]['active']
            CONFIRMED = parsed['statewise'][25]['confirmed']
            DEATHS = parsed['statewise'][25]['deaths']
            RECOVERED = parsed['statewise'][25]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Meghalaya(Screen):
    def meghalaya(self):
        try:

            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][26]['active']
            CONFIRMED = parsed['statewise'][26]['confirmed']
            DEATHS = parsed['statewise'][26]['deaths']
            RECOVERED = parsed['statewise'][26]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Odisha(Screen):
    def odisha(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][17]['active']
            CONFIRMED = parsed['statewise'][17]['confirmed']
            DEATHS = parsed['statewise'][17]['deaths']
            RECOVERED = parsed['statewise'][17]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Punjab(Screen):
    def punjab(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][15]['active']
            CONFIRMED = parsed['statewise'][15]['confirmed']
            DEATHS = parsed['statewise'][15]['deaths']
            RECOVERED = parsed['statewise'][15]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class UP(Screen):
    def up(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][7]['active']
            CONFIRMED = parsed['statewise'][7]['confirmed']
            DEATHS = parsed['statewise'][7]['deaths']
            RECOVERED = parsed['statewise'][7]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass


class Westbengal(Screen):
    def westbengal(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][10]['active']
            CONFIRMED = parsed['statewise'][10]['confirmed']
            DEATHS = parsed['statewise'][10]['deaths']
            RECOVERED = parsed['statewise'][10]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Telangana(Screen):
    def telangana(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][9]['active']
            CONFIRMED = parsed['statewise'][9]['confirmed']
            DEATHS = parsed['statewise'][9]['deaths']
            RECOVERED = parsed['statewise'][9]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Daman(Screen):
    def daman(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][35]['active']
            CONFIRMED = parsed['statewise'][35]['confirmed']
            DEATHS = parsed['statewise'][35]['deaths']
            RECOVERED = parsed['statewise'][35]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Dadra(Screen):
    def dadra(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][34]['active']
            CONFIRMED = parsed['statewise'][34]['confirmed']
            DEATHS = parsed['statewise'][34]['deaths']
            RECOVERED = parsed['statewise'][34]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Sikkim(Screen):
    def sikkim(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][37]['active']
            CONFIRMED = parsed['statewise'][37]['confirmed']
            DEATHS = parsed['statewise'][37]['deaths']
            RECOVERED = parsed['statewise'][37]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass
class Lakhsadweep(Screen):
    def lakshadweep(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][36]['active']
            CONFIRMED = parsed['statewise'][36]['confirmed']
            DEATHS = parsed['statewise'][36]['deaths']
            RECOVERED = parsed['statewise'][36]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup

            show_popup()

    pass


class Nagaland(Screen):
    def nagaland(self):
        try:
            url = "https://api.covid19india.org/data.json"

            payload = {}
            headers = {}
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, data=payload)

            p = response.text
            parsed = json.loads(p)
            print(parsed)
            ACTIVE = parsed['statewise'][33]['active']
            CONFIRMED = parsed['statewise'][33]['confirmed']
            DEATHS = parsed['statewise'][33]['deaths']
            RECOVERED = parsed['statewise'][33]['recovered']
            self.add_widget(Label(text="[b]TOTAL ACTIVE : [/b]", pos=(-120, 160), markup=True))
            self.add_widget(Label(text=str(ACTIVE), pos=(150, 160), markup=True))
            self.add_widget(
                Label(text="[b][color=#FFFF00]TOTAL CONFIRMED : [/b][/color]", pos=(-120, 120), markup=True))
            self.add_widget(Label(text=str(CONFIRMED), pos=(150, 120), markup=True))
            self.add_widget(Label(text="[b][color=#33FF7C]TOTAL RECOVERED : [/color][/b]", pos=(-120, 80), markup=True))
            self.add_widget(Label(text=str(RECOVERED), pos=(150, 80), markup=True))
            self.add_widget(Label(text="[b][color=#FF0000]TOTAL DEATHS : [/color][/b]", pos=(-120, 40), markup=True))
            self.add_widget(Label(text=str(DEATHS), pos=(150, 40), markup=True))
        except requests.exceptions.ConnectionError :
            def show_popup():
                show = P()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except requests.ConnectTimeout :
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()
        except json.JSONDecodeError:
            def show_popup():
                show = Z()  # Create a new instance of the P class
                print("OOOPSSS")
                popupWindow = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                # Create the Error

                popupWindow.open()  # show the popup
            show_popup()

    pass
sm = ScreenManager(transition=WipeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Result(name='result'))

sm.add_widget(IndiaResult(name='resulttwo'))
sm.add_widget(StateWise(name='state'))
sm.add_widget(Assam(name='assam'))
sm.add_widget(Haryana(name='haryana'))
sm.add_widget(Rajasthan(name='rajasthan'))
sm.add_widget(Andaman(name='andaman'))
sm.add_widget(Bihar(name='bihar'))
sm.add_widget(Chattisgarh(name='chattisgarh'))
sm.add_widget(Goa(name='goa'))
sm.add_widget(Himachal(name='himachal'))
sm.add_widget(Jharkhand(name='jharkhand'))
sm.add_widget(Kerala(name='kerala'))
sm.add_widget(Manipur(name='manipur'))
sm.add_widget(Mizoram(name='mizoram'))
sm.add_widget(Puducherry(name='puducherry'))
sm.add_widget(Tamilnadu(name='tamilnadu'))
sm.add_widget(Tripura(name='tripura'))
sm.add_widget(Uttarakhand(name='uttarakhand'))
sm.add_widget(Andhra(name='andhra'))
sm.add_widget(Maharastra(name='maharastra'))
sm.add_widget(Madhya(name='madhya'))
sm.add_widget(Arunachal(name='arunachal'))
sm.add_widget(Chandigarh(name='chandigarh'))
sm.add_widget(Delhi(name='delhi'))
sm.add_widget(Gujrat(name='gujrat'))
sm.add_widget(Jammu(name='jammu'))
sm.add_widget(Karnataka(name='karnataka'))
sm.add_widget(Ladakh(name='ladakh'))
sm.add_widget(Meghalaya(name='meghalaya'))
sm.add_widget(Odisha(name='odisha'))
sm.add_widget(Punjab(name='punjab'))
sm.add_widget(UP(name='up'))
sm.add_widget(Telangana(name='telangana'))
sm.add_widget(Westbengal(name='westbengal'))
sm.add_widget(Nagaland(name='nagaland'))
sm.add_widget(Daman(name='daman'))
sm.add_widget(Dadra(name ='dadra'))
sm.add_widget(Sikkim(name='sikkim'))
sm.add_widget(Lakhsadweep(name='lakhsadweep'))


class Multiple_LayoutApp(App):
    title = 'CORONA STATUS APP'
    def build(self):
        return sm

MlApp = Multiple_LayoutApp()

MlApp.run()