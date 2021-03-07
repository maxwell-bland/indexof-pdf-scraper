from bs4 import BeautifulSoup as bs
import urllib3 as ul3

def is_page(url):
  filename = url.split('/')[-1]
  if len(filename) == 0:
    return True, None
  else:
    return False, filename

def content(url):
  httpNode = ul3.PoolManager()
  response = httpNode.request('GET',url)
  return (bs(response.data, features="html.parser"))

def get_url_set(url=None, soup=None):
  tags = soup.find_all('a')
  s = set()
  for tag in tags:
    h = tag.get('href')
    if h[-1] == '/' or h[-4:] == '.pdf':
      s.add(url + h)
  return s

def traverse(url):
  is_a_page, file_name = is_page(url)
  if not is_a_page:
    return
  else:
    s = get_url_set(url, content(url))
    for new_url in s:
      if new_url[-4:] == '.pdf':
        print(new_url)
      traverse(new_url)

if __name__ == '__main__':
  root = input("Enter url: ")

  if not root.endswith('/'):
    root += '/'
  traverse(root)




