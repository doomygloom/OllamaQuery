import requests
import sys

# X: @owldecoy

def get_models(ip_address):
    url = f"http://{ip_address}:11434/api/tags"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [model['name'].split(":")[0] for model in data.get('models', [])]
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch models: {e}")
        sys.exit(1)

def ask_question(ip_address, model, question):
    url = f"http://{ip_address}:11434/api/generate"
    payload = {
        "model": model,
        "prompt": question,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("\n--- Answer ---")
        print(data.get('response', 'No response found.'))
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Failed to parse JSON.")

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <IP_ADDRESS> \"Your question here\"")
        sys.exit(1)

    ip_address = sys.argv[1]
    question = sys.argv[2]

    print(f"Fetching available models from {ip_address}...")
    models = get_models(ip_address)

    if not models:
        print("No models found.")
        sys.exit(1)

    print("\nAvailable models:")
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model}")

    try:
        choice = int(input("\nSelect a model by number: "))
        selected_model = models[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        sys.exit(1)

    print(f"\nUsing model: {selected_model}")
    ask_question(ip_address, selected_model, question)

if __name__ == "__main__":
    main()
