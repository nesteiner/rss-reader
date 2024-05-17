from feedparser import parse, USER_AGENT, FeedParserDict
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"

def parse_url(rss_url: str):
    try:
        response: FeedParserDict = parse(rss_url)

        print("\t{}".format(response.feed.title))
        print("\t{}".format(response.feed.description))
        print("\t{}".format(response.feed.link))
        print()

        for item in response.entries:
            print("title: {}".format(item.title))
            print("description: {}".format(item.description))
            print("link: {}".format(item.link))

    except Exception:
        print("{} is not a valid RSS feed input".format(rss_url))



def main():
    rss_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    parse_url(rss_url)

main()    