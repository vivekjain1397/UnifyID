from PIL import Image
import requests
import random

def getRandInts():
	link = "https://www.random.org/integers/?num=10000&min=1&max=255&col=1&base=10&format=plain&rnd=new"
	r = requests.get(link).text
	r = r.encode("ascii", "ignore")
	r = r.split()
	randlist = [int(num) for num in r]
	#randlist = my_randoms=[random.randrange(1,255,1) for _ in range (10000)]
	return randlist

i = 0
row, col = 256, 256
img = Image.new('L', (row, col))
data = []
while (i < 7):
	data += getRandInts()
	i += 1
data = data[:65536]
img.putdata(data)
img.show()



