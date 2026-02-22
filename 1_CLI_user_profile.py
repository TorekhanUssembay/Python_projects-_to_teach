def get_name():
    while True:
        name = input("Your name, please: ").strip()
        if name:
            return name
        print("Name can not be empty!")

def get_age():
    while True:
        try:
            age = int(input("Youage, please: "))
            if 1 <= age <= 120:
                return age
            print("Age must be between 1 and 120")
        except ValueError:
            print("Age must be a number")

def get_city():
    while True:
        city = input("You city, please: ")
        if city:
            return city
        print("City name can not be empty")

def get_job_title():
    while True:
        job_title = input("You job title, please: ")
        if job_title:
            return job_title
        print("Job title can not be empty")

def get_experience():
    while True:
        try:
            experience = int(input("Your experience, please: "))
            if experience >= 0:
                return experience
            print("Experince must be number and can not be empty")
        except ValueError:
            print("Experince mus be a number")

def display_user(name, age, city, job_title, experience, status):
    print("\n====================================")
    print("           EMPLOYEE PROFILE")
    print("====================================")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {city}")
    print(f"Position: {job_title}")
    print(f"Experience: {experience} years")
    print("------------------------------------")
    print(f"Status: {status}")
    print("====================================")

def determine_status(experience):
    if experience < 2:
        return "Junior"
    elif 2 <= experience <= 5:
        return "Middle level"
    else:
        return "Senior"

def main():

     name = get_name()
     age = get_age()
     city = get_city()
     job_title = get_job_title()
     experience = get_experience()

     status = determine_status(experience)

     display_user(name, age, city, job_title, experience, status)

if __name__ == "__main__":
    main()