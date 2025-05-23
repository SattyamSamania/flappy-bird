# Flappy Bird Game

A Python implementation of the classic Flappy Bird game using Pygame.

![Flappy Bird Game](https://github.com/SattyamSamania/flappy-bird/blob/main/screenshots/gameplay.png)

## Description

This is a clone of the popular Flappy Bird game where players control a bird, attempting to fly between columns of green pipes without hitting them. The game features:

- Smooth bird movement with gravity physics
- Randomly generated pipes with varying heights
- Score tracking
- Start and game over screens
- Fullscreen gameplay
- Visually enhanced graphics with detailed bird, pipes, and background

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/SattyamSamania/flappy-bird.git
   cd flappy-bird
   ```

2. Install the required dependencies:
   ```
   pip install pygame
   ```

## How to Play

1. Run the game:

   ```
   python flappy_bird.py
   ```

2. Game Controls:
   - Press **SPACE** to make the bird flap and start the game
   - Press **SPACE** to flap during gameplay
   - Press **ESC** to quit the game at any time
   - After game over, press **SPACE** to restart

## Game Features

- **Realistic Physics**: Smooth gravity and flapping mechanics
- **Progressive Difficulty**: Navigate through an endless series of pipes
- **Score Tracking**: Earn points for each pipe you successfully pass
- **Visual Effects**: Enhanced graphics with detailed bird, pipes, clouds, and ground textures

## Screenshots

- **Start Game**
  ![start game](https://github.com/SattyamSamania/flappy-bird/blob/main/screenshots/start_screen.png)
- **Game Play**  
  ![game play](https://github.com/SattyamSamania/flappy-bird/blob/main/screenshots/gameplay.png)
- **Game Over**  
  ![game over](https://github.com/SattyamSamania/flappy-bird/blob/main/screenshots/game_over.png)

## Customization

You can modify various game parameters in the code:

- `GRAVITY`: Controls how quickly the bird falls
- `FLAP_STRENGTH`: Controls how high the bird jumps when flapping
- `PIPE_GAP`: Controls the gap size between pipes
- `PIPE_FREQUENCY`: Controls how often new pipes appear
- `SCROLL_SPEED`: Controls how fast the game scrolls

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original Flappy Bird game by Dong Nguyen
- Pygame community for the excellent game development library
