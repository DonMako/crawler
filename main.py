import argparse
from crawler import crawler_function
import networkx as nx
import visualisation.page as page



def main(url, threshold):

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawler_function.crawl(list_urls, starting_index, threshold, G)

    page.create_graphe(G)

    page.display_page('graphe.png')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help = "The URL the program start crawling from", type = str)

    parser.add_argument("threshold", help = "The number of URLs the program need to crawl", type = str)
    args = parser.parse_args()
    main(args.url, args.threshold)
