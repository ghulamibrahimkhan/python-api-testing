import requests

def get_random_usernames():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests(url)
    data = response.json()

    if data["sucess"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["user_name"]
        country = user_data["location"]["country"]
        return user_data, country
    else:
        raise Exception("Failed To Fetch User Data")

