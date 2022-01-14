n = []
l = []
with open('inmatrix.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
      l.append(map(int, line.split(',')))
      n.append(map(int, line.split(',')))
    
print('senza list():')
print(n)
print('con list():')
print(l)