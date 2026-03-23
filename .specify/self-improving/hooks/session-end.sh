#!/bin/bash
# Session End Hook for Self-Improving Agent
# Triggers experience extraction and pattern abstraction

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

PROJECT_ROOT="/Users/niuniu/spec-driven"
WORKING_MEMORY="$PROJECT_ROOT/.specify/self-improving/memory/working"
SESSION_END_FILE="$WORKING_MEMORY/session_end.json"
EXTRACT_SCRIPT="$PROJECT_ROOT/.specify/self-improving/scripts/extract-experience.sh"

# Mark session as ended
cat > "$SESSION_END_FILE" << EOF
{
    "end_time": "$TIMESTAMP",
    "trigger": "session_end"
}
EOF

# Run experience extraction if script exists
if [ -x "$EXTRACT_SCRIPT" ]; then
    echo "[$TIMESTAMP] Triggering experience extraction..."
    bash "$EXTRACT_SCRIPT" 2>&1 | head -50
fi

# Also run session complete script
COMPLETE_SCRIPT="$PROJECT_ROOT/.specify/self-improving/scripts/session-complete.sh"
if [ -x "$COMPLETE_SCRIPT" ]; then
    echo "[$TIMESTAMP] Running session complete..."
    bash "$COMPLETE_SCRIPT" 2>&1 | head -50
fi

exit 0
