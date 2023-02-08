import argparse
from crawler import crawler_function
import networkx as nx
import visualisation.page as page



def main(url, threshold_urls, threshold_tokens):

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawler_function.crawl(list_urls, starting_index, threshold_urls, threshold_tokens, G)

    page.create_graphe(G)

    page.display_page('graphe.png')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help = "The URL the program start crawling from", type = str)
    parser.add_argument("threshold_urls", help = "The number of URLs the program need to crawl", type = int)
    parser.add_argument("threshold_tokens", help = "The number of words the program need to crawl", type = int)
    args = parser.parse_args()
    main(args.url, args.threshold_urls, args.threshold_tokens)
