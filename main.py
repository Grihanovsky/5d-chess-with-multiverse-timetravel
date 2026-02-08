import logic
import new_graphics
import pygame
import sys


pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5D Chess Alpha")


tile_size = WIDTH//18
start_x, start_y = WIDTH//16, HEIGHT//12


colset_light = [(255, 230, 200), (80, 40, 0), (240, 190, 137), (255, 255, 255), (220, 160, 120), (0, 0, 0)] # bg color, black tiles, white tiles, text color
colset_dark = [(60, 60, 80), (0, 0, 0), (180, 180, 200), (255, 255, 255), (200, 200, 220), (50, 50, 50)]	
colours = colset_dark

ui_dark, ui_light, pieces_texture = new_graphics.load_gui(WIDTH, HEIGHT)
ui = ui_light


font = pygame.font.Font(None, tile_size//4)
bulb,bulb_rect = ui_dark[0][0],ui_dark[1][0]
gear,gear_rect = ui_dark[0][1],ui_dark[1][1]

Black_is_up = False
Pieces = logic.Create_Pieces(Black_is_up)

board = logic.Board_set_up(8,Black_is_up)
board_rect = pygame.Rect(start_x, start_y,tile_size*8,tile_size*8)
turn = 0
players = ["W","B"]

selected = False
selected_piece = ""
targeted_cells_rects = []
index_longterm = -1

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

			elif gear_rect.collidepoint(event.pos):
				if Black_is_up == True:
					Black_is_up = False
				else:
					Black_is_up = True
				Pieces = logic.Create_Pieces(Black_is_up)
				board = logic.Board_set_up(8,Black_is_up)
				turn =0 
				selected = False

			for i in range(len(targeted_cells_rects)):
				if targeted_cells_rects[i].collidepoint(event.pos):
					#print(f"Tried to move to {targeted_cells_rects[i]} with {Pieces[index_longterm].name}")
					try:
						board = logic.Piece.Move_n_Take(Pieces[index_longterm],(int(move_list[i][0]),int(move_list[i][2])),board,Pieces)
						turn += 1
					except:
						pass
					move_list = []


			if board_rect.collidepoint(event.pos):
				#print("hit the board")
				index = logic.find_a_piece_by_position(board, Pieces, start_x, start_y, event.pos, tile_size)
				#print(Pieces[index_longterm].name)

				if index != None:
					
					if players[turn % 2] == Pieces[index].name[0]:
						#print(Pieces[index].name)

						move_list,board = logic.find_possible_moves(Pieces[index],board,Black_is_up)
						targeted_cells_rects = logic.find_recs_for_possible_moves(move_list,start_x, start_y,tile_size)
						index_longterm = index

						if selected_piece == Pieces[index].name:
							selected = False
							selected_piece = ""
						else:
							selected = True
							selected_piece = Pieces[index].name
					else:
						selected = False
						move_list = []


	window.fill(colours[0])

	new_graphics.draw_board(window,tile_size,start_x,start_y,colours,font,Black_is_up)

	#if turn == 4:
		#for i in range(len(board)):
			#print(board[i])

	for i in range(len(Pieces)):

		logic.Piece.Find_yourself(Pieces[i],board)

		if i >= 16 and i <= 23:  # draw stuff
			new_graphics.draw_pieces(window,pieces_texture[16],Pieces[i],start_x,start_y,tile_size,Black_is_up)
		elif i > 23:
			new_graphics.draw_pieces(window,pieces_texture[17],Pieces[i],start_x,start_y,tile_size,Black_is_up)
		else:
			new_graphics.draw_pieces(window,pieces_texture[i],Pieces[i],start_x,start_y,tile_size,Black_is_up)

	if selected:
		for i in range(len(move_list)):
			new_graphics.draw_possible_moves(window, tile_size, start_x, start_y, move_list[i],colours[3])


	#pygame.draw.rect(window, colours[5], bulb_rect) was here for debugging
	new_graphics.draw_theme_switch(window,bulb,WIDTH-WIDTH//30, HEIGHT//40)
	new_graphics.draw_settings_button(window,gear,WIDTH-WIDTH//16, HEIGHT//40)



	pygame.display.flip()

pygame.quit()
sys.exit()