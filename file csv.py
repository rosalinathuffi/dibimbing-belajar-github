import pandas as pd

#membuat table
data = {
    'Username': ['booker12','grey07','johnson81','jenkins46','smith79'],
    'Identifier': ['9012','2070','4081','9346','5079'],
    'First name': ['Rachel','Laura','Craig','Mary','Jamie'],
    'Last name': ['Booker','Grey','Johnson','Jenkins','Smith']
}

#membuat dataframe
df=pd.DataFrame(data)

#menampilkan data
print(data)