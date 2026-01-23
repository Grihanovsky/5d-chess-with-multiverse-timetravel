import pygame

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

def get_texture(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load(file+".png").convert_alpha()
	texture = pygame.transform.scale(preload,(width//scale_factor_x,height//scale_factor_y))
	texture_rect = texture.get_rect(topleft=(width-width//scale_factor_x, height//scale_factor_y))
	return texture, texture_rect

def get_piece(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load(file+".png").convert_alpha()
	texture = pygame.transform.scale(preload,(width//scale_factor_x,height//scale_factor_y))
	return texture

ui_light = [["bulb_light","gear_light"],["bulb_light_rect","gear_light_rect"]]

# light mode
for i in range(len(ui_light)):
	ui_light[0][i], ui_light[1][i] = get_texture(f"{ui_light[0][i]}", WIDTH, HEIGHT, WIDTH//60, HEIGHT//60)

ui_dark = [["bulb_dark","gear_dark"],["bulb_dark_rect","gear_dark_rect"]]

# dark mode
for i in range(len(ui_dark)):
	ui_dark[0][i], ui_dark[1][i] = get_texture(f"{ui_dark[0][i]}", WIDTH, HEIGHT, WIDTH//60, HEIGHT//60)

pieces = ["king_light","king_black","queen_white","queen_black"]

for i in range(len(pieces)):
	pieces[i] = get_piece(f"{pieces[i]}", WIDTH, HEIGHT, WIDTH//120, HEIGHT//120)
