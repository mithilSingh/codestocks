import requests as rq 


r=rq.get("https://i.annihil.us/u/prod/marvel/i/mg/9/c0/5f5942f05f5bd/clean.jpg")
print(r.text)