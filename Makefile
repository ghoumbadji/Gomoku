##
## EPITECH PROJECT, 2022
## B-AIA-500-COT-5-1-gomoku-damia.tobossi
## File description:
## Makefile
##

SRC	=	Board.py	\
		Commands/ErrorCommand.py	\
		Commands/command.py	\
		Info.py	\
		AI/AI.py	\
		Gomoku.py

NAME	=	pbrain-gomoku-ai

RM		=	@rm -f

$(NAME):
	@cp Gomoku.py $@
	@chmod +x $@

all: $(NAME)

exe:
	pyinstaller $(SRC) --name pbrain-gomoku-ai.exe --onefile

clean:
	$(RM) -rf __pycache__
	$(RM) -rf AI/__pycache__
	$(RM) -rf Commands/__pycache__
	$(RM) -rf build
	$(RM) -rf dist
	$(RM) -rf pbrain-gomoku-ai.exe.spec

fclean:	clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
