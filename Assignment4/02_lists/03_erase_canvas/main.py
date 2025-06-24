from graphics import *
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 40  # Larger for better visibility

def main():
    win = GraphWin("Eraser Tool", CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create grid (draw first)
    grid = []
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            cell = Rectangle(Point(col*CELL_SIZE, row*CELL_SIZE),
                           Point((col+1)*CELL_SIZE, (row+1)*CELL_SIZE))
            cell.setFill("blue")
            cell.draw(win)
            grid.append(cell)
    
    # Create eraser (draw last)
    eraser = Rectangle(Point(0, 0), 
                      Point(ERASER_SIZE, ERASER_SIZE))
    eraser.setFill("pink")
    eraser.setOutline("red")
    eraser.setWidth(2)
    eraser.draw(win)
    
    # Initial positioning
    win.getMouse()  # Wait for first click
    start_pos = win.getCurrentMouseLocation()
    eraser.move(start_pos.x, start_pos.y)
    
    # Main loop
    while True:
        try:
            current_pos = win.getCurrentMouseLocation()
            dx = current_pos.x - (eraser.getP1().x + ERASER_SIZE/2)
            dy = current_pos.y - (eraser.getP1().y + ERASER_SIZE/2)
            eraser.move(dx, dy)
            
            # Erase overlapping cells
            for cell in grid:
                if (eraser.getP1().x < cell.getP2().x and
                    eraser.getP2().x > cell.getP1().x and
                    eraser.getP1().y < cell.getP2().y and
                    eraser.getP2().y > cell.getP1().y):
                    cell.setFill("white")
            
            time.sleep(0.02)
        except GraphicsError:
            break  # Window closed

if __name__ == "__main__":
    main()