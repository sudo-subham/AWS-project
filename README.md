# Info Collector

A lightweight Flask web application for collecting, displaying, editing, and deleting user information.  
Data is stored in a **MySQL database hosted on AWS RDS**, and the app is deployed on an **EC2 instance**, accessible via a custom domain configured with **Route 53**.

🌐 Live Demo: [http://shubhampathak.xyz]

---

## 🚀 Features

- Collect user info (first name, last name, email, phone)
- View a list of submitted entries
- Edit existing entries
- Delete entries with confirmation
- Clean, responsive UI using Bootstrap 5
- Backend powered by Flask and MySQL (AWS RDS)
- Deployed on AWS EC2 with custom domain via Route 53

---

## 📁 Project Structure

info-collector/
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ └── edit.html
├── static/
  └── style.css



---

## ⚙️ Setup Instructions

### 1. Clone the repository

1. Clone the repository

```
git clone https://github.com/your-username/info-collector.git
cd info-collector
```
2. Set up a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
3. Install dependencies
```
pip install Flask mysql-connector-python
```

Configuration

Update your DB config in app.py:
```
db = mysql.connector.connect(
    host="your-rds-endpoint",
    user="your-db-user",
    password="your-db-password",
    database="your-db-name"
)
```
Start the Flask development server:

python app.py

Then open your browser to:

http://localhost:5000

screenshot 
<img width="1919" height="997" alt="image" src="https://github.com/user-attachments/assets/222d794c-d71c-4b61-b93d-4cd6ef03da8f" />


Database Schema

You’ll need a table like this in your RDS MySQL instance:
```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


📦 Deployment on AWS (Summary)
✅ EC2 Instance (Ubuntu)
Host the Flask app

Use nohup, gunicorn, or systemd to keep it running

Open port 5000 (or proxy with Nginx on port 80/443)

✅ RDS MySQL
Secure using security groups (allow access from EC2 only)

Use SSL (optional but recommended)

✅ Route 53
Domain: shubhampathak.xyz

Create A Record pointing to EC2 IP (or use a load balancer)

