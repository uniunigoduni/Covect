import re  
from collections import Counter
from tqdm import tqdm
from bs4 import BeautifulSoup

word_regex = re.compile(r"[^\w]")

with open("watch-history.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, 'lxml')    

titles = []
for a in soup.find_all("a"):
    if a.has_attr("href") and a.text:
        titles.append(a.text)

word_count = Counter()
for title in tqdm(titles, desc="Processing titles", unit="title"):
    words = (word for word in word_regex.sub(" ", title).split())    
    for word in words:        
        word_count[word] += 1

word_count_most_common = word_count.most_common()     
print(word_count_most_common)