import requests

def fetch_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        print(data["message"])
        for i in range(len(data)):
            id = data["data"]["data"][i]["id"]
            categories = data["data"]["data"][i]["categories"]
            content = data["data"]["data"][i]["content"]
            print( id, "\n ",categories, "\n ",content )
            print("***")
            # return id, categories, content
            
    else:
        raise Exception("e")
    
def main():
    # id, categories, content = fetch_jokes()
    fetch_jokes()
    # print(id)
    # print(categories)
    # print(content)

if __name__ == "__main__":
    main()