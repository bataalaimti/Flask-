# from bs4 import BeautifulSoup
# import requests
# # url = "https://www.mongolbank.mn/dblistofficialdailyrate.aspx"
# url = ''
# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(res.status_code) # Амжилттай болсон эсэх код хэвлэгднэ
# usd = soup.find(id='ContentPlaceHolder1_lblUSD').getText()
# usd_new = float(usd.replace(',', ''))
# print(usd_new)


