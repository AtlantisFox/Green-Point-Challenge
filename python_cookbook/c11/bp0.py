"""A simple script to import the daily picture of bing"""
import urllib.request
import re
import time


def main():
    """We use the xml api provided by bing to get the pic url"""
    hostname = "http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
    req = urllib.request.Request(hostname)
    webpage = urllib.request.urlopen(req)
    content = str(webpage.read())
    url_tail = re.search(r'<url>[^\s]*</url>', content)
    url = 'http://cn.bing.com' + str(url_tail.group())[5:-6]
    print(url)
    pic_file_name = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    urllib.request.urlretrieve(url, pic_file_name + url[-4:])


if __name__ == '__main__':
    main()