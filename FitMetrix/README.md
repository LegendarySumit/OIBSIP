<div align="center">

# 💪 FitMetrix

**Advanced Biometric Tracking & Health Analytics Dashboard**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-ff7f50)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

*Multi-User Profiles • Real-time BMI Calculation • Historical Analytics • Neon UI*

[Features](#-features) • [Quick Start](#-quick-start) • [Tech Stack](#-tech-stack) • [Project Structure](#-project-structure)

</div>

---

## 📖 About

**FitMetrix** is a professional-grade biometric tracking and health analytics desktop application designed to help users monitor their fitness metrics with precision and style. Built with Python and Tkinter, it combines powerful health analytics with a modern neon cyberpunk aesthetic that makes fitness tracking engaging and intuitive.

The application leverages a robust multi-user profile system with persistent JSON-based storage, enabling seamless data management across sessions. Whether you're tracking your BMI over time, monitoring health trends, or managing multiple family members' fitness profiles, FitMetrix provides the tools you need with a sleek, professional interface.

Featuring real-time biometric computation, custom vector-based trend visualization, and color-coded health categories, FitMetrix transforms health data into actionable insights at a glance.

---

## ✨ Features

- ✅ **Multi-User Profile Management** — Create and manage unlimited health profiles with persistent storage
- ✅ **Real-Time BMI Calculation** — Instant biometric metric computation with industry-standard algorithms
- ✅ **Health Status Classification** — Color-coded categories (Underweight, Normal, Overweight, Obese) for instant health insights
- ✅ **Historical Data Tracking** — Complete measurement history with automatic timestamp tracking for trend analysis
- ✅ **Custom Vector Graphing** — Native Tkinter Canvas-based visualization without external dependencies
- ✅ **Two-Tab Interface** — Seamless navigation between real-time diagnostics and historical analytics
- ✅ **Neon Cyberpunk UI** — Modern dark theme with cyan/purple accents for professional appearance
- ✅ **Cross-Platform Support** — Works on Windows, Linux, and macOS
- ✅ **JSON Persistence** — Automatic profile and measurement data persistence across sessions
- ✅ **Selective Data Management** — Delete specific entries with validation and data integrity checks

---

## 🛠️ Tech Stack

### Core Framework
- **Python 3.10+** — High-performance programming language
- **Tkinter** — Native GUI toolkit with no external dependencies

### Data Management
- **JSON** — Lightweight data persistence and profile storage

### Build & Distribution
- **PyInstaller** — Executable packaging for standalone distribution
- **Batch/Shell Scripts** — Cross-platform launch utilities

---

## 📁 Project Structure

```
FitMetrix/
├── app.py                      # Main application (715+ lines)
├── run.bat                     # Windows launcher
├── run.sh                      # Linux/macOS launcher
├── README.md                   # Documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── FitMetrix.spec             # PyInstaller configuration
├── bmi_profiles.json          # User profiles database (auto-generated)
├── best_score.json            # Achievement tracking (auto-generated)
├── build/                     # Build artifacts
└── dist/                      # Distribution executables
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10 or higher** (Tkinter is included)
- No additional dependencies required

### Installation

#### Option 1: Direct Python (Recommended for Development)
```bash
# Clone the repository
git clone https://github.com/LegendarySumit/FitMetrix.git
cd FitMetrix

# Run the application
python app.py
```

#### Option 2: Batch Script (Windows)
```batch
run.bat
```

#### Option 3: Shell Script (Linux/macOS)
```bash
bash run.sh
```

#### Option 4: Standalone Executable
Use the pre-built executable in the `dist/` folder for portable usage without Python installation.

---

## ⚙️ Configuration

### Default Settings
```python
Window Size: 700x580 pixels (optimized for all screen sizes)
Theme: Dark mode with cyan/purple accents
Database: bmi_profiles.json (auto-created in app directory)
```

### Data Storage
- **Profile Data**: Stored in `bmi_profiles.json` (auto-generated on first run)
- **Achievement Tracking**: Stored in `best_score.json` (tracks personal records)
- All data persists automatically between sessions

### Customization
Edit the `COLORS` dictionary in `app.py` to customize the color scheme:
```python
COLORS = {
    "bg_dark": "#090d16",           # Background color
    "accent_cyan": "#00f0ff",       # Primary accent
    "accent_purple": "#9d4edd",     # Secondary accent
    # ... more colors
}
```

---

## 📚 Usage

### Creating a Profile
1. Launch FitMetrix
2. Click the **"+ New Profile"** button
3. Enter a username for the new profile
4. Start logging your biometric data

### Recording Measurements
1. Select your profile from the dropdown
2. Switch to the **DIAGNOSTICS** tab
3. Enter your measurements:
   - **Height** (in cm)
   - **Weight** (in kg)
   - **Date** (automatically filled with current date)
4. Click **"Calculate BMI"** to compute and save
5. View instant health status classification with color coding

### Analyzing Trends
1. Navigate to the **HISTORICAL ANALYTICS** tab
2. View all past measurements in the data table
3. Observe trend visualization on the graph
4. Track progress over time with chronological data

### Deleting Entries
1. Select an entry in the historical data table
2. Click **"Delete Selected Entry"**
3. Confirm the deletion when prompted
4. Data updates automatically

---

## 📊 Health Categories

FitMetrix uses standard BMI classifications with color-coded indicators:

| Category | BMI Range | Color | Indicator |
|----------|-----------|-------|-----------|
| Underweight | < 18.5 | 🔵 Blue | Below healthy range |
| Normal Weight | 18.5 - 24.9 | 🟢 Green | Optimal health |
| Overweight | 25 - 29.9 | 🟡 Yellow | Above healthy range |
| Obese | ≥ 30 | 🔴 Red | Health risk category |

---

## 🔌 Data Management

### JSON Profile Format
```json
{
  "John_Doe": {
    "measurements": [
      {
        "date": "2026-05-28",
        "height_cm": 180,
        "weight_kg": 75,
        "bmi": 23.15,
        "category": "normal"
      }
    ]
  }
}
```

### Backup & Export
- Manually backup `bmi_profiles.json` and `best_score.json` from the app directory
- Store copies in a safe location for data recovery

---

## 🐛 Troubleshooting

### Issue: "Tkinter not found" Error
**Solution**: Install Tkinter using your package manager:
- **Windows**: Tkinter comes with Python (ensure it's selected during installation)
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk@3.10`

### Issue: Application Won't Launch
**Solution**: 
1. Ensure Python 3.10+ is installed: `python --version`
2. Navigate to the FitMetrix directory
3. Run directly: `python app.py`
4. Check for error messages and report issues

### Issue: Data Not Persisting
**Solution**:
1. Ensure the app directory has write permissions
2. Check that `bmi_profiles.json` exists in the app directory
3. Close the application completely before reopening

### Issue: UI Elements Misaligned
**Solution**: This shouldn't occur, but if it does:
1. Restart the application
2. Ensure your display resolution is at least 800x600
3. Report the issue with your screen resolution

---

## 🔮 Future Enhancements

- [ ] **BMI Trend Analytics** — Advanced statistical analysis and predictions
- [ ] **Export to PDF** — Generate printable health reports
- [ ] **Goal Tracking** — Set and monitor fitness goals
- [ ] **Database Migration** — SQLite backend for better scalability
- [ ] **Cloud Sync** — Multi-device profile synchronization
- [ ] **Dark/Light Theme Toggle** — User-selectable themes
- [ ] **Fitness Recommendations** — AI-powered health suggestions
- [ ] **Mobile App** — Cross-platform mobile companion
- [ ] **Data Visualization Charts** — Advanced charting with matplotlib
- [ ] **Nutrition Integration** — Calorie tracking and meal logging

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

MIT License © 2026 LegendarySumit - You are free to use, modify, and distribute this software with proper attribution.

---

## 👨‍💻 Author

**LegendarySumit**

- **GitHub**: [@LegendarySumit](https://github.com/LegendarySumit)
- **Project Repository**: [FitMetrix](https://github.com/LegendarySumit/FitMetrix)
- **Portfolio**: [LegendarySumit's Projects](https://github.com/LegendarySumit)

---

<div align="center">

### 💪 Transform Your Fitness Data Into Actionable Insights

*Build better health habits with precision tracking and professional analytics*

---

**⭐ Star this repo if you find it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/LegendarySumit/FitMetrix?style=social)](https://github.com/LegendarySumit/FitMetrix)

</div>
