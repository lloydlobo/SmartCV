import json

print("Hello from SmartCV")

CV_NAME = "John Doe"
CV_EMAIL = "johndoe@example.com"

base_data = {
    "name": CV_NAME,
    "email": CV_EMAIL,
}

applications = []

for i in range(10):
    application = base_data.copy()
    application['summary'] = "todo"
    application['id'] = i
    applications.append(application)

print(json.dumps(applications, indent=2))
