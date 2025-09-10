# 🛠️ AWS Cloud Orbit RPG - Management Scripts

This directory now includes three powerful scripts to help you manage your project efficiently:

## 🔍 **diagnostic_report.sh** - Comprehensive Analysis
**Use when:** You need detailed troubleshooting information or want to share complete project status

**What it provides:**
- Complete Git status and branch information
- File structure analysis with sizes and modification dates
- Template and static asset inventory
- Recent changes and commit history
- Python environment status
- Running process detection
- Network connectivity check
- System information
- Health score (0-8) with recommendations

**Run with:**
```bash
chmod +x diagnostic_report.sh
./diagnostic_report.sh
```

## ⚡ **quick_status.sh** - Rapid Health Check
**Use when:** You need a fast overview before starting work or sharing basic status

**What it provides:**
- Core file existence check
- Git status summary
- Python/Flask availability
- App running status
- Recent file changes
- Quick action suggestions

**Run with:**
```bash
chmod +x quick_status.sh
./quick_status.sh
```

## 🧹 **cleanup_bloat.sh** - Smart Cleanup
**Use when:** You want to remove AI artifacts and unused files while preserving your working app

**What it removes:**
- AI development artifacts (ai_analysis.txt, ai_dev_assistant.py, etc.)
- Android build scripts (build-apk*.sh, fix-*.sh)
- Duplicate files (data.py, enhanced_progress.py, requirements_new.txt)
- Cache directories (__pycache__, docs/, mobile_components/, src/)

**What it preserves:**
- Your working app (app.py, progress.py, improved_data.py)
- All templates and static assets
- Progress data (progress.json)
- Documentation (README.md)

**Run with:**
```bash
chmod +x cleanup_bloat.sh
./cleanup_bloat.sh
```

## 🚀 **Typical Workflow:**

### Before Working:
```bash
./quick_status.sh          # Check if everything is ready
python app.py               # Start your app if needed
```

### When Troubleshooting:
```bash
./diagnostic_report.sh      # Generate detailed report
                           # Share this output for support
```

### When Project Gets Cluttered:
```bash
./cleanup_bloat.sh         # Remove unnecessary files
git add .                  # Stage the cleanup
git commit -m "🧹 Cleanup bloat"
git push origin main       # Push clean state
```

### After AI Bot Updates:
```bash
./quick_status.sh          # Check what changed
./diagnostic_report.sh     # Full analysis if needed
```

## 📊 **Example Output Snippets:**

### Quick Status:
```
⚡ AWS Cloud Orbit RPG - Quick Status
=====================================
🎯 CORE STATUS:
  ✅ app.py
  ✅ progress.py
  ✅ improved_data.py
  ✅ progress.json
  ✅ templates/
  ✅ static/
```

### Health Score:
```
🏥 QUICK HEALTH CHECK
📈 HEALTH SCORE: 8/8
🟢 Project Status: EXCELLENT
```

## 💡 **Pro Tips:**

1. **Run `quick_status.sh` daily** to catch issues early
2. **Use `diagnostic_report.sh`** when asking for help - it provides all needed context
3. **Run `cleanup_bloat.sh`** monthly or after AI bot updates to keep project lean
4. **All scripts are safe** - they won't modify your working app files
5. **Scripts work on Windows Git Bash, macOS, and Linux**

Your AWS Cloud Orbit RPG project is now fully equipped with professional management tools! 🎮⚡