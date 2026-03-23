#!/bin/bash
# QA File Watch Hook
# Triggers QA verification when code changes are detected

PROJECT_ROOT="/Users/niuniu/spec-driven"
QA_LOG="$PROJECT_ROOT/.specify/memory/qa-triggers.log"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# File patterns to watch
BACKEND_PATTERNS=(
    "backend/app/models.py"
    "backend/app/serializers.py"
    "backend/app/views.py"
    "backend/app/viewsets.py"
    "backend/app/urls.py"
)

FRONTEND_PATTERNS=(
    "frontend/src/components/*.vue"
    "frontend/src/views/*.vue"
    "frontend/src/stores/*.ts"
    "frontend/src/api/*.ts"
    "frontend/src/types/*.ts"
)

# Check if any backend files changed recently (within last minute)
check_backend_changes() {
    for pattern in "${BACKEND_PATTERNS[@]}"; do
        if find "$PROJECT_ROOT/$pattern" -mmin -1 2>/dev/null | grep -q .; then
            echo "[$TIMESTAMP] Backend change detected: $pattern" >> "$QA_LOG"
            return 0
        fi
    done
    return 1
}

# Check if any frontend files changed recently
check_frontend_changes() {
    for pattern in "${FRONTEND_PATTERNS[@]}"; do
        if find "$PROJECT_ROOT/$pattern" -mmin -1 2>/dev/null | grep -q .; then
            echo "[$TIMESTAMP] Frontend change detected: $pattern" >> "$QA_LOG"
            return 0
        fi
    done
    return 1
}

# Main execution
if [ "$1" == "--check" ]; then
    if check_backend_changes; then
        echo "BACKEND_CHANGES_DETECTED"
        exit 0
    fi
    if check_frontend_changes; then
        echo "FRONTEND_CHANGES_DETECTED"
        exit 0
    fi
    echo "NO_CHANGES"
    exit 0
fi

echo "[$TIMESTAMP] QA Watch Hook initialized" >> "$QA_LOG"
exit 0
