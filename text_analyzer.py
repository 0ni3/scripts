def count_char(text, char):
  # text analyzer
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
  
file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre gunaVa gur snpr bs nzovthvgl""")
file.close()
filename = "newfile.txt"

with open(filename) as f:
   text = f.read()

print(count_char(text, "a"))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
