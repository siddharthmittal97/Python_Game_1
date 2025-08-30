from flask import Flask, render_template_string, request
import random
import os

app = Flask(__name__)

choices = ["Stone", "Paper", "Scissors"]

template = """
<!doctype html>
<html>
<head>
  <title>Stone Paper Scissors</title>
  <style>
    /* Catchy gradient background */
    body { 
      font-family: Arial; 
      text-align: center; 
      margin: 0; 
      padding: 0; 
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    button { 
      font-size: 20px; 
      margin: 10px; 
      padding: 10px 20px; 
      cursor: pointer;
      border: none;
      border-radius: 10px;
      box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
      transition: transform 0.2s;
    }

    button:hover {
      transform: scale(1.1);
    }

    .result { 
      font-size: 22px; 
      margin-top: 20px; 
      font-weight: bold;
      color: #fff;
      text-shadow: 1px 1px 2px #000;
    }

    .footer { 
      margin-top: 40px; 
      font-size: 14px; 
      color: #fff; 
      text-shadow: 1px 1px 2px #000;
    }

    h1 {
      font-size: 32px;
      color: #fff;
      text-shadow: 2px 2px 4px #000;
    }
  </style>
</head>
<body>
  <h1>Hey! Let's play Stone Paper Scissors 🎮</h1>
  <form method="post">
    <button name="choice" value="Stone">⛰️ Stone</button>
    <button name="choice" value="Paper">📄 Paper</button>
    <button name="choice" value="Scissors">✂️ Scissors</button>
  </form>
  {% if result %}
    <div class="result">{{ result }}</div>
  {% endif %}

  <div class="footer">
    Created by <strong>Siddharth Mittal</strong>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    result = None
    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = f"🤝 It's a tie! Both chose {user_choice}."
        elif (user_choice == "Stone" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Stone") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"🎉 You win! You: {user_choice}, Computer: {computer_choice}"
        else:
            result = f"😅 You lose! You: {user_choice}, Computer: {computer_choice}"

    return render_template_string(template, result=result)

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable for deployment
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT not set
    app.run(debug=True, host="0.0.0.0", port=port)
