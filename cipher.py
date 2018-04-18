import math
#Goal be able to encrypt/decrypt message using three different ciphers
#Have program ask:

   #"Would you like to encyrpt or decrypt your message"
encrypt_vs_decrypt = input('Would you prefer to encrypt or decrypt your desired message? \n >')
  
   #"What cipher would you like to utilize?  #Show list of available ciphers
chosen_variable = input('''What cipher would you like to utilize? \n 
1.) For the Transposition cipher enter: "Transposition or T"
2.) For the Atbash cipher enter: "Atbash or A" 
3.) For the Polybius cipher enter: 'Polybius' \n
>''')

#if transpositino is selected, give option to enter key, otherwise make key = 0
if chosen_variable.lower() == 'transposition':   
	key = input('''What is your key? 
***Key must be a number greater than 2 and less than 
half of the total characters typed
\n>''')
else:
	key = 0

   #"What is your message", store message in variable
personal_message = input('Please enter your message, only use letters and/or spaces: \n>')
   #run program based on cipher chosen

#monoalphabetic substitution dictionary
atbash_dict = {'a':'z', 'b':'y', 'c':'x','d':'w','e':'v','f':'u','g':'t',
'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'n':'m',
'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f',
'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a'
 }

#basic polybius square
polybius_square = {'a':'11', 'b':'12', 'c':'13', 'd':'14', 'e':'15',
 'f':'21', 'g':'22', 'h':'23', 'i':'24', 'j':'24', 'k':'25',
 'l':'31', 'm':'32', 'n':'33', 'o':'34', 'p':'35',
 'q':'41', 'r':'42', 's':'43', 't':'44', 'u':'45',
 'v':'51', 'w':'52', 'x':'53', 'u':'54', 'z':'55'
}

 #create cipher class that all cipher attributes have:
class Cipher():
 	"""create generic method/attributes that all ciphers utilize"""

 	def __init__(self, personal_message, key):   #attributes?-->cipher name, key?
 		self.personal_message = personal_message
 		self.key = key
  #create individual cipher class

class TranspositionCipher(Cipher):
	'''columnar cipher class that forms encrypted ciphertext
	   or decrypted plaintext, a key must be provided and the
	   key must be a number that is greater than 2 and less than 
	   the total character length of the message divided by 2
	   '''
	def __init__(self, personal_message, key):
		super().__init__(personal_message, key)
		self.ciphertext = ['']

	def encrypt(self):
		#encrypts personal message into ciphertext
		self.key = int(key)
		self.ciphertext = [''] * self.key

		for column in range(0, self.key):
			message_index = column
			while message_index < len(self.personal_message):
				self.ciphertext[column] += self.personal_message[message_index]
				message_index += self.key
		self.ciphertext = ''.join(self.ciphertext)
		encrypted_message = "Your encrypted message is: \n\n > {}".format(self.ciphertext)
		return encrypted_message

	def decrypt(self):
		#decrypt personal message into plaintext
		column_set = len(self.personal_message)/self.key  #get number of columns
		column_set = math.ceil(column_set)
		#get row vs columns
		grid= column_set * self.key
		#find out how many blocks to shade in grid-leng(personal_message)
		shaded_grid = grid - len(self.personal_message)
		rows_vs_shaded = self.key -shaded_grid
		plaintext = [''] * column_set

		column = 0
		row = 0
		for character in self.personal_message:
			plaintext[column] += character
			column += 1

			if (column == column_set) or (column == column_set - 1 and row >= rows_vs_shaded):
				column = 0
				row +=1

		decryption = ''.join(plaintext)
		decrypted_message = "Your decrypted message is: \n\n > {}".format(decryption)
		return decrypted_message.title()
	
		
class AtbashCipher(Cipher):
	'''cipher class that forms encrypted ciphertext
	   or decrypted plaintext, no key is needed as it utilizes
	   monoalphabetic substitution through the atbash dictionary
	   '''
	def __init__(self, personal_message, key ):
		super().__init__(personal_message, key)
		self.ciphertext = []

	def encrypt(self):
		#encrypts personal message into ciphertext
		self.ciphertext = []
		message_lower = self.personal_message.lower()
		
		for key in message_lower:
			if key in atbash_dict:
				self.ciphertext += atbash_dict[key]
			elif key == ' ':
				self.ciphertext += ' '
		encryption = ''.join(self.ciphertext)
		encrypted_message = "Your encrypted message is: \n\n > {}".format(encryption)
		return encrypted_message

	def decrypt(self):
		#decrypts personal message into plaintext
		plaintext = []
		message_lower = self.personal_message.lower()
		for value in message_lower:
			if value in atbash_dict:
				plaintext += atbash_dict[value]
			elif value == ' ':
				plaintext += ' '
		decryption = ''.join(plaintext)
		decrypted_message = "Your decrypted message is: \n\n > {}".format(decryption)
		return decrypted_message.title()


class PolybiusCipher(Cipher):
	'''cipher class that forms encrypted ciphertext or
	   decrypted plaintext, no key is needed as it utilizes
	   dictionary thats key and values make up a basic 
	   polybius square
	   '''

	def __init__(self, personal_message, key):
		super().__init__(personal_message, key)
		self.ciphertext = []

	def encrypt(self):
		#encrypts personal message into ciphertext
		self.ciphertext = []
		message_lower = self.personal_message.lower()
		for let in message_lower:
			if let in polybius_square:
				self.ciphertext.append(polybius_square[let])
			elif let == ' ':
				self.ciphertext.append('')
		encryption = ' '.join(self.ciphertext)
		encrypted_message = "Your encrypted message is: \n\n > {}".format(encryption)
		return encrypted_message

	def decrypt(self):
		#decrypts personal message into plaintext
		encrypted_message_list = self.personal_message.split()
		plaintext = ''
		for number in encrypted_message_list:
			for key, value in polybius_square.items():
				if number == value:
					plaintext += key
				elif number == ' ':
					plaintext += ' '
		decrypted_message = "Your decrypted message is: \n\n > {}".format(plaintext)
		return decrypted_message.title()

def main():
	if chosen_variable.lower() == 'transposition':
		trans_cipher = TranspositionCipher(personal_message, key)
		if encrypt_vs_decrypt == "encrypt":
			print(trans_cipher.encrypt())	
		elif encrypt_vs_decrypt == 'decrypt':
			trans_cipher.encrypt()
			print(trans_cipher.decrypt())
	elif chosen_variable.lower() == 'atbash':
		atbash_cipher = AtbashCipher(personal_message, key)
		if encrypt_vs_decrypt == 'encrypt':
			print(atbash_cipher.encrypt())
		elif encrypt_vs_decrypt == 'decrypt':
			print(atbash_cipher.decrypt())
	elif chosen_variable.lower() == 'polybius':
		polybius_cipher = PolybiusCipher(personal_message, key)
		if encrypt_vs_decrypt == 'encrypt':
			print(polybius_cipher.encrypt())
		elif encrypt_vs_decrypt == 'decrypt':
			print(polybius_cipher.decrypt())

if __name__=='__main__':
	main()
#run cipher that was chosen
#either encrypt or decrypt messaging depending input
#print message for 