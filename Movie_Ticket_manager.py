# Function to check seat availability
def is_seat_available(seats, seat_number):
    return seat_number not in seats


def movie_ticket():
    seats = {}

    while True:
        print("\n🎬 Movie Ticket Booking Application")
        print("1. Book a seat")
        print("2. View booked seats")
        print("3. Cancel a booking")
        print("4. Search booking")
        print("5. Exit")

        user = input("Enter your Choice (1-5): ")

        # ✅ Book Seat
        if user == '1':
            name = input("Enter your name: ")
            seat_number = input("Enter seat number: ")

            if is_seat_available(seats, seat_number):
                seats[seat_number] = name
                print(f"✅ Seat {seat_number} booked successfully for {name}.")
            else:
                print(f"❌ Sorry, seat {seat_number} is already booked.")

        # ✅ View Seats
        elif user == '2':
            if seats:
                print("\n📋 Booked Seats:")
                for seat_number, name in seats.items():
                    print(f"Seat {seat_number}: {name}")
            else:
                print("😒 No seats booked yet.")

        # ✅ Cancel Booking
        elif user == '3':
            cancel_seat = input("Enter seat number to cancel: ")
            if cancel_seat in seats:
                del seats[cancel_seat]
                print(f"✅ Booking for seat {cancel_seat} canceled successfully.")
            else:
                print("❌ Booking not found.")

        # ✅ Search Booking
        elif user == '4':
            search_seat = input("Enter seat number to search: ")
            if search_seat in seats:
                print(f"🔎 Seat {search_seat} is booked by {seats[search_seat]}.")
            else:
                print("❌ Booking not found.")

        # ✅ Exit
        elif user == '5':
            print("👋 Exiting Movie Ticket Booking Application.")
            break

        else:
            print("⚠️ Invalid choice. Please select 1-5.")


# Run program
movie_ticket()