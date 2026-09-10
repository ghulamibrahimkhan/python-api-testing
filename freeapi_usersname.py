import requests

def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username , country
    else:
        raise Exception("Failed To Fetch User Data")

def main():
    try:
        username, country = fetch_random_user_api()
        print(username)
        print(country)
    except Exception as request_failed:
        print(print(str(request_failed)))

if __name__ == "__main__":
    main()