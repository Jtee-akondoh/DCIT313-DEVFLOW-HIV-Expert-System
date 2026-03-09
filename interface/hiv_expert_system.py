from pyswip import Prolog
import os

class HIVExpertSystem:
    def __init__(self):
        """Initialize the expert system and load the knowledge base"""
        self.prolog = Prolog()
        
        # Get the path to the knowledge base file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        kb_path = os.path.join(current_dir, '..', 'knowledge_base', 'hiv_knowledge.pl')
        
        # Load the knowledge base
        self.prolog.consult(kb_path)
        print("=" * 60)
        print("    HIV/AIDS EXPERT SYSTEM - Knowledge Base Loaded")
        print("=" * 60)
        
        # Clear any existing dynamic facts
        self.reset_facts()
    
    def reset_facts(self):
        """Clear all dynamic facts from previous sessions"""
        list(self.prolog.query("retractall(has_risk_factor(_))"))
        list(self.prolog.query("retractall(user_symptom(_))"))
        list(self.prolog.query("retractall(knows_partner_status)"))
        list(self.prolog.query("retractall(uses_protection)"))
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("1. Get Information about HIV/AIDS")
        print("2. Assess Your Risk Level")
        print("3. Check Symptoms")
        print("4. Frequently Asked Questions")
        print("5. Exit")
        print("-" * 50)
    
    def get_information(self):
        """Provide information about various HIV/AIDS topics"""
        print("\n" + "=" * 50)
        print("INFORMATION CENTER")
        print("=" * 50)
        print("What would you like to know about?")
        print("1. HIV Transmission")
        print("2. Prevention Methods")
        print("3. Symptoms")
        print("4. Treatment Options")
        print("5. Testing Information")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        topic_map = {
            '1': 'transmission',
            '2': 'prevention',
            '3': 'symptoms',
            '4': 'treatment',
            '5': 'testing'
        }
        
        if choice in topic_map:
            # Query Prolog for information
            query = list(self.prolog.query(f"provide_information({topic_map[choice]}, Info)"))
            if query:
                print("\n" + "-" * 50)
                print(query[0]['Info'])
                print("-" * 50)
            input("\nPress Enter to continue...")
        elif choice == '6':
            return
        else:
            print("Invalid choice. Please try again.")
    
    def assess_risk(self):
        """Interactive risk assessment"""
        print("\n" + "=" * 50)
        print("RISK ASSESSMENT")
        print("=" * 50)
        print("Please answer the following questions honestly:")
        print("(Answer 'y' for yes, 'n' for no)")
        print("-" * 50)
        
        # Reset previous risk factors
        list(self.prolog.query("retractall(has_risk_factor(_))"))
        list(self.prolog.query("retractall(knows_partner_status)"))
        list(self.prolog.query("retractall(uses_protection)"))
        
        # Collect risk factors
        questions = [
            ("Have you had unprotected sex in the last 6 months?", "unprotected_sex"),
            ("Do you have multiple sexual partners?", "multiple_partners"),
            ("Have you ever shared needles for drug use?", "shared_needles"),
            ("Did you receive a blood transfusion before 1985?", "blood_transfusion_before_1985"),
        ]
        
        for question, factor in questions:
            response = input(f"{question} (y/n): ").strip().lower()
            if response == 'y':
                self.prolog.assertz(f"has_risk_factor({factor})")
        
        # Additional questions for more accurate assessment
        response = input("Do you always use protection during sex? (y/n): ").strip().lower()
        if response == 'y':
            self.prolog.assertz("uses_protection")
        
        response = input("Do you know your partner's HIV status? (y/n): ").strip().lower()
        if response == 'y':
            self.prolog.assertz("knows_partner_status")
        
        # Query risk level
        query = list(self.prolog.query("risk_level(Level)"))
        
        print("\n" + "=" * 50)
        print("RISK ASSESSMENT RESULT")
        print("=" * 50)
        
        if query:
            level = query[0]['Level']
            if level == 'high':
                print("⚠️  HIGH RISK: You should get tested immediately.")
                print("   Consider taking PEP (Post-Exposure Prophylaxis) within 72 hours.")
                print("   Contact your healthcare provider right away.")
            elif level == 'medium':
                print("⚠️  MEDIUM RISK: You should consider getting tested.")
                print("   Practice safer sex and talk to your healthcare provider.")
            elif level == 'low':
                print("✅ LOW RISK: Continue practicing safe behaviors.")
                print("   Regular testing is still recommended.")
            else:
                print("Unable to determine risk level. Please consult a healthcare provider.")
        else:
            print("Unable to determine risk level with the information provided.")
        
        input("\nPress Enter to continue...")
    
    def check_symptoms(self):
        """Symptom checker"""
        print("\n" + "=" * 50)
        print("SYMPTOM CHECKER")
        print("=" * 50)
        print("Please answer 'y' for symptoms you're experiencing:")
        print("-" * 50)
        
        # Reset previous symptoms
        list(self.prolog.query("retractall(user_symptom(_))"))
        
        # List of early symptoms to check
        early_symptoms = [
            ("fever", "Fever"),
            ("headache", "Headache"),
            ("fatigue", "Unexplained fatigue"),
            ("swollen_lymph_nodes", "Swollen lymph nodes"),
            ("sore_throat", "Sore throat"),
            ("rash", "Skin rash")
        ]
        
        early_count = 0
        for symptom_code, symptom_name in early_symptoms:
            response = input(f"{symptom_name}? (y/n): ").strip().lower()
            if response == 'y':
                self.prolog.assertz(f"user_symptom({symptom_code})")
                early_count += 1
        
        # Check for late symptoms
        late_symptoms = [
            ("rapid_weight_loss", "Rapid weight loss"),
            ("recurring_fever", "Recurring fever"),
            ("night_sweats", "Night sweats"),
            ("extreme_fatigue", "Extreme fatigue"),
            ("prolonged_swelling_lymph_nodes", "Prolonged swelling of lymph nodes"),
            ("diarrhea_more_than_week", "Diarrhea lasting more than a week"),
            ("sores_mouth_anus_genitals", "Sores in mouth/anus/genitals"),
            ("pneumonia", "Pneumonia"),
            ("memory_loss", "Memory loss")
        ]
        
        late_found = False
        for symptom_code, symptom_name in late_symptoms:
            response = input(f"{symptom_name}? (y/n): ").strip().lower()
            if response == 'y':
                self.prolog.assertz(f"user_symptom({symptom_code})")
                late_found = True
        
        print("\n" + "=" * 50)
        print("SYMPTOM CHECKER RESULTS")
        print("=" * 50)
        
        if late_found:
            print("⚠️  You reported some symptoms that can occur in later stages of HIV.")
            print("   This doesn't mean you have HIV, but you should see a doctor promptly.")
            print("   Many of these symptoms can be caused by other conditions.")
        elif early_count >= 3:
            print("⚠️  You reported multiple symptoms that can occur during early HIV infection.")
            print("   If you've had possible exposure, consider getting tested.")
            print("   These symptoms can also be caused by other viral infections.")
        elif early_count > 0:
            print("ℹ️  You reported some symptoms that can occur with HIV.")
            print("   However, these are common symptoms that can be caused by many conditions.")
            print("   If concerned, consult a healthcare provider.")
        else:
            print("✅ You didn't report any symptoms commonly associated with HIV.")
            print("   Remember: Many people with HIV have no symptoms for years.")
        
        print("\nIMPORTANT: These results are not a diagnosis.")
        print("Only an HIV test can confirm HIV status.")
        input("\nPress Enter to continue...")
    
    def faq(self):
        """Display frequently asked questions"""
        print("\n" + "=" * 50)
        print("FREQUENTLY ASKED QUESTIONS")
        print("=" * 50)
        
        faqs = [
            ("Q: How soon after exposure can HIV be detected?",
             "A: Most tests can detect HIV 2-4 weeks after exposure. The window period can be up to 3 months for some tests."),
            
            ("Q: Can I get HIV from kissing?",
             "A: No, HIV is not transmitted through saliva. Casual contact like kissing, hugging, or sharing food does not transmit HIV."),
            
            ("Q: Is there a cure for HIV?",
             "A: Currently, there is no cure for HIV, but it can be managed effectively with ART medication."),
            
            ("Q: What does U=U mean?",
             "A: Undetectable = Untransmittable. When a person with HIV maintains an undetectable viral load, they cannot transmit HIV to others."),
            
            ("Q: How accurate are HIV tests?",
             "A: Modern HIV tests are highly accurate (over 99% sensitivity and specificity) when done after the window period."),
            
            ("Q: Can I get HIV from oral sex?",
             "A: The risk is very low but not zero. Using barriers like condoms or dental dams reduces this risk."),
            
            ("Q: What should I do if I think I've been exposed?",
             "A: Contact a healthcare provider immediately. PEP medication can prevent infection if started within 72 hours.")
        ]
        
        for i, (question, answer) in enumerate(faqs, 1):
            print(f"\n{i}. {question}")
            print(f"   {answer}")
            print("-" * 40)
        
        input("\nPress Enter to continue...")
    
    def disclaimer(self):
        """Display medical disclaimer"""
        print("\n" + "!" * 60)
        print("MEDICAL DISCLAIMER")
        print("!" * 60)
        print("This expert system is for educational purposes only.")
        print("It is not a substitute for professional medical advice,")
        print("diagnosis, or treatment. Always seek the advice of your")
        print("physician or other qualified health provider with any")
        print("questions you may have regarding a medical condition.")
        print("!" * 60)
        input("\nPress Enter to acknowledge and continue...")
    
    def run(self):
        """Main program loop"""
        self.disclaimer()
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                self.get_information()
            elif choice == '2':
                self.assess_risk()
            elif choice == '3':
                self.check_symptoms()
            elif choice == '4':
                self.faq()
            elif choice == '5':
                print("\nThank you for using the HIV/AIDS Expert System.")
                print("Stay informed, stay safe!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    """Main function to run the expert system"""
    try:
        # Check if pyswip is installed
        import pyswip
    except ImportError:
        print("Error: pyswip library is not installed.")
        print("Please install it using: pip install pyswip")
        return
    
    # Create and run the expert system
    expert_system = HIVExpertSystem()
    expert_system.run()

if __name__ == "__main__":
    main()