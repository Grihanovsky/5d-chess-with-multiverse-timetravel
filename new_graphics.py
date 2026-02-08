import pygame


def draw_board(window,tile_size,start_x,start_y,colours,font,black_is_up): # works	

	for i in range(8):
		for j in range(8):


			x = start_x + j * tile_size
			y = start_y + i * tile_size
		 

			if (i + j) % 2 == 1:
				pygame.draw.rect(window, colours[1], (x, y, tile_size, tile_size))
				pygame.draw.rect(window, colours[5], (x, y+tile_size*0.9, tile_size, tile_size*0.1))
					
				if j == 0:
					if black_is_up:
						number_row_tile = font.render(str(8-i), True, colours[2])
					else:
						number_row_tile = font.render(str(i+1), True, colours[2])

				if i == 7:
					if black_is_up:
						letter_row_tile = font.render(chr(97+j), True, colours[2])
					else:
						letter_row_tile = font.render(chr(104-j), True, colours[2])



			else:
				pygame.draw.rect(window, colours[2], (x, y, tile_size, tile_size))
				pygame.draw.rect(window, colours[4], (x, y+tile_size*0.9, tile_size, tile_size*0.1))

				if j == 0:
					if black_is_up:
						number_row_tile = font.render(str(8-i), True, colours[1])
					else:
						number_row_tile = font.render(str(i+1), True, colours[1])

				if i == 7:
					if black_is_up:
						letter_row_tile = font.render(chr(97+j), True, colours[1])
					else:
						letter_row_tile = font.render(chr(104-j), True, colours[1])
								
			if j == 0:
				window.blit(number_row_tile, (x + tile_size//12, y + tile_size//12)) 

			if i == 7:
				window.blit(letter_row_tile, (x + tile_size - tile_size //5.5, y + tile_size - tile_size //3.5))
				
			
			pygame.draw.circle(window, colours[0], (x, y), 5)
			pygame.draw.rect(window, colours[0], (x, y, tile_size, tile_size), 3, 5)


def draw_theme_switch(window,switch, x,y):
	window.blit(switch, (x,y))

def draw_settings_button(window,gear, x,y):
    window.blit(gear, (x,y))

def draw_pieces(window,piece_texture,piece, x,y,tile_size,black_is_up):
	if piece.on_board:
		if black_is_up:
			if piece.name[1] == "P":
				if piece.name[0] == "W":
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))
				else:
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))

			else:
				if piece.name[0] == "W":
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))
				else:
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))
		
		
		else:
			if piece.name[1] == "P":
				if piece.name[0] == "W":
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))
				else:
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))

			else:
				if piece.name[0] == "W":
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))
				else:
					window.blit(piece_texture, (x+(tile_size//6)+tile_size*piece.position[1],y+(tile_size//7)+tile_size*(piece.position[0])))

def draw_possible_moves(window, tile_size, start_x, start_y, cell_attacked,colour):
	pygame.draw.circle(window, colour, (start_x + tile_size*int(cell_attacked[2])+tile_size//2, start_y + tile_size*int(cell_attacked[0])+tile_size//2), tile_size//4)


def load_gui(width, height):
	ui_dark = [["bulb_dark","gear_dark"],["bulb_dark_rect","gear_dark_rect"]]
	ui_light = [["bulb_light","gear_light"],["bulb_light_rect","gear_light_rect"]]

	for i in range(len(ui_light)):
		ui_light[0][i], ui_light[1][i] = load_textures(f"{ui_light[0][i]}", width, height, width//60, height//60)
		ui_dark[0][i], ui_dark[1][i] = load_textures(f"{ui_dark[0][i]}", width, height, width//60, height//60)


	#pieces = ["king_light","king_black","queen_white","queen_black","bishop_white","bishop_black","knight_white","knight_black","rook_white","rook_black","pawn_white","pawn_black"]
	pieces = ["rook_white","knight_white","bishop_white","queen_white","king_light","bishop_white","knight_white","rook_white","rook_black","knight_black","bishop_black","queen_black","king_black","bishop_black","knight_black","rook_black","pawn_white","pawn_black"]

	for i in range(len(pieces)):
		pieces[i] = load_pieces(f"{pieces[i]}", width, height, width//110, height//110)

	return ui_dark, ui_light, pieces

def load_textures(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load("5d-chess-with-multiverse-timetravel/ui/"+file+".png").convert_alpha()
	texture = pygame.transform.scale(preload,(width//scale_factor_x,height//scale_factor_y))
	if file[0] == "b":
		texture_rect = pygame.Rect(width-width//30, height//40,width//scale_factor_x,height//scale_factor_y)
	else:
		texture_rect = pygame.Rect(width-width//16, height//40,width//scale_factor_x,height//scale_factor_y)

	return texture, texture_rect

def load_pieces(file, width, height, scale_factor_x, scale_factor_y):
	preload = pygame.image.load("5d-chess-with-multiverse-timetravel/pieces_2d/"+file+".png").convert_alpha()
	texture = pygame.transform.scale(preload,(width//scale_factor_x,height//scale_factor_y))
	return texture