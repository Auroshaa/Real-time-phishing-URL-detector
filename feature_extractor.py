import re
from urllib.parse import urlparse
import tldextract
import socket

def extract_features(url):
    features = []

    # 1. UsingIP
    features.append(1 if re.match(r"^(http|https)?://(\d{1,3}\.){3}\d{1,3}", url) else -1)

    # 2. LongURL
    features.append(1 if len(url) >= 75 else -1)

    # 3. ShortURL
    features.append(1 if len(url) <= 20 else -1)

    # 4. Symbol@
    features.append(1 if "@" in url else -1)

    # 5. Redirecting//
    features.append(1 if url.count('//') > 2 else -1)

    # 6. PrefixSuffix
    hostname = urlparse(url).netloc
    features.append(1 if '-' in hostname else -1)

    # 7. SubDomains
    subdomain = tldextract.extract(url).subdomain
    features.append(1 if len(subdomain.split('.')) >= 2 else -1)

    # 8. HTTPS
    features.append(1 if urlparse(url).scheme == "https" else -1)

    # 9. DNS Record
    try:
        socket.gethostbyname(hostname)
        features.append(-1)
    except:
        features.append(1)

    return features
