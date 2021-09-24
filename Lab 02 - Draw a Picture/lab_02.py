import arcade
arcade.open_window(600,600,"lab_02")
#background color
arcade.set_background_color(arcade.csscolor.NAVY)
arcade.start_render()
#moon
arcade.draw_circle_filled(325, 300, 50, arcade.csscolor.LIGHT_SLATE_GRAY)
arcade.draw_circle_filled(440, 300, 130, arcade.csscolor.NAVY)
#STARS
arcade.draw_circle_filled(500, 400, 10, arcade.csscolor.WHEAT)
arcade.draw_circle_filled(600, 335, 10, arcade.csscolor.WHEAT)
arcade.draw_circle_filled(190, 540, 10, arcade.csscolor.WHEAT)
arcade.draw_circle_filled(210, 100, 10, arcade.csscolor.WHEAT)
arcade.draw_circle_filled(140, 300, 10, arcade.csscolor.WHEAT)
arcade.draw_circle_filled(195, 470, 10, arcade.csscolor.WHEAT)
#mountain
arcade.draw_triangle_filled(0,1,20,200,600,1,arcade.csscolor.PURPLE)
arcade.draw_triangle_filled(0,1,400,150,600,1,arcade.csscolor.MEDIUM_PURPLE)
arcade.draw_triangle_filled(0,1,100,100,600,1,arcade.csscolor.PLUM)
arcade.finish_render()
arcade.run()