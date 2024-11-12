import pygame
import random  # We need the random module to randomly move the mole


def main():
    try:
        pygame.init()

        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")  # Load the mole image

        # Set up the screen size (640x512 pixels)
        screen = pygame.display.set_mode((640, 512))

        # Set up the clock to control the frame rate
        clock = pygame.time.Clock()

        # Print statement to show the program is running
        print("Hello")

        # Grid settings: Each square is 32x32 pixels
        grid_size = 32  # Each grid square is 32x32 pixels
        grid_width = 20  # 20 columns in the grid
        grid_height = 16  # 16 rows in the grid

        # Initial position of the mole (top-left corner of the grid)
        mole_x, mole_y = 0, 0

        # Helper function to draw the grid
        def draw_grid():
            line_color = (0, 0, 0)  # Color for grid lines (black)

            # Draw vertical grid lines
            for x in range(0, 640, grid_size):
                pygame.draw.line(screen, line_color, (x, 0), (x, 512))

            # Draw horizontal grid lines
            for y in range(0, 512, grid_size):
                pygame.draw.line(screen, line_color, (0, y), (640, y))

        running = True
        while running:
            # Event loop to check for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If the user closes the window
                    running = False

                # If the user clicks the mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos  # Get the mouse position

                    # Check if the click is inside the mole's current square
                    mole_rect = pygame.Rect(mole_x * grid_size, mole_y * grid_size, grid_size, grid_size)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # If the mole is clicked, move it to a new random square
                        mole_x = random.randrange(0, grid_width)
                        mole_y = random.randrange(0, grid_height)

            # Fill the background with light green
            screen.fill("light green")

            # Draw the grid on the screen
            draw_grid()

            # Draw the mole in its current position (based on mole_x and mole_y)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * grid_size, mole_y * grid_size)))

            # Update the screen display
            pygame.display.flip()

            # Control the frame rate to be 60 frames per second
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
