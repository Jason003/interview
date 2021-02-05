class Codec:
    def __init__(self):
        self.d = {}
        self.idx = 0
        self.prefix = 'https://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        res = self.prefix + str(self.idx)
        self.d[res] = longUrl
        self.idx += 1
        return res

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.d[shortUrl]