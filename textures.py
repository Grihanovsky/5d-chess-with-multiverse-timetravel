import pygame

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

def get_texture(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load("ui/"+file+".png").convert_alpha()
	texture = pygame.transform.scale(preload,(width//scale_factor_x,height//scale_factor_y))
	texture_rect = texture.get_rect(topleft=(width-width//scale_factor_x, height//scale_factor_y))
	return texture, texture_rect

def get_piece(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load("pieces_2d/"+file+".png").convert_alpha()
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

pieces = ["king_light","king_black","queen_white","queen_black","bishop_white","bishop_black","knight_white","knight_black","rook_white","rook_black","pawn_white","pawn_black"]

for i in range(len(pieces)):
	pieces[i] = get_piece(f"{pieces[i]}", WIDTH, HEIGHT, WIDTH//100, HEIGHT//100)

def test_pieces(window,pieces,tile_size):
	x, y = 180, 140
	window.blit(pieces[9], (x,y))
	window.blit(pieces[7], (x+tile_size,y))
	window.blit(pieces[5], (x+tile_size*2,y))
	window.blit(pieces[1], (x+tile_size*3,y))
	window.blit(pieces[3], (x+tile_size*4,y))
	window.blit(pieces[5], (x+tile_size*5,y))
	window.blit(pieces[7], (x+tile_size*6,y))
	window.blit(pieces[9], (x+tile_size*7,y))
	for i in range(0,8):
		window.blit(pieces[11], (x+tile_size*i,y+tile_size))
	window.blit(pieces[8], (x,y+tile_size*7))
	window.blit(pieces[6], (x+tile_size,y+tile_size*7))
	window.blit(pieces[4], (x+tile_size*2,y+tile_size*7))
	window.blit(pieces[0], (x+tile_size*3,y+tile_size*7))
	window.blit(pieces[2], (x+tile_size*4,y+tile_size*7))
	window.blit(pieces[4], (x+tile_size*5,y+tile_size*7))
	window.blit(pieces[6], (x+tile_size*6,y+tile_size*7))
	window.blit(pieces[8], (x+tile_size*7,y+tile_size*7))
	for i in range(0,8):
		window.blit(pieces[10], (x+tile_size*i,y+tile_size*6))


