# Step-by-Step Guide: Generative AI "My Projects" Section for GitHub Profile

## 1. Fork or Clone the Repository

- Fork this repository to your GitHub account or clone it locally:
  ```sh
  git clone https://github.com/SubhranshuPan/generative-ai-projects-section.git
  cd generative-ai-projects-section
  ```

## 2. Set Up Python Environment

- Ensure you have Python 3.11+ installed.
- (Optional but recommended) Create and activate a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
  ```

## 3. Install Dependencies

- Install the required Python packages:
  ```sh
  pip install -r requirements.txt
  ```

## 4. Get Your OpenAI API Key

- Sign up at [OpenAI](https://platform.openai.com/signup) if you don’t have an API key.
- Copy your key.

## 5. Set Your API Key as an Environment Variable

- On Linux/macOS:
  ```sh
  export OPENAI_API_KEY=sk-...your-key...
  ```
- On Windows (CMD):
  ```bat
  set OPENAI_API_KEY=sk-...your-key...
  ```

## 6. Run the Project Generator Script

- Execute the script to generate your “My Projects” Markdown section:
  ```sh
  python generate_projects_section.py
  ```
- This will create or update `my-projects.md` with AI-generated summaries of your public GitHub repositories.

## 7. Add the Section to Your GitHub Profile README

- Open your GitHub profile repository (the one named `<your-github-username>`).
- Copy the content from `my-projects.md` and paste it into your `README.md` at the desired location.
- Commit and push the changes:
  ```sh
  git add README.md
  git commit -m "Update My Projects section"
  git push
  ```

## 8. Set Up GitHub Actions for Automation (Optional but Recommended)

- In your repository, create a secret named `OPENAI_API_KEY` in **Settings > Secrets and variables > Actions > New repository secret**.
- Ensure `.github/workflows/update-projects.yml` is present (see this repo for a template).
- The workflow will automatically update `my-projects.md` on a schedule and commit changes.

## 9. Customize and Extend

- Modify the Python script for custom formatting, tech stack detection, or to include pinned/starred repositories.
- Tweak workflow schedule or add notifications as needed.

---

## 🎉 You're Done!

Your GitHub profile will now feature a dynamic, AI-powered project showcase that updates automatically!