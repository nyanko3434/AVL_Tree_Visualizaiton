#!/bin/bash
# ============================================
# 🧠 AVL Tree Visualization 
# Setup & Run Script
# ============================================

# Exit immediately if a command fails
set -e

# Define project paths
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="$PROJECT_DIR/venv"

echo "📦 Starting setup for AVL Tree Visualization..."

# Step 1: Create virtual environment if not present
if [ ! -d "$VENV_DIR" ]; then
    echo "🧩 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "✅ Virtual environment already exists."
fi

# Step 2: Activate virtual environment
echo "⚙️  Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Step 3: Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Step 4: Install dependencies
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    echo "📥 Installing dependencies from requirements.txt..."
    pip install -r "$PROJECT_DIR/requirements.txt"
else
    echo "⚠️  No requirements.txt found! Skipping dependency installation."
fi

# Step 5: Run main.py
echo "🚀 Launching AVL Tree Visualization..."
python3 "$PROJECT_DIR/main.py"

# Step 6: Deactivate after exit
deactivate
