# WikiExtractor

This class extracts the `num_urls` number of links for the given `keyword`, extracts 1 paragraph from every link, and stores them in a JSON file.

### Modules Required:
argparse
requests
json
bs4


```zsh

python wiki_extractor.py --keyword="Indian Historical Events" --num_urls=10 --output="out.json"

```
