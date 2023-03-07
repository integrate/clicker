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

up_green = wrap.sprite.add("controls", 500, 60, "up_green")
plus_upgrade_price_text = wrap.sprite.add_text("0", 530, 60, font_size=30, bold=True, text_color=[19, 130, 10])
plus_upgrade_amount_text = wrap.sprite.add_text(" ", 530, 100, font_size=30, bold=True, text_color=[19, 130, 10])



def change_money(text_id, new_money, prefix="", postfix=""):
    l = wrap.sprite.get_left(text_id)
    wrap.sprite_text.set_text(text_id, prefix+str(int(new_money))+postfix)
    wrap.sprite.move_left_to(text_id, l)


def change_coin_money(new_money):
    global money
    money = new_money
    change_money(coin_text, new_money)


def change_plus_money(new_money):
    global click_plus
    click_plus = new_money
    change_money(plus_text, new_money)


def change_clock_money(new_money):
    global time_plus
    time_plus = new_money
    change_money(clock_text, new_money)

def change_plus_upgrade_money(new_price):
    global click_plus_upgrade_price
    click_plus_upgrade_price=new_price
    change_money(plus_upgrade_price_text, new_price)

def change_plus_upgrade_amount_money(new_money):
    global click_plus_upgrade
    click_plus_upgrade=new_money
    change_money(plus_upgrade_amount_text, new_money, "+", " за клик")

def upgrade_click():
    if money < click_plus_upgrade_price:
        return

    change_coin_money(money - click_plus_upgrade_price)
    change_plus_money(click_plus + click_plus_upgrade)
    change_plus_upgrade_money(click_plus_upgrade_price*click_plus_upgrade_price_grow)
    change_plus_upgrade_amount_money(click_plus_upgrade+2)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    if wrap.sprite.is_collide_point(up_green, pos_x, pos_y, True):
        upgrade_click()
        return
    change_coin_money(money + click_plus)


@wrap.always(1000)
def tick():
    change_coin_money(money + time_plus)


money = 0 #сколько всего денег

click_plus = 2 #денег за один клик
click_plus_upgrade = 2 #на сколько вырастет доход за клик при апгрейде

click_plus_upgrade_price = 10 #стоимость апгреда
click_plus_upgrade_price_grow = 1.05 #на сколько вырастет цена апгреда

time_plus = 0

change_coin_money(money)
change_plus_money(click_plus)
change_clock_money(time_plus)
change_plus_upgrade_money(click_plus_upgrade_price)
change_plus_upgrade_amount_money(click_plus_upgrade)