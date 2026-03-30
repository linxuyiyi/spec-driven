#!/bin/bash
# PostBash Hook for Self-Improving Agent
# Captures command output and exit codes for learning

TOOL_OUTPUT="$1"
EXIT_CODE="$2"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

PROJECT_ROOT="/Users/niuniu/spec-driven"
WORKING_MEMORY="$PROJECT_ROOT/.specify/self-improving/memory/working"
ERROR_LOG="$WORKING_MEMORY/last_error.json"

# Ensure directory exists
mkdir -p "$WORKING_MEMORY"

# If exit code is non-zero, log the error for self-correction
if [ "$EXIT_CODE" -ne 0 ]; then
    cat > "$ERROR_LOG" << EOF
{
    "timestamp": "$TIMESTAMP",
    "exit_code": $EXIT_CODE,
    "output": "$(echo "$TOOL_OUTPUT" | head -c 2000 | tr '\n' ' ' | sed 's/"/\\"/g')",
    "analyzed": false
}
EOF
    echo "[$TIMESTAMP] Error captured (exit code: $EXIT_CODE)" >> "$WORKING_MEMORY/error_log.txt"
fi

exit 0
