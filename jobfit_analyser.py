from PIL import Image
import pytesseract

import re

class ResumeAnalyzer:
    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Define job requirements
        self.job_requirements = {
            'software developer': {
                'required_skills': ['python', 'java', 'javascript', 'sql', 'git'],
                'preferred_skills': ['react', 'docker', 'aws', 'agile'],
                'experience': 2,
                'education': ['computer science', 'software engineering', 'it'],
                'salary_range': '$70,000 - $120,000'
            },
            'data analyst': {
                'required_skills': ['python', 'sql', 'excel', 'statistics'],
                'preferred_skills': ['tableau', 'power bi', 'r', 'machine learning'],
                'experience': 1,
                'education': ['data science', 'statistics', 'mathematics'],
                'salary_range': '$60,000 - $100,000'
            }
        }

    def extract_text(self, file_path):

        try:
            print("Reading resume...")
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            return text.lower()
        except Exception as e:
            print(f"Error extracting text: {str(e)}")
            return None

    def analyze_resume(self, text, job_role):
        """Analyze resume for job role"""
        if not text or job_role not in self.job_requirements:
            return None

        requirements = self.job_requirements[job_role]
        analysis = {
            'required_skills': self.analyze_skills(text, requirements['required_skills']),
            'preferred_skills': self.analyze_skills(text, requirements['preferred_skills']),
            'experience': self.analyze_experience(text, requirements['experience']),
            'education': self.analyze_education(text, requirements['education']),
            'recommendations': []
        }

        # Calculate overall score
        analysis['score'] = self.calculate_score(analysis)

        # Generate recommendations
        self.generate_recommendations(analysis, requirements)

        return analysis

    def analyze_skills(self, text, skills):
        """Analyze skills present in resume"""
        found_skills = [skill for skill in skills if skill in text]
        return {
            'found': found_skills,
            'missing': [skill for skill in skills if skill not in found_skills],
            'score': (len(found_skills) / len(skills)) * 100 if skills else 0
        }

    def analyze_experience(self, text, required_years):
        """Extract years of experience"""
        experience_patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'experience\s*:\s*(\d+)\+?\s*years?'
        ]

        years = []
        for pattern in experience_patterns:
            matches = re.findall(pattern, text)
            years.extend([int(y) for y in matches])

        years_found = max(years) if years else 0
        return {
            'years': years_found,
            'meets_requirement': years_found >= required_years,
            'score': min((years_found / required_years) * 100, 100) if required_years > 0 else 0
        }

    def analyze_education(self, text, required_fields):
        """Analyze education requirements"""
        found_fields = [field for field in required_fields if field in text]
        return {
            'found': found_fields,
            'missing': [field for field in required_fields if field not in found_fields],
            'score': (len(found_fields) / len(required_fields)) * 100 if required_fields else 0
        }

    def calculate_score(self, analysis):
        """Calculate overall score"""
        weights = {
            'required_skills': 0.4,
            'experience': 0.3,
            'education': 0.2,
            'preferred_skills': 0.1
        }

        return sum(analysis[key]['score'] * weights[key]
                   for key in weights.keys())

    def generate_recommendations(self, analysis, requirements):
        """Generate recommendations based on analysis"""
        if analysis['required_skills']['missing']:
            analysis['recommendations'].append(
                f"Add these crucial skills: {', '.join(analysis['required_skills']['missing'])}"
            )

        if not analysis['experience']['meets_requirement']:
            analysis['recommendations'].append(
                f"Highlight more experience - role requires {requirements['experience']} years"
            )

        if analysis['education']['missing']:
            analysis['recommendations'].append(
                f"Add education in: {', '.join(analysis['education']['missing'])}"
            )


def main():
    analyzer = ResumeAnalyzer()

    print("=== Resume Analyzer ===")
    print("\nSupported roles:")
    for role in analyzer.job_requirements.keys():
        print(f"- {role}")

    # Get inputs
    file_path = input("\nEnter resume image path: ").strip('"')
    job_role = input("Enter target role: ").lower()

    # Analyze resume
    print("\nAnalyzing resume...")
    text = analyzer.extract_text(file_path)

    if text:
        analysis = analyzer.analyze_resume(text, job_role)
        if analysis:
            # Display results
            print("\n=== Analysis Results ===")
            print(f"\nOverall Match: {analysis['score']:.1f}%")

            print("\nSkills Analysis:")
            print("Required Skills Found:", ', '.join(analysis['required_skills']['found']))
            print("Preferred Skills Found:", ', '.join(analysis['preferred_skills']['found']))

            print(f"\nExperience: {analysis['experience']['years']} years")
            print(f"Required: {analyzer.job_requirements[job_role]['experience']} years")

            print("\nEducation Fields Found:", ', '.join(analysis['education']['found']))

            if analysis['recommendations']:
                print("\nRecommendations:")
                for i, rec in enumerate(analysis['recommendations'], 1):
                    print(f"{i}. {rec}")

            print(f"\nSalary Range: {analyzer.job_requirements[job_role]['salary_range']}")

        else:
            print("Analysis failed. Please check the job role and try again.")
    else:
        print("Failed to extract text from resume.")


if __name__ == "__main__":
    main()