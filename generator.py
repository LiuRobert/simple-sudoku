from box import Box
import validator
import random


def generate_easy():
	return __generate(0.5)

def generate_medium():
	board = __generate_random_solved()
	board = __get_reduced_board(board, 55)
	return __board_to_boxes(board)

# Tries to remove as many numbers as number_to_remove from an already solver sudoku.
# But if a removed number results in the sudoku having more than one solution the number will not be removed.
def __get_reduced_board(board, number_to_remove, filter = None):
	print(number_to_remove)
	if filter is None:
		filter = []
	index_to_empty = __get_random(board, False, filter)
	if index_to_empty is None or number_to_remove == 0:
		return board
	filter.append(index_to_empty)
	new_board = board.copy()
	new_board[index_to_empty] = None
	if not validator.has_more_than_one_solution(new_board):
		board = new_board
	return __get_reduced_board(board, number_to_remove - 1, filter)


def __get_random(board, empty, filter = []):
	indexes = []
	for i in range(len(board)):
		if empty and board[i] is None:
			indexes.append(i)
		elif not empty and not board[i] is None:
			indexes.append(i)
	for number in filter:
		if number in indexes:
			indexes.remove(number)
	length = len(indexes)
	if length == 0:
		return None
	return indexes[random.randint(0, length -1)]


def __generate(chance):
	solved = __generate_random_solved()
	board = []
	has_more_than_one_solution = True
	while has_more_than_one_solution:
		board = __remove_board_numbers(solved, chance)
		has_more_than_one_solution = validator.has_more_than_one_solution(board)
	return __board_to_boxes(board)

def __board_to_boxes(board):
	boxes = []
	for i in range(len(board)):
		boxes.append(Box(i, board[i]))
	return boxes

def __remove_board_numbers(board, chance):
	new_board = board.copy()
	for i in range(len(new_board)):
		if random.random() > chance:
			new_board[i] = None
	return new_board

def __generate_random_solved(board = None):
	if board is None:
		board = []
		for i in range(81):
			board.append(None)
	index = __get_first_available_index(board)
	if index == -1:
		return board
	for number in __get_numbers():
		new_board = board.copy()
		new_board[index] = number
		if validator.validate_move(new_board, index):
			solved = __generate_random_solved(new_board)
			if not solved is None:
				return solved
	return None

def __get_numbers():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	random.shuffle(numbers)
	return numbers

def __get_first_available_index(board):
	for i in range(len(board)):
		if board[i] is None:
			return i
	return -1