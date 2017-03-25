names = ['sagar aryal', 'Rajesh Hamal','Deepak Olee']
names[0] = 'Sagar Aryal'

print(names)

names.append('Sachin Ramesh')
names.append('Sewag Virendar')
print('Names Finally: ', names)
print('Last name in the list :%s' %names[-1])


joined_names = '\n'.join(names)
print('\nJoined Names:')
print(joined_names)