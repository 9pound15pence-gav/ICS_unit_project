import pickle
roman_int_f = open('roman.txt.pk', 'rb')
int2roman = pickle.load(roman_int_f)
roman_int_f.close()
print(int2roman)