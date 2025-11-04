 #!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Keanu", job = "architect"):
        self.job = job
        self.name = name

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job

    def validity(self, name):
       if((type(name) == str) and (1<= len(name) <=25)):
          self._name = name.title()
       else:
          print("Name must be string between 1 and 25 characters.")
    name = property(get_name, validity)

    def approval(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
           print("Job must be in list of approved jobs." )
    job = property(get_job, approval)


rooney = Person(name="Rooney")
rooney.validity("Rooney")
rooney.approval("Plumber")

