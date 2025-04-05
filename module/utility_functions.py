import logging
import os

import openai  # Added missing import
from dotenv import load_dotenv
from privacy_consent import show_privacy_consent

from utils import (adalovelace_insights, davinci_insights, einstein_insights,
				   gandhi_insights, newton_thoughts, suntzu_insights)

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
	logging.error("OpenAI API key not found in environment variables.")
openai.api_key = openai_api_key

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
	if not show_privacy_consent():
		logging.info("User declined consent. Exiting application.")
		return

	user_input = "How can I innovate in my field?"
	newton_response = newton_thoughts(user_input)
	davinci_response = davinci_insights(user_input)
	einstein_response = einstein_insights(user_input)
	suntzu_response = suntzu_insights(user_input)
	gandhi_response = gandhi_insights(user_input)
	adalovelace_response = adalovelace_insights(user_input)

	print("Newton Response:", newton_response)
	print("Da Vinci Response:", davinci_response)
	print("Einstein Response:", einstein_response)
	print("Sun Tzu Response:", suntzu_response)
	print("Gandhi Response:", gandhi_response)
	print("Ada Lovelace Response:", adalovelace_response)


if __name__ == "__main__":
	main()
