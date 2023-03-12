import random

import wrap

wrap.add_sprite_dir("sprites")

wrap.world.create_world(1200, 700)

place = wrap.sprite.add("place", 600, 350, "place1")

coin_icon=wrap.sprite.add("controls", 900, 20, "coin")
coin_text = wrap.sprite.add_text("0", 930, 20, font_size=30, bold=True, text_color=[238, 157, 1],
                                 back_color=[57, 28, 1])

plus_icon=wrap.sprite.add("controls", 900, 60, "plus")
plus_text = wrap.sprite.add_text("0", 930, 60, font_size=30, bold=True, text_color=[36, 197, 10],
                                 back_color=[17, 57, 10])

clock_icon = wrap.sprite.add("controls", 900, 100, "clock")
clock_text = wrap.sprite.add_text("0", 930, 100, font_size=30, bold=True, text_color=[136, 0, 27],
                                  back_color=[57, 0, 17])

up_coin = wrap.sprite.add("controls", 850, 20, "up_yellow")
plus_upgrade_price_text = wrap.sprite.add_text("0", 820, 20, font_size=30, bold=True, text_color=[238, 157, 1],
                                               back_color=[57, 28, 1])
plus_upgrade_amount_text = wrap.sprite.add_text("0", 820, 60, font_size=30, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10])

worker1 = wrap.sprite.add("worker", 100, 600, "worker1")
worker1_level_text = wrap.sprite.add_text("0", 130, 495, font_size=15, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10])


worker2 = wrap.sprite.add("worker", 300, 550, "worker2_inv")
worker2_level_text = wrap.sprite.add_text("0", 300, 390, font_size=15, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10])
music_up = wrap.sprite.add("controls", 320, 570, "up_yellow")
music_upgrade_price_text = wrap.sprite.add_text("0", 350, 570, font_size=30, bold=True, text_color=[238, 157, 1],
                                                back_color=[57, 28, 1])

music_clock_icon=wrap.sprite.add("controls", 320, 610, "clock")
music_time_grow_text = wrap.sprite.add_text("0", 350, 610, font_size=30, bold=True, text_color=[136, 0, 27],
                                            back_color=[57, 0, 17])

worker3 = wrap.sprite.add("worker", 550, 550, "worker3_inv", False)
worker3_level_text = wrap.sprite.add_text("0", 550, 390, font_size=15, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10], visible=False)

singer_up = wrap.sprite.add("controls", 590, 570, "up_yellow", False)
singer_upgrade_price_text = wrap.sprite.add_text("0", 620, 570, font_size=30, bold=True, text_color=[238, 157, 1],
                                                 back_color=[57, 28, 1], visible=False)

singer_clock_icon = wrap.sprite.add("controls", 590, 610, "clock", False)
singer_time_grow_text = wrap.sprite.add_text("0", 620, 610, font_size=30, bold=True, text_color=[136, 0, 27],
                                             back_color=[57, 0, 17], visible=False)

business1 = wrap.sprite.add("business", 730, 330, "business1_inv", False)
business1_level_text = wrap.sprite.add_text("0", 700, 220, font_size=15, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10], visible=False)

business1_up = wrap.sprite.add("controls", 830, 330, "up_yellow", False)
business1_upgrade_price_text = wrap.sprite.add_text("0", 860, 330, font_size=30, bold=True, text_color=[238, 157, 1],
                                                    back_color=[57, 28, 1], visible=False)

business1_clock_icon = wrap.sprite.add("controls", 830, 370, "clock", False)
business1_time_grow_text = wrap.sprite.add_text("0", 860, 370, font_size=30, bold=True, text_color=[136, 0, 27],
                                                back_color=[57, 0, 17], visible=False)

business2 = wrap.sprite.add("business", 950, 580, "business2_inv", False)
business2_level_text = wrap.sprite.add_text("0", 920, 470, font_size=15, bold=True, text_color=[36, 197, 10],
                                                back_color=[17, 57, 10], visible=False)

business2_up = wrap.sprite.add("controls", 1030, 550, "up_yellow", False)
business2_upgrade_price_text = wrap.sprite.add_text("0", 1060, 550, font_size=30, bold=True, text_color=[238, 157, 1],
                                                    back_color=[57, 28, 1], visible=False)

business2_clock_icon = wrap.sprite.add("controls", 1030, 590, "clock", False)
business2_time_grow_text = wrap.sprite.add_text("0", 1060, 590, font_size=30, bold=True, text_color=[136, 0, 27],
                                                back_color=[57, 0, 17], visible=False)


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

def change_worker1_level(new_level):
    global worker1_level
    worker1_level = new_level
    change_money(worker1_level_text, worker1_level, "", " уровень", True)

def change_music_level(new_level):
    global music_level
    music_level = new_level
    change_money(worker2_level_text, music_level, "", " уровень", True)

