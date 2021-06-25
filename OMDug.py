def step1():
    print(
        'Утка-маляр решила погулять. '
        'Взять ей зонтик? '
    )
    option = ''
    options = {'Да': True, 'Нет': False}
    while option not in options:
        print('Выберите {}/{}'.format(*options))
        option = input()

        if options[option]:
            step2_umbrella()
        else:
            return step2_non_umbrella()


def step2_umbrella():
    print(
        'Утка-маляр попала под дождик. '
        'Воспользоваться ли ей зонтиком? '
    )
    option = ''
    options = {'Да': True, 'Нет': False}
    while option not in options:
        print('Выберите {}/{}'.format(*options))
        option = input()

        if options[option]:
            return step3_umbrella()
        else:
            return step3_rain_with_umbrella()


def step2_non_umbrella():
    print('Начался дождь! Утку смыло в океан ')


def step3_umbrella():
    print(
        'Утка-маляр открыла зонтик. '
        'Куда пойти утке? '
    )
    option = ''
    options = {'В парк': True, 'К озеру': False}
    while option not in options:
        print('Выберите {}/{}'.format(*options))
        option = input()

        if options[option]:
            return step4_park()
        else:
            return step4_lake()


def step3_rain_with_umbrella():
    print('У утки переохлаждение - помянем ')


def step4_park():
    print(
        'Утка-маляр в парке! '
        'Что делать утке? '
    )
    option = ''
    options = {'Погулять': True, 'Домой': False}
    while option not in options:
        print('Выберите {}/{}'.format(*options))
        option = input()

        if options[option]:
            return step5_walking()
        else:
            return step5_home()


def step4_lake():
    print(
        'Утка-маляр уплыла в небытье'
    )


def step5_walking():
    print(
        'Утка-маляр гуляла долго...больше ее никто не видел'
    )


def step5_home():
    print(
        'Утка-маляр пришла домой и теперь греет лапки'
    )


if __name__ == '__main__':
    step1()
