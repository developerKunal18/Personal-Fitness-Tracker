from storage import initialize_storage

from fitness_manager import (
    add_workout,
    view_workouts,
    search_workouts,
    filter_workouts_by_date,
    update_workout,
    delete_workout,
    show_statistics
)

from utils import (
    get_valid_date,
    get_valid_number,
    get_valid_id
)


def display_menu():
    print("\n========== PERSONAL FITNESS TRACKER ==========")
    print("1. Add Workout")
    print("2. View All Workouts")
    print("3. Search Workout")
    print("4. Filter Workouts by Date")
    print("5. Update Workout")
    print("6. Delete Workout")
    print("7. Fitness Statistics")
    print("8. Exit")
    print("===============================================")


def get_workout_details():
    workout_date = get_valid_date(
        "Enter workout date (YYYY-MM-DD): "
    )

    exercise = input("Enter exercise name: ").strip()

    duration = get_valid_number(
        "Enter workout duration in minutes: ",
        minimum=0.1
    )

    calories = get_valid_number(
        "Enter estimated calories burned: ",
        minimum=0
    )

    notes = input("Enter workout notes: ").strip()

    if not exercise:
        print("Exercise name cannot be empty.")
        return None

    return workout_date, exercise, duration, calories, notes


def main():
    initialize_storage()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            details = get_workout_details()

            if details:
                add_workout(*details)

        elif choice == "2":
            view_workouts()

        elif choice == "3":
            keyword = input(
                "Enter exercise name or notes keyword: "
            ).strip()

            search_workouts(keyword)

        elif choice == "4":
            workout_date = get_valid_date(
                "Enter date (YYYY-MM-DD): "
            )

            filter_workouts_by_date(workout_date)

        elif choice == "5":
            workout_id = get_valid_id(
                "Enter workout ID to update: "
            )

            details = get_workout_details()

            if details:
                update_workout(workout_id, *details)

        elif choice == "6":
            workout_id = get_valid_id(
                "Enter workout ID to delete: "
            )

            delete_workout(workout_id)

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Thank you for using Personal Fitness Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
