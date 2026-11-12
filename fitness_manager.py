from storage import load_workouts, save_workouts


def add_workout(workout_date, exercise, duration, calories, notes):
    workouts = load_workouts()

    workout_id = max(
        [workout["id"] for workout in workouts],
        default=0
    ) + 1

    workout = {
        "id": workout_id,
        "date": workout_date,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        "notes": notes
    }

    workouts.append(workout)
    save_workouts(workouts)

    print("\nWorkout added successfully!")


def display_workouts(workouts):
    if not workouts:
        print("\nNo workout records found.")
        return

    print("\n" + "-" * 100)
    print(
        f"{'ID':<5} {'Date':<15} {'Exercise':<22} "
        f"{'Duration':<15} {'Calories':<12}"
    )
    print("-" * 100)

    for workout in workouts:
        print(
            f"{workout['id']:<5} "
            f"{workout['date']:<15} "
            f"{workout['exercise'][:21]:<22} "
            f"{str(workout['duration']) + ' min':<15} "
            f"{str(workout['calories']) + ' kcal':<12}"
        )

    print("-" * 100)


def view_workouts():
    display_workouts(load_workouts())


def search_workouts(keyword):
    workouts = load_workouts()
    keyword = keyword.lower()

    results = [
        workout for workout in workouts
        if keyword in workout["exercise"].lower()
        or keyword in workout["notes"].lower()
    ]

    display_workouts(results)


def filter_workouts_by_date(workout_date):
    workouts = load_workouts()

    results = [
        workout for workout in workouts
        if workout["date"] == workout_date
    ]

    display_workouts(results)


def update_workout(workout_id, workout_date, exercise,
                   duration, calories, notes):
    workouts = load_workouts()

    for workout in workouts:
        if workout["id"] == workout_id:
            workout["date"] = workout_date
            workout["exercise"] = exercise
            workout["duration"] = duration
            workout["calories"] = calories
            workout["notes"] = notes

            save_workouts(workouts)
            print("\nWorkout updated successfully!")
            return

    print("\nWorkout ID not found.")


def delete_workout(workout_id):
    workouts = load_workouts()

    updated_workouts = [
        workout for workout in workouts
        if workout["id"] != workout_id
    ]

    if len(updated_workouts) == len(workouts):
        print("\nWorkout ID not found.")
        return

    save_workouts(updated_workouts)
    print("\nWorkout deleted successfully.")


def show_statistics():
    workouts = load_workouts()

    if not workouts:
        print("\nNo workout data available.")
        return

    total_workouts = len(workouts)

    total_duration = sum(
        workout["duration"] for workout in workouts
    )

    total_calories = sum(
        workout["calories"] for workout in workouts
    )

    average_duration = total_duration / total_workouts

    exercise_counts = {}

    for workout in workouts:
        exercise = workout["exercise"]

        exercise_counts[exercise] = (
            exercise_counts.get(exercise, 0) + 1
        )

    popular_exercise = max(
        exercise_counts,
        key=exercise_counts.get
    )

    print("\n========== FITNESS STATISTICS ==========")
    print(f"Total Workouts: {total_workouts}")
    print(f"Total Duration: {total_duration:g} minutes")
    print(f"Total Estimated Calories: {total_calories:g} kcal")
    print(f"Average Workout Duration: {average_duration:.2f} minutes")
    print(f"Most Practiced Exercise: {popular_exercise}")
    print("========================================")
