import json
import logging

import jsonschema
from jsonschema import validate

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load your data
data_file_path = 'data/data.json'
schema_file_path = 'config/schema.json'

try:
    with open(data_file_path, 'r') as file:
        data = json.load(file)
    logging.info(f"Loaded data from {data_file_path}")
except FileNotFoundError:
    logging.error(f"File not found: {data_file_path}")
    data = None

# Load the schema
try:
    with open(schema_file_path, 'r') as file:
        schema = json.load(file)
    logging.info(f"Loaded schema from {schema_file_path}")
except FileNotFoundError:
    logging.error(f"File not found: {schema_file_path}")
    schema = None

# Validate the data
if data and schema:
    try:
        validate(instance=data, schema=schema)
        logging.info("Data is valid")
    except jsonschema.exceptions.ValidationError as err:
        logging.error("Data is invalid")
        logging.error(err)
else:
    logging.error("Validation skipped due to missing data or schema")