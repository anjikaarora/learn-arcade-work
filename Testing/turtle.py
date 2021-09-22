import arcade
arcade.open_window(600,600,"turtle")
#background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
#shell
arcade.draw_ellipse_filled(300, 350, 200, 250, arcade.csscolor.PERU)
arcade.draw_ellipse_filled(300, 350, 150, 200, arcade.csscolor.ORANGE)
#turtle head
arcade.draw_arc_filled(300, 460, 80, 100, arcade.csscolor.LIME_GREEN, 0, 180)
#turtle tail
arcade.draw_arc_filled(300, 460, 80, 100, arcade.csscolor.LIME_GREEN, 0, 180)
#turtle shell design
arcade.draw_text(".",
                 300, 400,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 250, 300,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 275, 275,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 260, 350,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 256, 386,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 299, 300,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 345, 323,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 360, 389,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 340, 370,
                 arcade.color.BLACK, 24)
arcade.draw_text(".",
                 300, 349,
                 arcade.color.BLACK, 24)
arcade.finish_render()
arcade.run()