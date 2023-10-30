import requests
from bs4 import BeautifulSoup


class FBLogin:
    fb_url = "https://m.facebook.com"
    email = ""
    passw = ""

    def __int__(self, email, passw):
        self.email = email
        self.passw = passw

    def login_is_success(self, resp):
        if "nem felel meg egyetlen fióknak sem" in resp.text:
            print("[!] NOT VALID USERNAME OR PASSWORD")
            return False
        elif "Helytelen jelszó" in resp.text:
            print("[!] NOT VALID PASSWORD")
            return False
        elif "elírtad az e-mail-címedet" in resp.text:
            print("[*] MISTAKE WITH EMAIL")
            return False
        elif "hiba lépett fel" in resp.text:
            print("[*] ERROR TO CONNECTION")
            return False

        elif "login_error" in resp.text:
            print("[-] LOGIN ERROR")
            return False

        else:
            print("[+] VALID LOGIN!")
            return True

    def fb_login(self,email,passw):
        # leszedjük a szükséges formokat és a cookie-kat
        resp_data = requests.get(self.fb_url + "/login.php")
        soup = BeautifulSoup(resp_data.text, 'html.parser')
        lsd = soup.find('input', {'type': 'hidden', 'name': 'lsd'})["value"]
        jazoest = soup.find('input', {'type': 'hidden', 'name': 'jazoest'})["value"]
        m_ts = soup.find('input', {'type': 'hidden', 'name': 'm_ts'})["value"]
        li = soup.find('input', {'type': 'hidden', 'name': 'li'})["value"]
        cookies = resp_data.cookies.get_dict()

        data = {
            "email": email,
            "pass": passw,
            'lsd': lsd,
            'jazoest': jazoest,
            'm_ts': m_ts,
            'li': li,
            'try_number': '0',
            'unrecognized_tries': '0',

        }

        cookies = {
            'sb': cookies['sb'],
            'datr': cookies['datr']
        }

        # elküldjük a login formot a cookie-kal
        response = requests.post(url=self.fb_url + '/login.php', data=data, cookies=cookies)

        return self.login_is_success(response)
