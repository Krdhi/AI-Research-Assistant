# 📚 AI Research Assistant — PDF/URL Analyzer with GPT-4

*Analyze and summarize documents from either PDFs or web links with GPT-powered insights.*

---

## 🌍 Project Description

This tool allows users to extract content from **PDF files** or **web URLs**, analyze the content using **GPT‑4**, and generate:

* Key bullet-point summaries
* Contradiction detection
* Topic tags

Built using **Python 3.13**, **Gradio UI**, **OpenAI API**, and **PyMuPDF**.

---

## 📁 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## ✨ Features

| Capability           | Details                                              |
| -------------------- | ---------------------------------------------------- |
| 📄 Analyze PDFs      | Extracts clean text from uploaded PDF files          |
| 🔗 Analyze URLs      | Scrapes article text from webpages (HTML `<p>` tags) |
| 🤖 GPT‑4 Integration | Summarizes with bullet points, contradictions, tags  |
| 🔐 Secure API        | OpenAI API key entered securely via Gradio UI        |
| 🖥️ Gradio Interface | Clean, shareable interface (no local Flask needed)   |
| 💡 PyCharm Ready     | Pure Python script with no notebook dependencies     |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create a virtual environment

```bash
python3.13 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

If using Colab instead:

```python
!pip install gradio pymupdf openai requests beautifulsoup4
```

---

## 💻 Usage

```bash
python app.py
```

Then open the Gradio interface in your browser (localhost or share link). You’ll see options to:

* Upload a PDF OR
* Paste a URL
* Enter your OpenAI API key
* Click “Run Analysis” to get results

---

## 🧠 GPT Prompt Logic

The app sends a prompt to GPT‑4 asking for:

* A concise summary
* Contradictions (if any)
* Topic/theme tags

You can tweak the logic inside the `analyze_text()` function.

---

## 📂 Project Structure

```
ai-research-assistant/
├── app.py                 # Main script
├── requirements.txt       # All required packages
└── README.md              # This file
```

---

## 📝 Notes

* Works with **Python 3.13** (tested on PyCharm)
* API key is not stored or logged
* Supports up to \~6000 characters of text in a single request

---

## 📜 License

Released under the **MIT License** — free for personal and commercial use.
Use responsibly.

---

## 🙌 Acknowledgements

* [OpenAI](https://platform.openai.com/)
* [Gradio](https://www.gradio.app/)
* [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
