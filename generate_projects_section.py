import requests
import openai
import os

GITHUB_USERNAME = "SubhranshuPan"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Store your key in environment variable

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_description(repo_name, repo_description):
    prompt = (
        f"Write a concise, engaging description for a GitHub project called '{repo_name}'. "
        f"Here is the original description: '{repo_description}'. "
        "Include main features, technologies, and a use case."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=80,
    )
    return response.choices[0].text.strip()

def main():
    repos = fetch_repositories(GITHUB_USERNAME)
    md_lines = [
        "# 🚀 My Projects\n",
        "Here are some of my featured projects on GitHub:\n"
    ]
    for repo in repos:
        name = repo['name']
        url = repo['html_url']
        desc = repo['description'] or "No description provided."
        ai_desc = generate_description(name, desc)
        tech = repo.get('language', 'N/A')
        md_lines.append(
            f"## [{name}]({url})\n**Description:**  \n{ai_desc}\n\n**Tech Stack:** {tech}\n\n---\n"
        )
    with open("my-projects.md", "w", encoding="utf-8") as f:
        f.writelines(md_lines)

if __name__ == "__main__":
    main()