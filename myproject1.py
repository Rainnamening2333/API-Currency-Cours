import requests

API_KEY = "Your_api"
BASE_URL = "http://data.fixer.io/api/latest"

params = {
    'access_key': API_KEY,
    'symbols': "USD,RUB,EUR,CNY"
}

while True:
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get('success'):
            rates = data['rates']

            try:
                user_choice = input('Choose a course [1: EUR/USD, 2: EUR/RUB, 3: EUR/CNY, 4: Exit]: ').strip()

                if not user_choice.isdigit():
                    raise ValueError

                user_choice = int(user_choice)

                if user_choice == 1:
                    print(f'EUR/USD: {rates["USD"]}')
                elif user_choice == 2:
                    print(f'EUR/RUB: {rates["RUB"]}')
                elif user_choice == 3:
                    print(f'EUR/CNY: {rates["CNY"]}')
                elif user_choice == 4:
                    print("Exiting the programm...")
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")

            except ValueError:
                print("Erorr: Enter a number (1, 2, 3 or 4).")

        else:
            print("API Erorr:")

    else:
        print(f'HTTP Erorr: {response.status_code}')


