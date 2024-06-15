import hashlib

import requests


class Pwned:
    def __init__(self, password: str):
        self.password: str = password

    def sha1_hash(self) -> tuple:
        sha1_password = (
            hashlib.sha1(self.password.encode()).hexdigest().upper()
        )
        return sha1_password[:5], sha1_password[5:]

    def get_leaked_password(self) -> int:
        response = requests.get(
            'https://api.pwnedpasswords.com/range/' + self.sha1_hash()[0]
        ).text
        if self.sha1_hash()[1] in response:
            pos_index = response.find(self.sha1_hash()[1])
            count_pwned = response[pos_index + len(self.sha1_hash()[1]) + 1 :]
            return int(count_pwned.split()[0])

        return 0

    def isPwned(self) -> bool:
        return bool(self.get_leaked_password())


if __name__ == '__main__':
    pw = Pwned('123')
    print(pw.get_leaked_password())
