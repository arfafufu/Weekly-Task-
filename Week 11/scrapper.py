import requests
from bs4 import BeautifulSoup
import csv


def get_cars_data(car):
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    cars = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        if not tables:
            print("No tables found on the webpage.")
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    cars.append({'name': name, 'price': price})
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return cars


# create a function to scrape data from the webpage, the above code can be used inside the function
def scrapper(car_list):
    all_cars = []
    for car in car_list:
        print(f"Scraping data for: {car}")
        cars = get_cars_data(car)
        if cars:
            all_cars.extend(cars)
        else:
            print(f"No data found for {car}")
    return all_cars


# create a function to save data to a csv file
def save_to_file(data, filename):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} records to {filename}")


if __name__ == "__main__":
    # Example list of car model slugs as used in PakWheels URLs
    car_models = ["toyota-corolla", "honda-civic", "suzuki-alto"]

    data = scrapper(car_models)
    save_to_file(data, "cars_data.csv")