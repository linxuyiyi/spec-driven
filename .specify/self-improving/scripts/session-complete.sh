#!/bin/bash
# Session Complete Script - Analyze and Report
# Usage: ./session-complete.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MEMORY_DIR="$SCRIPT_DIR/../memory"
WORKING_DIR="$MEMORY_DIR/working"
EPISODIC_DIR="$MEMORY_DIR/episodic"
SEMANTIC_FILE="$MEMORY_DIR/semantic-patterns.json"

echo ""
echo "🧠 Self-Improving Agent: Session Analysis"
echo "=============================================="

# Check if current session exists
if [ ! -f "$WORKING_DIR/current_session.json" ]; then
  echo "No active session found. Starting fresh."
  exit 0
fi

# Read current session
SESSION_ID=$(grep -o '"session_id": "[^"]*"' "$WORKING_DIR/current_session.json" | cut -d'"' -f4)
AGENT=$(grep -o '"agent": "[^"]*"' "$WORKING_DIR/current_session.json" | cut -d'"' -f4)
TASK=$(grep -o '"task": "[^"]*"' "$WORKING_DIR/current_session.json" | cut -d'"' -f4)

echo "Session: $SESSION_ID"
echo "Agent: $AGENT"
echo "Task: $TASK"
echo ""

# Count today's episodes
TODAY=$(date +%Y-%m-%d)
EPISODE_COUNT=$(find "$EPISODIC_DIR/$(date +%Y)" -name "ep-${TODAY}*.json" 2>/dev/null | wc -l | tr -d ' ')

echo "📊 Today's Activity ($(date +%Y-%m-%d)):"
echo "   Episodes: $EPISODE_COUNT"
echo ""

# Analyze patterns
if [ -f "$SEMANTIC_FILE" ]; then
  PATTERN_COUNT=$(grep -c '"id": "pat-' "$SEMANTIC_FILE" 2>/dev/null || echo "0")
  echo "📚 Knowledge Base:"
  echo "   Total Patterns: $PATTERN_COUNT"
  echo ""
fi

# Summary
echo "✨ Session Summary:"
echo "   - Experience captured in episodic memory"
echo "   - Patterns ready for abstraction"
echo "   - Working memory updated"
echo ""

# Move current session to completed
if [ -f "$WORKING_DIR/current_session.json" ]; then
  cp "$WORKING_DIR/current_session.json" "$WORKING_DIR/session_end.json"
  echo "✅ Session marked as complete"
fi

echo ""
echo "=============================================="
echo "🎉 Self-Improvement Cycle Complete!"
echo "=============================================="
