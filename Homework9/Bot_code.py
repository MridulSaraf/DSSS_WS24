import nest_asyncio
nest_asyncio.apply()
import logging
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def load_model():
    print("Loading the model...")
    huggingface_token = ""#"***MY Token***"
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=huggingface_token)
    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=huggingface_token)
    print("Model loaded successfully!")
    return tokenizer, model

tokenizer, model = load_model()

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your AI assistant. How can I help you today?")

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"Received message: {user_message}")

    try:
        user_message = update.message.text
        contextual_prompt = f"Answer this query in detail: {user_message}"
        inputs = tokenizer.encode(contextual_prompt, return_tensors="pt")
        #inputs = tokenizer.encode(user_message, return_tensors="pt")
        outputs = model.generate(inputs,max_length=250, num_beams=5, no_repeat_ngram_size=3,encoder_no_repeat_ngram_size=3,top_p=0.9, 
        temperature=0.7 )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Generated response: {response}")
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Error during processing: {e}")
        await update.message.reply_text("I encountered an error. Please try again later.")

        
def main():
    telegram_token = ""#"***MY Token***"
    application = Application.builder().token(telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()
    # Debug log
    logger.info("Bot is starting...")
    # Starting the bot without closing the event loop
    try:
        asyncio.get_running_loop().run_until_complete(application.run_polling())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            logger.warning("Detected running event loop.")
            asyncio.create_task(application.run_polling())
        else:
            logger.error(f"An unexpected error occurred: {e}")
            raise e
if __name__ == "__main__":
    main()

