
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# search

query = "python Machine Learning"

for j in search(query, num=10, stop=10, pause=2):
    print(j)

# Returned URLs

# https://www.coursera.org/learn/machine-learning-with-python
# https://www.coursera.org/learn/machine-learning-with-python#about
# https://www.coursera.org/learn/machine-learning-with-python#syllabus
# https://www.coursera.org/learn/machine-learning-with-python#reviews
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://machinelearningmastery.com/machine-learning-with-python/
# https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
# https://www.w3schools.com/python/python_ml_getting_started.asp
# https://towardsai.net/p/machine-learning/machine-learning-algorithms-for-beginners-with-python-code-examples-ml-19c6afd60daa
# https://www.edx.org/course/machine-learning-with-python-a-practical-introduct    