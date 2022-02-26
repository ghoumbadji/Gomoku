# Gomoku

## Goal of the project
The goal of the project is to implement a Gomoku Narabe game bot. It is an Artificial Intelligence able to play five-in-row game using the protocol described [here](https://svn.code.sf.net/p/piskvork/code/trunk/source/doc/protocl2en.htm).

## How does my bot work ?
### Data modeling
    A 2D tensor (matrix) has been used to represent the goban (Gomoku board)
### Algorithm
    (Coming soon)
### Possible improvements
    (Coming soon)

## Prerequisites
- Python 3.8 and later
- make (only on Linux or on git bash(Windows))

## How to create binary ?
### Linux
    make re
### Windows 10 and later
    make exe

## How to test the AI ?
The AI can be tested on pisvork platform.
In order to test the program, follow theses rules.
- Download pisvork [here](https://sourceforge.net/projects/piskvork/)
- Create AI .exe file on Windows
- Launch pisvork on Windows (you can use wine on Linux)
- Upload your AI in 'players' section
- Start the game
