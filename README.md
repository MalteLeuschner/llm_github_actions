![Waterkant Image](waterkant.png)

<h1 align="center">
   Auto-documentation with LLMs in Python
</h1>


We implement a github actions llm that creates docstrings, typing, linting, and sphinx autodocumenation
This was done during coding.waterkant hackathon in Kiel

## Setup-instructions

Since several attendees asked how to set up the workflow and non-existent documentation for a tool that documents for you is amusing but not very helpful, here is a short explanation on how to get this tool working:

1. **Generate GROQ API Key:**
   - The action uses the [GROQ](https://groq.com/) API to generate docstrings and summarize the code. 
   - Generate an [API key](https://console.groq.com/keys) and save it under the name `GROQ_API_KEY` in the [repo's secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).

2. **Copy the .github Folder:**
   - Copy the `.github` folder from this repo to your project's root folder. Ignore everything else in this repo; the files in `src/` are just there as examples.

3. **Configure Source Path:**
   - If your `.py` files are in a folder called `src`, the action should work as is. Otherwise, edit the `llm-documenter.yml` file to change the value of the `SOURCE_PATH` environment variable to represent your source folder.
   ```yaml
   env:
     SOURCE_PATH: your_source_folder
   ```
   - If they to not already, all your code-folders do also need __init__.py-files, even if the files are empty. Sphinx-autodoc will ignore them if they don't have one.

4. **Push Changes:**
   - After every push, you can manually start the action in the github-actions-tab. It will:
     - Add docstrings to `.py` files that have changed, add typing and lint your files. The changes will be pushed to a new "commented_branch".
     - Summarize your project, build a Sphinx documentation, and put it in the `docs` folder in a gh_pages-branch.

5. **Publish Documentation (Optional):**
   - If your repo is public, you can make the documentation accessible via [GitHub Pages](https://docs.github.com/en/pages/quickstart).

6. **Profit!**


We tried to make the action as non-invasive as possible, we did already encounter some issues with complex return-values and class imports from other modules in one project.
The Landing page for the documentation is additionally a bit prone to hallucination since we added it last minute.
What we are trying to say is that we do not guarantee anything, a start in documenting is a start though :).
