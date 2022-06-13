from assets import *
from core import *


@on_button(kb.RegionalCities.buttons, state=st.CreateAd.regional_city)
def _():
    ctx.state = st.CreateAd.city
    send_message(txt.ask_city, reply_markup=kb.Cities(ctx.text))


@on_button(kb.Cities.buttons, state=st.CreateAd.city)
def _():
    ctx.data['city'] = ctx.text
    ctx.state = st.CreateAd.institution_type
    send_message(txt.ask_institution_type)


@on_text(state=st.CreateAd.institution_type)
def _():
    ctx.data['institution_type'] = ctx.text
    ctx.state = st.CreateAd.institution_name
    send_message(txt.ask_institution_name)


@on_text(state=st.CreateAd.institution_name)
def _():
    ctx.data['institution_name'] = ctx.text
    ctx.state = st.CreateAd.institution_address
    send_message(txt.ask_institution_address)


@on_text(state=st.CreateAd.institution_address)
def _():
    ctx.data['institution_address'] = ctx.text
    ctx.state = st.CreateAd.vacancy_title
    send_message(txt.ask_vacancy_title)


@on_text(state=st.CreateAd.vacancy_title)
def _():
    ctx.data['vacancy_title'] = ctx.text
    ctx.state = st.CreateAd.work_experience
    send_message(txt.ask_work_experience)


@on_text(state=st.CreateAd.work_experience)
def _():
    ctx.data['work_experience'] = ctx.text
    ctx.state = st.CreateAd.salary
    send_message(txt.ask_salary)


@on_text(state=st.CreateAd.salary)
def _():
    ctx.data['salary'] = ctx.text
    ctx.state = st.CreateAd.schedule
    send_message(txt.ask_schedule)


@on_text(state=st.CreateAd.schedule)
def _():
    ctx.data['schedule'] = ctx.text
    ctx.state = st.CreateAd.working_hours
    send_message(txt.ask_working_hours)


@on_text(state=st.CreateAd.working_hours)
def _():
    ctx.data['working_hours'] = ctx.text
    ctx.state = st.CreateAd.additional_info
    send_message(txt.ask_additional_info)

# ===
# @on_text(state=st.CreateAd.working_hours)
# def _():
#     with models.Vacancy.proxy() as v:
#         v.working_hours = ctx.text
#
#     ctx.state = st.CreateAd.additional_info
#     send_message(txt.ask_additional_info)
