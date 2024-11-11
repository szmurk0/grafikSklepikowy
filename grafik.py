import random

DAYS = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]
POSITIONS = ["Hotdog", "Bułki", "Kasa"]

workers = []

def add_worker():
    name = input("Podaj imię i nazwisko pracownika: ")
    days_positions = {}
    for day in DAYS:
        selected_positions = input(f"Na jakie pozycje {name} chce się zapisać w {day} (oddziel przecinkami lub zostaw puste, jeśli brak): ")
        if selected_positions:
            days_positions[day] = [position.strip() for position in selected_positions.split(",")]
    workers.append({
        "name": name,
        "days_positions": days_positions
    })

schedule = {day: {position: None for position in POSITIONS} for day in DAYS}

def assign_workers():
    for worker in workers:
        for day, available_positions in worker["days_positions"].items():
            free_positions = [pos for pos in available_positions if schedule[day][pos] is None]
            if free_positions:
                position = random.choice(free_positions)
                schedule[day][position] = worker["name"]

def display_schedule():
    for day, positions in schedule.items():
        print(f"{day}:")
        for position, worker in positions.items():
            print(f"  {position}: {worker if worker else 'Brak przydziału'}")
        print()

while True:
    add_worker()
    cont = input("Czy chcesz dodać kolejnego pracownika? (tak/nie): ")
    if cont.lower() != "tak":
        break

assign_workers()
display_schedule()
