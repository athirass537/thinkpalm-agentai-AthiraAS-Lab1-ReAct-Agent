
def get_car_price(make, model, year, km_driven):
    # Expanded mock logic for more makes/models
    base_prices = {
        ('Hyundai', 'i20'): 600000, ('Hyundai', 'Creta'): 900000,
        ('Maruti', 'Swift'): 550000, ('Maruti', 'Baleno'): 650000,
        ('Honda', 'City'): 700000, ('Honda', 'Amaze'): 600000,
        ('Toyota', 'Innova'): 1200000, ('Toyota', 'Etios'): 700000,
        ('Ford', 'Ecosport'): 800000, ('Ford', 'Figo'): 500000,
    }
    price = base_prices.get((make.title(), model.title()), 500000)
    try:
        age = 2026 - int(year)
    except Exception:
        age = 5
    try:
        km = int(km_driven)
    except Exception:
        km = 50000
    depreciation = age * 0.07 * price
    km_penalty = (km // 10000) * 0.03 * price
    estimated_price = max(100000, price - depreciation - km_penalty)
    return f"Estimated price is ₹{estimated_price/100000:.1f} lakhs."

def find_nearest_branch(city):
    branches = {
        'Chennai': 'Anna Nagar', 'Bangalore': 'Koramangala', 'Delhi': 'Connaught Place',
        'Mumbai': 'Andheri', 'Pune': 'Baner', 'Hyderabad': 'Banjara Hills',
        'Kolkata': 'Salt Lake', 'Ahmedabad': 'Navrangpura', 'Jaipur': 'Malviya Nagar',
    }
    return f"Nearest branch is {branches.get(city.title(), 'Main Branch')}."

def book_inspection_slot(date, time):
    return f"Inspection slot booked for {date} at {time}."

def answer_faq(question):
    faqs = {'documents': 'You need RC, insurance, and ID proof.', 'payment': 'Payment is made instantly after sale.', 'inspection': 'Inspection takes about 30 minutes.'}
    for key, value in faqs.items():
        if key in question.lower():
            return value
    return "Sorry, I don't have an answer for that FAQ."

# Minimal interactive agent for old car resale

import re

# Known values for better extraction
KNOWN_MAKES = ['Hyundai', 'Maruti', 'Honda', 'Toyota', 'Ford']
KNOWN_MODELS = ['i20', 'Creta', 'Swift', 'Baleno', 'City', 'Amaze', 'Innova', 'Etios', 'Ecosport', 'Figo']
KNOWN_CITIES = ['Chennai', 'Bangalore', 'Delhi', 'Mumbai', 'Pune', 'Hyderabad', 'Kolkata', 'Ahmedabad', 'Jaipur']


class InteractiveReActAgent:
    def __init__(self):
        self.slots = {}
        self.last_action = None

    def reset(self):
        self.slots = {}
        self.last_action = None

    def extract_info(self, user_input):
        # Make
        if not self.slots.get("make"):
            for make in KNOWN_MAKES:
                if make.lower() in user_input.lower():
                    self.slots["make"] = make
                    break
        # Model
        if not self.slots.get("model"):
            for model in KNOWN_MODELS:
                if model.lower() in user_input.lower():
                    self.slots["model"] = model
                    break
        # Year
        if not self.slots.get("year"):
            m = re.search(r'(19|20)\d{2}', user_input)
            if m:
                self.slots["year"] = m.group(0)
        # KM Driven
        if not self.slots.get("km_driven"):
            m = re.search(r'(\d{4,7})(?: ?km)?', user_input)
            if m:
                self.slots["km_driven"] = m.group(1)
        # City
        if not self.slots.get("city"):
            for city in KNOWN_CITIES:
                if city.lower() in user_input.lower():
                    self.slots["city"] = city
                    break

    def need_more_info(self):
        required = ["make", "model", "year", "km_driven", "city"]
        for r in required:
            if r not in self.slots:
                return r
        return None

    def ask_for_missing(self, missing):
        questions = {
            "make": "Which car make is it? (e.g., Hyundai, Maruti, Honda, Toyota, Ford)",
            "model": "What is the model? (e.g., i20, Swift, City, Creta, Baleno, Innova, etc.)",
            "year": "What is the year of manufacture? (e.g., 2018)",
            "km_driven": "How many kilometers has it been driven? (e.g., 45000)",
            "city": "Which city are you in? (e.g., Chennai, Bangalore, Delhi, Mumbai, etc.)",
        }
        return questions.get(missing, f"Please provide {missing}.")

    def handle_faq(self, user_input):
        faq_keywords = ["document", "payment", "inspection", "faq"]
        if any(word in user_input.lower() for word in faq_keywords):
            return answer_faq(user_input)
        return None

    def handle_booking(self):
        print("\nAI: Please provide a preferred date (YYYY-MM-DD) and time (e.g., 15:00) for your inspection slot.")
        date = input("Date: ")
        time = input("Time: ")
        confirmation = book_inspection_slot(date, time)
        print(f"AI: {confirmation}\nThank you! Our team will contact you soon.")

    def run_interactive(self):
        print("Welcome to the Old Car Resale AI Assistant!, Please help me with your car details?")
        self.reset()
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            # FAQ handling
            faq_response = self.handle_faq(user_input)
            if faq_response:
                print(f"AI: {faq_response}")
                continue

            # Info extraction
            self.extract_info(user_input)
            missing = self.need_more_info()
            if missing:
                print(self.ask_for_missing(missing))
                continue

            # All info collected, proceed
            make = self.slots["make"]
            model = self.slots["model"]
            year = self.slots["year"]
            km_driven = self.slots["km_driven"]
            city = self.slots["city"]
            price = get_car_price(make, model, year, km_driven)
            branch = find_nearest_branch(city)
            print(f"\nAI: Your {make} {model} ({year}) is estimated around {price.split('is ')[-1]}. The nearest inspection branch is {branch.split('is ')[-1]}. Would you like me to book an inspection slot? (yes/no)")
            self.last_action = "quoted"

            # Booking flow
            book_input = input("\nYou: ")
            if book_input.strip().lower() in ["yes", "y"]:
                self.handle_booking()
                self.reset()
            else:
                print("AI: Okay, let me know if you need anything else or want to book later.")
                self.reset()

if __name__ == "__main__":
    agent = InteractiveReActAgent()
    agent.run_interactive()
