# Running LLMs on a Laptop using Ollama

## 1. Run LLMs on Laptop

Ollama allows you to run Large Language Models (LLMs) locally on your machine.

### Install and Use Ollama
- Download and install Ollama from the official website.
- After installation, you can pull and run models locally.

---

## 2. Models for Laptop

Before choosing a model, consider your system RAM.

### Example Model Pull
```bash
ollama pull your-model-name
```

### List Available Models
```bash
ollama list
```

### Notes:
- Smaller models (e.g., 1.5, 3B, 7B) work well on laptops.
- Larger models require higher RAM and GPU support.

---

## 3. Impact on RAM

- When you run a model, it loads into RAM.
- During prompt execution:
    - RAM usage increases significantly.
    - Memory remains occupied until the response is generated.
- Recommendation:
    - Monitor RAM usage while running prompts.
    - Ensure sufficient free memory before running large models.

---

## 4. Running Ollama Server

Ollama runs on a local server by default.

Default Endpoint
> http://localhost:11434/

Start Server (if not running)
> ollama serve

---

## 5. Using Ollama via Application
1. Open the Ollama app.
2. Select the downloaded model.
3. Enter your prompt and generate responses.

---

## 6. To run the above app

Create .env File with below content
```bash
MODEL_NAME={your-model-name}
```

command to run python app
```bash
python app.py
```