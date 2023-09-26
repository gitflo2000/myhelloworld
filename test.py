import pandas as pd

print("This line will be printed.")
print("Das ist eine neue Zeile.")

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)