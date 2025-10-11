import pygame
from avl_tree.tree import AVLTree
from visualization.visualizer import AVLVisualizer
from ui.controller import Controller

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("AVL Tree Visualization (Pygame)")

    clock = pygame.time.Clock()
    tree = AVLTree()
    visualizer = AVLVisualizer(screen)
    controller = Controller(tree, visualizer)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                controller.handle_event(event)

        
        visualizer.draw(controller.root_node)

        # Draw UI 
        for name, rect in controller.buttons.items():
            pygame.draw.rect(screen, (180, 180, 180), rect)
            
            font = visualizer.font
            text_surf = font.render(name, True, (0, 0, 0))
            text_rect = text_surf.get_rect(center=rect.center)
            screen.blit(text_surf, text_rect)

        # draw user input string
        input_surf = visualizer.font.render(controller.user_input, True, (255, 255, 255))
        screen.blit(input_surf, (50, 520))

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
