# Research Agent

## 📌 Overview
The **Research Agent** is an AI-powered automation system built with **CrewAI**, designed to:

- **Conduct in-depth research** on a given topic
- **Analyze product images** for quality and compliance
- **Generate structured reports** based on findings

This project utilizes **multimodal agents**, enabling text-based research and **image processing** capabilities.

---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/research_agent.git
cd research_agent
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set API Keys
This project requires **OpenAI API** and **Serper API**. Add your keys to an `.env` file:
```ini
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

---

## 🎯 Project Structure
```
research_agent/
│── .venv/                # Virtual environment (optional)
│── db/                   # Database (if needed for storage)
│── knowledge/            # Pre-stored research data
│   ├── user_preference.txt
│── src/
│   ├── research_agent/
│   │   ├── config/        # Configuration files
│   │   │   ├── agents.yaml
│   │   │   ├── tasks.yaml
│   │   ├── tools/         # Custom tools for agents
│   │   │   ├── custom_tool.py
│   │   ├── crew.py        # CrewAI logic
│   │   ├── main.py        # Main execution script
│── tests/                 # Test cases
│── README.md              # Project documentation
│── pyproject.toml         # Python project metadata
│── .gitignore             # Ignoring unnecessary files
```

---

## 📜 Configuration Files
### `agents.yaml` - Defines AI Agents
```yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    Expert in finding and summarizing complex data.

reporting_analyst:
  role: >
    {topic} Reporting Analyst
  goal: >
    Create detailed reports based on {topic}
  backstory: >
    Skilled in organizing data into structured reports.

expert_analyst:
  role: >
    Visual Quality Inspector
  goal: >
    Perform detailed quality analysis of product images
  backstory: >
    Senior quality control expert in visual inspection.
```

### `tasks.yaml` - Defines Tasks for Agents
```yaml
research_task:
  description: >
    Conduct in-depth research about {topic}
  expected_output: >
    10 key insights on {topic}
  agent: researcher

reporting_task:
  description: >
    Generate a structured report based on research findings.
  expected_output: >
    A detailed markdown report.
  agent: reporting_analyst

inspection_task:
  description: >
    Analyze product images for quality, defects, and compliance.
  expected_output: >
    A structured quality assessment report.
  agent: expert_analyst
```

---

## 🛠 Running the Agent
### 🔹 Run Research & Image Analysis
```bash
python src/research_agent/main.py
```

### 🔹 Train the CrewAI Model
```bash
python src/research_agent/main.py train 10 model_output.pkl
```

### 🔹 Replay a Specific Task
```bash
python src/research_agent/main.py replay inspection_task
```

---

## 🎨 Customization Guide
1️⃣ **Modify Agents:**
   - Edit `agents.yaml` to change roles, goals, or backstories.

2️⃣ **Update Tasks:**
   - Customize `tasks.yaml` to define new research or analysis objectives.

3️⃣ **Add New Tools:**
   - Implement new tools in `tools/custom_tool.py` to extend capabilities.

---

## 📌 Best Practices
✅ Ensure **API keys** are valid and stored securely.
✅ Use **specific task descriptions** for better AI performance.
✅ Keep dependencies **up-to-date** to avoid compatibility issues.
✅ Run tests before deploying changes.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License
This project is open-source and available under the **MIT License**.

🚀 **Happy Researching!**

