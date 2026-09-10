# 🏥 KMD Hospital Management System (Oracle DB)

## 📌 Description
A desktop application built to manage hospital operations, including patient registration, doctor records, and appointment scheduling. It uses a robust Oracle Database backend for data integrity.

## 🛠️ Technologies Used
*   Python
*   CustomTkinter (for modern GUI)
*   Oracle Database (oracledb library)
*   SQL

## ✨ Key Features
*   **Patient Registration:** Add new patients with validated IDs, contact info, and DOB.
*   **Doctor Registry:** Maintain a database of doctors and their specializations.
*   **Appointment Scheduling:** Book appointments linking patients to specific doctors.
*   **Analytics:** View a dynamic count of doctors grouped by their specialization.
*   **Database Integration:** Uses primary keys, foreign keys, and sequences for efficient data handling.

## 🚀 How to Run
1. Execute the `database.sql` script in your Oracle SQL environment to create tables and sequences.
2. Install required Python libraries: `pip install customtkinter oracledb`.
3. Update the database connection credentials in `app.py` (user, password, dsn).
4. Run the application: `python app.py`.
