# AI Research Assistant

This project is an AI-powered research assistant that helps you generate detailed research outputs using advanced language models and web tools.

## Features

- Uses LLMs (like GPT-4o or Llama3) for generating research summaries.
- Integrates Wikipedia and DuckDuckGo search tools for up-to-date information.
- Saves research outputs to a text file with timestamps.
- Structured output using Pydantic models.

## Getting Started

### Prerequisites

- Python 3.10+
- API keys for OpenAI or Groq (set in `.env`)

### Installation

1. Clone this repository.
2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Set your API keys in the `.env` file:

    ```
    OPENAI_API_KEY="your_openai_key"
    GROQ_API_KEY="your_groq_key"
    ```

### Usage

Run the main script:

```sh
python main.py
```

Enter your research query when prompted. The assistant will search, summarize, and save the output to `research_output.txt`.

---

## Demo Video


https://github.com/user-attachments/assets/4bd6ea0c-de1e-4c14-909c-816a1f2d2462



---

## Contributing

Feel free to open issues or submit pull requests!

## Contact

Created by **Fahad Siddiqui**  
Email: fahads.dev@gmail.com

---

If you find this project useful, please ⭐️ star