def change_music_buy_price(new_money):
    global music_buy_price
    music_buy_price = new_money
    change_money(music_upgrade_price_text, new_money)


def change_music_time_upgrade(new_grow):
    global music_time_upgrade
    music_time_upgrade = new_grow
    change_money(music_time_grow_text, new_grow, "+")


def change_singer_level(new_level):
    global singer_level
    singer_level = new_level
    change_money(worker3_level_text, singer_level, "", " уровень", True)

def change_singer_buy_price(new_money):
    global singer_buy_price
    singer_buy_price = new_money
    change_money(singer_upgrade_price_text, new_money)


def change_singer_time_upgrade(new_grow):
    global singer_time_upgrade
    singer_time_upgrade = new_grow
    change_money(singer_time_grow_text, new_grow, "+")


def change_business1_level(new_level):
    global business1_level
    business1_level = new_level
    change_money(business1_level_text, business1_level, "", " уровень", True)

def change_business1_buy_price(new_money):
    global business1_buy_price
    business1_buy_price = new_money
    change_money(business1_upgrade_price_text, new_money)


def change_business1_time_upgrade(new_grow):
    global business1_time_upgrade
    business1_time_upgrade = new_grow
    change_money(business1_time_grow_text, new_grow, "+")


def change_business2_level(new_level):
    global business2_level
    business2_level = new_level
    change_money(business2_level_text, business2_level, "", " уровень", True)

def change_business2_buy_price(new_money):
    global business2_buy_price
    business2_buy_price = new_money
    change_money(business2_upgrade_price_text, new_money)


def change_business2_time_upgrade(new_grow):
    global business2_time_upgrade
    business2_time_upgrade = new_grow
    change_money(business2_time_grow_text, new_grow, "+")


def upgrade_click():
    if money < click_plus_upgrade_price:
        return

    change_worker1_level(worker1_level+1)

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

    change_music_level(music_level + 1)
    if music_level == 10:
        wrap.sprite.show(worker3)
        wrap.sprite.show(worker3_level_text)
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

    change_singer_level(singer_level + 1)
    if singer_level == 10:
        wrap.sprite.set_costume(place, "place2")
        wrap.sprite.show(business1)
        wrap.sprite.show(business1_level_text)
        wrap.sprite.show(business1_up)
        wrap.sprite.show(business1_upgrade_price_text)
        wrap.sprite.show(business1_clock_icon)
        wrap.sprite.show(business1_time_grow_text)


def upgrade_business1():
    global business1_buy_price_grow, business1_level
    if money < business1_buy_price:
        return

    if wrap.sprite.get_costume(business1) == "business1_inv":
        wrap.sprite.set_costume(business1, "business1_1")

    change_coin_money(money - business1_buy_price)
    change_business1_buy_price(business1_buy_price * business1_buy_price_grow)
    business1_buy_price_grow += business1_buy_price_grow_grow

    change_clock_money(time_plus + business1_time_upgrade)
    change_business1_time_upgrade(business1_time_upgrade + business1_time_upgrade_grow)

    change_business1_level(business1_level + 1)
    if business1_level == 10:
        wrap.sprite.set_costume(business1, "business1_2")

        wrap.sprite.show(business2)
        wrap.sprite.show(business2_level_text)
        wrap.sprite.show(business2_up)
        wrap.sprite.show(business2_upgrade_price_text)
        wrap.sprite.show(business2_clock_icon)
        wrap.sprite.show(business2_time_grow_text)

    if business1_level == 20:
        wrap.sprite.set_costume(business1, "business1_3")


