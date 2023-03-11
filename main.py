import random

import wrap

wrap.add_sprite_dir("sprites")

wrap.world.create_world(1200, 700)

place = wrap.sprite.add("place", 600, 350, "place1")

wrap.sprite.add("controls", 900, 20, "coin")
coin_text = wrap.sprite.add_text("0", 930, 20, font_size=30, bold=True, text_color=[238, 157, 1],
                                 back_color=[57, 28, 1])

wrap.sprite.add("controls", 900, 60, "plus")
plus_text = wrap.sprite.add_text("0", 930, 60, font_size=30, bold=True, text_color=[36, 197, 10],
                                 back_color=[17, 57, 10])

wrap.sprite.add("controls", 900, 100, "clock")
clock_text = wrap.sprite.add_text("0", 930, 100, font_size=30, bold=True, text_color=[136, 0, 27],
                                  back_color=[57, 0, 17])

up_coin = wrap.sprite.add("controls", 850, 20, "up_yellow")
plus_upgrade_price_text = wrap.sprite.add_text("0", 820, 20, font_size=30, bold=True, text_color=[238, 157, 1],
                                               back_color=[57, 28, 1])
plus_upgrade_amount_text = wrap.sprite.add_text("0", 820, 60, font_size=30, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10])

worker1 = wrap.sprite.add("worker", 100, 600, "worker1")

worker2 = wrap.sprite.add("worker", 300, 550, "worker2_inv")
music_up = wrap.sprite.add("controls", 320, 570, "up_yellow")
music_upgrade_price_text = wrap.sprite.add_text("0", 350, 570, font_size=30, bold=True, text_color=[238, 157, 1],
                                                back_color=[57, 28, 1])

wrap.sprite.add("controls", 320, 610, "clock")
music_time_grow_text = wrap.sprite.add_text("0", 350, 610, font_size=30, bold=True, text_color=[136, 0, 27],
                                            back_color=[57, 0, 17])

worker3 = wrap.sprite.add("worker", 550, 550, "worker3_inv", False)
singer_up = wrap.sprite.add("controls", 590, 570, "up_yellow", False)
singer_upgrade_price_text = wrap.sprite.add_text("0", 620, 570, font_size=30, bold=True, text_color=[238, 157, 1],
                                                 back_color=[57, 28, 1], visible=False)

singer_clock_icon=wrap.sprite.add("controls", 590, 610, "clock", False)
singer_time_grow_text = wrap.sprite.add_text("0", 620, 610, font_size=30, bold=True, text_color=[136, 0, 27],
                                             back_color=[57, 0, 17], visible=False)

# business1 = wrap.sprite.add("business", 730, 330, "business2_1")

# business2 = wrap.sprite.add("business", 950, 580, "business3_1")


def change_money(text_id, new_money, prefix="", postfix="", left_side=True):
    text = prefix + str(int(new_money)) + postfix
    if left_side:
        l = wrap.sprite.get_left(text_id)
        wrap.sprite_text.set_text(text_id, text)
        wrap.sprite.move_left_to(text_id, l)
    else:
        r = wrap.sprite.get_right(text_id)
        wrap.sprite_text.set_text(text_id, text)
        wrap.sprite.move_right_to(text_id, r)


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
    click_plus_upgrade_price = new_price
    change_money(plus_upgrade_price_text, new_price, "-", left_side=False)


def change_plus_upgrade_amount_money(new_money):
    global click_plus_upgrade
    click_plus_upgrade = new_money
    change_money(plus_upgrade_amount_text, new_money, "+", " за клик", False)


def change_music_buy_price(new_money):
    global music_buy_price
    music_buy_price = new_money
    change_money(music_upgrade_price_text, new_money)


def change_music_time_upgrade(new_grow):
    global music_time_upgrade
    music_time_upgrade = new_grow
    change_money(music_time_grow_text, new_grow, "+")

def change_singer_buy_price(new_money):
    global singer_buy_price
    singer_buy_price = new_money
    change_money(singer_upgrade_price_text, new_money)

def change_singer_time_upgrade(new_grow):
    global singer_time_upgrade
    singer_time_upgrade = new_grow
    change_money(singer_time_grow_text, new_grow, "+")


