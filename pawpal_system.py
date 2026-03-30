# "logic layer" where all your backend classes live

class Owner:
    def __init__(self, name, time_available, preferences):
        self.name = name
        self.time_available = time_available
        self.preferences = preferences
        self.pet = None       # Owner "1" --> "1" Pet
        self.tasks = []       # Owner "1" --> "*" Task

    def add_pet(self, pet):
        pass

    def get_summary(self):
        pass


class Pet:
    def __init__(self, name, species, age, health_notes):
        self.name = name
        self.species = species
        self.age = age
        self.health_notes = health_notes

    def get_profile(self):
        pass


class Task:
    def __init__(self, name, category, duration, priority, preferred_time):
        self.name = name
        self.category = category
        self.duration = duration
        self.priority = priority
        self.preferred_time = preferred_time

    def edit(self, field, value):
        pass

    def to_dict(self):
        pass


class Schedule:
    def __init__(self, date, tasks, total_duration, reasoning):
        self.date = date
        self.tasks = tasks
        self.total_duration = total_duration
        self.reasoning = reasoning

    def display(self):
        pass

    def get_reasoning(self):
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def generate_schedule(self):
        pass

    def explain_plan(self):
        pass
