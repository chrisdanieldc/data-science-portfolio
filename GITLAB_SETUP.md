# GitLab Setup Instructions

## Step 1: Create GitLab Repository

1. Go to https://gitlab.com and log in
2. Click the "+" button in the top navigation bar
3. Select "New project/repository"
4. Choose "Create blank project"
5. Fill in the details:
   - **Project name**: `data-science-portfolio` (or your preferred name)
   - **Project description**:
     ```
     Data science portfolio demonstrating NLP, analytics, SQL, and full-stack development skills. Includes production-ready web app with OpenAI integration, marketing attribution models, fraud detection system, and advanced SQL query patterns.
     ```
   - **Visibility Level**: Select "Public" (so employers can view it)
   - **Initialize repository with a README**: Leave this UNCHECKED (we already have one)
6. Click "Create project"

After creation, GitLab will show you the repository URL. It will look like:
```
git@gitlab.com:yourusername/data-science-portfolio.git
```

Copy this URL - you'll need it in the next step.

## Step 2: Push Your Code to GitLab

```bash
# Navigate to your portfolio directory
cd /Users/jasila/Desktop/data_science_projects/data-science-portfolio

# Add all files to git
git add .

# Create initial commit
git commit -m "Initial commit: Data science portfolio

Portfolio includes:
- NLP text summarization web app with OpenAI GPT-4
- Analytics projects (attribution modeling, fraud detection)
- SQL query examples and best practices
- Docker support for deployment"

# Add GitLab as remote (replace with your actual repository URL)
git remote add origin git@gitlab.com:yourusername/data-science-portfolio.git

# Push to GitLab
git branch -M main
git push -u origin main
```

## Step 3: Add Topics/Tags

After pushing, go back to your GitLab repository page:

1. Click on "Settings" in the left sidebar
2. Click "General"
3. Expand "Project description, topics, avatar"
4. Add these topics (comma-separated):
   ```
   data-science, python, sql, machine-learning, nlp, fastapi, docker, analytics, fraud-detection
   ```
5. Click "Save changes"

## Step 4: Verify Everything Looks Good

1. Check that all files are visible on GitLab
2. Verify the README.md displays properly on the main page
3. Browse through the project folders to ensure everything uploaded correctly

## Troubleshooting

### If you get "Permission denied (publickey)" error:

You need to set up SSH keys with GitLab:

```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy your public key
cat ~/.ssh/id_ed25519.pub
```

Then:
1. Go to GitLab → Settings → SSH Keys
2. Paste your public key
3. Click "Add key"
4. Try the push command again

### Alternative: Use HTTPS instead of SSH

If SSH is problematic, use HTTPS URL instead:

```bash
# Add remote with HTTPS (replace with your URL)
git remote add origin https://gitlab.com/yourusername/data-science-portfolio.git

# Push
git push -u origin main
```

You'll be prompted for your GitLab username and password.

## After Setup

Add the repository URL to your:
- Resume
- LinkedIn profile
- Portfolio website
- Job applications

## Making Updates Later

```bash
# After making changes to any files
git add .
git commit -m "Description of what you changed"
git push
```
