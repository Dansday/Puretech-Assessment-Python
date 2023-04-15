from datetime import datetime

def get_price(item, date):
    database = {
        "A": [
            ["1970-01-01", 20.0],
            ["2020-01-01", 20.0],
            ["2020-02-01", 25.7],
            ["2020-03-01", 25.7],
            ["2020-04-01", 23.5],
            ["2020-05-01", 18.5]
        ],
        "B": [
            ["1970-01-01", 30.6],
            ["2020-01-01", 30.9],
            ["2020-02-01", 30.9],
            ["2020-03-01", 30.9],
            ["2020-04-01", 37.5],
            ["2020-05-01", 30.0]
        ],
        "C": [
            ["1970-01-01", 0.0],
            ["2020-01-01", 5.0],
            ["2020-02-01", 15.3],
            ["2020-03-01", 16.0],
            ["2020-04-01", 16.0],
            ["2020-05-01", 10.0]
        ]
    }

    # The effective date format is year-month-day (%Y-%m-%d)
    # Date value of 1970-01-01 is the base price
    
    for i in range(len(database[item])):
        effective_date = datetime.strptime(database[item][i][0], "%Y-%m-%d")
        if effective_date <= datetime.strptime(date, "%Y-%m-%d"):
            price = database[item][i][1]
        else:
            break
    
    return price
    

if __name__ == "__main__":
    print("Press CTRL+C to exit\n")

    while True:
        try:
            item = input("Choose item: ")
            date = input("Choose date (YYYY-MM-DD): ")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        
        price = get_price(item, date)
        print(f"Price: RM {price}\n")
