# WikiExtractor

This class extracts the `num_urls` number of links for the given `keyword`, extracts 1 paragraph from every link, and stores them in a JSON file using the basic Python modules.


```zsh

python wiki_extractor.py --keyword="Indian Historical Events" --num_urls=10 --output="out.json"

```
<br>
Due to time constraints, multiprocessing couldn't be implemented.
