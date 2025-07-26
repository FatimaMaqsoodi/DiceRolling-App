```markdown
# 🎲 Flask Dice Roller App with History (Python Backend)

A simple and interactive **dice rolling web app** built using **Flask (Python)**. Users can roll up to 10 dice at a time, see visual dice results, view roll history, and remove history as needed — all powered without JavaScript!

---

## 📁 Project Folder: `Project/`

### 📦 Features
- 🎲 Roll 1–10 dice at once  
- 🧠 View history of previous rolls  
- 🗑️ Clear entire roll history  
- 🌙 Toggle Dark/Light Mode  
- 🎨 Clean, animated, responsive UI using HTML and CSS  
- ✅ Fully Python-powered logic (no JavaScript required for functionality)  

---

## 🚀 Getting Started

### 🔧 Prerequisites
Make sure the following are installed:
- Python 3.x
- `pip` package manager
- Flask (`pip install flask`)

---

## 📂 File Structure

```

Project/
├── app.py                  # Main Flask app
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Styling (Light + Dark Mode)
└── README.md               # Project documentation

````

---

## ⚙️ How It Works

- **Backend:** Python’s `random.randint()` handles dice logic.  
- **Frontend:** HTML+CSS display dynamic dice outcomes visually.  
- **Session:** History is stored using Flask sessions — no database needed.  
- **Limits:** User can roll up to 10 dice at once.  

---

## ▶️ Run the App

1. Open terminal in your project folder:
   ```bash
   python app.py
````

2. Then open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 🛠️ Customize or Enhance

You can enhance the app by adding:

* 🎯 Custom number of sides on dice (e.g., D4, D20)
* 🕹️ Keyboard shortcuts to roll again
* 📦 Export history to JSON
* 🧾 Save history across sessions using SQLite or MySQL
* 👥 Multi-user support with login system

---
## 🙌 Contributions

Feel free to fork, suggest improvements, or add features! All contributions are welcome.

---

## 📄 License

This project is free and open source. Use it for **learning**, **fun**, or as a base for more advanced Python web apps.

```
