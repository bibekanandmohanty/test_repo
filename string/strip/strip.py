x=" python"
print(x.strip())
print(x.strip('p'))
print(x.strip('n'))
x="python is easy"
print(x.strip('easy'))
x="python is easy python and is popular"
print(x.rstrip('python'))
print(x.lstrip('python'))
print(x.split())
print(x.split(is))
x="pythonyy"
print(x.strip('p').rstrip('y'))




