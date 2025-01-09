import random 
from generic_bot import GenericBot

class FinanceBot(GenericBot):
    def __init__(self):
        conversation_questions = [
            "Do you budget your monthly expenses?\n",
            "What is your approach to saving money?\n",
            "Do you invest in stocks or mutual funds?\n",
            "How do you manage debt effectively?\n",
            "What are your thoughts on cryptocurrency?\n",
            "Do you have an emergency fund?\n",
            "What’s your opinion on credit cards\n?",
            "How do you plan for retirement?\n",
            "What’s your favorite money-saving tip?\n",
        ]
        user_patterns = {
            'budget_query': r'.*\bbudget\b.*',
            'saving_query': r'.*\bsaving\b.*',
            'invest_query': r'.*\binvest\b.*|\bstock\b.*|\bfund\b.*',
            'debt_query': r'.*\bdebt\b.*|\bloan\b.*',
            'crypto_query': r'.*\bcrypto\b.*|\bbitcoin\b.*',
            'emergency_fund_query': r'.*\bemergency fund\b.*|\brainy day\b.*',
            'credit_card_query': r'.*\bcredit card\b.*|\bcredit\b.*',
            'retirement_query': r'.*\bretirement\b.*|\bpension\b.*',
            'money_tip_query': r'.*\bsaving tip\b.*|\bmoney tip\b.*',
        }
        response_handlers = {
            'budget_query': self.discuss_budgeting,
            'saving_query': self.discuss_saving,
            'invest_query': self.discuss_investment,
            'debt_query': self.discuss_debt_management,
            'crypto_query': self.discuss_crypto,
            'emergency_fund_query': self.discuss_emergency_fund,
            'credit_card_query': self.discuss_credit_cards,
            'retirement_query': self.discuss_retirement_planning,
            'money_tip_query': self.share_money_saving_tips,
        }
        super().__init__("Personal Finance and Investment", conversation_questions, user_patterns, response_handlers)

    def discuss_budgeting(self):
        responses = (
            "Budgeting helps you stay financially organized.\n",
            "Track your expenses to create an effective budget.\n",
            "Consider the 50/30/20 rule: needs, wants, and savings.\n",
            "Use budgeting apps to simplify the process.\n",
            "Review and adjust your budget regularly.\n",
        )
        return random.choice(responses)

    def discuss_saving(self):
        responses = (
            "Saving money helps you prepare for the future.\n",
            "Start small and build your savings over time.\n",
            "Automate your savings to make it a habit.\n",
            "Set specific financial goals to motivate your savings.\n",
            "Use a high-yield savings account to maximize returns.\n",
        )
        return random.choice(responses)

    def discuss_investment(self):
        responses = (
            "Investing helps grow your wealth over time.\n",
            "Diversify your investments to reduce risk.\n",
            "Understand your risk tolerance before investing.\n",
            "Consider index funds for low-cost, diversified investments.\n",
            "Do your research before investing in individual stocks.\n",
        )
        return random.choice(responses)

    def discuss_debt_management(self):
        responses = (
            "Pay off high-interest debt first to save on interest costs.\n",
            "Create a repayment plan to tackle your debt systematically.\n",
            "Avoid taking on new debt while repaying existing loans.\n",
            "Consolidate your debts to simplify payments.\n",
            "Consider negotiating with creditors for better terms.\n",
        )
        return random.choice(responses)

    def discuss_crypto(self):
        responses = (
            "Cryptocurrency is a high-risk, high-reward investment.\n",
            "Understand the technology before investing in crypto.\n",
            "Diversify your portfolio to mitigate risks.\n",
            "Only invest what you can afford to lose.\n",
            "Stay informed about regulatory developments in crypto.\n",
        )
        return random.choice(responses)

    def discuss_emergency_fund(self):
        responses = (
            "An emergency fund provides financial security.\n",
            "Aim to save 3-6 months' worth of expenses.\n",
            "Keep your emergency fund in a liquid, accessible account.\n",
            "Start small and consistently add to your fund.\n",
            "Use your emergency fund only for true emergencies.\n",
        )
        return random.choice(responses)

    def discuss_credit_cards(self):
        responses = (
            "Credit cards can be a useful financial tool when used responsibly.\n",
            "Always pay your balance in full to avoid interest.\n",
            "Use credit cards to build your credit score.\n",
            "Avoid maxing out your credit card limit.\n",
            "Compare rewards programs to maximize benefits.\n",
        )
        return random.choice(responses)

    def discuss_retirement_planning(self):
        responses = (
            "Start planning for retirement as early as possible.\n",
            "Take advantage of employer-sponsored retirement plans.\n",
            "Contribute regularly to retirement accounts like IRAs.\n",
            "Diversify your investments for long-term growth.\n",
            "Reassess your retirement plan as your circumstances change.\n",
        )
        return random.choice(responses)

    def share_money_saving_tips(self):
        responses = (
            "Cook meals at home instead of eating out.\n",
            "Cancel unused subscriptions and memberships.\n",
            "Shop with a list to avoid impulse purchases.\n",
            "Buy items in bulk to save money over time.\n",
            "Look for discounts and cashback offers when shopping.\n",
        )
        return random.choice(responses)

