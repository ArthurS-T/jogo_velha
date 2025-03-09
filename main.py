from random import randrange


def display_board(quadro):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(quadro[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def entrar_movimento(quadro):
	ok = False
	while not ok:
		move = input("Entre o seu movimento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("Movimento não permitido, repita!")
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		sign = quadro[row][col]
		ok = sign not in ['O','X'] 
		if not ok:
			print("Localização ocupada no quadro, repita o seu movimento")
			continue
	quadro[row][col] = 'O'


def lista_de_quadrados_livres(quadro):
	livre = []	
	for row in range(3): 
		for col in range(3):
			if quadro[row][col] not in ['O','X']:
				livre.append((row,col))
	return livre


def vitoria_para(quadro,sgn):
	if sgn == "X":
		quem = 'computador'
	elif sgn == "O":
		quem = 'jogador'
	else:
		quem = None
	cross1 = cross2 = True #checando as diagonais
	for rc in range(3):
		if quadro[rc][0] == sgn and quadro[rc][1] == sgn and quadro[rc][2] == sgn:
			return quem
		if quadro[0][rc] == sgn and quadro[1][rc] == sgn and quadro[2][rc] == sgn:
			return quem
		if quadro[rc][rc] != sgn:
			cross1 = False
		if quadro[2 - rc][2 - rc] != sgn:
			cross2 = False
	if cross1 or cross2:
		return quem
	return None


def desenhar_movimento(quadro):
	livre = lista_de_quadrados_livres(quadro)
	cnt = len(livre)
	if cnt > 0:	
		this = randrange(cnt)
		row, col = livre[this]
		quadro[row][col] = 'X'


quadro = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
quadro[1][1] = 'X' # Computador sempre começa com X no meio
livre = lista_de_quadrados_livres(quadro)
turno_jogador = True
while len(livre):
	display_board(quadro)
	if turno_jogador:
		entrar_movimento(quadro)
		vencedor = vitoria_para(quadro,'O')
	else:	
		desenhar_movimento(quadro)
		vencedor = vitoria_para(quadro,'X')
	if vencedor != None:
		break
	turno_jogador = not turno_jogador		
	livre = lista_de_quadrados_livres(quadro)

display_board(quadro)
if vencedor == 'jogador':
	print("Você venceu!")
elif vencedor == 'computador':
	print("Eu venci!")
else:
	print("Empate!")
