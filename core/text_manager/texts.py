from aiogram.utils.i18n import gettext as _


class ButtonText:
    def main_menu(self) -> str:
        return "📖 Главное меню"

    def new_order(self) -> str:
        return "🔥 Новый заказ"

    def to_order(self) -> str:
        return "🛒 Перейти к заказу"

    def my_orders(self) -> str:
        return "🛒 Мои заказы"

    def order(self) -> str:
        return "🧾 Перейти к заказу"

    def wallet(self) -> str:
        return "👛 Кошелёк"

    def history(self) -> str:
        return "📨 Операции"

    def referrals(self) -> str:
        return "💰 Рефералы"

    def faq(self) -> str:
        return "💡 FAQ"

    def help(self) -> str:
        return "⛑️ Помощь"

    def cheques(self) -> str:
        return "🦋 Чеки"

    def cheques_create_check(self) -> str:
        return "🧾 Создать чек"

    def cheques_create_multi_check(self) -> str:
        return "🧾 Создать мульти-чек"

    def cheques_with_count(self) -> str:
        return "💼 Чеки ({count})"

    def cheques_multi_with_count(self) -> str:
        return "💼 Мульти-чеки ({count})"

    def cheques_min_sum(self) -> str:
        return "📉 Мин {min_sum} руб"

    def cheques_max_sum(self) -> str:
        return "📈 Макс {max_sum} руб"

    def cheques_min_quantity(self) -> str:
        return "📉 Мин {min_quantity}"

    def cheques_max_quantity(self) -> str:
        return "📈 Макс {max_quantity}"

    def decline(self) -> str:
        return "❌ Отклонить"

    def accept(self) -> str:
        return "✅ Подтвердить"

    def cheques_list(self) -> str:
        return "💼 Список чеков"

    def subscribe_channel(self) -> str:
        return "📣 Канал"

    def subscribe_group(self) -> str:
        return "👥 Группа"

    def subscribe_private_group(self) -> str:
        return "🔒 Приватная группа"

    def send_cheque(self) -> str:
        return "💵 Отправить"

    def change_amount(self) -> str:
        return "💸 Изменить сумму"

    def change_quantity(self) -> str:
        return "📦 Изменить количество"

    def remove(self) -> str:
        return "🗑️ Удалить"

    def add_subscribe(self) -> str:
        return "➕ Добавить подписку"

    def subscribes(self) -> str:
        return "🔔 Подписки"

    def check_subscribes(self) -> str:
        return "🔔 Проверить подписки"

    def my_bots(self) -> str:
        return "🤖 Мои боты"

    def bot_in_list(self) -> str:
        return "🤖 @{bot_username}"

    def bot_create(self) -> str:
        return "🛠️ Создать"

    def admin_panel(self) -> str:
        return "👨‍💻 Админ-панель"

    def categories(self) -> str:
        return "🗄️ Категории"

    def products(self) -> str:
        return "🧾 Услуги"

    def cancel(self) -> str:
        return "❌ Отмена"

    def back(self) -> str:
        return "↩️ Назад"

    def yes(self) -> str:
        return "✅ Да"

    def no(self) -> str:
        return "❌ Нет"

    def pagination_next(self) -> str:
        return "▶️"

    def pagination_prev(self) -> str:
        return "◀️"

    def replenish(self) -> str:
        return "💳 Пополнить"

    def replenish_balance(self) -> str:
        return "💳 Пополнить баланс"

    def pay(self) -> str:
        return "💳 Оплатить"

    def pay_amount(self) -> str:
        return "💳 Пополнить на {amount} руб."

    def original(self) -> str:
        return "Как есть"

    def broadcast(self) -> str:
        return "✉️ Рассылка"

    def rules(self) -> str:
        return "❕ Правила"

    def offer(self) -> str:
        return "🪧 Оферта"


