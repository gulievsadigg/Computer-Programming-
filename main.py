# Carbon Footprint Monitoring Tool
# This tool calculates the carbon footprint based on user input of their energy usage, waste production, and business travel.

import json
from fpdf import FPDF

class CarbonCalculator:
    """A class to encapsulate the carbon footprint calculations and report generation."""
    
    def _init_(self):
        """Initialize the calculator with conversion factors."""
        # These factors could be more accurately determined in future research
        self.electricity_factor = 0.0005  # kgCO2 per euro spent on electricity
        self.gas_factor = 0.0053          # kgCO2 per euro spent on gas
        self.fuel_factor = 2.32           # kgCO2 per euro spent on transportation fuel
        self.waste_factor = 0.57          # kgCO2 per kg of waste
        self.travel_factor = 2.31         # kgCO2 per liter of fuel

    def get_input(self, prompt, input_type=float):
        """Safely get user input and convert to the specified type."""
        while True:
            try:
                return input_type(input(prompt))
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type._name_} value.")
    
    def calculate_footprint(self):
        """Gather user input and calculate the carbon footprint."""
        # Gather energy usage
        electricity_bill = self.get_input("Enter your average monthly electricity bill in euros: ")
        gas_bill = self.get_input("Enter your average monthly natural gas bill in euros: ")
        fuel_bill = self.get_input("Enter your average monthly fuel bill for transportation in euros: ")
        
        # Gather waste information
        waste_kg = self.get_input("Enter how much waste you generate per month in kilograms: ")
        recycle_percent = self.get_input("Enter how much of that waste is recycled or composted (in percentage): ")
        
        # Gather business travel information
        km_year = self.get_input("Enter how many kilometers your employees travel per year for business purposes: ")
        fuel_efficiency = self.get_input("Enter the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers: ")

        # Perform calculations
        energy_co2 = (electricity_bill * self.electricity_factor + gas_bill * self.gas_factor + fuel_bill * self.fuel_factor) * 12
        waste_co2 = waste_kg * (self.waste_factor - (recycle_percent / 100)) * 12
        travel_co2 = km_year / 100 * fuel_efficiency * self.travel_factor

        # Sum and return the results
        total_co2 = energy_co2 + waste_co2 + travel_co2
        return {
            "energy_co2": energy_co2,
            "waste_co2": waste_co2,
            "travel_co2": travel_co2,
            "total_co2": total_co2
        }

# Report Generation using FPDF
class PDFReport(FPDF):
    def _init_(self, title='Carbon Footprint Report'):
        super()._init_()
        self.title = title

    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, self.title, 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_report_section(self, title, content):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(content)

def add_report_section(self, title, content):
    self.add_page()
    self.chapter_title(title)
    self.chapter_body(content)

def generate_report(data):
    """Generate a PDF report from the calculated data."""
    pdf = PDFReport()
    pdf.add_page()
    
    # Add the problem statement and importance of the issue
    problem_statement = "Carbon footprint directly impacts climate change. Reducing it is vital for environmental sustainability. This report analyzes the carbon footprint based on energy usage, waste production, and business travel."
    pdf.add_report_section('Problem Statement', problem_statement)
    
    # Add data analysis
    analysis = (
        f"Energy Usage CO2: {data['energy_co2']:.2f} kg\n"
        f"Waste Production CO2: {data['waste_co2']:.2f} kg\n"
        f"Business Travel CO2: {data['travel_co2']:.2f} kg\n"
        f"Total CO2 Footprint: {data['total_co2']:.2f} kg"
    )
    pdf.add_report_section('Analysis Summary', analysis)
    
    # Add conclusions and suggestions
    conclusions = (
        "Conclusions and suggestions for future work will involve "
        "optimization of resource usage, investment in renewable energy, "
        "and promoting recycling and waste management programs to reduce "
        "the overall carbon footprint."
    )
    pdf.add_report_section('Conclusions and Suggestions', conclusions)
    
    # Save the PDF to a file
    pdf.output('carbon_footprint_report.pdf')

def main():
    calculator = CarbonCalculator()
    footprint_data = calculator.calculate_footprint()
    
    # Generate report with the footprint data
    generate_report(footprint_data)

    print("The carbon footprint has been calculated and the report has been generated.")

if _name_ == "_main_":
    main()
