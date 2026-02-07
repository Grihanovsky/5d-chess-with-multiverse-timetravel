import logic
import new_graphics
import pygame
import sys


pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5D Chess Alpha")

Black_is_up = True

tile_size = WIDTH//18
start_x, start_y = WIDTH//16, HEIGHT//12


colset_light = [(255, 230, 200), (80, 40, 0), (240, 190, 137), (0, 0, 0), (220, 160, 120), (0, 0, 0)] # bg color, black tiles, white tiles, text color
colset_dark = [(60, 60, 80), (0, 0, 0), (180, 180, 200), (255, 255, 255), (200, 200, 220), (50, 50, 50)]	
colours = colset_dark

ui_dark, ui_light, pieces = new_graphics.load_gui(WIDTH, HEIGHT)
ui = ui_light


font = pygame.font.Font(None, tile_size//4)
bulb,bulb_rect = ui_dark[0][0],ui_dark[1][0]
gear,gear_rect = ui_dark[0][1],ui_dark[1][1]




running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if bulb_rect.collidepoint(event.pos):
				colours = colset_dark if colours == colset_light else colset_light
				bulb = ui_dark[0][0] if bulb == ui_light[0][0] else ui_light[0][0]
				gear = ui_dark[0][1] if gear == ui_light[0][1] else ui_light[0][1]
			if gear_rect.collidepoint(event.pos):
				if Black_is_up == True:
					Black_is_up = False
				else:
					Black_is_up = True

	window.fill(colours[0])
	new_graphics.draw_board(window,tile_size,start_x,start_y,colours,font,Black_is_up)
	new_graphics.draw_pieces(window,pieces,start_x,start_y,tile_size)


	#pygame.draw.rect(window, colours[5], bulb_rect) was here for debugging
	new_graphics.draw_theme_switch(window,bulb,WIDTH-WIDTH//30, HEIGHT//40)
	new_graphics.draw_settings_button(window,gear,WIDTH-WIDTH//16, HEIGHT//40)



	pygame.display.flip()

pygame.quit()
sys.exit()