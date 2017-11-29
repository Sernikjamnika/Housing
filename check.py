from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()

print(lb.fit_transform(['yes', 'noornot', 'no', 'yes']))