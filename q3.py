import requests

def get_usd_to_myr(date, value):
    url = f"https://api.bnm.gov.my/public/exchange-rate/usd/date/{date}?session=0900&quote=rm"
    headers = {
        "Accept": "application/vnd.BNM.API.v1+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Error: Unable to retrieve exchange rate data"

    data = response.json()
    rate = float(data['data']['rate']['buying_rate'])
    myr = rate * value
    return round(myr, 2)

if __name__ == "__main__":
    try:
        value = float(input("Enter USD: $"))
        date = input("Enter date (YYYY-MM-DD): ")
        myr = get_usd_to_myr(date, value)

        if isinstance(myr, str):
            print(myr)
        else:
            print(f"MYR {myr}")
    except KeyboardInterrupt:
        print("\nGoodbye")
    finally:
        pass