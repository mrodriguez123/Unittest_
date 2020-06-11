from collections import namedtuple

facts = ('Name', 'Year born', 'Favorite Foods')
Nata = ('Nata', 1965, ['Paella', 'Calamares en su tinta', 'Langosta'] )
Javi = ('Javi', 1962, ['Macarrones con chorizo', 'Angulas', 'Bogabante'])
Moni = ('Moni', 2000, ['Sushi', 'Pizza', 'Macarrones con chorizo'])
Bea = ('Bea', 2002, ['Macarrones con chorizo', 'Helado', 'Palmitos'])
members = (Nata, Javi, Moni, Bea)

#returns the facts for a single person
def individual_facts(keys, person):
	diction = {}
	for i in range(len(keys)):
		diction[keys[i]]= person[i]
	return diction
individual_facts(facts, Nata)


#list of dictionaries of the facts of everyone in the fam
def family_facts(keys, lists):
	x= []
	for i in range(len(lists)):
		x.append(individual_facts(keys, lists[i]))
	return x

family_facts(facts, members)


Family_member = namedtuple('Family_member', ['Name', 'Year_Born', 'Favorite_Foods'])
# creates a list of namedtuples for all the data in the family
def fam_facts_tuple(data):
	ans= []
	for i in range(len(data)):
		#for j in range(len(person)):
		name= data[i][0]
		year_born= data[i][1]
		fav_foods= data[i][2]
		ans.append(Family_member(name, year_born, fav_foods))
	return ans
fam_facts_tuple(members)


