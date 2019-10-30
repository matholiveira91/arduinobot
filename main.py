from telegram.ext import Updater, CommandHandler, MessageHandler 
import logging
import serial

TOKEN="631080010:AAGXA9Jegz1PehP5kwkkG-vChNOPzqxhZn4"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

conexao = serial.Serial('/dev/ttyACM0', 9600)

# Commands
def start(bot, update):
    """Send a message when the command /start is issued."""
    message_start = (
        f"Olá, { update.message.from_user.full_name}, envie /on ou /off para alterar o comportamento do bot"
        )
    update.message.reply_text(message_start)

def down(bot, update):
    conexao.write("0".encode("utf-8"))

def up(bot, update):
    conexao.write("1".encode("utf-8"))

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# Motor
def main():
    """Start the bot."""
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("off", down))
    dp.add_handler(CommandHandler("on", up))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

