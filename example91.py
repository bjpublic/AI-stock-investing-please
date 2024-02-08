import pickle

f = open("my_data.dat", 'rb')
data = pickle.load(f)
f.close()

print(data)