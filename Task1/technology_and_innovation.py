import random 
from generic_bot import GenericBot

class TechBot(GenericBot):
    def __init__(self):
        conversation_questions = [
            "What is your favorite tech gadget?\n",
            "What do you think about AI?\n",
            "How often do you upgrade your devices?\n",
            "Do you prefer Android or iOS?\n",
            "What are your thoughts on smart home devices?\n",
            "Have you tried virtual or augmented reality?\n",
            "What’s your opinion on self-driving cars?\n",
            "Which programming language do you find most exciting?\n",
            "What’s your go-to tech tool for productivity?\n",
        ]
        user_patterns = {
            'gadgets_query': r'.*\bgadget\b.*|\bdevice\b.*',
            'ai_query': r'.*\bai\b.*|\bartificial intelligence\b.*',
            'upgrade_query': r'.*\bupgrade\b.*|\bupdate\b.*',
            'os_query': r'.*\bandroid\b.*|\bios\b.*|\bwindows\b.*',
            'smart_home_query': r'.*\bsmart home\b.*|\bhome assistant\b.*',
            'vr_ar_query': r'.*\bvirtual reality\b.*|\baugmented reality\b.*|\bvr\b.*|\bar\b.*',
            'self_driving_query': r'.*\bself-driving\b.*|\bautonomous car\b.*',
            'programming_language_query': r'.*\bprogramming language\b.*|\bcoding\b.*',
            'productivity_tool_query': r'.*\bproductivity\b.*|\btool\b.*|\bapp\b.*',
        }
        response_handlers = {
            'gadgets_query': self.discuss_gadgets,
            'ai_query': self.discuss_ai,
            'upgrade_query': self.discuss_upgrading_devices,
            'os_query': self.discuss_operating_systems,
            'smart_home_query': self.discuss_smart_home_devices,
            'vr_ar_query': self.discuss_vr_ar,
            'self_driving_query': self.discuss_self_driving_cars,
            'programming_language_query': self.discuss_programming_languages,
            'productivity_tool_query': self.discuss_productivity_tools,
        }
        super().__init__("Technology and Innovation", conversation_questions, user_patterns, response_handlers)

    def discuss_gadgets(self):
        responses = (
            "Tech gadgets are amazing tools to simplify life.\n",
            "Smartphones are probably the most popular gadgets!\n",
            "Wearable devices like smartwatches are very convenient.\n",
            "Drones are fascinating for photography and exploration.\n",
            "Gaming consoles are another popular tech gadget.\n",
        )
        return random.choice(responses)

    def discuss_ai(self):
        responses = (
            "AI is transforming industries worldwide.\n",
            "It’s fascinating how AI is evolving so quickly.\n",
            "AI assistants like Siri and Alexa are making lives easier.\n",
            "Machine learning is a key part of AI development.\n",
            "Ethical AI development is a crucial topic of discussion.\n",
        )
        return random.choice(responses)

    def discuss_upgrading_devices(self):
        responses = (
            "Upgrading devices ensures you have the latest features.\n",
            "Consider your needs before upgrading.\n",
            "Sometimes software updates can give your device new life.\n",
            "Make sure to recycle or properly dispose of old devices.\n",
            "New devices often have better energy efficiency.\n",
        )
        return random.choice(responses)

    def discuss_operating_systems(self):
        responses = (
            "Choosing an OS often depends on personal preference.\n",
            "Android offers more customization compared to iOS.\n",
            "iOS is known for its seamless integration across Apple devices.\n",
            "Windows is popular for productivity and gaming.\n",
            "Linux is favored by developers for its flexibility and open-source nature.\n",
        )
        return random.choice(responses)

    def discuss_smart_home_devices(self):
        responses = (
            "Smart home devices can make life more convenient.\n",
            "Voice-controlled assistants like Alexa and Google Home are great tools.\n",
            "Smart thermostats help save energy.\n",
            "Security cameras and smart locks add an extra layer of protection.\n",
            "Smart lighting systems can be controlled remotely.\n",
        )
        return random.choice(responses)

    def discuss_vr_ar(self):
        responses = (
            "Virtual reality offers immersive experiences in gaming and education.\n",
            "Augmented reality is transforming industries like retail and healthcare.\n",
            "AR apps like Pokémon GO have been wildly popular.\n",
            "VR headsets like Oculus Quest are leading the market.\n",
            "The potential for VR and AR in training and simulations is enormous.\n",
        )
        return random.choice(responses)

    def discuss_self_driving_cars(self):
        responses = (
            "Self-driving cars could revolutionize transportation.\n",
            "Safety is a major focus for autonomous car technology.\n",
            "Companies like Tesla and Waymo are leading the way.\n",
            "Self-driving cars could reduce traffic congestion in the future.\n",
            "Legal and ethical challenges are being addressed in this field.\n",
        )
        return random.choice(responses)

    def discuss_programming_languages(self):
        responses = (
            "Python is very popular for its simplicity and versatility.\n",
            "JavaScript is essential for web development.\n",
            "C++ is widely used in game development and systems programming.\n",
            "Java is still a favorite for enterprise applications.\n",
            "Rust is gaining attention for its performance and memory safety.\n",
        )
        return random.choice(responses)

    def discuss_productivity_tools(self):
        responses = (
            "Apps like Notion and Evernote are great for note-taking.\n",
            "Trello and Asana help manage projects effectively.\n",
            "Google Workspace offers excellent collaboration tools.\n",
            "Time management tools like RescueTime can boost efficiency.\n",
            "Communication tools like Slack streamline team workflows.\n",
        )
        return random.choice(responses)

