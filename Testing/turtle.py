import arcade
arcade.open_window(600,600,"turtle")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_arc_filled(300, 460, 80, 100, arcade.csscolor.LIME_GREEN, 0, 180)
arcade.draw_ellipse_filled(300, 350, 200, 250, arcade.csscolor.PERU)
arcade.draw_ellipse_filled(300, 350, 150, 200, arcade.csscolor.ORANGE)
arcade.finish_render()
arcade.run()