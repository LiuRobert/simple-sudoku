import math
from box import Box

def validate_boxes(boxes):
	board = []
	for box in boxes:
		board.append(box.number)

	for i in range(len(board)):
		if board[i] is None:
			boxes[i].set_valid(True)
		else:
			boxes[i].set_valid(__validate_move(board, i))

def solve(boxes):
	board = []
	for box in boxes:
		board.append(box.number)
	board = __solve(board)
	for i in range(len(boxes)):
		boxes[i].number = board[i]
	return boxes

def __solve(board):
	index = __get_first_available_index(board)
	if index == -1:
		return board
	for number in range(1, 10):
		new_board = board.copy()
		new_board[index] = number
		if __validate_move(new_board, index):
			solved = __solve(new_board)
			if not solved is None:
				return solved
	return None

def __get_first_available_index(board):
	for i in range(len(board)):
		if board[i] is None:
			return i
	return -1

def __validate_move(board, index):
	valid = True
	valid = valid & __check_horizontal(board, index)
	valid = valid & __check_vertical(board, index)
	valid = valid & __check_quadrant(board, index)
	return valid

def __check_horizontal(board, index):
	number = board[index]
	start_index = index - (index % 9)
	for i in range(start_index, start_index + 9):
		if i != index and board[i] == number:
			return False
	return True

def __check_vertical(board, index):
	number = board[index]
	start_index = index % 9
	for i in range(start_index, start_index + 73, 9):
		if i != index and board[i] == number:
			return False
	return True

def __check_quadrant(board, index):
	number = board[index]
	row_start = index - index % 3
	# print(row_start)
	row = math.floor(index / 9)
	start_index = row_start - row % 3 * 9
	for row_index in range(3):
		current_row_start_index = start_index + row_index * 9
		for i in range(current_row_start_index, current_row_start_index + 3):
			if i != index and board[i] == number:
				return False
	return True
