#Fancy color feature add-on
class SnakeRenderer:
    # Colors
    color_tail = (174, 255, 248)
    color_head = (58, 203, 189)

    def __init__(self):
        pass

    def render(self, snake_body, canvas, grid):
        assert isinstance(snake_body, list)

        dr = (self.color_head[0] - self.color_tail[0]) * 1.0 / (len(snake_body) - 1)
        dg = (self.color_head[1] - self.color_tail[1]) * 1.0 / (len(snake_body) - 1)
        db = (self.color_head[2] - self.color_tail[2]) * 1.0 / (len(snake_body) - 1)
        color = list(self.color_tail)

        for part in snake_body:
            canvas.create_oval(
                part.x * grid,
                part.y * grid,
                part.x * grid + grid,
                part.y * grid + grid,
                fill = '#{r:02X}{g:02X}{b:02x}'.format(r=int(color[0]), g=int(color[1]), b=int(color[2])),
                outline = ''
            )
            color = [color[0] + dr, color[1] + dg, color[2] + db]
