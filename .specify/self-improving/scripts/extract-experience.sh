#!/bin/bash
# Experience Extraction Script for Self-Improving Agent
# Usage: ./extract-experience.sh <agent> <task> <outcome> [rating] [comments]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MEMORY_DIR="$SCRIPT_DIR/../memory"
EPISODIC_DIR="$MEMORY_DIR/episodic"
SEMANTIC_FILE="$MEMORY_DIR/semantic-patterns.json"
WORKING_DIR="$MEMORY_DIR/working"

# Ensure directories exist
mkdir -p "$EPISODIC_DIR/$(date +%Y)"
mkdir -p "$WORKING_DIR"

# Parameters
AGENT="$1"
TASK="$2"
OUTCOME="$3"
RATING="${4:-5}"
COMMENTS="${5:-No comments}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
DATE=$(date +%Y-%m-%d)
EPISODE_ID="ep-${DATE}-$(date +%s)"

echo "🧠 Self-Improving Agent: Extracting Experience"
echo "=============================================="
echo "Agent: $AGENT"
echo "Task: $TASK"
echo "Outcome: $OUTCOME"
echo "Rating: $RATING/10"
echo "Comments: $COMMENTS"
echo "=============================================="

# Create episodic memory
cat > "$EPISODIC_DIR/$(date +%Y)/${EPISODE_ID}.json" << EOFEPISODIC
{
  "id": "$EPISODE_ID",
  "timestamp": "$TIMESTAMP",
  "agent": "$AGENT",
  "task": "$TASK",
  "outcome": "$OUTCOME",
  "situation": "User requested feature implementation",
  "approach": "Followed multi-agent workflow with spec-first approach",
  "result": "$OUTCOME - Rating: $RATING/10",
  "lesson": "To be extracted by pattern analysis",
  "related_pattern": "pending_analysis",
  "user_feedback": {
    "rating": $RATING,
    "comments": "$COMMENTS"
  }
}
EOFEPISODIC

echo "✅ Episodic memory saved: $EPISODIC_DIR/$(date +%Y)/${EPISODE_ID}.json"

# Update working memory
cat > "$WORKING_DIR/current_session.json" << EOFCURRENT
{
  "session_id": "session-${DATE}-$(date +%s)",
  "started": "$TIMESTAMP",
  "agent": "$AGENT",
  "task": "$TASK",
  "outcome": "$OUTCOME",
  "episode_id": "$EPISODE_ID"
}
EOFCURRENT

echo "✅ Working memory updated"

# Extract patterns based on rating
if [ "$RATING" -ge 8 ]; then
  echo "✨ High rating detected - reinforcing successful patterns"
  PATTERN_LEVEL="best_practice"
elif [ "$RATING" -le 4 ]; then
  echo "⚠️  Low rating detected - identifying improvement areas"
  PATTERN_LEVEL="weakness"
else
  PATTERN_LEVEL="standard"
fi

echo ""
echo "📊 Experience Extraction Complete"
echo "=============================================="
echo "Episode ID: $EPISODE_ID"
echo "Pattern Level: $PATTERN_LEVEL"
echo "Next: Pattern abstraction and skill update"
echo "=============================================="
