import pygame
import random
import time
import sys

# ====================== CONFIGURATION ======================
# Customize these if you want
PLATE_FORMAT = "XXX XXXX"  # 3 letters, space, 4 numbers (common US style)
FONT_SIZE = 220
BACKGROUND_COLOR = (0, 0, 0)          # Black
TEXT_COLOR = (255, 255, 255)          # White
# You can also try: (0, 180, 0) for green plate look

# =========================================================

def generate_license_plate():
    """Generate a random license plate in standard format"""
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    numbers = ''.join(random.choices('0123456789', k=4))
    return f"{letters} {numbers}"


def main():
    # Get user input
    print("=== License Plate Random Display ===\n")
    try:
        num_plates = int(input("How many license plates to generate? "))
        if num_plates < 1:
            num_plates = 1
    except:
        print("Invalid input. Defaulting to 10 plates.")
        num_plates = 10

    try:
        duration = float(input("How many seconds to display each plate? "))
        if duration < 0.5:
            duration = 0.5
    except:
        print("Invalid input. Defaulting to 3 seconds.")
        duration = 3.0

    # Initialize Pygame
    pygame.init()

    # Set up full screen display
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()

    # Load font (using a bold sans-serif font that looks good for plates)
    try:
        font = pygame.font.SysFont("Arial Black", FONT_SIZE, bold=True)
    except:
        font = pygame.font.SysFont(None, FONT_SIZE, bold=True)

    # Hide mouse cursor
    pygame.mouse.set_visible(False)

    print(f"\nDisplaying {num_plates} plates. Press ESC to quit.\n")

    for i in range(num_plates):
        plate = generate_license_plate()

        # Create text surface
        text_surface = font.render(plate, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))

        # Main display loop for this plate
        start_time = time.time()
        running = True

        while running and (time.time() - start_time) < duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Exiting...")
                        pygame.quit()
                        sys.exit()

            # Fill background
            screen.fill(BACKGROUND_COLOR)

            # Draw the license plate
            screen.blit(text_surface, text_rect)

            # Optional: subtle border like real plates
            border_rect = text_rect.inflate(60, 40)
            pygame.draw.rect(screen, TEXT_COLOR, border_rect, width=8, border_radius=12)

            pygame.display.flip()
            pygame.time.wait(30)  # ~33 FPS

    # Cleanup
    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
