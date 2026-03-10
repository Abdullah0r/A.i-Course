f = open('hero.text','a')
for i in range(50):
   f.write(F'\n this is line{i + 1}')
f.close()
f = open('hero.text','r')
content = f.read()
print(content)
f.close()