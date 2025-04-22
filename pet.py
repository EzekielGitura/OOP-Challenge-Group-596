class Pet:
    def __init__(self, name="Pedro"):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.favorite_treats = ["🦴 Bacon Treats", "🥩 Beef Jerky", "🧀 Cheese Bits"]
        self.mood = "😊"
        self.cleanliness = 5
        self.trick_mastery = {}  # Store trick proficiency levels
        
    def update_mood(self):
        if self.happiness >= 8:
            self.mood = "🤗"
        elif self.happiness >= 5:
            self.mood = "😊"
        elif self.happiness >= 3:
            self.mood = "😐"
        else:
            self.mood = "😢"
            
    def eat(self, treat=None):
        if treat in self.favorite_treats:
            print(f"🎉 {self.name} loves {treat}! Extra happiness boost!")
            self.happiness = min(10, self.happiness + 2)
            self.hunger = max(0, self.hunger - 4)
        else:
            print(f"🍽️ {self.name} is eating regular food...")
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
        
    def sleep(self):
        print(f"😴 {self.name} is taking a cozy nap... Zzzz")
        self.energy = min(10, self.energy + 5)
        
    def play(self, game=None):
        if self.energy < 2:
            print(f"😫 {self.name} is too tired to play!")
            return
            
        games = {
            "fetch": "🎾 Playing fetch in the park!",
            "tug": "🧶 Playing tug of war!",
            "hide": "🏃 Playing hide and seek!",
            "swim": "🏊 Going for a swim!"
        }
        
        if game in games:
            print(games[game])
        else:
            print(f"🎮 {self.name} is playing around!")
            
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        self.cleanliness = max(0, self.cleanliness - 1)
        
    def train(self, trick):
        if self.energy < 3:
            print(f"😫 {self.name} is too tired to learn new tricks!")
            return
            
        if trick not in self.trick_mastery:
            self.trick_mastery[trick] = 1
            print(f"🌟 {self.name} is learning to {trick}! (Proficiency: 1/5)")
        else:
            self.trick_mastery[trick] = min(5, self.trick_mastery[trick] + 1)
            print(f"📈 {self.name}'s {trick} proficiency increased to {self.trick_mastery[trick]}/5!")
            
        self.energy -= 1
        self.happiness = min(10, self.happiness + 1)
        
    def show_tricks(self):
        if not self.trick_mastery:
            print(f"📚 {self.name} doesn't know any tricks yet!")
        else:
            print(f"\n🎓 {self.name}'s Trick Collection:")
            for trick, level in self.trick_mastery.items():
                stars = "⭐" * level
                print(f"- {trick}: {stars}")
                
    def bathe(self):
        print(f"🛁 {self.name} is getting squeaky clean!")
        self.cleanliness = 10
        self.happiness = max(0, self.happiness - 1)  # Most pets don't love baths!
        
    def cuddle(self):
        print(f"🤗 {self.name} is enjoying cuddle time!")
        self.happiness = min(10, self.happiness + 2)
        self.energy = max(0, self.energy - 1)
        
    def get_status(self):
        self.update_mood()
        print(f"\n📊 {self.name}'s Status Report:")
        print(f"Mood: {self.mood}")
        print(f"Hunger: {'🔴' * self.hunger}{'⚪' * (10-self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'⚡' * self.energy}{'⚪' * (10-self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'💖' * self.happiness}{'⚪' * (10-self.happiness)} ({self.happiness}/10)")
        print(f"Cleanliness: {'✨' * self.cleanliness}{'⚪' * (10-self.cleanliness)} ({self.cleanliness}/10)")
        print(f"Favorite Treats: {', '.join(self.favorite_treats)}")
        print(f"Tricks Learned: {', '.join(self.trick_mastery.keys()) if self.trick_mastery else 'None'}")
        print(f"Trick Mastery Levels: {self.trick_mastery if self.trick_mastery else 'None'}")
        print(f"Current Mood: {self.mood}")
        print(f"Current Cleanliness: {self.cleanliness}/10")    
        print(f"Current Trick Mastery: {self.trick_mastery if self.trick_mastery else 'None'}")
        