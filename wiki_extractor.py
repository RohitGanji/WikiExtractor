import argparse
import requests
import json
import argparse
from bs4 import BeautifulSoup as bs

class WikiExctrator:
    
    def __init__(self, keyword, num_urls, output):
        self.keyword = keyword
        self.num_urls = num_urls
        self.output = output
        self.wiki = "https://en.wikipedia.org"
        self.no_results = 'There were no results matching the query.'
        print(f"\n    Keyword: {self.keyword}\nNo. of URLs: {self.num_urls}\nOutput Name: {self.output}\n\n")
        self.extract()
    
    def extract_links(self):
        results = requests.get(f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit={self.num_urls}&search={self.keyword.replace(' ','+')}")
        if self.no_results in results.text:
            print(self.no_results)
        else:
            soup = bs(results.content, "html.parser")
            links = soup.find('ul', {'class':'mw-search-results'}).find_all('a')
            if len(links) > self.num_urls:
                links = links[:self.num_urls]
        return links
        
    def extract(self):
        count = 0
        lis = []
        links = self.extract_links()
        if len(links) != 0:
            for link in links:
                url = self.wiki+link["href"]
                result = requests.get(url)
                soup = bs(result.content, "html.parser")
                para = soup.find('div', {'class':'mw-parser-output'}).find_all('p')[1].text
                lis.append({'url': url, 'paragraph': para})
                count += 1
                print(f"Links Extracted: {count}", end='\r')
        
        with open(self.output, 'w') as jsonfile:
            json.dump(lis, jsonfile)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="WikiExtractor")

    parser.add_argument("--keyword", required=True, help="Keywords to search")
    parser.add_argument("--num_urls", type=int, required=True, help="Number of urls to extract")
    parser.add_argument("--output", required=True, help="Name of the output JSON file")

    args = vars(parser.parse_args())
    
    wiki = WikiExctrator(args["keyword"], args["num_urls"], args["output"])
