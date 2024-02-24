class Game():
	def __init__(self):
		self.gameArray = [
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0],
		]

		self.gameIndexInArray = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9],
		]
  
		self.index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  
	def PrintStateGame(self):
		print('\n~~~~~~~~~~~~~~~~~~~~~game state~~~~~~~~~~~~~~~~~~~~~\n')
  
		for i in range(0,3):
			print('\t', self.gameArray[i], '\t\t', self.gameIndexInArray[i])
   
		print('\n~~~~~~~~~~~~~~~~~~~~~game state~~~~~~~~~~~~~~~~~~~~~')

	def PrintPreInfoGame(self, name):
		self.PrintStateGame()
		print(f'Ваш хід {name}, оберіть поле для вводу із вільних індексів {self.index}:')
  
	def CalculateStep(self, inputGameIndex, name):
		if inputGameIndex in self.index:
			self.index.remove(inputGameIndex)
   
			if inputGameIndex == 1 or inputGameIndex == 2 or inputGameIndex == 3:
				self.gameArray[0][inputGameIndex - 1] = name
    
			elif inputGameIndex == 4 or inputGameIndex == 5 or inputGameIndex == 6:
				self.gameArray[1][inputGameIndex - 4] = name
    
			elif inputGameIndex == 7 or inputGameIndex == 8 or inputGameIndex == 9:
				self.gameArray[2][inputGameIndex - 7] = name
    
		else:
			return False
			
	def PrintError(self, numberError):
		if numberError == 1:
			print('Неправильна дія! Такого індекса не має у доступних!')
  
	def StepOne(self, name):
		self.PrintPreInfoGame(name)

		index = int(input('Обраний індекс: '))

		if self.CalculateStep(index, name) == False:
			self.PrintError(1)
   
		finVarGame = self.FinGame()
		if finVarGame == True:
			print('Кінець гри')
			return True

		else:
			return False

  
	def FinGame(self):
		###
		return False
  		###
  
GameEngOne = Game()

while True:
	step = GameEngOne.StepOne('X')
	if step == True:
		break

	step = GameEngOne.StepOne('O')
	if step == True:
		break