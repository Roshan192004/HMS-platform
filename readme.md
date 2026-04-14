# 🏥 Hospital Management System (HMS)

A full-stack Django-based Hospital Management System built to streamline hospital workflows including patient management, appointments, prescriptions, billing, pharmacy, and administrative control.

This project demonstrates modular backend architecture, relational database handling, role-based access control, and real-world workflow implementation.

---

## 🚀 Features

### 👤 Patient Module
- Patient registration & login  
- Book / cancel appointments  
- View and download prescriptions  
- Access medical history  

### 👨‍⚕️ Doctor Module
- View scheduled appointments  
- Add and manage prescriptions  
- Track patient treatment records  

### 🏢 Reception Module
- Monitor total patients and doctors  
- View today's appointments  
- Manage booking flow  

### 💰 Billing & Payments
- Generate bills automatically  
- Track payment status  
- Maintain transaction records  

### 💊 Pharmacy Module
- Medicine stock management  
- Prescription validation  
- Sales tracking  

### 📊 Admin Dashboard
- Role-based access control  
- System monitoring  
- Reports overview  
- User management  

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x  
- **Database:** SQLite (Development)  
- **Frontend:** HTML, CSS  
- **Authentication:** Django Authentication System  
- **Version Control:** Git & GitHub  

---

## 🏗️ Project Architecture

### Modular Django Apps
- `accounts`
- `patients`
- `doctors`
- `appointments`
- `billing`
- `Reception`
- `pharmacy`

### Key Backend Concepts Implemented
- Relational database modeling (ForeignKey, One-to-Many)
- Full CRUD operations
- Date-based filtering using Django timezone
- Role-based dashboard separation
- File handling (prescription downloads)
- Structured URL routing
- Session management and authentication
- QuerySet filtering and validation

---

## 📚 What I Learned

- Designing and managing relational databases  
- Storing and retrieving structured data efficiently  
- Implementing complete CRUD functionality  
- Managing sessions and user authentication  
- Handling role-based permissions  
- Building modular backend architecture  
- Debugging real-world workflow issues  

---

## 🔮 Future Enhancements

- Mobile application support  
- SMS / Email notifications  
- Online consultation (video integration)  
- AI-based health analytics  
- Insurance integration  
- Production deployment with MySQL/PostgreSQL  

---

## 📂 Project Structure

```bash
hms/
│
├── accounts/
├── patients/
├── doctors/
├── appointments/
├── billing/
├── Reception/
├── pharmacy/
│
├── templates/
├── static/
├── media/
│
└── manage.py
```

---

## ⚙️ Installation

```bash
git clone <your-repository-url>
cd hms

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Author

Roshan Pal 

B.Tech CSE | Full Stack Developer | Data Analyst

## ❤️ Show some love

⭐ If you found this project useful, consider giving it a star.
