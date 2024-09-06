import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sailing Game")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

# Boat properties
boat_size = 10
boat_x = boat_size * 2
boat_y = height - boat_size * 2
boat_speed = 0
boat_angle = -math.pi / 4

# Wind properties
wind_strength = 10
wind_angle = -math.pi / 2

# Tiller properties
tiller_width = 300
tiller_height = 30
tiller_x = (width - tiller_width) // 2
tiller_y = height - 60
tiller_handle_width = 20
tiller_handle_x = tiller_x + tiller_width // 2 - tiller_handle_width // 2
max_turn_speed = 0.025

# Button properties
button_width = 100
button_height = 40
button_y = 10
pause_go_button_x = width // 2 - button_width // 2
reset_button_x = width // 2 + button_width + 10

# Game state
game_running = False

def angle_diff(a, b):
    return (a - b + math.pi) % (2 * math.pi) - math.pi

def lerp(a, b, t):
    return a + (b - a) * t

def calculate_boat_speed(boat_angle, wind_angle, wind_strength):
    angle_to_wind = angle_diff(boat_angle, wind_angle)
    abs_angle_to_wind = abs(angle_to_wind)
    
    if abs_angle_to_wind < math.pi / 12:
        t = abs_angle_to_wind / (math.pi / 12)
        return lerp(0, wind_strength * 0.1, t)
    elif abs_angle_to_wind < math.pi / 6:
        t = (abs_angle_to_wind - math.pi / 12) / (math.pi / 12)
        return lerp(wind_strength * 0.1, wind_strength * 0.2, t)
    elif abs_angle_to_wind < math.pi / 2:
        t = (abs_angle_to_wind - math.pi / 6) / (math.pi / 3)
        return lerp(wind_strength * 0.2, wind_strength * 0.4, t)
    elif abs_angle_to_wind < 3 * math.pi / 4:
        t = (abs_angle_to_wind - math.pi / 2) / (math.pi / 4)
        return lerp(wind_strength * 0.4, wind_strength * 0.6, t)
    else:
        t = (abs_angle_to_wind - 3 * math.pi / 4) / (math.pi / 4)
        return lerp(wind_strength * 0.6, wind_strength * 0.3, t)

def draw_boat(surface, x, y, angle, size):
    points = [
        (x + math.cos(angle) * size * 2, y + math.sin(angle) * size * 2),
        (x + math.cos(angle + 2.5) * size, y + math.sin(angle + 2.5) * size),
        (x + math.cos(angle + math.pi) * size * 0.5, y + math.sin(angle + math.pi) * size * 0.5),
        (x + math.cos(angle - 2.5) * size, y + math.sin(angle - 2.5) * size)
    ]
    pygame.draw.polygon(surface, WHITE, points)

def draw_wind_indicator(surface, x, y, angle, length):
    end_x = x + math.cos(angle) * length
    end_y = y + math.sin(angle) * length
    pygame.draw.line(surface, RED, (x, y), (end_x, end_y), 3)
    pygame.draw.polygon(surface, RED, [
        (end_x, end_y),
        (end_x - math.cos(angle - math.pi/6) * 10, end_y - math.sin(angle - math.pi/6) * 10),
        (end_x - math.cos(angle + math.pi/6) * 10, end_y - math.sin(angle + math.pi/6) * 10)
    ])

def draw_tiller(surface):
    # Draw tiller background
    pygame.draw.rect(surface, GRAY, (tiller_x, tiller_y, tiller_width, tiller_height))
    
    # Draw center line
    center_x = tiller_x + tiller_width // 2
    pygame.draw.line(surface, RED, (center_x, tiller_y), (center_x, tiller_y + tiller_height), 2)
    
    # Draw tiller handle
    pygame.draw.rect(surface, WHITE, (tiller_handle_x, tiller_y, tiller_handle_width, tiller_height))

def draw_button(surface, x, y, width, height, text, color):
    pygame.draw.rect(surface, color, (x, y, width, height))
    font = pygame.font.Font(None, 30)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surface, text_rect)

running = True
clock = pygame.time.Clock()
dragging_tiller = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                
                if tiller_y <= mouse_y <= tiller_y + tiller_height and tiller_x <= mouse_x <= tiller_x + tiller_width:
                    dragging_tiller = True
                    # Set tiller handle position directly when clicking
                    tiller_handle_x = max(tiller_x, min(tiller_x + tiller_width - tiller_handle_width, mouse_x - tiller_handle_width // 2))
                
                # Check for button clicks
                if button_y <= mouse_y <= button_y + button_height:
                    if pause_go_button_x <= mouse_x <= pause_go_button_x + button_width:
                        game_running = not game_running  # Toggle game state
                    elif reset_button_x <= mouse_x <= reset_button_x + button_width:
                        # Reset boat position
                        boat_x = boat_size * 2
                        boat_y = height - boat_size * 2
                        boat_speed = 0
                        boat_angle = -math.pi / 4
                        game_running = False  # Stop the game
                        # Reset tiller to center
                        tiller_handle_x = tiller_x + tiller_width // 2 - tiller_handle_width // 2

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging_tiller = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging_tiller:
                mouse_x, _ = event.pos
                tiller_handle_x = max(tiller_x, min(tiller_x + tiller_width - tiller_handle_width, mouse_x - tiller_handle_width // 2))

    if game_running:
        # Calculate turn rate based on tiller position (reversed)
        tiller_center = tiller_x + tiller_width // 2
        turn_rate = -((tiller_handle_x + tiller_handle_width // 2) - tiller_center) / (tiller_width // 2) * max_turn_speed

        boat_angle += turn_rate
        boat_speed = calculate_boat_speed(boat_angle, wind_angle, wind_strength)

        # Update boat position
        boat_x += math.cos(boat_angle) * boat_speed * 0.1
        boat_y += math.sin(boat_angle) * boat_speed * 0.1

        # Wrap the boat around the screen
        boat_x = boat_x % width
        boat_y = boat_y % height

    screen.fill(BLUE)

    # Draw boat with proper rotation
    draw_boat(screen, boat_x, boat_y, boat_angle, boat_size)

    # Draw wind indicator
    draw_wind_indicator(screen, width - 50, 50, -wind_angle, 40)

    # Draw tiller
    draw_tiller(screen)

    # Draw buttons
    draw_button(screen, pause_go_button_x, button_y, button_width, button_height, "Pause/Go", GREEN if game_running else RED)
    draw_button(screen, reset_button_x, button_y, button_width, button_height, "Reset", GRAY)

    # Display boat speed and angle to wind
    font = pygame.font.Font(None, 36)
    speed_text = font.render(f"Speed: {boat_speed:.1f} knots", True, WHITE)
    angle_text = font.render(f"Angle to wind: {math.degrees(abs(angle_diff(boat_angle, wind_angle))):.1f}°", True, WHITE)
    screen.blit(speed_text, (10, 10))
    screen.blit(angle_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()