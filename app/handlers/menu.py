from assets import *


@on_button(kb.MainMenu.change_lang)
def _():
    if ctx.lang == c.UA:
        ctx.lang = c.RU
    else:
        ctx.lang = c.UA

    edit_message_text(txt.main_menu, reply_markup=kb.MainMenu())


@on_button(kb.MainMenu.my_ads)
def _():
    answer_callback_query(txt.no_my_ads)


@on_button(kb.MainMenu.create_ad)
def _():
    ctx.state = st.CreateAd.regional_city
    send_message(txt.creating_ad_info)
    send_message(txt.ask_regional_city, reply_markup=kb.RegionalCities())
