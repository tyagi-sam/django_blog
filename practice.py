name = input('Enter file: ')
fhand = open(name,'r')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

bigword = 0
bigcount = 0
for word,count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)




pip install Pillow

from PIL import Image, ImageFilter
while True:
    img = input('Drop an image: ')
    x = Image.open(img)

    imgg = x.filter(ImageFilter.BoxBlur(0))
    imgg.save('blurredimg.jpg')
    imgg.show()
if x == 'done':
    exit()
