import hashlib
def shortURL(url):
    urlhash = hashlib.md5(url)
    return urlhash.hexdigest()[:8]

if __name__ == '__main__':
    url = "https://trello.com/b/E0syxtlo/halley-s-comet"
    print shortURL(url)


