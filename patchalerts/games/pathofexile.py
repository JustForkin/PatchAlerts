from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.base_class import Site


class PathOfExile(Site):
	def __init__(self):
		super().__init__('Path of Exile', icon='https://i.imgur.com/4FYaeCh.png', homepage='https://pathofexile.com')

	def scan(self):
		forums = ['https://www.pathofexile.com/forum/view-forum/dev-manifesto',
				"https://www.pathofexile.com/forum/view-forum/patch-notes",
				'https://www.pathofexile.com/forum/view-forum/news']
		ignore_authors = ['natalia_ggg']  # Ignore marketing manager(s). Lowercase.

		for forum in forums:
			soup = BeautifulSoup(requests.get(forum).text, "html.parser")
			table = soup.find(attrs={"class": 'viewForumTable'})
			elem = table.find('tbody').find('tr')
			ttl = elem.find(attrs={'class': 'title'})
			link = ttl.find('a')
			_url = 'https://www.pathofexile.com' + link["href"]
			author = elem.find(attrs={'class': 'profile-link'})
			if author.text.lower() in map(str.lower, ignore_authors):
				continue

			page = BeautifulSoup(requests.get(_url).text, "html.parser")
			dsc = page.find(attrs={'class': 'newsPost'})
			if not dsc:
				dsc = page.find(attrs={"class": 'content-container'}).find(attrs={'class': 'content'})
			_title = ttl.text
			_desc = dsc.getText('\n')
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#af6025")


if __name__ == "__main__":
	lol = PathOfExile()
	for u in lol.scan():
		print(u)
