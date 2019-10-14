from bs4 import BeautifulSoup

broken_html='<ul class=country><li>Population</li><li><a>wbq</a></li></ul>'
soup=BeautifulSoup(broken_html,'html.parser')
fixed_html=soup.prettify()
print(soup.ul.contents)

for child in soup.ul.contents:
    print(child.string)
