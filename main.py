from pet import Pet
import time

def main():
    # Create our pet with a fun introduction
    print("🎉 Welcome to Virtual Pet Simulator! 🎉")
    print("\nCreating a new pet...")
    time.sleep(1)
    
    pedro = Pet()
    
    # Morning routine simulation
    print("\n🌅 Morning Activities:")
    pedro.get_status()
    pedro.sleep()  # Start fresh
    pedro.eat("🦴 Bacon Treats")
    pedro.get_status()
    
    # Training session
    print("\n📚 Training Session:")
    pedro.train("roll over")
    pedro.train("sit")
    pedro.train("high five")
    pedro.show_tricks()
    
    # Playtime activities
    print("\n🎮 Afternoon Fun:")
    pedro.play("fetch")
    pedro.play("swim")
    pedro.get_status()
    
    # Evening routine
    print("\n🌙 Evening Care:")
    pedro.bathe()
    pedro.eat("🧀 Cheese Bits")
    pedro.cuddle()
    
    # Final status check
    print("\n📊 End of Day Report:")
    pedro.get_status()
    pedro.show_tricks()

if __name__ == "__main__":
    main()
