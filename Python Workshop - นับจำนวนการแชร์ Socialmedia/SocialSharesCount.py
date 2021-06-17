import socialshares
url=input("ป้อน URL : ")
counts=socialshares.fetch(url,['facebook','google'])

print(counts)
