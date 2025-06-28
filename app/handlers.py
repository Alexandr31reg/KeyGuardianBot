from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,  # type: ignore
                                   text=f"🔐 Key Guardian — ваш надёжный помощник для безопасного хранения всех логинов и паролей!\n\n"
                                        f"Забудьте о беспокойстве за сохранность учётных данных — наш бот бережно сохранит всю вашу конфиденциальную информацию в зашифрованном виде. Больше никаких сложных комбинаций символов и бесконечных списков — всё хранится централизованно и доступно одним кликом прямо в Telegram.\n\n"
                                        f"✅ Удобство и простота использования\n"
                                        f"✅ Высокая степень шифрования и защита данных\n"
                                        f"✅ Быстрый доступ ко всей необходимой информации\n\n"
                                        f"Начните пользоваться Key Guardian прямо сейчас и забудьте о проблемах с забытыми паролями навсегда!", reply_markup=kb.start_kb)