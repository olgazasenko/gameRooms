import time
import string
from sys import exit
from random import randint

class State(object):
	def __init__(self):
		pass
		
	def enter(self):
		pass

class DangerousRoom(State):
	def enter(self):
		monster = Monster()
		print "\nThere is a monster in this room."
		time.sleep(1)
		player = Player()
		distance = abs(monster.position - player.position) + 1
		print "He is located at a distance %d from you." % distance
		time.sleep(1)
		print "You have two choices:"
		print "1. Shoot him."
		print "2. Throw a grenade."
		while True:
			try:
				choice = int(raw_input("> "))
			except ValueError:
				print "You entered not a number."
			if distance > 5:
				if choice == 2:
					print "Good choice! The monster is far away and it is better to throw a grenade."
					print "He blows up."
					del monster
					return 'siren_room'
				elif choice == 1:
					print "Bad decision. The monster is too far."
					gamble = randint(1,5)
					# The chance that we shot the monster is 1 in 5
					if gamble == 1:
						print "But good news is that you shot it!"
						del monster
						return 'siren_room'
					else:
						print "You missed!"
						time.sleep(1)
						print "The monster comes closer."
						print "He lifts his huge hammer."
						return 'dead'
				else:
					print "Please, choose between 1 and 2."
			else:
				if choice == 1:
					print "Good choice! The monster is close and it is too dangerous to throw a grenade."
					print "You shot him!"
					del monster
					return 'siren_room'
				elif choice == 2:
					print "Bad decision. The monster is close and it is too dangerous to throw a grenade."
					print "You both blow up."
					del monster
					return 'dead'
				else:
					print "Please, choose between 1 and 2."				
		
class SirenRoom(State):
	def enter(self):
		text_array = ["-------------------------------------------",
		"\nDo you know what/who a siren is?",
		"Well guess what. This room is full of sirens.",
		"They are beautiful. Very beautiful. And they are singing.",
		"Their voices are so pleasant. You just want to stay here forever.",
		"However, you can already see the rage in their eyes.",
		"You know they are going to kill you.",
		"You have to act fast.",
		"1. You can just run for the door.",
		"2. Distract them by throwing some chocolate at them and then "
		"run for the door.",
		"3. Start singing too. Maybe they will accept you as their own. "
		"Then you will sneak out while they are asleep.",
		"Choose:"]
		for s in text_array:
			print s 
			time.sleep(1.5)
		while True:
			try:
				choice = int(raw_input("> "))
			except ValueError:
				print "You entered not a number."
			if choice == 1:
				print "What a stupid idea!"
				print "They grab you with their sharp claws."
				return 'dead'
			elif choice == 2:
				print "You know how to deal with women!"
				return 'water_room'
			elif choice == 3:
				print "Hm. This is not the worst strategy."
				print "But here you purely rely on your luck."
				gamble = randint(1, 2)
				# The probability of at least one of the sirens waking up is 1 in 2.
				if gamble == 1:
					text_array = ["Oh shit! One of them woke up!",
					"She starts singing again.",
					"Everybody else wakes up.",
					"You feel drugged by their voices and slowly fall asleep.",
					"They eat you while you are sleeping."]
					for s in text_array:
						print s 
						time.sleep(1.5)
					return 'dead'
				else:	
					print "Thank God nobody woke up!"
					print "Success!"
					return 'water_room'
			else:
				print "Please, choose between 1, 2 and 3."	
		
class WaterRoom(State):
	def enter(self):
		text_array = ["-----------------------------------------------",
		"There is water everywhere.",
		"You have to swim underwater until you reach the other door.",
		"You have to do it on one breath and with eyes closed.",
		"Guess the distance you'll have to swim.",
		"Hint: It is an even number between 2 and 10."]
		for s in text_array:
			print s 
			time.sleep(1.5)
		distance = randint(1, 5) * 2 
		print "Cheat: %d." % distance
		while True:
			try:
				choice = int(raw_input("> "))
			except ValueError:
				print "You entered not a number."
			if choice == distance:
				print "Hell yeah! You got it!"
				return 'lit_room'
			elif choice > distance:
				print "You swam too far! Hit your head and died."
				return 'dead'
			else:
				print "Not enough! You drown."
				return 'dead'
		
class LitRoom(State):
	def enter(self):
		print "---------------------------------------------------"
		time.sleep(1)
		print "Whoa! This is a literature room! Let's see if you like books."
		print "Answer the question:"
		time.sleep(1)
		print "Who wrote the Shawshank Redemption?"
		answer = raw_input("> ")
		if "STEPHEN" in string.upper(answer) or "KING" in string.upper(answer):
			print "Awesome!"
			return 'diamond_room'
		else:
			print "Boo! You lose! The book worm eats you."
			return 'dead'
		
class DiamondRoom(State):
	def enter(self):
		print "--------------------------------------------------"
		time.sleep(1)
		print "So sparkly in here! This room is full of diamonds!"
		print "How many do you take?"
		quantity = raw_input("> ")
		if int(quantity) < 50:
			print "Alright. Seems like you're not greedy."
			time.sleep(1)
			print "This game is finished and we send you into outer space."
			print "With your %d diamonds." % int(quantity)
			return 'finished'
		else:
			print "You greedy bastard!"
			time.sleep(1)
			print "The diamond rain starts. You end up buried underneath."
			return 'dead'
		
class Finished(State):
	def enter(self):
		print "You won!"
		exit(1)
		
class Dead(State):
	
	funny_deaths = ["\nAll your life flashes before your eyes.\n" +
					"You say your last word and close your eyes foerever.",
					"\nIn the end you realize the purpose of living in this world.\n" +
					"But it is too late.",
					"\nYou will never see the sunshine again. This is the end."
					]
	
	def enter(self):
		time.sleep(1)
		print self.funny_deaths[randint(0, len(self.funny_deaths) - 1)]
		exit(1)
		
class Character(object):

	def __init__(self):
		self.position = randint(1, 10)		
	
class Player(Character):

	def attack_gothon(self, gothon):
		pass

	def throw_grenade(self, gothon):
		pass
		
class Monster(Character):

	def __init__(self):
		self.position = randint(1, 10)
		self.dead = False
		
	# or
	# def __init__(self):
    #    self.dead = False
    #    super(Gothon, self).__init__()
		
class Map(object):

	states = {
		'dangerous_room': DangerousRoom(),
		'siren_room': SirenRoom(),
		'water_room': WaterRoom(),
		'lit_room': LitRoom(),
		'diamond_room': DiamondRoom(),
		'finished': Finished(),
		'dead': Dead()
	}
	
	def __init__(self, init_state):	
		self.init_state = init_state
	
	# calls the function that corresponds to the next state
	def next_state(self, next_state):
		val = self.states.get(next_state)
		return val
		
	def starting_state(self):
		return self.next_state(self.init_state)
		
class GameEngine(object):

	def __init__(self, a_map):
		self.map = a_map
		
	def play(self):
		current_state = self.map.starting_state()
		final_state = self.map.next_state('finished')
		
		while current_state != final_state:
			next_state_name = current_state.enter()
			current_state = self.map.next_state(next_state_name)
			
		# enter the final state
		current_state.enter()