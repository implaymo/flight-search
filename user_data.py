import requests

class UserData:

    def __init__(self):
        print("Welcome to The Cheapest Flights!")
        print("Our job is to find you the cheapest flight deals! Join us, for the lastest prices.")
        self.first_name = input("What's your first name?\n")
        self.last_name = input("What's your last name?\n")
        self.email = input("What's your email?\n")
        self.email_confirmation = input("Type your email again.\n")
        if self.email == self.email_confirmation:
            print("Welcome to the Clube!")
        else:
            print("Wrong information. Sorry, we can't let you in.")
            exit()


    def put_user_data(self):
        params = {
            "user":{
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email_confirmation
            }
        }

        header = {
            "Content-Type": "application/json"
        }

        response = requests.post(url="https://api.sheety.co/3864f9e32cb6490ca4e1118527c50e15/flightDeals/users",
                                 json=params, headers=header)
        response.raise_for_status()

        data = response.json()
        print(data)
