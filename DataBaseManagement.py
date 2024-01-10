class DataBaseManagement:

    def __init__(self, doctorFilePath, patientFilePath, drugFilePath):
        self.doctorFilePath = doctorFilePath
        self.patientFilePath = patientFilePath
        self.drugFilePath = drugFilePath

    def insert(self, choice):
        match int(choice):
            case 1:
                with open(self.doctorFilePath, 'a') as f:
                    print("please inter Doctor's name : ")
                    name = input()
                    print("please inter Doctor's phone number : ")
                    number = input()
                    print("please inter Doctor's email : ")
                    email = input()
                    print("please inter Doctor's address : ")
                    address = input()
                    final_string = f"{name}-{number}-{email}-{address};"
                    f.write(final_string)
            case 2:
                with open(self.drugFilePath, 'a') as f:
                    print("please inter Drug's name : ")
                    name = input()
                    print("please inter Drug's price : ")
                    price = input()
                    print("please inter related doctor : ")
                    related_patient = None
                    self.show_all_doctors()
                    related_doctor = input()
                    self.show_all_patients()
                    print("please inter related patient : ")
                    related_patient = input()

                    final_string = f"{name}-{price}-{related_doctor}-{related_patient};"
                    f.write(final_string)
            case 3:
                with open(self.patientFilePath, 'a') as f:
                    print("please inter Patient's name : ")
                    name = input()
                    print("please inter Patient's phone number : ")
                    number = input()
                    print("please inter Patient's email : ")
                    email = input()
                    print("please inter Patient's address : ")
                    address = input()
                    final_string = f"{name}-{number}-{email}-{address};"
                    f.write(final_string)

    def search(self, choice):
        match int(choice):
            case 1:
                with open(self.doctorFilePath, 'r') as f:
                    doctors = f.read().split(";")
                    print("please inter doctor's name")
                    name_input = input()
                    result_output = None
                    for doctor in doctors:
                        doctor_name = doctor.split("-")[0]
                        if doctor_name == name_input:
                            phone = doctor.split("-")[1]
                            email = doctor.split("-")[2]
                            address = doctor.split("-")[-1]
                            result_output = f"""
                                name : {doctor_name}
                                phone : {phone}
                                email : {email}
                                address : {address}
                            """
                    if result_output != None:
                        print(result_output)
                    else:
                        print("There is no doctor with this name")

            case 2:
                with open(self.drugFilePath,'r') as f:
                    drugs = f.read().split(";")
                    print("please inter patient's name")
                    name_input = input()
                    for drug in drugs:
                        if drug.split('-')[-1] == name_input:
                            print(drug[0])

            case 3:
                with open(self.patientFilePath, 'r') as f:
                    patients = f.read().split(";")
                    print("please inter patient's name")
                    name_input = input()
                    result_output = None
                    for patient in patients:
                        patient_name = patient.split("-")[0]
                        if patient_name == name_input:
                            phone = patient.split("-")[1]
                            email = patient.split("-")[2]
                            address = patient.split("-")[-1]
                            result_output = f"""
                                    name : {patient_name}
                                    phone : {phone}
                                    email : {email}
                                    address : {address}
                                """
                    if result_output != None:
                        print(result_output)
                    else:
                        print("There is no patient with this name")

    def update(self, choice):
        match int(choice):
            case 1:
                print("please inter doctor's name you want update")
                self.show_all_doctors()
                selected_name = input()
                f = open(self.doctorFilePath,'r')
                doctors = f.read().split(";")
                new_doctors = []
                for doctor in doctors:
                    if doctor.split('-')[0] == selected_name:
                        print("please inter new Doctor's name : ")
                        name = input()
                        print("please inter new Doctor's phone number : ")
                        number = input()
                        print("please inter new Doctor's email : ")
                        email = input()
                        print("please inter new Doctor's address : ")
                        address = input()
                        final_string = f"{name}-{number}-{email}-{address}"
                        new_doctors.append(final_string)
                    else:
                        new_doctors.append(doctor)

                f = open(self.doctorFilePath,'w')
                f.write(";".join(new_doctors))
                f.close()



            case 2:
                print("please inter patient's name you want update")
                self.show_all_patients()
                selected_name = input()
                f = open(self.patientFilePath, 'r')
                patients = f.read().split(";")
                new_patients = []
                for patient in patients:
                    if patient.split('-')[0] == selected_name:
                        print("please inter new patient's name : ")
                        name = input()
                        print("please inter new patient's phone number : ")
                        number = input()
                        print("please inter new patient's email : ")
                        email = input()
                        print("please inter new patient's address : ")
                        address = input()
                        final_string = f"{name}-{number}-{email}-{address}"
                        new_patients.append(final_string)
                    else:
                        new_patients.append(patient)

                f = open(self.patientFilePath, 'w')
                f.write(";".join(new_patients))
                f.close()

    def delete(self, choice):

        if int(choice) == 1:
            f = open(self.doctorFilePath, 'r')
            doctors = f.read().split(';')
            print("please inter doctor's name you want delete")
            self.show_all_doctors()
            selected_name = input()
            new_doctors = []
            for doctor in doctors:
                name_doc = doctor.split('-')[0]
                if name_doc != selected_name:
                    new_doctors.append(doctor)
            f = open(self.doctorFilePath, 'w')
            res_string = ";".join(new_doctors)
            f.write(res_string)
            f.close()
        elif int(choice) == 2:
            f = open(self.drugFilePath, 'r')
            drugs = f.read().split(";")
            print("please inter drug's name ")
            drug_name = input()
            print("please inter related patient's name")
            related_patient = input()
            new_drugs = []
            for drug in drugs:
                p = drug.split('-')[-1]
                n = drug.split('-')[0]
                if not (drug_name == n and related_patient == p):
                    new_drugs.append(drug)
                f = open(self.drugFilePath, 'w')
                res = ";".join(new_drugs)
                f.write(res)
                f.close()


        elif int(choice) == 3:
            f = open(self.patientFilePath, 'r')
            patients = f.read().split(';')
            print("please inter patient's name you want delete")
            self.show_all_patients()
            selected_name = input()
            new_patients = []
            for patient in patients:
                name_pati = patient.split('-')[0]
                if name_pati != selected_name:
                    new_patients.append(patient)
            f = open(self.patientFilePath, 'w')
            res_string = ";".join(new_patients)
            f.write(res_string)
            f.close()

    def show_all_doctors(self):
        with open(self.doctorFilePath, 'r') as f2:
            doctors = f2.read().split(";")
            counter = 1
            for doctor in doctors:
                name_doc = doctor.split('-')[0]
                if name_doc != "":
                    print(f"{counter}){name_doc}")
                counter += 1

    def show_all_patients(self):
        with open(self.patientFilePath, 'r') as f3:
            patients = f3.read().split(";")
            counter = 1
            for patient in patients:
                name_pat = patient.split('-')[0]
                if name_pat != "":
                    print(f"{counter}){name_pat}")
                counter += 1

    def show_all_drugs(self):
        with open(self.drugFilePath, 'r') as f:
            drugs = f.read().split(";")
            counter = 1
            for drug in drugs:
                drug_name = drug.split('-')[0]
                related_patients = drug.split('-')[-1]
                if drug_name != "":
                    print(f"{counter}) name : {drug_name}  related patient : {related_patients}")
                counter += 1
