from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_weather(city):
    try:
        city = city.replace(" ", "+")
        url = f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select_one('#wob_loc').getText().strip()
        time = soup.select_one('#wob_dts').getText().strip()
        info = soup.select_one('#wob_dc').getText().strip()
        weather = soup.select_one('#wob_tm').getText().strip()
        print("Location:", location)
        print("Time:", time)
        print("Weather Info:", info)
        print("Temperature:", weather + "°C")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    city = input("Enter the Name of City -> ")
    city = city + " weather"
    get_weather(city)
    print("Have a Nice Day :)")
