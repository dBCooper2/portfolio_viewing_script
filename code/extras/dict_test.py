d = {'dict1': 
		{
			'foo': 1, 
			'bar': 2
		}, 
	 'dict2': 
	 	{
	 		'baz': 3, 
	 		'quux': 4
	 	}
	 }
	 
if type(d) == dict:
	print("this is correct")

for i in d.keys():
    print(i)
    for j in d[i].keys():
        print(j)