import pickle
favorite = ['a','s','d','r','w','t','w']
save_file = open('C:\\Users\\Lampadov\\Desktop\\favorites.dat', 'wb')
pickle.dump(favorite, save_file)
save_file.close()
load_file = open('C:\\Users\\Lampadov\\Desktop\\favorites.dat', 'rb')
loaded = pickle.load(load_file)
load_file.close()
print(loaded)
