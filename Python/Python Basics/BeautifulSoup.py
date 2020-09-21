from bs4 import BeautifulSoup


NAVIGATING HTML
soup=BeautifulSoup(html_string, "html.parser")

A PART
print(soup.body)
print(soup.body.div)            Only First DIV
print(soup.find("div"))         Only First DIV
print(soup.find_all("div"))     All DIV's(List)


SELECTING BY ID
print(soup.find(id="first"))


SELECTING BY CLASS
print(soup.find(class_="first"))


SELECTING BY ATTRIBUTE
print(soup.find(attrs={"data-example" : "yes"}))


SELECTING BY CSS SELECTOR
print(soup.select("#first"))[0]      ID         Gives just the first one
print(soup.select(".first"))         CLASS      Gives just the first one


GET TEXT
el = (soup.select("#first"))[0]
print(el.get_text())


GET NAME OF THE TAG
print(el.name)


GET DICT OF ATTRS
print(el.attrs)


GET CONTENTS UNDER BODY
print(soup.body.contents)           In List Format with New Line Characters


FOR NEXT SIBLING
print(soup.body.contents[1].next_sibling)


FOR PARENT
print(.parent)


FINDING NEXT SIBLING
data = soup.find(id="first").find_next_sibling()        Ignores New Line Characters
