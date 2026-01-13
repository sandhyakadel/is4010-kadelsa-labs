# AI Agent Instructions for IS4010 Course Repository

This file provides context and instructions for AI coding agents working on the IS4010: AI-Enhanced Application Development course materials.

**Format**: This file follows the [AGENTS.md standard](https://agents.md/) - a vendor-neutral, open format for guiding AI coding agents.

---

## Repository Overview

This is the **student-facing template repository** for IS4010, a university course teaching Python (weeks 0-8) and Rust (weeks 9-14) with integrated AI tooling. Students fork this repo to complete weekly labs with automated GitHub Actions grading.

**Sister repository**: Instructor materials (slides, solutions, grading scripts) are in a separate private repository.

---

## Repository Structure

```
is4010-course/
├── week00-week14/          # Weekly lab directories
│   ├── lab*.md             # Lab instructions
│   ├── tests/              # pytest test files (weeks 3-8)
│   ├── src/                # Rust source (weeks 9-14)
│   ├── Cargo.toml          # Rust project files (weeks 9-14)
│   └── notebook.ipynb      # Interactive Jupyter notebooks
├── resources/
│   ├── SETUP_GUIDE.md      # Comprehensive tool installation guide
│   └── TROUBLESHOOTING.md  # Common issues and solutions
├── .github/workflows/      # GitHub Actions CI/CD (one per week)
├── requirements.txt        # Python dependencies
└── README.md               # Student-facing course overview
```

**Key concepts**:
- Each week is self-contained (students work on one week at a time)
- Tests run automatically on push via GitHub Actions
- Weeks 0-2: Setup/verification; Weeks 3-8: Python with pytest; Weeks 9-14: Rust with cargo

---

## Build & Test Commands

### Python (Weeks 0-8)
```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
source venv/Scripts/activate  # Windows Git Bash

# Install dependencies
pip install -r requirements.txt

# Run tests for a specific week
pytest week03/tests/ -v
pytest week04/tests/ -v
# etc.
```

### Rust (Weeks 9-14)
```bash
# Build and test
cd week09
cargo build
cargo test --verbose
cargo fmt --check
cargo clippy -- -D warnings
```

### GitHub Actions
Each week has a workflow file: `.github/workflows/week*.yml`
- Automatically runs on push to `week*/` paths
- Shows pass/fail status via badges in README
- Missing lab files show red (fail), passing tests show green

---

## Code Style & Conventions

### Python
- **Style**: PEP 8, modern idiomatic Python 3.10+
- **Type hints**: Use where appropriate
- **Docstrings**: NumPy-style for educational clarity
- **Testing**: pytest with clear test names (`test_function_returns_expected_value`)

### Rust
- **Style**: Follow `rustfmt` and `clippy` recommendations
- **Linting**: All clippy warnings must pass (`-D warnings`)
- **Testing**: Built-in `cargo test` with descriptive test names

### Markdown (Lab Instructions)
- **Capitalization**: Sentence case, not title case
- **Proper names**: GitHub, VS Code, Python, Rust (correct capitalization)
- **Links**: Descriptive anchor text ("Personal Access Token" not "click here")
- **Hyperlinks**: 15+ links to official docs per lab minimum
- **Code blocks**: Always specify language (```python, ```bash, ```rust)

---

## Lab Structure Standards

Every lab must include:
1. **Header**: Due date, points, learning objectives with hyperlinks
2. **Background**: Context, real-world applications, key concepts
3. **Prerequisites**: Required setup and tools
4. **Instructions**: Clear step-by-step guidance with examples
5. **Expected Repository Structure**: Cumulative tree showing all previous labs
6. **Testing** (Labs 3+): pytest or cargo test integration
7. **Troubleshooting** (Labs 4+): 10+ common issues with solutions
8. **Submission**: Git commands, verification steps, completion checklist

---

## Testing Requirements

### Python Tests (Weeks 3-8)
- Test files: `week*/tests/test_lab*.py`
- Import pattern: `from lab03 import function_name`
- Environment: Add `export PYTHONPATH="${PYTHONPATH}:week03"` before pytest
- Mock interactions: Use `unittest.mock.patch` for input/print/random
- Flexible assertions: Work with any correct implementation

### Rust Tests (Weeks 9-14)
- Built-in: Tests in `src/main.rs` or `tests/` directory
- Run: `cargo test --verbose`
- Formatting: `cargo fmt --check` must pass
- Linting: `cargo clippy -- -D warnings` must pass

---

## GitHub Actions CI/CD

### Workflow Pattern (All weeks)
```yaml
on:
  workflow_dispatch:  # Manual trigger
  push:
    paths:
      - 'week*/**'
      - '.github/workflows/week*.yml'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - Check if lab file exists
      - Run tests if file exists
      - Exit 1 (fail/red) if file missing
      - Exit 0 (pass/green) only if tests pass
```

**Key principle**: Missing files = RED badge, not gray/skipped

---

## Python Tooling

### Required (Students)
- Python 3.10+ from python.org
- Virtual environment: `python -m venv venv`
- Package manager: `pip`

### Optional (Instructor demos)
- `uv`: Modern Python package manager (documented but not required)
- Students see `uv` in demos; SETUP_GUIDE points to official docs

### Common Issues
- `ensurepip` error: Python missing pip (see lab01.md troubleshooting)
- `python` vs `python3`: Use `python3` before venv, `python` after activation
- `pip` vs `pip3`: Same pattern (documented in lab01.md)

---

## Security & Academic Integrity

### Critical Rules
- **NEVER** commit solutions to this public repository
- **NEVER** commit API keys, tokens, or credentials
- Students use private forks with instructor as collaborator
- `.gitignore` already excludes `venv/`, `.env`, credentials

### Student AI Usage
- AI tools (GitHub Copilot, Claude, Gemini CLI) are **encouraged**
- Students must understand and document AI-assisted code
- Academic integrity requires explanation of AI contributions

---

## Contributing Guidelines

### When Creating/Updating Labs
1. **Analyze existing patterns** before creating new content
2. **Read SETUP_GUIDE.md** for tool installation standards
3. **Test all code examples** in specified environment
4. **Add directory structure section** to every lab
5. **Include testing** for Labs 3+ (pytest/cargo test)
6. **Cross-reference resources** (link to SETUP_GUIDE, other labs)
7. **Verify all hyperlinks** work (use curl/HTTP checks)

### Commit Messages
```bash
# Good examples
git commit -m "Add Lab 05 with dictionary and file I/O exercises"
git commit -m "Fix week03 workflow to handle missing lab file"
git commit -m "Update SETUP_GUIDE with uv reference and troubleshooting"

# Include context in multi-line messages
git commit -m "Update week01 workflow to verify hello.py

- Check if week01/hello.py exists
- Run the program if found
- Fail with clear message if missing
- Matches lab01.md requirements"
```

---

## Development Tips

### Finding Things
- Lab instructions: `week*/lab*.md`
- Tests: `week*/tests/` (Python) or `week*/src/` (Rust)
- Workflows: `.github/workflows/week*.yml`
- Student resources: `resources/SETUP_GUIDE.md`, `resources/TROUBLESHOOTING.md`

### Quick Checks
```bash
# Verify all workflows
ls .github/workflows/

# Check Python tests
pytest week03/tests/ week04/tests/ -v

# Check Rust projects
for week in week{09..14}; do
  echo "=== $week ==="
  cd $week && cargo test && cd ..
done

# Find references to a concept
grep -r "virtual environment" week*/lab*.md
```

### Before Pushing
- [ ] All code examples tested
- [ ] Links verified (no 404s)
- [ ] Consistent formatting (sentence case, proper names)
- [ ] No solutions committed
- [ ] GitHub Actions would pass (if applicable)

---

## Quick Reference

- **Python version**: 3.10+ minimum, 3.13+ recommended
- **Rust version**: Latest stable via rustup
- **Testing frameworks**: pytest (Python), cargo test (Rust)
- **CI/CD**: GitHub Actions (one workflow per week)
- **Documentation style**: Sentence case, descriptive links, code examples
- **Student workflow**: Fork → Clone → Work → Test → Push → Check badges

---

**Last Updated**: 2025-01-13
**Questions?** See README.md or SETUP_GUIDE.md
