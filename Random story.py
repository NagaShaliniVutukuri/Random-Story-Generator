import random 

characters = [
    "a fearless astronaut who dreams of exploring the unknown",
    "a mischievous fox with a knack for solving mysteries",
    "a time-traveling scientist obsessed with rewriting history",
    "a lost pirate searching for redemption",
    "an AI-powered robot longing to understand human emotions"
]

settings = [
    "on a distant alien planet filled with bioluminescent forests and dangerous creatures",
    "in a magical underwater city hidden beneath crystal-clear waves",
    "inside a top-secret lab where bizarre experiments come to life",
    "on a deserted island with hidden caves and ancient ruins",
    "in a parallel universe where time flows backward"
]

conflicts = [
    "trying to stop an alien invasion that threatens to destroy all life",
    "searching for a legendary artifact that holds unimaginable power",
    "escaping from a collapsing dimension before it ceases to exist",
    "outsmarting a cunning villain bent on conquering the world",
    "solving an ancient cosmic puzzle that could change the fate of the universe"
]

complications = [
    "but they were betrayed by someone they trusted along the way",
    "only to discover that their quest had unintended consequences",
    "while being pursued by a mysterious figure who knew their every move",
    "and had to make a heartbreaking sacrifice to continue",
    "but realized the answers they sought came at a terrible cost"
]

resolutions = [
    "and ultimately saved the day, becoming a symbol of hope for generations to come.",
    "but their journey led them to uncover a greater mystery, leaving the world in awe.",
    "and their courage and wisdom became legendary across galaxies.",
    "but they vanished into the unknown, leaving behind an unforgettable legacy.",
    "and they changed the world forever, inspiring countless others to follow their path."
]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    complication = random.choice(complications)
    resolution = random.choice(resolutions)
    
    story = (
        f"Once upon a time, {character} found themselves {setting}. "
        f"They were {conflict}. "
        f"As their journey unfolded, they faced many challenges, {complication}. "
        f"In the end, {resolution}"
    )
    return story

def main():
    print("Welcome to the long Random story Generator!")
    
    while True:
        print("\nHere is your story:")
        print(generate_story())
        choice = input("\nDo you want to generate another story? (y/n):").strip().lower()
        if choice != 'y':
            print("\nThank you for using the Long Random story Generator. Goodbye!")
            break

if __name__ =="__main__":
    main()