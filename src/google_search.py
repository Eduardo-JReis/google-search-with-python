
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# search

query = "python Machine Learning"

for j in search(query, num=10, stop=10, pause=2):
    print(j)