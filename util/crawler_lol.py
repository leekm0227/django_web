import requests
import json


url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
page = 1
maxPage = 841

f = open("lotto.txt", 'w')

while page < maxPage:
    response = requests.get(url + str(page))
    data = json.loads(response.text)
    print("%s, %s, %s, %s, %s, %s, %s" % (data["drwtNo1"], data["drwtNo2"], data["drwtNo3"], data["drwtNo4"], data["drwtNo5"], data["drwtNo6"], data["bnusNo"]))
    f.write("%s, %s, %s, %s, %s, %s, %s\n" % (data["drwtNo1"], data["drwtNo2"], data["drwtNo3"], data["drwtNo4"], data["drwtNo5"], data["drwtNo6"], data["bnusNo"]))
    page = page + 1

f.close()

print("finish")