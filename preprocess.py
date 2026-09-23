
import json
from pathlib import Path

# Get the project folder
BASE_DIR = Path(__file__).resolve().parent

# Load raw LinkedIn posts
file_path = BASE_DIR / "data" / "raw_posts.json"

with open(file_path, "r", encoding="utf-8") as file:
    posts = json.load(file)


# Function to categorize post length
def get_length_category(word_count):
    if word_count < 50:
        return "Short"
    elif word_count < 100:
        return "Medium"
    else:
        return "Long"


# Preprocess each post
processed_posts = []

for post in posts:
    text = post["text"]

    # Count words in the post
    word_count = len(text.split())

    # Create a processed record
    processed_post = {
        "text": text,
        "engagement": post["engagement"],
        "word_count": word_count,
        "length": get_length_category(word_count)
    }

    processed_posts.append(processed_post)


# Display results
print("Total posts:", len(processed_posts))

for post in processed_posts:
    print("\nLength:", post["length"])
    print("Word count:", post["word_count"])
    print("Engagement:", post["engagement"])


# Save processed data
output_file = BASE_DIR / "data" / "processed_posts.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(processed_posts, file, indent=4, ensure_ascii=False)

print("\nProcessed data saved successfully!")