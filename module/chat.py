import logging
import os
from pathlib import Path

import httpx
import openai
from dotenv import load_dotenv
from tenacity import retry, wait_random_exponential, stop_after_attempt

from module.bias_detection import evaluate_bias

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Set your OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
	logging.error("OpenAI API key not found in environment variables.")
openai.api_key = openai_api_key

# Set your Azure OpenAI API key and endpoint
azure_openai_api_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
if not azure_openai_api_key or not azure_openai_endpoint:
	logging.error("Azure OpenAI API key or endpoint not found in environment variables.")


@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, model="gpt-4"):
	try:
		response = openai.ChatCompletion.create(
			model=model,
			messages=messages
		)
		return response.choices[0].message['content'].strip()
	except Exception as e:
		logging.error("Unable to generate ChatCompletion response")
		logging.error(f"Exception: {e}")
		return str(e)


def get_internet_answer(question):
	messages = [
		{"role": "system", "content": "You are a helpful assistant."},
		{"role": "user", "content": question}
	]
	response = chat_completion_request(messages)
	return response


def list_fine_tuning_jobs():
	all_jobs = []
	try:
		first_page = openai.FineTuningJob.list(limit=20)
		all_jobs.extend(first_page.data)
		logging.info(f"Next page cursor: {first_page.after}")
		for job in first_page.data:
			logging.info(job.id)
	except Exception as e:
		logging.error("Unable to list fine-tuning jobs")
		logging.error(f"Exception: {e}")
	return all_jobs


def upload_file_for_fine_tuning(file_path):
	try:
		response = openai.File.create(
			file=Path(file_path),
			purpose="fine-tune",
		)
		logging.info(f"File uploaded successfully: {response['id']}")
		return response
	except Exception as e:
		logging.error("Unable to upload file for fine-tuning")
		logging.error(f"Exception: {e}")
		return None


def create_fine_tuning_job(model, training_file_id):
	try:
		response = openai.FineTuningJob.create(
			model=model,
			training_file=training_file_id,
		)
		logging.info(f"Fine-tuning job created successfully: {response['id']}")
		return response
	except openai.error.APIConnectionError as e:
		logging.error("The server could not be reached")
		logging.error(e.__cause__)  # an underlying Exception, likely raised within httpx.
	except openai.error.RateLimitError as e:
		logging.error("A 429 status code was received; we should back off a bit.")
	except openai.error.APIError as e:
		logging.error("Another non-200-range status code was received")
		logging.error(e.status_code)
		logging.error(e.response)
	except Exception as e:
		logging.error("An error occurred while creating the fine-tuning job")
		logging.error(f"Exception: {e}")
		return None


def make_post_request(url, data):
	try:
		response = httpx.post(url, json=data)
		logging.info(f"Response status code: {response.status_code}")
		logging.info(f"Response headers: {response.headers}")
		return response
	except Exception as e:
		logging.error("An error occurred while making the POST request")
		logging.error(f"Exception: {e}")
		return None


def azure_chat_completion_request(messages, model="deployment-name"):
	try:
		headers = {
			"Content-Type": "application/json",
			"api-key": azure_openai_api_key
		}
		payload = {
			"model": model,
			"messages": messages
		}
		response = httpx.post(azure_openai_endpoint, headers=headers, json=payload)
		response.raise_for_status()
		return response.json()["choices"][0]["message"]["content"].strip()
	except httpx.HTTPStatusError as e:
		logging.error("Unable to generate Azure ChatCompletion response")
		logging.error(f"Exception: {e}")
		return str(e)


def evaluate_and_mitigate_bias(df, label_name, protected_attribute_name, privileged_groups, unprivileged_groups):
	"""Evaluate and mitigate bias in the dataset."""
	return evaluate_bias(df, label_name, protected_attribute_name, privileged_groups, unprivileged_groups)

# Example usage of evaluate_and_mitigate_bias function
# df = ...  # Load your DataFrame here
# label_name = "label"
# protected_attribute_name = "protected_attribute"
# privileged_groups = [{'protected_attribute': 1}]
# unprivileged_groups = [{'protected_attribute': 0}]
# evaluate_and_mitigate_bias(df, label_name, protected_attribute_name, privileged_groups, unprivileged_groups)
