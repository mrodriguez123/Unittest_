import unittest
import main
import pytest

facts = ('Name', 'Year born', "Favorite Foods")
Nata = ('Nata', 1965, [('Paella', 'Calamares en su tinta', 'Langosta')] )
Javi = ('Javi', 1962, [('Macarrones con chorizo', 'Angulas', 'Bogabante')])
Moni = ('Moni', 2000, [('Sushi', 'Pizza', 'Macarrones con chorizo')])
Bea = ('Bea', 2002, [ ('Macarrones con chorizo', 'Helado', 'Palmitos')])
members = (Nata, Javi, Moni, Bea)

class TestMain(unittest.TestCase):

	def test_individual_facts(self):
		self.assertEqual(main.individual_facts(facts, Nata)['Name'], 'Nata')
		self.assertEqual(main.individual_facts(facts, Javi)['Favorite Foods'], [('Macarrones con chorizo', 'Angulas', 'Bogabante')])
		self.assertEqual(main.individual_facts(facts, Moni)['Year born'], 2000)
		self.assertEqual(main.individual_facts(facts, Bea)['Year born'], 2002)

	def test_family_facts(self):
		self.assertEqual(main.family_facts(facts, members)[0]['Year born'], 1965)
		self.assertEqual(main.family_facts(facts,members)[1]['Name'], 'Javi')
		self.assertEqual(main.family_facts(facts, members)[2]['Favorite Foods'], [('Sushi', 'Pizza', 'Macarrones con chorizo')])
		self.assertEqual(main.family_facts(facts, members)[3]['Year born'], 2002)
		
	def test_fam_facts_tuple(self):
		self.assertEqual(main.fam_facts_tuple(members)[0][1], 1965)
		self.assertEqual(main.fam_facts_tuple(members)[1][0], 'Javi')
		self.assertEqual(main.fam_facts_tuple(members)[2][2], [('Sushi', 'Pizza', 'Macarrones con chorizo')])
		self.assertEqual(main.fam_facts_tuple(members)[3][1], 2002)



if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