class MessageText:
    def main_menu(self) -> str:
        return _("<b>📖 Главное меню</b>\n\nВыберите интересующий Вас раздел:")

    def init(self) -> str:
        return _("Устанавливаю кнопку главного меню.")

    def admin_list_orders(self) -> str:
        return _(
            "<b>👨‍💻 Панель администратора</b>\n"
            "   -> <b>🛒 Управление заказами</b>\n"
            "\n"
            "🔸 Нажмите на статус, чтобы включить или выключить отображение заказов с соответствующим статусом.\n"  # noqa
            "\n"
            "🔸 Введите user_id в формате <b>'id-********'</b> для настройки фильтра по ID пользователя.\n"  # noqa
            "🔸 Введите order_id в формате <b>'o_id-********'</b> для настройки фильтра по ID заказа.\n"  # noqa
            "🔸 Введите целевую ссылку заказа в формате <b>'link-********'</b> для настройки фильтра по ссылке.\n"  # noqa
            "\n"
            "🔸 Текущие настройки фильтров:\n"
            "   ▫️ id: {user_id}\n"
            "   ▫️ order_id: {order_id}\n"
            "   ▫️ link: {link}\n"
            "   ▫️ Статусы:\n"
        )

    def admin_broadcast_error(self) -> str:
        return (
            "<b>👨‍💻 Панель администратора</b>\n"
            "   <b>└ ✉️ Рассылка</b>\n"
            "\n"
            "Произошла ошибка. Попробуйте еще раз."
        )

    def my_orders(self) -> str:
        return _(
            "<b>🛒 Мои заказы</b>\n"
            "\n"
            "Здесь все ваши заказы собраны в 3 группы по статусам:\n"
            "\n"
            "🟢 <b>Активные -</b> {pending} | {new} | {in_progress}\n"
            "\n"
            "✅ <b>Завершенные -</b> {completed} | {partial}\n"
            "\n"
            "❌ <b>Отмененные -</b> {canceled}\n"
            "\n"
            "Вы можете включать/выключать отображение групп нажатием на соответствующую кнопку.\n"  # noqa
            "Или нажмите на кнопку <b>🛒 Все заказы</b>, чтобы отобразить все."
        )

    def my_orders_not_found(self) -> str:
        return _("🤷‍♂️ Заказ не найден!")

    def my_orders_already_paid(self) -> str:
        return _("☝️ Заказ уже оплачен!")

    def my_orders_successfully_paid(self) -> str:
        return _("🎉 Заказ успешно оплачен!")

    def my_orders_insufficient_funds(self) -> str:
        return _(
            "🙁 Недостаточно средств на балансе!\n"
            "Не хватает: {replenish_amount} руб."
        )

    def order_info(self) -> str:
        return _(
            "<b>🛒 Мои заказы</b>\n"
            "   <b>└🧾 Информация о заказе:</b>\n"
            "\n"
            "<b>{name}</b>\n"
            "ID:                     <b>{id}</b>\n"
            "Export ID:         <b>{export_id}</b>\n"
            "Статус:            <b>{status}</b>\n"
            "Ссылка:            <b>{url}</b>\n"
            "Количество:    <b>{quantity}</b>\n"
            "Стоимость:      <b>{price}</b>\n"
        )

    def order_info_not_exported(self) -> str:
        return _("Присваивается после оплаты")

    def wallet(self) -> str:
        return _(
            "<b>👛 Кошелёк</b>\n"
            "\n"
            "💰 Ваш баланс: <b>{balance}</b> руб.\n"
            "\n"
            "💳 Выберите действие или введите сумму пополнения.\n"
        )

    def wallet_get_sum(self) -> str:
        return _(
            "<b>👛 Кошелёк</b>\n"
            "   <b>└💳 Пополнение</b>\n"
            "\n"
            "Выберите или введите сумму для пополнения:\n"
        )

    def wallet_replenish_min_sum(self) -> str:
        return _("☝️ Минимальная сумма пополнения - {min_sum} руб!")

    def wallet_replenish_choose_method(self) -> str:
        return _(
            "<b>👛 Кошелёк</b>\n"
            "   <b>└💳 Пополнение</b>\n"
            "      <b>└ Выбор способа Оплаты</b>\n"
            "\n"
            "Сумма пополнения: {amount} руб.\n"
        )

    def wallet_history(self) -> str:
        return _("<b>👛 Кошелёк</b>\n   <b>└📨 Операции</b>\n\n{operations}\n")

    def wallet_no_history(self) -> str:
        return _("🤷‍♂️ У вас нет операций по счету.")

    def wallet_success_payment(self) -> str:
        return _(
            "<b>💰 Оплата прошла успешно.</b>\n"
            "Сервис: <b>{gateway_name}</b>\n"
            "Сумма: <b>{amount}</b> руб."
        )

    def referrals(self) -> str:
        return _(
            "<b>🤝 Партнерская программа</b>\n"
            "\n"
            "🏆 Вознаграждения по реферальной (партнерской) \n"
            "программе разделены на два уровня:\n"
            "├  За пользователей которые присоединились по Вашей ссылке "
            "- рефералы 1 уровня\n"
            "└  За пользователей которые присоединились по ссылкам Ваших"
            " рефералов - рефералы 2 уровня"
            "\n"
            "🤑 Сколько можно заработать?\n"
            "├  За реферала 1 уровня: {level_one_percents}%\n"
            "└  За реферала 2 уровня: {level_two_percents}%\n"
            "\n"
            "🥇 Статистика:\n"
            "├  Всего заработано: {total_bonus_amount}\n"
            "└  Лично приглашенных: {referrals_count}\n"
            "\n"
            "🎁 Бонус за регистрацию:\n"
            "└  За каждого пользователя который активировал бот по вашей"
            " реферальной ссылке, через ваш чек, или через бота, которого вы"
            " создали вы, так же получаете {bonus_amount}"
            " рублей.\n"
            "\n"
            "⤵️ Ваши ссылки:\n"
            "└ https://t.me/{bot_username}?start=ref_{user_id}\n"
        )

    def referral_payment() -> str:
        return _(
            "💰 Вы получили реферальное вознаграждение в размере"
            " <b>{affiliate_bonus}</b> руб."
        )

    def referrals_try_own_link(self) -> str:
        return _(
            "☝️ Вы не можете регистрироваться по собственной"
            " реферальной ссылке!"
        )

    def referrals_incorrect_link(self) -> str:
        return _(
            "Вы попытались зарегистрироваться по некорректной"
            " реферальной ссылке."
            "\n"
            "🤷‍♂️ Пользователя с таким идентификатором не существует."
        )

    def referrals_bind_link(self) -> str:
        return _(
            "🔗 По вашей реферальной ссылке зарегистрировался новый"
            " пользователь."
        )

    def referrals_bind_bot(self) -> str:
        return _("🤖 В вашем боте зарегистрировался новый пользователь.")

    def referrals_bind_cheque(self) -> str:
        return _("🦋 По вашему чеку зарегистрировался новый пользователь.")

    def referrals_get_bonus(self) -> str:
        return _(
            "{cause_description}\n"
            "🎁 Вы получили бонус в размере"
            " <b>{amount}</b> руб."
        )

    def cheque_activate_wrong_number(self) -> str:
        return _(
            "🤷‍♂️ Чека с идентификатором <b>'{cheque_number}'</b>"
            " не существует."
            "\n"
            "🤔 Возможно он был удален владельцем."
        )

    def cheque_try_reactivation(self) -> str:
        return _("☝️ Вы не можете активировать чек повторно!")

    def cheque_fully_activated(self) -> str:
        return _("🙁 Этот чек уже полностью использован!")

    def cheque_try_own_cheque(self) -> str:
        return _("☝️ Вы не можете активировать свой же чек!")

    def cheque_needs_subscriptions(self) -> str:
        return _(
            "☝️ Вы пока не можете активировать данный чек\n"
            "\n"
            "Он доступен только для подписчиков"
            " указанных ниже каналов и групп:\n"
            "{subscribes_list}\n"
            "\n"
            "Подпишитесь на них и нажмите кнопку ниже 👇\n"
        )

    def cheque_your_cheque_activated(self) -> str:
        return _("🦋 Ваш {cheque_type} был активирован!")

    def cheque_successfully_activated(self) -> str:
        return _(
            "🦋 Вы активировали чек!\n"
            "💰 Ваш баланс пополнен на <b>{amount}</b> руб."
        )

    def try_later(self) -> str:
        return _("🤷‍♂️ Что-то пошло не так. Повторите попытку позже.")

    def new_order_choose_category(self) -> str:
        return _(
            "🔥 <b>Создание нового заказа!</b>\n"
            "   <b>└🗄️ Выбор категории</b>"
        )

    def new_order_choose_subcategory(self) -> str:
        return _(
            "<b>🔥 Создание нового заказа!</b>\n"
            "   <b>└🗃️ Выбор подкатегории</b>\n"
            "\n"
            "🗄️ Категория: <b>{category_name}</b>\n"
        )

    def new_order_choose_product(self) -> str:
        return _(
            "<b>🔥 Создание нового заказа!</b>\n"
            "   <b>└🧾 Выбор услуги</b>\n"
            "\n"
            "🗄️ Категория: <b>{category_name}</b>\n"
            "🗃️ Подкатегория: <b>{subcategory_name}</b>\n"
        )

    def new_order_enter_amount(self) -> str:
        return _(
            "<b>🔥 Создание нового заказа!</b>\n"
            "   <b>└📦 Количество</b>\n"
            "\n"
            "🗄️ Категория: <b>{category_name}</b>\n"
            "🗃️ Подкатегория: <b>{subcategory_name}</b>\n"
            "🧾 Услуга: <b>{title}</b>\n"
            "💵 Цена: <b>{price} руб</b> за одну единицу (Подписчик, лайк, репост...)\n"  # noqa
            "\n"
            "👇 Введите количество для заказа от {min_quantity} до {max_quantity}:"  # noqa
        )

    def new_order_wrong_quantity(self) -> str:
        return _(
            "☝️ Введите целое число в диапазоне от {min_quantity} до {max_quantity}"  # noqa
        )

    def new_order_enter_url(self) -> str:
        return _(
            "<b>🔥 Создание нового заказа!</b>\n"
            "   <b>└🔗 Адрес целевой страницы</b>\n"
            "\n"
            "🗄️ Категория: <b>{category_name}</b>\n"
            "🗃️ Подкатегория: <b>{subcategory_name}</b>\n"
            "🧾 Услуга: <b>{title}</b>\n"
            "💵 Цена: <b>{price} руб</b> за одну единицу (Подписчик, лайк, репост...)\n"  # noqa
            "📦 Количество: <b>{quantity}</b>\n"
            "\n"
            "👇 Введите адрес целевой страницы (ссылка на фото, профиль, видео):"  # noqa
        )

    def new_order_wrong_link(self) -> str:
        return _("☝️ Введите ссылку в формате: <b>'https://example.com'</b>")

    def my_bots(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "\n"
            "💰 Ваши боты помогают вам <b>зарабатывать!</b>\n"
            "\n"
            "🏆 Каждый новый пользователь, который зарегистрируется через вашего"  # noqa
            " бота, автоматически становится вашим <b>рефералом</b>.\n"
            "\n"
            "⚙️ Здесь вы можете управлять своими ботами.\n"
        )

    def my_bots_manage_bot(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└📇 Информация о боте</b>\n"
            "\n"
            "Имя: <b>@{bot_username}</b>\n"
            "Токен: <b>{bot_token}</b>"
        )

    def my_bots_manage_unauthorized_bot(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└📇 Информация о боте</b>\n"
            "\n"
            "Имя: <b>Неавторизованный</b>"
            "\n"
            "Токен: <b>{bot_token}</b>\n"
            "<b>⚠️ Токен недействителен.</b>\n"
            "\n"
            "👇 Введите новый токен:"
        )

    def my_bots_create_instruction(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└🛠️ Создание бота</b>\n"
            "\n"
            "🔗 Перейдите к @BotFather.\n"
            "\n"
            "⌨️ Введите команду /newbot и следуйте инструкциям.\n"
            "\n"
            "🔑 Скопируйте <b>API Токен</b>, который вы получите после создания бота.\n"  # noqa
            "\n"
            "👇 Вернитесь сюда и введите его:"
        )

    def my_bots_not_token(self) -> str:
        return _("☝️ Это не токен!")

    def my_bots_already_exist(self) -> str:
        return _("☝️ Такой бот уже существует!")

    def my_bots_token_incorrect(self) -> str:
        return _("☝️ Токен введен неправильно. Попробуйте еще раз.")

    def my_bots_bot_ready(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└🛠️ Бот готов!</b>\n"
            "\n"
            "🤖 Ваш новый бот @{bot_username} готов к использованию!"
            "\n"
            "🔗 Ссылка для приглашения:\n"
            "   <a href='https://t.me/{bot_username}'>{bot_username}</a>"
        )

    def my_bots_token_is_retired(self) -> str:
        return _("'Неавторизованный'")

    def my_bots_delete_confirm(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└🗑️ Удаление бота</b>\n"
            "\n"
            "Вы уверены, что хотите удалить бота:\n"
            "   {bot_username}?"
        )

    def my_bots_delete_confirmed(self) -> str:
        return _(
            "<b>🤖 Управление ботами</b>\n"
            "   <b>└🗑️ Удаление бота</b>\n"
            "\n"
            "Бот {bot_username} успешно был удалён."
        )

    def cheque_inline_title_personal(self) -> str:
        return _("🦋 <b>Персональный чек</b>")

    def cheque_inline_title_multi(self) -> str:
        return _("🦋 <b>Мульти-чек</b>")

    def cheque_inline_description_personal(self) -> str:
        return _("💰 Внутри <b>{amount}</b> руб!")

    def cheque_inline_description_multi(self) -> str:
        return _(
            "💰 Внутри <b>{quantity}</b> активаций(я) по <b>{amount}</b> руб!"
        )

    def cheques(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "\n"
            "Чеки позволяют отправлять деньги прямо в сообщениях.\n"
            "\n"
            "🔸 Персональный чек - для отправки денег одному пользователю.\n"
            "\n"
            "🔸 Мульти-чек - можно отправить нескольким пользователям, а также  настроить условия"  # noqa
            " активации(наличие подписок у пользователя на определенные каналы и группы).\n"  # noqa
            "\n"
            "<b>👇 Выберите тип чека:</b>"
        )

    def cheques_low_balance(self) -> str:
        return _(
            "🙁 Ваш баланс равен нулю.\n"
            "👇 Пополните его, чтобы создавать чеки!"
        )

    def cheques_personal_get_amount(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 🧍 Персональный чек</b>\n"
            "      <b>└ 💸 Стоимость активации</b>\n"
            "\n"
            "<b>👇 Введите или выберите сумму чека:</b>"
        )

    def cheques_multi_get_amount(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 💸 Стоимость активации</b>\n"
            "\n"
            "Укажите стоимость <b>одной</b> активации.\n"
            "\n"
            "Чем больше сумма активации, тем больше каналов/групп можно добавить в условия подписки:\n"  # noqa
            "🔸 <b>{check_min_sum}</b> руб - <b>3</b> канала/группы\n"
            "🔸 <b>{sum_for_four}</b> руб - <b>4</b> канала/группы\n"
            "🔸 <b>{sum_for_five}</b> руб - <b>5</b> каналов/групп\n"
            "\n"
            "<b>👇 Введите или выберите сумму:</b>"
        )

    def cheques_amount_must_be_positive(self) -> str:
        return _("☝️ Сумма должна быть положительной!")

    def cheques_wrong_amount(self) -> str:
        return _(
            "☝️ Введите сумму не превышающую ваш баланс!\n"
            "💰 Ваш баланс: <b>{balance}</b> руб."
        )

    def cheques_get_quantity(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 💸 Стоимость активации</b>\n"
            "         <b>└ 📦 Количество активаций</b>\n"
            "\n"
            "Сколько пользователей смогут активировать этот чек?\n"
            "\n"
            "🔸 Одна активация: <b>{cheque_amount}</b>\n"
            "\n"
            "🔸 Максимум активаций с вашим балансом: <b>{max_quantity}</b>\n"
            "\n"
            "<b>👇 Введите количество активаций или выберите один из предложенных вариантов:</b>"  # noqa
        )

    def cheques_enter_positive_quantity(self) -> str:
        return _("☝️ Введите положительное целое число!")

    def cheques_wrong_quantity(self) -> str:
        return _("☝️ Вы можете указать не больше {max_quantity} активации!\n")

    def cheques_confirm_multi(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 💸 Стоимость активации</b>\n"
            "         <b>└ 📦 Количество активаций</b>\n"
            "            <b>└ ✔️ Подтвердить</b>\n"
            "\n"
            "<b>Общая сумма чека: {total_amount} руб</b>\n"  # noqa
            "\n"
            "<b>Внутри чека: {quantity} активаций(я) по {amount} руб\n</b>"
            "\n"
            "<b>🔸 Пожалуйста, подтвердите корректность данных:</b>"
        )

    def cheques_confirm_personal(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 🧍 Персональный чек</b>\n"
            "      <b>└ 💸 Стоимость активации</b>\n"
            "            <b>└ ✔️ Подтвердить</b>\n"
            "\n"
            "<b>Сумма чека: {amount} руб</b>\n"
            "\n"
            "🔸 <b>Пожалуйста, подтвердите корректность данных:</b>"
        )

    def cheques_insufficient_funds(self) -> str:
        return _("🙁 Недостаточно средств, пополните баланс!")

    def cheques_list_personal(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 🧍 Персональные чеки</b>\n"
            "\n"
            "Список Ваших персональных чеков:"
        )

    def cheques_list_multi(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чеки</b>\n"
            "\n"
            "Список Ваших мульти-чеков:"
        )

    def cheques_info_multi(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🏷 Информация о чеке</b>\n"
            "\n"
            "Общая сумма: <b>{total_amount}</b> руб\n"
            "Статус: <b>{status}</b>\n"
            "\n"
            "Внутри: <b>{quantity} / {total_quantity}</b> активации.\n"
            "1 активация - <b>{amount}</b> руб\n"
            "\n"
            "Ссылка на чек:\n"
            '<span class="tg-spoiler">{cheque_link}</span>'
        )

    def cheques_info_personal(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 🧍 Персональные чек</b>\n"
            "      <b>└ 🏷 Информация о чеке</b>\n"
            "\n"
            "Сумма: <b>{amount}</b> руб\n"
            "Статус: <b>{status}</b>\n"
            "\n"
            "Ссылка на чек:\n"
            "<span class='tg-spoiler'>{cheque_link}</span>"
        )

    def cheque_delete_confirm(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└🗑️ Удаление чека</b>\n"
            "\n"
            "Вы точно хотите удалить чек?"
        )

    def cheque_delete_subscription_confirm(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└🗑️ Удаление подписки</b>\n"
            "\n"
            "Вы точно хотите удалить подписку из чека?"
        )

    def cheque_delete_error(self) -> str:
        return _(
            "🤷‍♂️ Что-то пошло не так!\n"
            "🤔 Такого чека не существует или вы не являетесь его владельцем!"
        )

    def cheque_successfully_deleted(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n   <b>└🗑️ Удаление чека</b>\n\nЧек успешно удален"
        )

    def cheque_subscribes_info(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписки</b>\n"
            "\n"
            "Здесь собраны подписки, которые были добавлены в чек.\n"
            "\n"
        )

    def cheque_add_subscribe(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписки</b>\n"
            "         <b>└ ➕ Добавить подписку</b>\n"
            "\n"
            "👇 Выберите тип подписки:\n"
            "\n"
        )

    def cheque_add_channel(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписки</b>\n"
            "         <b>└ 📣 Добавить канал</b>\n"
            "\n"
            "🔸 Бот должен быть <b>администратором канала</b>, а также иметь"
            " <b>разрешение на приглашение</b> пользователей в канал.\n"
            "\n"
            "👇 Перешлите сюда сообщение из канала.\n"  # noqa
            "\n"
        )

    def cheque_add_group(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписки</b>\n"
            "         <b>└ 👥 Добавить публичную группу</b>\n"
            "\n"
            "Чтобы ограничить ваш мульти-чек публичной группой, отправьте сюда инвайт-ссылку на нее.\n"  # noqa
            "\n"
            "Например https://t.me/{bot_username}"
        )

    def cheque_add_private_group(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписки</b>\n"
            "         <b>└ 🔒 Добавить приватную группу</b>\n"
            "\n"
            "🔸 Бот должен быть <b>администратором группы</b>, а также иметь"
            " <b>разрешение на приглашение</b> пользователей в группу."
            "\n"
            "Для добавления приватной группы в чек, введите её идентификатор.\n"  # noqa
            "\n"
            "☝️ Если он вам неизвестен, то отправьте в группе команду <b>/get_group_id</b>.\n"  # noqa
            "В ответ бот пришлет вам идентификатор группы. Скопируйте его и введите сюда.\n"  # noqa
            "\n"
            "👇 Введите идентификатор группы:\n"
        )

    def cheque_no_more_subscribes(self) -> str:
        return _("☝️ Вы больше не можете добавлять подписки в этот чек!")

    def cheque_message_not_from_channel(self) -> str:
        return _("☝️ Это не сообщение из канала.")

    def cheque_bot_not_channel_admin(self) -> str:
        return _("☝️ Бот не добавлен в администраторы канала!")  # noqa

    def cheque_not_a_channel(self) -> str:
        return _("☝️ Это не канал!")

    def cheque_not_a_public_group(self) -> str:
        return _(
            "🤷‍♂️ Такой группы не существует!\n"
            "🤔 Или эта группа является приватной.\n"
            "☝️ Попробуйте выбрать подписку на приватную группу."
        )

    def cheque_wrong_group_id(self) -> str:
        return _("☝️ Идентификатор группы должен быть числом!")

    def cheque_bot_not_in_group(self) -> str:
        return _(
            "☝️ Такой группы не существует или бот не добавлен в группу!"
        )

    def cheque_group_is_not_private(self) -> str:
        return _("☝️ Это не приватная группа!")

    def cheque_bot_is_not_group_admin(self) -> str:
        return _(
            "☝️ Бот не является администратором группы"
            " или у него нет права приглашать пользователей!"
        )

    def cheque_subscribe_already_added(self) -> str:
        return _("☝️ Этот канал уже добавлен в этот чек!")

    def cheque_subscribe_added(self) -> str:
        return _("🎉 Подписка на канал/группу успешно добавлена в чек.")

    def cheque_subscribe_deleted(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└🗑️ Удаление подписки</b>\n"
            "\n"
            "Подписка успешно удалена."
        )

    def cheque_subscribe(self) -> str:
        return _(
            "<b>🦋 Чеки</b>\n"
            "   <b>└ 👬 Мульти-чек</b>\n"
            "      <b>└ 🔔 Подписка</b>\n"
            "\n"
            "Подписка на канал/группу привязанная к этому мульти-чеку:\n"
            "\n"
            "Название канала/группы: {title}\n"
            "\n"
            "Ссылка: {link}"
        )
