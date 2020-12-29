# Scraping journal artcles for 7 types of herbs from PubMed


import time, requests
from bs4 import BeautifulSoup
import pandas as pd

# Generate URL for each herb
def generate_url(herb):
	URLSTART="https://pubmed.ncbi.nlm.nih.gov"
	HERBURL = "/?term={}".format(herb)+"+stress+anxiety"
	articles = []
	main_url = URLSTART + HERBURL
	main_page = requests.get(main_url).text
	Msoup = BeautifulSoup(main_page,"html.parser")
	i=1
	while(len(articles) < int(Msoup.select("meta[name='log_resultcount']")[0]['content']) and len(articles) < 5000):
		if i == 1:
			url = URLSTART + HERBURL
		else:	
			url = URLSTART + HERBURL + '&page={}'.format(i)

		page = requests.get(url).text
		soup = BeautifulSoup(page,"html.parser")
		for e in soup.select('.permalink-text'):
		  articles.append(e['value'])
		articles = list(set(articles))
		i += 1
	return articles

# Extract meta-data for each herb from all pages
def extract_data(articles,h,herb_name):

	
	herb,title,abstract = [], [], []

	for i in articles:
		articleurl = i

		article = requests.get(articleurl)

		d = BeautifulSoup(article.text, 'html.parser')
		herb=herb_name
		try:
			title.append(d.select("meta[property='og:title']")[0]['content'])
		except:
			title.append(None)	
		try:
			abstract.append(d.find(class_="abstract-content selected").get_text())
		except:
			abstract.append(None)
	dff = pd.DataFrame({'Herb' : herb,'Title' : title,'Abstract' : abstract})
	return dff


herb_list = ['rhodiola rosea', 'vitamin B', 'bacopa monnieri', 'green tea', 'lavender', 'holy basil','turmeric', 'chamomile','ashwagandha', 'Bergamot','Chinese Skullcap','Damiana','Eleuthro','Folic acid','Ginkgo biloba','Ginseng (Siberian)','Magnolia Officinalis','lemon balm','Passionflower','Valerian']
herb = ['+'.join(h.split(' ')) for h in herb_list]
herb_df = pd.DataFrame() #columns = ['Herb' , 'Title' , 'Authors' , 'Journal Title' , 'ISSN' , 'Abstract URL' , 'PMID' , 'DOI' , 'Affiliations' , 'Abstract' , 'Keywords'])


for i in range(len(herb)):
	articles = generate_url(herb[i])
	print(herb_list[i])
	print('*Done*')
	dff = extract_data(articles,herb[i],herb_list[i])
	print('**Done**')
	herb_df = herb_df.append(dff)
herb_df = herb_df.reset_index(drop=True)
herb_df = herb_df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True)
print(herb_df)

herb_df.to_csv('Medicinal Herb Articles.csv', index=False)


	
