import pygame
import math

class Box():
	def __init__(self, n, number = None):
		self.size = 100
		self.x = n % 9 * self.size
		self.y = math.floor(n / 9) * self.size
		self.rect = rect = pygame.Rect(self.x, self.y, 100 ,100)
		self.number = number
		self.font = pygame.font.SysFont(None, 100)
		self.text_offset_y = 20
		self.text_offset_x = 30
		self.text_color = (0, 0, 0)
		self.background_color = (220, 220, 220)
		self.border_color = (105, 105, 105)
		self.selected = False

	def render(self, display):
		pygame.draw.rect(display, self.background_color, self.rect)
		pygame.draw.rect(display, self.border_color, self.rect, width = 1)
		if not self.number is None:
			text = self.font.render(str(self.number), False, self.text_color)
			text_rect = pygame.Rect(self.x + self.text_offset_x, self.y + self.text_offset_y, self.size - self.text_offset_x, self.size - self.text_offset_y)
			display.blit(text, text_rect)

	def set_valid(self, valid):
		if valid:
			self.text_color = (0, 0, 0)
		else:
			self.text_color = (255, 0, 0)

	def set_selected(self, selected):
		self.selected = selected
		if self.selected:
			self.background_color = (95, 186, 194)
		else:
			self.background_color = (220, 220, 220)

	def on_key_up(self, key):
		if not self.selected:
			return
		if key == pygame.K_1 or key == pygame.K_KP1:
			self.number = 1
		elif key == pygame.K_2 or key == pygame.K_KP2:
			self.number = 2
		elif key == pygame.K_3 or key == pygame.K_KP3:
			self.number = 3
		elif key == pygame.K_4 or key == pygame.K_KP4:
			self.number = 4
		elif key == pygame.K_5 or key == pygame.K_KP5:
			self.number = 5
		elif key == pygame.K_6 or key == pygame.K_KP6:
			self.number = 6
		elif key == pygame.K_7 or key == pygame.K_KP7:
			self.number = 7
		elif key == pygame.K_8 or key == pygame.K_KP8:
			self.number = 8
		elif key == pygame.K_9 or key == pygame.K_KP9:
			self.number = 9
		elif key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
			self.number = None
