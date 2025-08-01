# 🃏 Study Session Card Draw

A fun and lightweight Python + web project to **gamify your study routine** using a deck of cards. Let chance decide your focus and break durations — with a clean web UI powered by AWS Lambda.

## 📦 Project Structure

| Path                 | Purpose                          |
|----------------------|----------------------------------|
| `frontend/`          | Single-page UI (HTML + Tailwind) |
| `lambda/`            | AWS Lambda backend (Python)      |
| `randomised_sessions.py` | Local Python script (CLI use)     |

---

## 📖 How it Works

The project is based on a simple concept:
1. Draw a card from a deck to determine your study session length.
2. Draw another card to determine your break length.

The card values are mapped to time using simple algebraic formulas to ensure your sessions and breaks fall within a healthy range. **The final calculated duration is rounded to the nearest multiple of 5 minutes** for simplicity.

### ♦️ Card Value Mapping


| Card  | Value |
|-------|-------|
| Ace   | 1     |
| 2–10  | 2–10  |
| Jack  | 11    |
| Queen | 12    |
| King  | 13    |

### 🔢 Formulas

- **Study Session (S):** Your session will be between 45 and 100 minutes.

<div align="center">

<b>S</b> = 45 + ($C_S$ − 1) × 4.23

</div>

Where $C_S$ is the card value for the study session.


- **Break Duration (B):** Your break will be between 10 and 20 minutes.

<div align="center">

<b>B</b> = 10 + ($C_B$ − 1) × 0.83

</div>

Where $C_B$ is the card value for the break.

## 🌐 Web App (Hosted via S3 + Lambda)

A responsive single-page app (SPA) with Tailwind UI and card image previews.

- Calls AWS Lambda via API Gateway.
- Gets card name + suit + calculated durations.
- Dynamically fetches card images using:  
  `https://deckofcardsapi.com/static/img/{CODE}.png`

### Try it locally

```bash
open frontend/index.html
```

Or check the live version:  
🔗 [https://study.eishaenan.com](https://study.eishaenan.com)

---

## 🐍 Run Locally (CLI Version)
### Prerequisites

You only need Python installed on your computer.

### Running the Script

1.  **Clone the repository:**
    ```
    git clone https://github.com/EishaEnan/randomised-sessions.git
    cd randomised-sessions
    ```

2.  **Run the script:**
    ```
    python randomised-sessions.py
    ```
The script will automatically draw both cards and print your session and break times.

## 💡 Example Output
```
--- Let's get focused! ---
Your study card is: 8!
Your session will be: 75.0 minutes.

Your break card is: Queen!
Your break will be: 20.0 minutes.
```
---

## ☁️ Lambda Backend

The Lambda function (see `lambda/lambda_function.py`) returns JSON:

```json
{
  "study_card_name": "Jack",
  "study_card_suit": "Spades",
  "study_duration": 90.0,
  "break_card_name": "3",
  "break_card_suit": "Hearts",
  "break_duration": 10.0
}
```

It does **not** fetch images — only calculates values.  
The frontend handles the display and image loading.

---
## 📜 License

This project is licensed under the [MIT License](LICENSE).
