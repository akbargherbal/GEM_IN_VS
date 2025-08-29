# Commit Format Guidelines for Gemini CLI Bridge

## Primary Format Structure

```
<type>(<phase>.<task>): <description>

[optional body]

[optional footer]
```

## Phase-Task Reference System

### Phase Codes
- **P1**: Core Workflow "Steel Thread" 
- **P2**: Reliability & Hardening
- **P3**: Documentation & Release

### Task Codes (from your plan)
- **P1.T1**: Persistent Gemini CLI Process Launch
- **P1.T2**: Input File (`prompt.md`) Monitoring  
- **P1.T3**: Stdin/Stdout Bridging
- **P1.T4**: Append-Only Output Logging
- **P2.T1**: Process Crash Detection & Restart
- **P2.T2**: Graceful Shutdown (Ctrl+C)
- **P2.T3**: Automatic File Creation & UTF-8 Support
- **P2.T4**: Cross-Platform Validation
- **P3.T1**: Increase Test Coverage to >= 85%
- **P3.T2**: Write README.md
- **P3.T3**: Code Cleanup and Commenting

## Commit Types

### Primary Types
- `feat`: New feature implementation
- `fix`: Bug fixes
- `test`: Adding or modifying tests
- `refactor`: Code restructuring without changing functionality
- `docs`: Documentation changes
- `style`: Code formatting, linting fixes
- `perf`: Performance improvements
- `build`: Build system or dependency changes

### Special Types
- `wip`: Work in progress (for end-of-day commits)
- `checkpoint`: Major milestone reached
- `hotfix`: Critical production fixes

## Commit Examples

### Feature Development
```bash
feat(P1.T1): implement persistent gemini CLI process launch

- Add subprocess.Popen with stdin/stdout piping
- Handle process initialization and basic error cases
- Validate process starts successfully with test prompt

Resolves core requirement for long-running child process.
```

```bash
feat(P1.T2): add prompt.md file monitoring with 200ms polling

- Implement file modification time checking
- Add polling loop with configurable interval
- Handle file not found scenarios gracefully
```

### Bug Fixes
```bash
fix(P1.T3): resolve UTF-8 encoding issues in subprocess communication

- Explicitly set encoding='utf-8' for all subprocess pipes
- Add UTF-8 BOM handling for cross-platform compatibility
- Test with non-ASCII characters in prompts

Fixes issue where emoji and international characters were corrupted.
```

### Testing
```bash
test(P2.T1): add comprehensive tests for process restart logic

- Mock subprocess.Popen for isolated testing
- Test exponential backoff delay progression
- Validate max retry limit enforcement
- Cover edge cases for process.poll() responses

Coverage increased from 45% to 72%.
```

### Work in Progress
```bash
wip(P1.T3): partial implementation of stdout bridging

- Basic non-blocking read structure in place
- TODO: Handle partial reads and buffering edge cases
- Need to test with multi-line responses

End of day checkpoint - continuing tomorrow.
```

### Documentation
```bash
docs(P3.T2): add comprehensive setup and usage instructions

- Document prerequisites and installation steps
- Add step-by-step user workflow walkthrough
- Include troubleshooting section for common issues
- Provide examples of 5-turn conversation workflow
```

### Refactoring
```bash
refactor(P2.T3): extract file operations into dedicated functions

- Move file creation logic to create_default_files()
- Centralize UTF-8 file I/O in read_prompt() and append_response()
- Improve code organization and testability

No functional changes, improved maintainability.
```

### Milestones and Checkpoints
```bash
checkpoint(P1): complete core workflow steel thread

All Phase 1 tasks implemented:
- ✅ P1.T1: Persistent CLI process launch
- ✅ P1.T2: File monitoring (200ms polling)
- ✅ P1.T3: Stdin/stdout bridging
- ✅ P1.T4: Append-only output logging

Manual testing: 5-turn conversation successful.
Ready for Phase 2 hardening work.
```

## Advanced Patterns

### Multi-Task Commits (when appropriate)
```bash
feat(P2.T2,P2.T3): implement graceful shutdown and file auto-creation

- Add SIGINT handler for clean process termination
- Auto-create prompt.md and response.md on startup
- Ensure UTF-8 encoding across all file operations

Addresses both graceful shutdown and file handling requirements.
```

### Hotfix Pattern
```bash
hotfix(P1.T3): fix critical stdout buffer deadlock on Windows

- Force line buffering mode for subprocess stdout
- Add platform-specific buffer flush calls
- Prevent hanging on large responses

Critical fix for Windows compatibility issue.
```

### Cross-Phase Dependencies
```bash
fix(P1.T1→P2.T1): enhance process launch to support restart logic

- Modify initial process creation to be restart-compatible
- Add process state tracking for restart detection
- Prepare foundation for P2.T1 restart implementation

Prerequisite changes for upcoming restart feature.
```

## Branch Naming Convention

Match your commit format with branch names:

```bash
feature/P1.T1-process-launch
feature/P2.T1-process-restart
fix/P1.T3-utf8-encoding
docs/P3.T2-readme
test/P2.T1-restart-coverage
```

## Git Aliases for Efficiency

Add these to your `.gitconfig`:

```ini
[alias]
    # Quick commit with phase-task format
    cf = "!f() { git commit -m \"feat($1): $2\"; }; f"
    cx = "!f() { git commit -m \"fix($1): $2\"; }; f"
    ct = "!f() { git commit -m \"test($1): $2\"; }; f"
    cd = "!f() { git commit -m \"docs($1): $2\"; }; f"
    
    # Work in progress
    wip = "!f() { git add -A && git commit -m \"wip($1): $2\"; }; f"
    
    # Checkpoint commits
    checkpoint = "!f() { git commit -m \"checkpoint($1): $2\"; }; f"
```

Usage examples:
```bash
git cf P1.T1 "implement persistent gemini CLI process launch"
git cx P1.T3 "resolve UTF-8 encoding issues"
git wip P1.T2 "partial file monitoring implementation"
```

## Quality Gates for Commits

### Before Committing
- [ ] Commit addresses single logical change
- [ ] Phase-task reference is accurate
- [ ] Description is clear and actionable
- [ ] Code passes existing tests (`pytest`)
- [ ] Code is formatted (`black .`)

### Commit Message Checklist
- [ ] Type accurately reflects the change
- [ ] Phase.Task reference is correct
- [ ] Description starts with lowercase verb
- [ ] Body explains "why" not just "what" (when needed)
- [ ] Breaking changes noted in footer

## Integration with Development Workflow

### Daily Workflow Integration
```bash
# Morning: Start new task
git checkout develop
git pull
git checkout -b feature/P1.T2-file-monitoring

# During development: Regular WIP commits
git wip P1.T2 "basic polling structure implemented"
git wip P1.T2 "add file modification detection"

# End of task: Final feature commit
git cf P1.T2 "implement prompt.md file monitoring with 200ms polling"

# Create PR
gh pr create --title "feat(P1.T2): implement file monitoring" --base develop
```

This format gives you:
1. **Clear traceability** back to your project plan
2. **Easy filtering** of commits by phase or task
3. **Consistent structure** for team collaboration
4. **Progress tracking** aligned with your milestone structure
5. **Automated tooling support** through aliases and conventions