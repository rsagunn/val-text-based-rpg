# Val-Text-Based-RPG : Valorant Swiftplay MATCH POINT
kills = 0
# Welcome user to the game and ask their name
name = input("Welcome to Valorants finest game, what is your name? ")
print(f" Hi {name}! I hope you will love this game...\n")

# Start game
# Describe the starting scene
print("You are playing a quick round of Valorant Swiftplay on the map of Abyss defender side.")
print("Go defend [A] site.")
print("Go defend [B] site")
ans1 = input("Choice: ").lower().strip()

if ans1 == "a": #ans1
    print("The enemy team comes through A main and they kill 1 of your teammates.")
    print("[U]se your abilities to hold them off longer and play in a corner")
    print("[P]lay backsite and wait for them to push.")
    ans2 = input("Choice: ").lower().strip()
    kills += 1
    if ans2 == "u": #ans2
        
        print("All enemies are pushed on site, one of them tries to plant the spike.")
        print("[K]ill the spike planter and one other enemy, then falling back to A main.")
        print("[W]ait another 20 seconds in your corner")
        ans3 = input("Choice: ").lower().strip()
        kills += 1
        
        if ans3 == "k": #ans3
            print("All of your allies die because they are braindead.")
            print("[U]se your wall ability to retake the site and use your cove to hide you defusing the spike.")
            print("[R]etake site with no abilities")
            print("[S]ave your weapons")
            ans4 = input("Choice: ").lower().strip()
            kills += 1
            
            if ans4 == "u": #ans4
                print("You fake the spike and one by one enemies come inside the cove and you kill them, but there is one more person.")
                print("[H]alf the spike")
                print("[S]tick the spike")
                ans5 = input("Choice: ")
                kills += 1
                
                if ans5 == "h": #ans5
                    print("Enemies peek at you after you get off the spike. You aim at the enemy and you win the game. Congratulations")
                    print(f"Total kills: {kills}!")
                    print(f"Goodbye, {name}!")
                elif ans5 == "s": #elif5
                    print("Enemies peek you when the spike is halved, but you have no time to pull out your gun. You died, GAME OVER.")
                    print(f"Total kills: {kills}!")
                    print(f"Goodbye, {name}!")
                    
                else: #else5
                    print(f"Thats not one of the choices! Total kills: {kills}")
                    kills -= 1
            
            elif ans4 == "r": #elif4
                print("The enemies saw you from backsite and headshots you. GAME OVER")
                print(f"Total kills: {kills}!")
                print(f"Goodbye, {name}!")
                
            elif ans4 == "s": #elif4
                print("Enemies double swing you and you get out aimed. GAME OVER")
                print(f"Total kills: {kills}!")
                print(f"Goodbye, {name}!")
                
            else: #else4
                print("fThats not a awnser! Total kills: {kills}")
                kills -= 1
                
        elif ans3 == "w": #elif3
            print("One enemy spotted you then you died. GAME OVER")
            print(f"Total kills: {kills}!")
            print(f"Goodbye, {name}!")
        
        else: #else3
            print(f"Thats not a awnser! Total kills: {kills}")
            kills -= 1
            
    elif ans2 == "p": # elif ans2
        print("The enemy team pushes backsite. You lose the gunfight and die. GAME OVER")
        print(f"Total kills: {kills}!")
        print(f"Goodbye, {name}!")
    
    else: #else 2
        print(f"Thats not a awnser! Total kills: {kills}")
        kills -= 1

        
elif ans1 == "b": #elif1
    print("The enemy lurker kills you by flanking you and you die. GAME OVER")
    print(f"Total kills: {kills}!")
    print(f"Goodbye, {name}!")
    
else: #else 1
    print(f"Thats not a awnser! Total kills: {kills}")
    kills -= 1
