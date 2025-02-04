import arcade
from widgets.Player import Player
from widgets.DebuggingSquare import TestSquare

MOVEMENT_SPEED = 5

class DebuggingView(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = Player(100, 100, 50, 50)
        self.square = TestSquare(200, 200, 50, 50)
    
        self.background = None
        self.camera = None
        
    def setup(self):
        self.camera = arcade.Camera(self.width, self.height)
        try:    
            self.background = arcade.load_texture(r"ressources\CharacterBranch\34713.jpg")
        except:

            self.background = None
    
    def on_draw(self):
        self.clear()
        
        self.camera.use()
        arcade.start_render()
        
        #region drawing background
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            1920, 1080,
                                            self.background)
        
        
        arcade.draw_lrwh_rectangle_textured(0, 1080,
                                            1920, 1080,
                                            self.background)
        
        arcade.draw_lrwh_rectangle_textured(1700, 0,
                                            1920, 1080,
                                            self.background)
        
        
        arcade.draw_lrwh_rectangle_textured(1700, 1080,
                                            1920, 1080,
                                            self.background)
        # endregion
        self.player.draw()
        self.square.draw()
        

    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        
        self.camera.move_to(player_centered)



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player.stop_moving()
            self.player.moving_up = True
        elif key == arcade.key.DOWN:
            self.player.stop_moving()
            self.player.moving_down = True
        elif key == arcade.key.LEFT:
            self.player.stop_moving()
            self.player.moving_left = True
        elif key == arcade.key.RIGHT:
            self.player.stop_moving()
            self.player.moving_right = True
            
    def update(self, delta_time):
        self.player.update(delta_time)
        
        #test collision
        if self.player.isColliding(self.square.x, self.square.y, self.square.width, self.square.height):
            #
            pass
            
        self.center_camera_to_player()
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass
            
if __name__ == "__main__":
    window = DebuggingView(1920, 1080, "Debugging View")
    window.setup()
    arcade.run()