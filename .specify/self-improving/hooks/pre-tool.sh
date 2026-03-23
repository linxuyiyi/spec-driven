#!/bin/bash
# PreToolUse Hook for Self-Improving Agent
# Logs tool usage for later analysis

TOOL_NAME="$1"
TOOL_INPUT="$2"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Get project root
PROJECT_ROOT="/Users/niuniu/spec-driven"
WORKING_MEMORY="$PROJECT_ROOT/.specify/self-improving/memory/working"

# Ensure working memory directory exists
mkdir -p "$WORKING_MEMORY"

# Log tool usage to current session
SESSION_FILE="$WORKING_MEMORY/current_session.json"

if [ ! -f "$SESSION_FILE" ]; then
    echo '{"start_time":"'"$TIMESTAMP"'","tools":[]}' > "$SESSION_FILE"
fi

# Append tool usage (simple JSON append - production would use proper JSON manipulation)
# For now, we just track that tools were used
echo "$TIMESTAMP - Tool: $TOOL_NAME" >> "$WORKING_MEMORY/tool_log.txt"

exit 0
