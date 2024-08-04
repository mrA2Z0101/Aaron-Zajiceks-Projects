import requests

def check_website(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return "UP", response.elapsed.total_seconds()
        else:
            return "DOWN", None
    except requests.RequestException:
        return "DOWN", None
    
def main():
    websites = [
        'https://www.google.com',
        'https://www.github.com',
        'https://www.stackoverflow.com',
        'https://www.youtube.com'
        #Enter more Website URLs Here
    ]

    response_time_threshold = 2

    for website in websites:
        status, response_time = check_website(website)
        if status == "UP":
            print(f"Website {website} is UP. Response time: {response_time: .2f} seconds")
            if response_time > response_time_threshold:
                print(f"Website {website} is slow. Response time: {response_time: .2f} seconds.")
        else:
            print(f"Website {website} is DOWN.")

if __name__ == "__main__":
    main()
    