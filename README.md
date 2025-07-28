📚 Book Review Platform (FastAPI + MSSQL)

A backend application for managing user reviews of books using FastAPI and MSSQL. Includes models for Users, Books, and Reviews with logic to prevent duplicate reviews.

📌 Features
- Add books and user reviews
- Prevent duplicate reviews by same user
- Relational models with validation
- SQLAlchemy ORM for DB operations

🧰 Tech Stack
- **Backend**: FastAPI, Python 3.10
- **Database**: MSSQL Server, SQLAlchemy
- **Validation**: Pydantic
- **Tools**: Git, VS Code

🚀 How to Run
1. Clone the repo  
   ```bash
  git clone https://github.com/gopimuthukumar/Mini_Project_1.git
   cd book-review-platform
   ```
2. Install dependencies  
   ```bash
     pip install -r requirements.txt
   ```

3. Set up MSSQL database and update `database.py`

4. Run the app  
   ```bash
   uvicorn main:app --reload
   ```

## 📁 Folder Structure
```
.
├── main.py
├── models/
├── routes/
├── database.py
├── requirements.txt
```

## 📝 Author
[Gopi Muthukumar](https://github.com/gopimuthukumar)
