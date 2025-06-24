'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
'''

class Codec:

    def __init__(self) :
        self.encoding_map = {}
        self.decoding_map = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, long_url):                                             # tc : O(1)         sc : O(n)
        if long_url not in self.encoding_map :
            short_url = self.base_url + str(len(self.encoding_map) + 1 )
            self.encoding_map[long_url] = short_url
            self.decoding_map[short_url] = long_url
        return self.encoding_map[long_url]
        

    def decode(self, short_url):
        return self.decoding_map[short_url]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))