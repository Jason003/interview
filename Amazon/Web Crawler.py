# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import collections
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHostname(url):
            url = url[7:]
            idx = url.find('/')
            return url if idx == -1 else url[:idx]
        hostname = getHostname(startUrl)
        dq = collections.deque([startUrl])
        seen = {startUrl}
        while dq:
            curr = dq.popleft()
            for nxt in htmlParser.getUrls(curr):
                if nxt not in seen and getHostname(nxt) == hostname:
                    seen.add(nxt)
                    dq.append(nxt)
        return list(seen)
