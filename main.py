from bs4 import BeautifulSoup as bs
import requests
import tweepy

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    html = session.get(url)

    # create new soup
    soup = bs(html.text, "html.parser")

    # Store all the weather variables in desc dictionary

    desc = {'location': soup.find("div", attrs={"id": "wob_loc"}).text,
            'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
            'time': soup.find("div", attrs={"id": "wob_dts"}).text,
            'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
            'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text,
            'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
            'wind': soup.find("span", attrs={"id": "wob_ws"}).text}

    # Location
    # Current Temperature
    # Current Day/Time
    # Weather Description
    # Precipitation
    # Humidity %
    # Wind

    return desc


if __name__ == "__main__":
    location = str(input("Enter a city to get current weather data of: "))
    URL = f"https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather+{location}"

    # Get weather data of location

    data = get_weather_data(URL)

    # Twitter Keys

    consumer_key = "CONSUMER KEY"
    consumer_secret = "CONSUMER SECRET"
    access_token = "ACCESS TOKEN"
    access_token_secret = "ACCESS TOKEN SECRET"

    # Create Client with Twitter Keys

    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    # String that will be used for tweet

    output = f"Weather in {location}" + '\n'
    for key in data:
        output = output + data[key] + '\n'

    # Create Tweet

    response = client.create_tweet(
        text=output
    )

    # Print Status

    print(f"https://twitter.com/user/status/{response.data['id']}")
