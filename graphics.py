import pygame
import sys

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5D Chess Alpha")

import textures

# cosmetic var
tile_size = WIDTH//18
start_x, start_y = WIDTH//16, HEIGHT//12
colset_light = [(255, 230, 200), (80, 40, 0), (240, 190, 137), (0, 0, 0), (220, 160, 120), (0, 0, 0)] # bg color, black tiles, white tiles, text color
colset_dark = [(60, 60, 80), (0, 0, 0), (180, 180, 200), (255, 255, 255), (200, 200, 220), (50, 50, 50)]	
font = pygame.font.Font(None, WIDTH//48)
	
# defaults
colors = colset_dark
bulb, bulb_rect = textures.ui_dark[0][0], textures.ui_dark[1][0]
gear, gear_rect = textures.ui_dark[0][1], textures.ui_dark[1][1]
king_white = textures.pieces[0]

def open_settings(window, colors, WIDTH, HEIGHT):
	x, y = WIDTH//6, HEIGHT//3
	pygame.draw.rect(window, colors[2], (WIDTH//2-(0.5*x), HEIGHT//2-(0.5*y), x, y))
	pygame.draw.rect(window, colors[1], (WIDTH//2-(0.5*x), HEIGHT//2-(0.5*y), x, y), 5)
	
def draw_grid(window, tile_size, start_x, start_y, colors):
	for i in range(8):
		for j in range(8):
			x = start_x + i * tile_size
			y = start_y + j * tile_size
			if (i + j) % 2 == 0:
				pygame.draw.rect(window, colors[1], (x, y, tile_size, tile_size))
				pygame.draw.rect(window, colors[5], (x, y+tile_size*0.9, tile_size, tile_size*0.1))
			else:
				pygame.draw.rect(window, colors[2], (x, y, tile_size, tile_size))
				pygame.draw.rect(window, colors[4], (x, y+tile_size*0.9, tile_size, tile_size*0.1))
			pygame.draw.circle(window, colors[0], (x, y), 5)
			pygame.draw.rect(window, colors[0], (x, y, tile_size, tile_size), 3, 5)

		#letters & numbers on sides
		letter_row_tile = font.render(chr(65+i), True, colors[3])
		number_row_tile = font.render(str(i+1), True, colors[3])
		window.blit(letter_row_tile, (start_x + i * tile_size + tile_size//2.2, start_y + tile_size * 8 + tile_size//4)) # this is really bad code
		window.blit(number_row_tile, (start_x - tile_size//2.5, start_y + i * tile_size + tile_size//2.5)) # but it works so i dont really care actually
		
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if bulb_rect.collidepoint(event.pos):
				colors = colset_dark if colors == colset_light else colset_light
				bulb = textures.ui_dark[0][0] if bulb == textures.ui_light[0][0] else textures.ui_light[0][0]
				bulb_rect = textures.ui_dark[1][0] if bulb == textures.ui_light[1][0] else textures.ui_light[1][0]
				gear = textures.ui_dark[0][1] if gear == textures.ui_light[0][1] else textures.ui_light[0][1]
				gear_rect = textures.ui_dark[1][1] if gear == textures.ui_light[1][1] else textures.ui_light[1][1]
			#elif gear_rect.collidepoint(event.pos):
				

	window.fill((colors[0]))
	draw_grid(window, tile_size,start_x,start_y,colors)
	
	window.blit(bulb, (WIDTH-WIDTH//30, HEIGHT//40))
	window.blit(gear, (WIDTH-WIDTH//16, HEIGHT//40))
	
	#open_settings(window, colors, WIDTH, HEIGHT)
	
	textures.test_pieces(window,textures.pieces,tile_size)
	
	#window.blit(textures.pieces[1], (170,130))
	#	this is format for all the pieces grigory if you connect graphics to logic do it with this
	pygame.display.flip()

pygame.quit()
sys.exit()