def upgrade_click():
    if money < click_plus_upgrade_price:
        return

    change_coin_money(money - int(click_plus_upgrade_price))
    change_plus_money(click_plus + int(click_plus_upgrade))
    change_plus_upgrade_money(click_plus_upgrade_price * click_plus_upgrade_price_grow)
    change_plus_upgrade_amount_money(click_plus_upgrade + 2)


def upgrade_music():
    global music_buy_price_grow, music_level
    if money < music_buy_price:
        return

    if wrap.sprite.get_costume(worker2) == "worker2_inv":
        wrap.sprite.set_costume(worker2, "worker2")

    change_coin_money(money - music_buy_price)
    change_music_buy_price(music_buy_price * music_buy_price_grow)
    music_buy_price_grow += music_buy_price_grow_grow

    change_clock_money(time_plus + music_time_upgrade)
    change_music_time_upgrade(music_time_upgrade + music_time_upgrade_grow)

    music_level += 1
    if music_level == 10:
        wrap.sprite.show(worker3)
        wrap.sprite.show(singer_up)
        wrap.sprite.show(singer_upgrade_price_text)
        wrap.sprite.show(singer_time_grow_text)
        wrap.sprite.show(singer_clock_icon)

def upgrade_singer():
    global singer_buy_price_grow, singer_level
    if money < singer_buy_price:
        return

    if wrap.sprite.get_costume(worker3) == "worker3_inv":
        wrap.sprite.set_costume(worker3, "worker3")

    change_coin_money(money - singer_buy_price)
    change_singer_buy_price(singer_buy_price * singer_buy_price_grow)
    singer_buy_price_grow += singer_buy_price_grow_grow

    change_clock_money(time_plus + singer_time_upgrade)
    change_singer_time_upgrade(singer_time_upgrade + singer_time_upgrade_grow)

    singer_level += 1
    # if music_level == 20:
    #     wrap.sprite.show(worker3)
    #     wrap.sprite.show(singer_up)
    #     wrap.sprite.show(singer_upgrade_price_text)
    #     wrap.sprite.show(singer_time_grow_text)
    #     wrap.sprite.show(singer_clock_icon)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    if wrap.sprite.is_collide_point(up_coin, pos_x, pos_y, True):
        upgrade_click()
    elif wrap.sprite.is_collide_point(music_up, pos_x, pos_y, True):
        upgrade_music()
    elif wrap.sprite.is_collide_point(singer_up, pos_x, pos_y, True):
        upgrade_singer()
    else:
        change_coin_money(money + click_plus)


@wrap.always(1000)
def tick():
    change_coin_money(money + time_plus)


money = 0  # сколько всего денег

click_plus = 2  # денег за один клик
click_plus_upgrade = 2  # на сколько вырастет доход за клик при апгрейде

click_plus_upgrade_price = 10  # стоимость апгреда
click_plus_upgrade_price_grow = 1.05  # на сколько вырастет цена апгреда

time_plus = 0

music_level = 0
music_buy_price = 10000  # стоимость покупки музыканта
music_buy_price_grow = 1.02 # рост цены музыканта
music_buy_price_grow_grow = 0.02283 # ускорение роста цены музыканта
music_time_upgrade = 1 # доход от прокачки музыканта
music_time_upgrade_grow = 1 # увеличение дохода от прокачки музыканта

singer_level = 0
singer_buy_price = 50000  # стоимость покупки музыканта
singer_buy_price_grow = 1.02 # рост цены музыканта
singer_buy_price_grow_grow = 0.02283 # ускорение роста цены музыканта
singer_time_upgrade = 5 # доход от прокачки музыканта
singer_time_upgrade_grow = 5 # увеличение дохода от прокачки музыканта

change_coin_money(money)
change_plus_money(click_plus)
change_clock_money(time_plus)

change_plus_upgrade_money(click_plus_upgrade_price)
change_plus_upgrade_amount_money(click_plus_upgrade)

change_music_buy_price(music_buy_price)
change_music_time_upgrade(music_time_upgrade)

change_singer_buy_price(singer_buy_price)
change_singer_time_upgrade(singer_time_upgrade)