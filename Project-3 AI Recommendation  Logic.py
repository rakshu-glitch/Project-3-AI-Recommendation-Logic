# Smart Course Recommendation System
# Project: AI Recommendation Logic

print("\n===================================")
print(" Welcome to Smart Recommendation System ")
print("===================================\n")

# Available courses and related interests
courses = {
    "Machine Learning": ["ai", "data", "programming"],
    "Data Science": ["data", "analytics", "ai"],
    "Python Programming": ["programming", "coding"],
    "Web Development": ["programming", "design"],
    "Cyber Security": ["security", "technology"],
    "Cloud Computing": ["technology", "computing"],
    "Digital Marketing": ["marketing", "business"],
    "Graphic Design": ["design", "creativity"]
}

# Taking user details
name = input("Enter your name: ")

print("\nEnter your interests separated by commas")
print("Example: ai, programming, data")

interests = input("Your interests: ").lower().split(",")

# Remove extra spaces
user_interests = []

for interest in interests:
    user_interests.append(interest.strip())

# Ask how much the user likes each interest
ratings = {}

print("\nRate each interest from 1 to 5")

for interest in user_interests:

    while True:

        try:
            rating = int(input(f"{interest}: "))

            if 1 <= rating <= 5:
                ratings[interest] = rating
                break

            else:
                print("Please enter a value between 1 and 5")

        except:
            print("Invalid input")

# Recommendation section
recommendations = []

for course, categories in courses.items():

    score = 0
    matched = []

    for category in categories:

        if category in ratings:

            score += ratings[category]
            matched.append(category)

    if score > 0:

        recommendations.append({
            "course": course,
            "score": score,
            "matched": matched
        })

# Sort recommendations
recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Display results
print("\n")
print("===================================")
print(" Personalized Recommendations ")
print("===================================\n")

if len(recommendations) == 0:

    print("Sorry, no recommendations found.")

else:

    for i, item in enumerate(recommendations, start=1):

        print(f"{i}. {item['course']}")
        print(f"Match Score: {item['score']}")

        print("Why this course?")

        print(
            f"Because you showed interest in "
            f"{', '.join(item['matched'])}."
        )

        print("-" * 35)

# Career suggestions
print("\nSuggested Career Areas\n")

career_map = {
    "Machine Learning": "Machine Learning Engineer",
    "Data Science": "Data Scientist",
    "Python Programming": "Software Developer",
    "Web Development": "Frontend/Backend Developer",
    "Cyber Security": "Security Analyst",
    "Cloud Computing": "Cloud Engineer",
    "Digital Marketing": "Marketing Specialist",
    "Graphic Design": "Graphic Designer"
}

shown = []

for item in recommendations[:3]:

    career = career_map[item["course"]]

    if career not in shown:
        print("•", career)
        shown.append(career)

# Simple roadmap
print("\nLearning Roadmap\n")

if "programming" in user_interests:
    print("Step 1 -> Learn Python Basics")
    print("Step 2 -> Practice Coding Problems")

if "data" in user_interests:
    print("Step 3 -> Learn Data Analysis")

if "ai" in user_interests:
    print("Step 4 -> Study Machine Learning")

print("Step 5 -> Build Projects")
print("Step 6 -> Create Portfolio")

print("\nThank you,", name)
print("Hope these recommendations help you!")