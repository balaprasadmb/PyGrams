''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
input_list = []

'''00	06	60	66 = 3
0 0 0 2 0 0 0 0 0 0  -1 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0  0 0 0 2
1 2 4 4
[row,col],
01 02 03 04 05
10 20 30 40 50
16 26 36 46 56
61 62 63 64 65 = 5

00 01 02  1 04 05 06
10 11 12 13 14 15 16
20 21 22 23 24 25 26
30 31 32 33 34 35 36
40 41 42 43 44 45 46
50 51 52 53 54 55 56
60 61 62  2 64 65 66'''
#0,2 = 0,1  0,3  1,1  1,2  1,3
#1,1 = 0,0  0,1  0,2  1,0  2,0  1,2  2,1  2,2
#3,5 = 2,4  2,5  2,6  3,4  3,6  4,4  4,5  4,6
#0,3 = 0,2  0,4  1,1  1,2  1,4

def get_availables(row, col, oppnent):
	moves = []
	if [row,col] == [0,0] or [row,col] == [0,6] or [row,col] == [6,0] or [row,col] == [6,6]:
		n = 3
		if [row,col] == [0,0]:
			moves = [[row, col+1], [row+1, col], [row+1, col+1]]
		if [row,col] == [0,6]:
			moves = [[row, col-1], [row+1, col-1], [row+1, col]]
		if [row,col] == [6,0]:
			moves = [[row -1, col], [row-1, col+1], [row, col+1]]
		if  [row,col] == [6,6]:
			moves = [[row -1, col-1], [row-1, col], [row, col-1]]
	elif row == 0 or col ==0 or row ==6 or col==6:
		n=5
		if row == 0:
			moves = [[row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
		if col == 0:
			moves = [[row-1, col], [row-1, col+1], [row, col+1], [row+1, col], [row+1, col+1]]
		if row == 6:
			moves = [[row, col-1], [row-1, col-1], [row-1, col], [row-1, col+1], [row, col+1]]
		if col == 6:
			moves = [[row-1, col], [row-1, col-1], [row, col-1], [row+1, col-1], [row+1, col]]
	else:
		n=8
		moves = [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
	for move in moves:
		print move[0]
		if input_list[move[0]][move[1]] == -1 or input_list[move[0]][move[1]] == oppnent:
			moves.remove(move)
#	max_val = max(row, col)
#	min_val = min(row, col)
#	for i in range(min_val-1, max_val+1):
#		for j in range(i, max_val+1):
#			print j
#			if i>=0 and i<7 and j>=0 and j<7 and [i, j] != [row, col] and input_list[i][j] == 0:
#				moves.append([i,j])
	return moves
        
def find_position(player):
	for i in range(0, 7):
		for j in range(0,7):
			if input_list[i][j] == player:
				return i, j

def move_to_position():
	pass

def main():
	inputs = raw_input().split()
	temp = []
	for i in range(0, 49):
		temp.append(int(inputs[i]))
		if len(temp) == 7:
			input_list.append(temp)
			temp = []
	player = int(inputs[49])
	print 'Player_id: ' + str(player)
	opp = 3 - player
	print 'Opp_id: ' + str(opp)
	row, col = find_position(player)
	print 'player position: ' + str(row) + ',' + str(col)
	op_row, op_col = find_position(opp)
	print 'Opp position: ' + str(op_row) + ',' + str(op_col)
	avail_moves = get_availables(row, col, opp)
	print avail_moves
	print avail_moves[0]
	avail_moves = get_availables(op_row, op_col, player)
	print avail_moves
	print avail_moves[0]

main()
