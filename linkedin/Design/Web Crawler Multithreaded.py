from concurrent import futures
from collections import deque
'''
There are three key problems for the followup:

How to make sure that an URL is not crawled twice.
Bloom filter with multiple hash functions can be used to check if an URL has been crawled. The implementation can either be centralized (single point of failure and the centralized implementation should have replicas) or distributed to each worker. If distributed to each worker, it's better to be replicated in 3 workers so that when one worker fails, the state still persists. It's possible that the bloom filter returns false positive result when collision happens (two different URLs have the same hash), we may have an anti-entropy pipeline built to handle the unprocessed URLs if that turns out to be an issue in practice.

How to make sure that the workload is distributed well.
A hash code can be calculated based on domain and a worker will only work on a range of hash codes (It doesn't necessary mean that a domain will only be processed by a single node, a better design is to have a domain processed by multiple nodes so that if one fails, there're still workers working on this domain). If a worker receives an URL that it shouldn't work on, send it to the right worker. We need to pay attention to how to start the job so that at the first beginning not all the requests rush to a single node. One way to do that is to randomly pick a batch of URLs to start. We need to have some mechanism to determine which worker handles which range of hash codes. This mechanism can either be centralized (probably use Zookeeper) or each worker maintain a copy of it. For the latter case, Workers keep sending heartbeat to other workers. When a worker A hasn't received heartbeat from worker B for a period of time (lets say 30 secs), it updates the service discovery meta data and distribute it to all other workers using gossip protocol. The caveat is that a worker that hasn't received the latest service discovery meta data may send request to failed nodes and the URL is left unprocessed in some edge cases. One way to mitigate that is to have two or three nodes working on the same URL(we have bloom filter mentioned in #1 to make sure that no duplicated http gets sent out to external network).

How to detect node failure and handle the failure.
With the service discovery module mentioned in #2, node failure can be detected. However, it's possible that a "failed node" node doesn't actually die due to network delay. In that case, the first node received its heartbeat will update the service discovery metadata and send it out to other workers.
'''
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}

        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))

        return list(seen)
