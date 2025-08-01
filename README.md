# 🃏 Study Session Card Draw

A fun and simple Python script to gamify your study sessions. Draw a card from a standard deck to determine your study duration and your break duration, making your study routine unpredictable and engaging.

## 📖 How it Works

The project is based on a simple concept:
1. Draw a card from a deck to determine your study session length.
2. Draw another card to determine your break length.

The card values are mapped to time using simple algebraic formulas to ensure your sessions and breaks fall within a healthy range. **The final calculated duration is rounded to the nearest multiple of 5 minutes.**

### Card Value Mapping

<div align="center">

| Card  | Value |
|-------|-------|
| Ace   | 1     |
| 2–10  | 2–10  |
| Jack  | 11    |
| Queen | 12    |
| King  | 13    |

</div>

### Formulas

* **Study Session ($S$):** Your session will be between 45 and 100 minutes.
    $$S = 45 + (C_S - 1) \times 4.23$$
    *Where* $C_S$ *is the card value for the study session.*

* **Break Duration ($B$):** Your break will be between 10 and 20 minutes.
    $$B = 10 + (C_B - 1) \times 0.83$$
    *Where* $C_B$ *is the card value for the break.*

## 🚀 Getting Started

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

## 📜 License

This project is licensed under the [MIT License](LICENSE).