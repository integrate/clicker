import random

import wrap
wrap.add_sprite_dir("sprites")

wrap.world.create_world(1200, 700)

place = wrap.sprite.add("place", 600, 350)

wrap.sprite.add("controls", 900, 20, "coin")
coin_text = wrap.sprite.add_text("0", 930, 20, font_size=30, bold=True, text_color=[238, 157, 1])

wrap.sprite.add("controls", 900, 60, "plus")
plus_text = wrap.sprite.add_text("0", 930, 60, font_size=30, bold=True, text_color=[36, 197, 10])

wrap.sprite.add("controls", 900, 100, "clock")
clock_text = wrap.sprite.add_text("0", 930, 100, font_size=30, bold=True, text_color=[136, 0, 27])


def change_money(text_id, new_money):
    l = wrap.sprite.get_left(text_id)
    wrap.sprite_text.set_text(text_id, str(new_money))
    wrap.sprite.move_left_to(text_id, l)

def change_coin_money(new_money):
    global money
    money = new_money
    change_money(coin_text, new_money)

def change_plus_money(new_money):
    global click_plus
    click_plus=new_money
    change_money(plus_text, new_money)

def change_clock_money(new_money):
    global time_plus
    time_plus = new_money
    change_money(clock_text, new_money)

money = 0
change_coin_money(money)

click_plus = 1
change_plus_money(click_plus)

time_plus = 0
change_clock_money(time_plus)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click():
    change_coin_money(money+click_plus)

@wrap.always(1000)
def tick():
    change_coin_money(money+time_plus)