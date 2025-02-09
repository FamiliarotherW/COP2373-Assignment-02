# WinsonMaProgrammingExercise02.py

import re

def calculate_spam_score(message, spam_keywords):
    #Calculate spam
    score = 0
    triggered = []
    for keyword in spam_keywords:
        matches = re.findall(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE)
        score += len(matches)
        if matches:
            triggered.append((keyword, len(matches)))
    return score, triggered
    
def assess_spam_likelihood(score):
    #Rates spam likelihood
    if score >= 10:
        return "Very High"
    elif score >= 5:
        return "High"
    elif score >= 2:
        return "Medium"
    elif score >= 1:
        return "Low"
    else:
        return "Very Low"
        
def main():
    spam_keywords = [" guaranteed", "free", "prize", "win", "offer", "discount", "limited time", "act now", "apply now", "click here", "subscribe", "unsubscribe",
        "earn money", "work from home", "online casino", "jackpot", "lottery",
        "miracle", "cure", "weight loss", "increase size", "dating", "fun",
        "nigeria", "bank account", "credit card", "debt", "loan", "urgent",
        "confidential", "exclusive", "remove", "guarantee", "100% free"
    ]
    
    message = input("Enter email: \n")
    score, triggered = calculate_spam_score(message, spam_keywords)
    likelihood = assess_spam_likelihood(score)
    
    print("\nSpam Score: ", score)
    print("Likelihood: ", likelihood)
    
    if triggered:
        print("\nTriggered keywords: ")
        for keyword, count in triggered:
            print(f"-{keyword} (x{count})")
    else:
        print("\nNo spam words found. ")
        
if __name__ == "__main__": 
    main()