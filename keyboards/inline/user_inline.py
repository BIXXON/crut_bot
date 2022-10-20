# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки при поиске профиля через админ-меню
open_profile_inl = InlineKeyboardMarkup()
#input_kb = InlineKeyboardButton(text="💵 Пополнить", callback_data="user_input")
input_kb = InlineKeyboardButton(text="💰 Баланс 💰", callback_data="ball")
#mybuy_kb = InlineKeyboardButton(text="🛒 Мои покупки", callback_data="my_buy")
open_profile_inl.add(input_kb)

bal_profile = InlineKeyboardMarkup()
bal_profile_kb = InlineKeyboardButton(text="💵 Пополнить баланс", url='https://t.me/igorkurbonov')
bal_profile.add(bal_profile_kb, InlineKeyboardButton(text="👤 Кабинет 👤", callback_data="user_profil"))

# Кнопка с возвратом к профилю
to_profile_inl = InlineKeyboardMarkup()
to_profile_inl.add(InlineKeyboardButton(text="👤 Кабинет 👤", callback_data="user_profile"))
