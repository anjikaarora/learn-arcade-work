import arcade
arcade.open_window(600,600,"drawing testing")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.BEIGE)
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.PERU)
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.PERU)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 300, arcade.csscolor.PLUM)
arcade.draw_line(500, 550, 550, 600, arcade.color.RAJAH, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.RAJAH, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.RAJAH, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.RAJAH, 3)
arcade.draw_circle_filled(500, 550, 40, arcade.color.DARK_GOLDENROD)
arcade.draw_text("sand :)",
                 150, 230,
                 arcade.color.BLACK, 24)
arcade.finish_render()
arcade.run()

import arcade
arcade.open_window(600,600,"lab_02")
#background color
arcade.set_background_color(arcade.csscolor.PLUM)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.BEIGE)
arcade.draw_lrtb_rectangle_filled(135, 300, 400, 300, arcade.csscolor.NAVY)
arcade.draw_lrtb_rectangle_filled(200, 335, 360, 300, arcade.csscolor.NAVY)
arcade.draw_circle_filled(325, 300, 30, arcade.csscolor.BLACK)
arcade.draw_circle_filled(150, 300, 30, arcade.csscolor.BLACK)

'''arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.PERU)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 300, arcade.csscolor.PLUM)
arcade.draw_line(500, 550, 550, 600, arcade.color.RAJAH, 3)
arcade.draw_circle_filled(500, 550, 40, arcade.color.DARK_GOLDENROD)
arcade.draw_text("sand :)",
                 150, 230,
                 arcade.color.BLACK, 24)'''
arcade.finish_render()
arcade.run()