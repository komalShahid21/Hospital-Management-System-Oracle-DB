import customtkinter as ctk
import oracledb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class HospitalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KMD Hospital - Patient Management System")
        self.geometry("720x700")
        self.resizable(False, False)

        header = ctk.CTkFrame(self, height=70, fg_color="#025784")
        header.pack(fill="x")
        title_label = ctk.CTkLabel(header, text="KMD Hospital - Patient Management System",
                                   font=("Arial", 22, "bold"), text_color="white")
        title_label.place(relx=0.5, rely=0.5, anchor="center")

        self.tabview = ctk.CTkTabview(self, width=680, height=460, fg_color="#D3D3D3")
        self.tabview.pack(pady=15)

        self.patient_tab = self.tabview.add("Patient Info")
        self.doctor_tab = self.tabview.add("Doctor Registry")
        self.appointment_tab = self.tabview.add("Appointments")
        self.doctor_count_tab = self.tabview.add("Doctor Count")

        self.build_patient_tab()
        self.build_doctor_tab()
        self.build_appointment_tab()
        self.build_doctor_count_tab()

    def build_patient_tab(self):
        title = ctk.CTkLabel(self.patient_tab, text="Patient Registration",
                             font=("Calibri", 20, "bold"), text_color="#004d4d")
        title.pack(pady=12)

        form_container = ctk.CTkFrame(self.patient_tab, fg_color="#D3D3D3", corner_radius=12)
        form_container.pack(pady=10, padx=10)

        self.patient_patient_id = ctk.CTkEntry(form_container, placeholder_text="Patient ID",
                                               width=350, height=35, border_color="#025784")
        self.patient_patient_id.pack(pady=10)

        self.patient_first_name = ctk.CTkEntry(form_container, placeholder_text="First Name",
                                               width=350, height=35, border_color="#025784")
        self.patient_first_name.pack(pady=10)

        self.patient_last_name = ctk.CTkEntry(form_container, placeholder_text="Last Name",
                                              width=350, height=35, border_color="#025784")
        self.patient_last_name.pack(pady=10)

        self.patient_dob = ctk.CTkEntry(form_container, placeholder_text="DOB (YYYY-MM-DD)",
                                        width=350, height=35, border_color="#025784")
        self.patient_dob.pack(pady=10)

        self.patient_gender = ctk.CTkEntry(form_container, placeholder_text="Gender",
                                           width=350, height=35, border_color="#025784")
        self.patient_gender.pack(pady=10)

        self.patient_contact = ctk.CTkEntry(form_container, placeholder_text="Contact Number",
                                            width=350, height=35, border_color="#025784")
        self.patient_contact.pack(pady=10)

        self.patient_email = ctk.CTkEntry(form_container, placeholder_text="Email",
                                          width=350, height=35, border_color="#025784")
        self.patient_email.pack(pady=10)

        submit_button = ctk.CTkButton(self.patient_tab, text="Create Patient",
                                      command=self.create_patient, font=("Arial", 14, "bold"),
                                      fg_color="#006666", hover_color="#025784", width=250)
        submit_button.pack(pady=15)

        self.patient_output = ctk.CTkLabel(self.patient_tab, text="", font=("Arial", 13))
        self.patient_output.pack(pady=5)

    def build_doctor_tab(self):
        title = ctk.CTkLabel(self.doctor_tab, text="Register New Doctor",
                             font=("Calibri", 20, "bold"), text_color="#004d4d")
        title.pack(pady=12)

        form_container = ctk.CTkFrame(self.doctor_tab, fg_color="#D3D3D3", corner_radius=12)
        form_container.pack(pady=10, padx=10)

        self.doctor_doctor_id = ctk.CTkEntry(form_container, placeholder_text="Doctor ID",
                                             width=350, height=35, border_color="#025784")
        self.doctor_doctor_id.pack(pady=10)

        self.doctor_first_name = ctk.CTkEntry(form_container, placeholder_text="First Name",
                                              width=350, height=35, border_color="#025784")
        self.doctor_first_name.pack(pady=10)

        self.doctor_last_name = ctk.CTkEntry(form_container, placeholder_text="Last Name",
                                             width=350, height=35, border_color="#025784")
        self.doctor_last_name.pack(pady=10)

        self.doctor_specialization = ctk.CTkEntry(form_container, placeholder_text="Specialization",
                                                  width=350, height=35, border_color="#025784")
        self.doctor_specialization.pack(pady=10)

        self.doctor_contact = ctk.CTkEntry(form_container, placeholder_text="Contact Number",
                                           width=350, height=35, border_color="#025784")
        self.doctor_contact.pack(pady=10)

        submit_button = ctk.CTkButton(self.doctor_tab, text="Submit Doctor Info",
                                      command=self.create_doctor, font=("Arial", 14, "bold"),
                                      fg_color="#006666", hover_color="#025784", width=250)
        submit_button.pack(pady=15)

        self.doctor_output = ctk.CTkLabel(self.doctor_tab, text="", font=("Arial", 13))
        self.doctor_output.pack(pady=5)

    def build_appointment_tab(self):
        title = ctk.CTkLabel(self.appointment_tab, text="Create Appointment",
                             font=("Calibri", 20, "bold"), text_color="#004d4d")
        title.pack(pady=12)

        form_container = ctk.CTkFrame(self.appointment_tab, fg_color="#D3D3D3", corner_radius=12)
        form_container.pack(pady=10, padx=10)

        self.appointment_Appointment_id = ctk.CTkEntry(form_container, placeholder_text="Appointment ID",
                                                       width=350, height=35, border_color="#025784")
        self.appointment_Appointment_id.pack(pady=10)

        self.appointment_patient_id = ctk.CTkEntry(form_container, placeholder_text="Patient ID",
                                                   width=350, height=35, border_color="#025784")
        self.appointment_patient_id.pack(pady=10)

        self.appointment_doctor_id = ctk.CTkEntry(form_container, placeholder_text="Doctor ID",
                                                  width=350, height=35, border_color="#025784")
        self.appointment_doctor_id.pack(pady=10)

        self.appointment_date = ctk.CTkEntry(form_container, placeholder_text="Appointment Date (YYYY-MM-DD)",
                                             width=350, height=35, border_color="#025784")
        self.appointment_date.pack(pady=10)

        self.appointment_reason = ctk.CTkEntry(form_container, placeholder_text="Reason for Visit",
                                               width=350, height=35, border_color="#025784")
        self.appointment_reason.pack(pady=10)

        submit_button = ctk.CTkButton(self.appointment_tab, text="Create Appointment",
                                      command=self.create_appointment, font=("Arial", 14, "bold"),
                                      fg_color="#006666", hover_color="#025784", width=250)
        submit_button.pack(pady=15)

        self.appointment_output = ctk.CTkLabel(self.appointment_tab, text="", font=("Arial", 13))
        self.appointment_output.pack(pady=5)

    def build_doctor_count_tab(self):
        title = ctk.CTkLabel(self.doctor_count_tab, text="Doctor Count by Specialization",
                             font=("Calibri", 20, "bold"), text_color="#004d4d")
        title.pack(pady=12)

        self.doctor_count_output = ctk.CTkTextbox(self.doctor_count_tab, width=650, height=340,
                                                  fg_color="#2F2E2E", corner_radius=12)
        self.doctor_count_output.pack(pady=10)

        refresh_button = ctk.CTkButton(self.doctor_count_tab, text="Refresh Count",
                                       command=self.load_doctor_count, font=("Arial", 14, "bold"),
                                       fg_color="#006666", hover_color="#025784", width=150)
        refresh_button.pack(pady=5)

        self.load_doctor_count()

    def load_doctor_count(self):
        connection = None
        try:
            connection = oracledb.connect(user="KMD_USER", password="kmd123", dsn="localhost:1521/freepdb1")
            cursor = connection.cursor()
            cursor.execute("SELECT SPECIALIZATION, COUNT(*) FROM DOCTORS_AT_KMD_HOSPITAL GROUP BY SPECIALIZATION ORDER BY SPECIALIZATION")
            rows = cursor.fetchall()
            self.doctor_count_output.delete("0.0", ctk.END)
            for row in rows:
                self.doctor_count_output.insert(ctk.END, f"{row[0]}: {row[1]}\n")
        except oracledb.Error as e:
            self.doctor_count_output.delete("0.0", ctk.END)
            self.doctor_count_output.insert(ctk.END, f"Error: {e}")
        finally:
            if connection:
                connection.close()

    def create_patient(self):
        if not self.validate_patient_input():
            return
        connection = None
        try:
            connection = oracledb.connect(user="KMD_USER", password="kmd123", dsn="localhost:1521/freepdb1")
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO PATIENTS_AT_KMD_HOSPITAL
                (PATIENT_ID, FIRST_NAME, LAST_NAME, DOB, GENDER, CONTACT_NUMBER, EMAIL)
                VALUES (:patient_id, :first_name, :last_name, TO_DATE(:dob, 'YYYY-MM-DD'), :gender, :contact, :email)
            """, {
                'patient_id': int(self.patient_patient_id.get()),
                'first_name': self.patient_first_name.get(),
                'last_name': self.patient_last_name.get(),
                'dob': self.patient_dob.get(),
                'gender': self.patient_gender.get(),
                'contact': self.patient_contact.get(),
                'email': self.patient_email.get()
            })
            connection.commit()
            self.patient_output.configure(text="Patient added successfully!", text_color="green")
            self.clear_patient_fields()
        except oracledb.Error as e:
            self.patient_output.configure(text=f"Error: {e}", text_color="red")
        except ValueError:
            self.patient_output.configure(text="Patient ID must be a valid number.", text_color="red")
        finally:
            if connection:
                connection.close()

    def clear_patient_fields(self):
        self.patient_patient_id.delete(0, ctk.END)
        self.patient_first_name.delete(0, ctk.END)
        self.patient_last_name.delete(0, ctk.END)
        self.patient_dob.delete(0, ctk.END)
        self.patient_gender.delete(0, ctk.END)
        self.patient_contact.delete(0, ctk.END)
        self.patient_email.delete(0, ctk.END)

    def validate_patient_input(self):
        try:
            int(self.patient_patient_id.get())
        except ValueError:
            self.patient_output.configure(text="Patient ID must be a number.", text_color="red")
            return False
        if not self.patient_first_name.get() or not self.patient_last_name.get() or not self.patient_contact.get():
            self.patient_output.configure(text="Fill required fields (Patient ID, First Name, Last Name, Contact).", text_color="red")
            return False
        return True

    def create_doctor(self):
        if not self.validate_doctor_input():
            return
        connection = None
        try:
            connection = oracledb.connect(user="KMD_USER", password="kmd123", dsn="localhost:1521/freepdb1")
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO DOCTORS_AT_KMD_HOSPITAL
                (DOCTOR_ID, FIRST_NAME, LAST_NAME, SPECIALIZATION, CONTACT_NUMBER)
                VALUES (:doctor_id, :first_name, :last_name, :specialization, :contact)
            """, {
                'doctor_id': int(self.doctor_doctor_id.get()),
                'first_name': self.doctor_first_name.get(),
                'last_name': self.doctor_last_name.get(),
                'specialization': self.doctor_specialization.get(),
                'contact': self.doctor_contact.get()
            })
            connection.commit()
            self.doctor_output.configure(text="Doctor added successfully!", text_color="green")
            self.clear_doctor_fields()
            self.load_doctor_count()
        except oracledb.Error as e:
            self.doctor_output.configure(text=f"Error: {e}", text_color="red")
        except ValueError:
            self.doctor_output.configure(text="Doctor ID must be a valid number.", text_color="red")
        finally:
            if connection:
                connection.close()

    def clear_doctor_fields(self):
        self.doctor_doctor_id.delete(0, ctk.END)
        self.doctor_first_name.delete(0, ctk.END)
        self.doctor_last_name.delete(0, ctk.END)
        self.doctor_specialization.delete(0, ctk.END)
        self.doctor_contact.delete(0, ctk.END)

    def validate_doctor_input(self):
        try:
            int(self.doctor_doctor_id.get())
        except ValueError:
            self.doctor_output.configure(text="Doctor ID must be a number.", text_color="red")
            return False
        if not self.doctor_first_name.get() or not self.doctor_last_name.get() or not self.doctor_contact.get():
            self.doctor_output.configure(text="Fill required fields (Doctor ID, First Name, Last Name, Contact).", text_color="red")
            return False
        return True

    def create_appointment(self):
        if not self.validate_appointment_input():
            return
        connection = None
        try:
            connection = oracledb.connect(user="KMD_USER", password="kmd123", dsn="localhost:1521/freepdb1")
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO APPOINTMENTS_AT_KMD_HOSPITAL
                (APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, REASON_FOR_VISIT)
                VALUES (:appointment_id, :patient_id, :doctor_id, TO_DATE(:appointment_date, 'YYYY-MM-DD'), :reason)
            """, {
                'appointment_id': int(self.appointment_Appointment_id.get()),
                'patient_id': int(self.appointment_patient_id.get()),
                'doctor_id': int(self.appointment_doctor_id.get()),
                'appointment_date': self.appointment_date.get(),
                'reason': self.appointment_reason.get()
            })
            connection.commit()
            self.appointment_output.configure(text="Appointment created successfully!", text_color="green")
            self.clear_appointment_fields()
        except oracledb.Error as e:
            self.appointment_output.configure(text=f"Error: {e}", text_color="red")
        except ValueError:
            self.appointment_output.configure(text="IDs must be valid numbers.", text_color="red")
        finally:
            if connection:
                connection.close()

    def clear_appointment_fields(self):
        self.appointment_Appointment_id.delete(0, ctk.END)
        self.appointment_patient_id.delete(0, ctk.END)
        self.appointment_doctor_id.delete(0, ctk.END)
        self.appointment_date.delete(0, ctk.END)
        self.appointment_reason.delete(0, ctk.END)

    def validate_appointment_input(self):
        try:
            int(self.appointment_Appointment_id.get())
            int(self.appointment_patient_id.get())
            int(self.appointment_doctor_id.get())
        except ValueError:
            self.appointment_output.configure(text="Appointment ID, Patient ID, and Doctor ID must be numbers.", text_color="red")
            return False
        if not self.appointment_patient_id.get() or not self.appointment_doctor_id.get() or not self.appointment_date.get():
            self.appointment_output.configure(text="Fill required fields (Appointment ID, Patient ID, Doctor ID, Date).", text_color="red")
            return False
        return True


if __name__ == "__main__":
    app = HospitalApp()
    app.mainloop()