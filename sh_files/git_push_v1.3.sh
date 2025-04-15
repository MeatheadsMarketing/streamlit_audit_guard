#!/bin/bash

echo "📦 Initializing Git Repo and pushing StreamlitAuditGuard v1.3..."

# Initialize and configure
git init
git add .
git commit -m "StreamlitAuditGuard v1.3 – Final Launch Validator and Interface"
git branch -M main

# Remove existing origin if it already exists
git remote remove origin 2>/dev/null

# Set correct remote
git remote add origin https://github.com/MeatheadsMarketing/streamlit_audit_guard.git

# Create tag for v1.3
git tag -a v1.3 -m "Finalized structure, scoring, and launch-ready validator UI"

# Pull and rebase in case of any remote history
git pull origin main --rebase

# Push everything including the tag
git push -u origin main --tags

echo "✅ StreamlitAuditGuard v1.3 pushed and tagged successfully."