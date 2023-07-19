class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

class Feedback:
    def __init__(self, student, feedback_text):
        self.student = student
        self.feedback_text = feedback_text
        self.instructor_response = None

class FeedbackSystem:
    def __init__(self):
        self.feedback_list = []

    def submit_feedback(self, student, feedback_text):
        feedback = Feedback(student, feedback_text)
        self.feedback_list.append(feedback)

    def view_feedbacks(self):
        for index, feedback in enumerate(self.feedback_list, 1):
            print(f"{index}. Student: {feedback.student.name} (Roll Number: {feedback.student.roll_number})")
            print(f"   Feedback: {feedback.feedback_text}")
            if feedback.instructor_response:
                print(f"   Instructor Response: {feedback.instructor_response}")
            print("-" * 30)

    def respond_to_feedback(self, feedback_index, response_text):
        if 1 <= feedback_index <= len(self.feedback_list):
            feedback = self.feedback_list[feedback_index - 1]
            feedback.instructor_response = response_text
        else:
            print("Invalid feedback index.")

def main():
    feedback_system = FeedbackSystem()

    # Some sample students and their feedbacks
    student1 = Student("John Doe", "12345")
    student2 = Student("Jane Smith", "67890")

    feedback_system.submit_feedback(student1, "The lectures are clear and easy to follow.")
    feedback_system.submit_feedback(student2, "The assignments are challenging but help us learn.")

    # Instructor views the feedbacks
    print("Feedbacks:")
    feedback_system.view_feedbacks()

    # Instructor responds to feedback
    feedback_index = int(input("Enter the feedback index you want to respond to: "))
    response_text = input("Enter your response: ")
    feedback_system.respond_to_feedback(feedback_index, response_text)

    # Updated feedback list
    print("Updated Feedbacks:")
    feedback_system.view_feedbacks()

if __name__ == "__main__":
    main()
