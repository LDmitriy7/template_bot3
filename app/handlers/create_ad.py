from assets import *


@on_button(kb.RegionalCities.buttons, state=st.CreateAd.regional_city)
def _():
    with model.Ad.proxy() as ad:
        ad.regional_city = ctx.text

    ctx.state = st.CreateAd.city
    send_message(txt.ask_city, reply_markup=kb.Cities(ctx.text))


@on_button(kb.Cities.buttons, state=st.CreateAd.city)
def _():
    with model.Ad.proxy() as ad:
        ad.city = ctx.text

    ctx.state = st.CreateAd.institution_type
    send_message(txt.ask_institution_type)


@on_text(state=st.CreateAd.institution_type)
def _():
    with model.Institution.proxy() as inst:
        inst.type = ctx.text

    ctx.state = st.CreateAd.institution_name
    send_message(txt.ask_institution_name)


@on_text(state=st.CreateAd.institution_name)
def _():
    with model.Institution.proxy() as inst:
        inst.name = ctx.text

    ctx.state = st.CreateAd.institution_address
    send_message(txt.ask_institution_address)


@on_text(state=st.CreateAd.institution_address)
def _():
    with model.Institution.proxy() as inst:
        inst.address = ctx.text

    ctx.state = st.CreateAd.vacancy_title
    send_message(txt.ask_vacancy_title)


@on_text(state=st.CreateAd.vacancy_title)
def _():
    with model.Vacancy.proxy() as vac:
        vac.title = ctx.text

    ctx.state = st.CreateAd.work_experience
    send_message(txt.ask_work_experience)


@on_text(state=st.CreateAd.work_experience)
def _():
    with model.Vacancy.proxy() as vac:
        vac.work_experience = ctx.text

    ctx.state = st.CreateAd.salary
    send_message(txt.ask_salary)


@on_text(state=st.CreateAd.salary)
def _():
    with model.Vacancy.proxy() as vac:
        vac.salary = ctx.text

    ctx.state = st.CreateAd.schedule
    send_message(txt.ask_schedule)


@on_text(state=st.CreateAd.schedule)
def _():
    with model.Vacancy.proxy() as vac:
        vac.schedule = ctx.text

    ctx.state = st.CreateAd.working_hours
    send_message(txt.ask_working_hours)


@on_text(state=st.CreateAd.working_hours)
def _():
    with model.Vacancy.proxy() as vac:
        vac.working_hours = ctx.text

    ctx.state = st.CreateAd.extra_info
    send_message(txt.ask_additional_info)


@on_text(state=st.CreateAd.extra_info)
def _():
    with model.Ad.proxy() as ad:
        ad.extra_info = ctx.text
        ad.institution = model.Institution.get()
        ad.vacancies = [model.Vacancy.get()]
        ad.save_to_collection()

    # if ctx.data.get('edit_mode'):
    #     ctx.state = 'edit'
    #     send_message(txt.show_ad.format(ad))
    # else:
    #     ctx.state = '...'
    #     send_message('...')
