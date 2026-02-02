# 🤖 Gemini-Powered Code-Fixing Agent

A robust, autonomous AI agent built with the **Google Gemini 2.0 SDK**. This agent doesn't just "chat"—it interacts with your local filesystem to audit directories, read source code, fix bugs, and execute Python scripts to verify its own solutions in real-time.

## 🚀 The Mission
The goal was to move beyond simple LLM prompts and build a **fully agentic loop**. This architecture allows the model to act as a "junior developer" that follows an iterative workflow:
1. **Observe**: Scan the workspace to understand project structure.
2. **Reason**: Identify bugs or missing features in existing code.
3. **Act**: Write code fixes and create new files.
4. **Validate**: Run the code and use the STDOUT/STDERR feedback to self-correct until the task is complete.



## 🧠 Core Skills Mastered
Through the development of this agent, I have mastered several critical AI engineering concepts:

### 1. Function Calling & Tool Definition
I implemented a strict schema-driven approach using `types.FunctionDeclaration`. This allows the LLM to interact with my custom Python logic (file system operations and subprocess execution) with 100% type safety.

### 2. The Agentic "Reasoning" Loop
Implemented a multi-turn conversation loop (`MAX_ITERATIONS`) that maintains stateful memory. This allows the agent to:
* Use the result of Tool A to inform the call for Tool B.
* Handle complex tasks that require multiple steps (e.g., "Find the bug, fix it, and tell me if the tests pass").

### 3. System Instruction Engineering
Crafted high-performance system prompts that enforce persona, security constraints (relative pathing), and a "Read-Before-Write" operational philosophy.

### 4. Advanced Error Handling & Safety
* **Sandboxing Logic:** Implemented path validation using `pathlib` to ensure the agent cannot perform operations outside the permitted working directory.
* **Self-Correction:** Developed a feedback loop where Python `Tracebacks` and `Subprocess Errors` are fed back to the LLM as observations, allowing it to debug its own mistakes.



## 🛠️ Toolset (Functions)
The agent is equipped with the following capabilities:
* `get_files_content`: Audits directory structures and file sizes.
* `get_file_content`: Reads source code with safety buffers.
* `write_file`: Dynamically generates or updates `.py` files.
* `run_python_file`: Executes code in a subprocess and captures output for analysis.

## 💻 Tech Stack
* **LLM:** Google Gemini 2.0 Flash Lite (Optimized for speed/cost in agentic loops).
* **SDK:** `google-genai` (Python).
* **Environment:** Python 3.10+, `python-dotenv`, `pathlib`.

## 🚦 Getting Started

### Installation
```bash
git clone [https://github.com/YOUR_USERNAME/gemini-code-fixing-agent.git](https://github.com/YOUR_USERNAME/gemini-code-fixing-agent.git)
cd gemini-code-fixing-agent
pip install -r requirements.txt