def upgrade_business2():
    global business2_buy_price_grow, business2_level
    if money < business2_buy_price:
        return

    if wrap.sprite.get_costume(business2) == "business2_inv":
        wrap.sprite.set_costume(business2, "business2_1")

    change_coin_money(money - business2_buy_price)
    change_business2_buy_price(business2_buy_price * business2_buy_price_grow)
    business2_buy_price_grow += business2_buy_price_grow_grow

    change_clock_money(time_plus + business2_time_upgrade)
    change_business2_time_upgrade(business2_time_upgrade + business2_time_upgrade_grow)

    change_business2_level(business2_level + 1)
    if business2_level == 10:
        wrap.sprite.set_costume(business2, "business2_2")

    if business2_level == 20:
        wrap.sprite.set_costume(business2, "business2_3")

    if business2_level == 25:
        wrap.sprite.hide(coin_icon)
        wrap.sprite.hide(coin_text)
        wrap.sprite.hide(clock_icon)
        wrap.sprite.hide(clock_text)
        wrap.sprite.hide(plus_icon)
        wrap.sprite.hide(plus_text)
        wrap.sprite.hide(up_coin)
        wrap.sprite.hide(plus_upgrade_amount_text)
        wrap.sprite.hide(plus_upgrade_price_text)


        wrap.sprite.hide(worker1)
        wrap.sprite.hide(worker1_level_text)

        wrap.sprite.hide(worker2)
        wrap.sprite.hide(worker2_level_text)
        wrap.sprite.hide(music_up)
        wrap.sprite.hide(music_upgrade_price_text)
        wrap.sprite.hide(music_clock_icon)
        wrap.sprite.hide(music_time_grow_text)

        wrap.sprite.hide(worker3)
        wrap.sprite.hide(worker3_level_text)
        wrap.sprite.hide(singer_up)
        wrap.sprite.hide(singer_upgrade_price_text)
        wrap.sprite.hide(singer_clock_icon)
        wrap.sprite.hide(singer_time_grow_text)

        wrap.sprite.hide(business1)
        wrap.sprite.hide(business1_level_text)
        wrap.sprite.hide(business1_up)
        wrap.sprite.hide(business1_upgrade_price_text)
        wrap.sprite.hide(business1_clock_icon)
        wrap.sprite.hide(business1_time_grow_text)

        wrap.sprite.hide(business2)
        wrap.sprite.hide(business2_level_text)
        wrap.sprite.hide(business2_up)
        wrap.sprite.hide(business2_upgrade_price_text)
        wrap.sprite.hide(business2_clock_icon)
        wrap.sprite.hide(business2_time_grow_text)

        wrap.sprite.set_costume(place, "place3")


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    if wrap.sprite.is_collide_point(up_coin, pos_x, pos_y, True):
        upgrade_click()
    elif wrap.sprite.is_collide_point(music_up, pos_x, pos_y, True):
        upgrade_music()
    elif wrap.sprite.is_collide_point(singer_up, pos_x, pos_y, True):
        upgrade_singer()
    elif wrap.sprite.is_collide_point(business1_up, pos_x, pos_y, True):
        upgrade_business1()
    elif wrap.sprite.is_collide_point(business2_up, pos_x, pos_y, True):
        upgrade_business2()
    else:
        change_coin_money(money + click_plus)


@wrap.always(1000)
def tick():
    change_coin_money(money + time_plus)


money = 3000000000  # сколько всего денег

click_plus = 2  # денег за один клик
click_plus_upgrade = 2  # на сколько вырастет доход за клик при апгрейде

click_plus_upgrade_price = 10  # стоимость апгреда
click_plus_upgrade_price_grow = 1.05  # на сколько вырастет цена апгреда

time_plus = 0

worker1_level = 1

music_level = 0
music_buy_price = 10000  # стоимость покупки музыканта
music_buy_price_grow = 1.02  # рост цены музыканта
music_buy_price_grow_grow = 0.02283  # ускорение роста цены музыканта
music_time_upgrade = 1  # доход от прокачки музыканта
music_time_upgrade_grow = 1  # увеличение дохода от прокачки музыканта

singer_level = 0
singer_buy_price = 50000  # стоимость покупки фокусника
singer_buy_price_grow = 1.02  # рост цены фокусника
singer_buy_price_grow_grow = 0.02283  # ускорение роста цены фокусника
singer_time_upgrade = 5  # доход от прокачки фокусника
singer_time_upgrade_grow = 5  # увеличение дохода от прокачки фокусника

business1_level = 0
business1_buy_price = 100000  # стоимость покупки фокусника
business1_buy_price_grow = 1.02  # рост цены фокусника
business1_buy_price_grow_grow = 0.02283  # ускорение роста цены фокусника
business1_time_upgrade = 10  # доход от прокачки фокусника
business1_time_upgrade_grow = 10  # увеличение дохода от прокачки фокусника

business2_level = 0
business2_buy_price = 500000  # стоимость покупки фокусника
business2_buy_price_grow = 1.02  # рост цены фокусника
business2_buy_price_grow_grow = 0.02283  # ускорение роста цены фокусника
business2_time_upgrade = 50  # доход от прокачки фокусника
business2_time_upgrade_grow = 50  # увеличение дохода от прокачки фокусника

change_coin_money(money)
change_plus_money(click_plus)
change_clock_money(time_plus)
change_worker1_level(worker1_level)

change_plus_upgrade_money(click_plus_upgrade_price)
change_plus_upgrade_amount_money(click_plus_upgrade)

change_music_buy_price(music_buy_price)
change_music_time_upgrade(music_time_upgrade)
change_music_level(music_level)

change_singer_buy_price(singer_buy_price)
change_singer_time_upgrade(singer_time_upgrade)
change_singer_level(singer_level)

change_business1_buy_price(business1_buy_price)
change_business1_time_upgrade(business1_time_upgrade)
change_business1_level(business1_level)

change_business2_buy_price(business2_buy_price)
change_business2_time_upgrade(business2_time_upgrade)
change_business2_level(business2_level)