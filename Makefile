##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## Makefile
##

NAME	=	groundhog

all: $(NAME)

$(NAME):
	cp main.py $(NAME)
	chmod 755 $(NAME)

clean:
	rm -rf __pycache__

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: re fclean all
