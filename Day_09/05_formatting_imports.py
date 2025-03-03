from datetime import datetime  # Imports on top of the file
from math import cos, pi  # Inbuilt

print(pi)
print(cos(pi / 2))
print(cos(0))

now = datetime.now()
print(now)


print(f"The Current date is: {now:%d-%m-%Y}")
print(f"The Current date is: {now:%d/%m/%Y}")
print(f"The Current date is: {now:%d %m %Y}")
print(f"The Current date is: {now:%d %B %Y}")
print(f"The Current date is: {now:%d %b %Y}")
