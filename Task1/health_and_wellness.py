import random 
from generic_bot import GenericBot

class HealthBot(GenericBot):
    def __init__(self):
        conversation_questions = [
            "How often do you exercise?\n",
            "What does a healthy diet mean to you?\n",
            "How do you manage stress in your daily life?\n",
            "What is your go-to strategy for getting quality sleep?\n",
            "How do you stay hydrated throughout the day?\n",
            "What motivates you to maintain a healthy lifestyle?\n",
            "How often do you visit your doctor for checkups?\n",
            "What are your favorite activities for staying active?\n",
            "How do you handle days when you feel unmotivated?\n",
        ]
        user_patterns = {
            'exercise_query': r'.*\bexercise\b.*',
            'diet_query': r'.*\bdiet\b.*',
            'stress_query': r'.*\bstress\b.*',
            'sleep_query': r'.*\bsleep\b.*',
            'hydration_query': r'.*\bwater\b.*|\bhydration\b.*',
            'motivation_query': r'.*\bmotivation\b.*|\bgoals\b.*',
            'checkup_query': r'.*\bdoctor\b.*|\bcheckup\b.*',
            'activity_query': r'.*\bactivity\b.*|\bhobbies\b.*',
            'unmotivation_query': r'.*\bunmotivated\b.*|\blazy\b.*',
        }
        response_handlers = {
            'exercise_query': self.provide_exercise_advice,
            'diet_query': self.provide_diet_advice,
            'stress_query': self.provide_stress_advice,
            'sleep_query': self.provide_sleep_advice,
            'hydration_query': self.provide_hydration_advice,
            'motivation_query': self.provide_motivation_advice,
            'checkup_query': self.provide_checkup_advice,
            'activity_query': self.provide_activity_advice,
            'unmotivation_query': self.provide_unmotivation_advice,
        }
        super().__init__("Health and Wellness", conversation_questions, user_patterns, response_handlers)

    def provide_exercise_advice(self):
        responses = (
            "Regular exercise is vital for overall health.\n",
            "Try to exercise at least 3 times a week.\n",
            "Incorporate strength training and cardio into your routine.\n",
            "Find an activity you enjoy to stay consistent.\n",
            "Stretching before and after workouts helps prevent injuries.\n",
        )
        return random.choice(responses)

    def provide_diet_advice(self):
        responses = (
            "A balanced diet is essential for a healthy lifestyle.\n",
            "Focus on whole foods and limit processed items.\n",
            "Eat a variety of fruits and vegetables daily.\n",
            "Stay mindful of portion sizes and avoid overeating.\n",
            "Ensure your meals include proteins, healthy fats, and carbs.\n",
        )
        return random.choice(responses)

    def provide_stress_advice(self):
        responses = (
            "Meditation and mindfulness can help reduce stress.\n",
            "Make time for hobbies to relax and unwind.\n",
            "Exercise is a great way to manage stress.\n",
            "Try deep breathing exercises during stressful moments.\n",
            "Talking to a friend or counselor can be beneficial.\n",
        )
        return random.choice(responses)

    def provide_sleep_advice(self):
        responses = (
            "Aim for 7-8 hours of quality sleep every night.\n",
            "Establish a regular sleep schedule, even on weekends.\n",
            "Avoid screens and caffeine before bedtime.\n",
            "Create a relaxing bedtime routine to wind down.\n",
            "Ensure your bedroom is dark, quiet, and cool.\n",
        )
        return random.choice(responses)

    def provide_hydration_advice(self):
        responses = (
            "Drink at least 8 glasses of water per day.\n",
            "Carry a water bottle with you to stay hydrated.\n",
            "Add fruits like lemon or cucumber to water for flavor.\n",
            "Monitor your urine color—it should be light yellow.\n",
            "Start your day with a glass of water.\n",
        )
        return random.choice(responses)

    def provide_motivation_advice(self):
        responses = (
            "Set realistic goals to stay motivated.\n",
            "Celebrate small achievements along the way.\n",
            "Remember why you started your health journey.\n",
            "Surround yourself with supportive people.\n",
            "Track your progress to see how far you've come.\n",
        )
        return random.choice(responses)

    def provide_checkup_advice(self):
        responses = (
            "Regular checkups are important for early detection of issues.\n",
            "Aim to visit your doctor at least once a year.\n",
            "Keep track of your medical history and test results.\n",
            "Don’t hesitate to ask your doctor questions.\n",
            "Vaccinations and screenings are part of staying healthy.\n",
        )
        return random.choice(responses)

    def provide_activity_advice(self):
        responses = (
            "Find activities that you enjoy and make them part of your routine.\n",
            "Group activities can make exercise more fun.\n",
            "Try exploring nature through hiking or cycling.\n",
            "Dancing is a great way to stay active and have fun.\n",
            "Switch up your activities to keep things interesting.\n",
        )
        return random.choice(responses)

    def provide_unmotivation_advice(self):
        responses = (
            "On unmotivated days, start small—just 5 minutes of activity.\n",
            "Remind yourself of the benefits of staying active.\n",
            "Listen to motivational music or podcasts.\n",
            "Rest days are okay, but don’t let them turn into weeks.\n",
            "Visualize the results you want to achieve.\n",
        )
        return random.choice(responses)
