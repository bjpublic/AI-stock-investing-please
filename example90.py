import pickle

box = [1, 3, 5, 4, 2]

f = open("my_data.dat", 'wb')
pickle.dump(box, f)
f.close()