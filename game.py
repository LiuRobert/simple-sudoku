import pygame
from box import Box
import validator
import generator

size = 900, 900
pygame.init()
pygame.font.init() 
display = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

light_gray = (220, 220, 220)
dark_gray = (105, 105, 105)
black = (0, 0, 0)

running = True

outlines = []
outlines.append(pygame.Rect(0, 0, 300, 300))
outlines.append(pygame.Rect(300, 0, 300, 300))
outlines.append(pygame.Rect(600, 0, 300, 300))

outlines.append(pygame.Rect(0, 300, 300, 300))
outlines.append(pygame.Rect(300, 300, 300, 300))
outlines.append(pygame.Rect(600, 300, 300, 300))

outlines.append(pygame.Rect(0, 600, 300, 300))
outlines.append(pygame.Rect(300, 600, 300, 300))
outlines.append(pygame.Rect(600, 600, 300, 300))

boxes = []
for i in range(0, 81):
	boxes.append(Box(i, None))


def on_update():
	validator.validate_boxes(boxes)
	for box in boxes:
		box.render(display)
	for outline in outlines:
		pygame.draw.rect(display, black, outline, width = 6)
	pygame.display.update()


def on_mouse_up():
	x, y = pygame.mouse.get_pos()
	for box in boxes:
		selected = x > box.x and x < box.x + box.size and y > box.y and y < box.y + box.size
		box.set_selected(selected)

def get_selected_box():
	for i in range(len(boxes)):
		if boxes[i].selected:
			return boxes[i], i 
	return None, -1


def on_key_up(key):
	global boxes
	selected_box, index = get_selected_box()
	if not selected_box is None: 
		new_index = None
		if key == pygame.K_UP:
			new_index = index - 9
		elif key == pygame.K_LEFT:
			new_index = index - 1
		elif key == pygame.K_RIGHT:
			new_index = index + 1
		elif key == pygame.K_DOWN:
			new_index = index + 9
		if not new_index is None and new_index >= 0 and new_index < len(boxes):
			boxes[index].set_selected(False)
			boxes[new_index].set_selected(True)

	for box in boxes:
		box.on_key_up(key)
	if key == pygame.K_c:
		boxes = validator.solve(boxes)
	elif key == pygame.K_j:
		boxes = generator.generate_easy()
	elif key == pygame.K_k:
		boxes = generator.generate_medium()
	# elif key == pygame.K_l:
	# 	boxes = generator.generate_hard()


on_update()
while running:
	for event in pygame.event.get():
		updated = False
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			updated = True
			on_mouse_up()
		elif event.type == pygame.KEYUP:
			updated = True
			on_key_up(event.key)
		if updated:
			on_update()