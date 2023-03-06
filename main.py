import wrap
wrap.add_sprite_dir("sprites")

wrap.world.create_world(1200, 700)

place = wrap.sprite.add("place", 600, 350)

wrap.sprite.add("controls", 900, 20, "coin")
coin_text = wrap.sprite.add_text("0", 930, 20, font_size=30, bold=True, text_color=[238, 157, 1])
wrap.sprite.add("controls", 900, 60, "plus")
coin_text = wrap.sprite.add_text("0", 930, 60, font_size=30, bold=True, text_color=[238, 157, 1])
