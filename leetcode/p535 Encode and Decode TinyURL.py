class Codec:

    url_list = []

    def encode(self, longUrl):
        self.url_list.append(longUrl)
        return len(self.url_list) - 1

    def decode(self, shortUrl):
        return self.url_list[shortUrl]



if __name__ == '__main__':
    codec = Codec()
    print(codec.decode(codec.encode('xxxxx')))
    print(codec.url_list)

