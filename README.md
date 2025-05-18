# OllamaQuery

Interact with an Ollama API, retrieve available models, and query a selected model with a prompt.

* Fetches available models from a specified IP address.
* Allows selecting an available model from the list.
* Sends a prompt to the chosen model and displays the response.

## Requirements

* Python 3.x
* `requests` library

Install the `requests` library:

```
pip install requests
```

## Usage

Run the script from the command line:

```
python OllamaQuery.py <IP_ADDRESS> "Your question here"
```

### Example:

```
python OllamaQuery.py 192.168.1.100 "What is the capital of France?"
```

### Output:

```
Fetching available models from 192.168.1.100...
Available models:
1. modelA
2. modelB

Select a model by number: 1

Using model: modelA
--- Answer ---
The capital of France is Paris.
```
