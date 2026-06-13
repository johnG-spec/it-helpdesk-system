import datetime

# Mock database of IT support tickets
tickets = [
    {"id": 101, "issue": "Wi-Fi router in Lab 2 dropped connection", "category": "Networking", "priority": "High", "status": "Open"},
    {"id": 102, "issue": "User forgot Windows login password", "category": "Authentication", "priority": "Medium", "status": "Open"},
    {"id": 103, "issue": "Printer jamming constantly on 2nd floor", "category": "Hardware", "priority": "Low", "status": "Resolved"}
]

def display_menu():
    print("\n" + "="*35)
    print("   CAMPUS IT HELPDESK TICKETING")
    print("="*35)
    print("1. View All Active Tickets")
    print("2. Log a New IT Support Issue")
    print("3. Resolve an Existing Ticket")
    print("4. Exit System")
    print("="*35)

def view_tickets():
    print("\n--- CURRENT IT SUPPORT TICKETS ---")
    for t in tickets:
        print(f"[{t['status']}] Ticket #{t['id']} | Category: {t['category']} | Priority: {t['priority']}")
        print(f"    Details: {t['issue']}")
        print("-" * 35)

def log_ticket():
    print("\n--- LOG NEW IT SUPPORT ISSUE ---")
    issue = input("Enter a description of the technical issue: ")
    print("Select Category: 1. Networking  2. Hardware  3. Authentication  4. Software")
    cat_choice = input("Choice (1-4): ")
    categories = {"1": "Networking", "2": "Hardware", "3": "Authentication", "4": "Software"}
    category = categories.get(cat_choice, "General IT")
    
    print("Select Priority Level: 1. Low  2. Medium  3. High")
    pri_choice = input("Choice (1-3): ")
    priorities = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priorities.get(pri_choice, "Low")
    
    new_id = tickets[-1]["id"] + 1 if tickets else 101
    new_ticket = {
        "id": new_id,
        "issue": issue,
        "category": category,
        "priority": priority,
        "status": "Open"
    }
    tickets.append(new_ticket)
    print(f"\n[SUCCESS] Ticket #{new_id} successfully created and assigned to the IT queue.")

def resolve_ticket():
    view_tickets()
    try:
        t_id = int(input("\nEnter the Ticket ID you wish to mark as RESOLVED: "))
        for t in tickets:
            if t["id"] == t_id:
                t["status"] = "Resolved"
                print(f"\n[SUCCESS] Ticket #{t_id} status updated to RESOLVED.")
                return
        print("\n[ERROR] Ticket ID not found.")
    except ValueError:
        print("\n[ERROR] Invalid input. Please enter a valid numerical ID.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        if choice == "1":
            view_tickets()
        elif choice == "2":
            log_ticket()
        elif choice == "3":
            resolve_ticket()
        elif choice == "4":
            print("\nExiting IT Helpdesk System. Goodbye!")
            break
        else:
            print("\n[INVALID] Please select a valid option from 1 to 4.")

if __name__ == "__main__":
    main()
