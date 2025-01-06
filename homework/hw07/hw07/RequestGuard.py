import requests
import re

class RequestGuard:
    def __init__(self, domain):
        self.domain = domain
        self.forbidden = self.parse_robots()

    def can_follow_link(self, url):
        if self.domain not in url:
            return False
        for sub in self.forbidden:
            if re.search(rf'{self.domain}{sub}',url):
                return False
        return True


    def make_get_request(self, *args, **kwargs):
        if self.can_follow_link(*args[0]):
            return requests.get(*args[0],*args[1:],**kwargs)
        else:
            return False

    def parse_robots(self):
        blacklist = []
        robots = requests.get(f'{self.domain}/robots.txt').text
        blacklist += re.findall(r'Disallow: (/.*)\b', robots)
        return blacklist


if __name__ == '__main__':
    pass