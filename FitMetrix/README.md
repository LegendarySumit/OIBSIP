# 🧬 FitMetrix - Advanced BMI Dashboard

**Professional biometric tracking and health analytics desktop application** featuring multi-user profiles, historical data persistence, and custom vector-based trend visualization.

---

## 🎯 Features

### Core Functionality
- **Multi-User Profile Management** - Create and manage multiple health profiles with persistent JSON storage
- **BMI Calculation Engine** - Real-time biometric metric computation with health category classification
- **Health Status Classification** - Color-coded categories: Underweight (Blue), Normal (Green), Overweight (Yellow), Obese (Red)
- **Historical Data Tracking** - Complete record of all measurements with timestamp tracking
- **Custom Vector Graphing** - Native Tkinter Canvas-based trend visualization without external dependencies

### User Interface
- **Neon Cyberpunk Aesthetic** - Dark theme with cyan accents matching professional gaming/tech standards
- **Two-Tab Architecture**:
  - **DIAGNOSTICS** - Real-time input form and instant BMI output gauge
  - **HISTORICAL ANALYTICS** - Column-based data table and chronological trend line visualization
- **Responsive Layout** - Optimized window sizing (700x580) with intelligent padding management

### Data Management
- **JSON Persistence** - Automatic profile and measurement persistence across sessions
- **Entry Deletion** - Selective historical record removal with validation
- **Profile Switching** - Seamless user profile transitions with data refresh

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.10 or higher
- Tkinter (included with Python)

### Quick Start

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

**Direct Python:**
```bash
python app.py
```

### Workflow
1. **Create Profile** - Click "+ New Profile" and enter unique username
2. **Run Diagnostics** - Select profile, enter weight (kg) and height (cm), click "RUN METRIC TEST"
3. **View Analytics** - Switch to "HISTORICAL ANALYTICS" tab to see trend graph
4. **Manage Data** - Select history entries and click "Clear Entry" to remove

---

## 🏗️ Architecture

### Class Structure
```
AdvancedBMIDashboard
├── UI Components
│   ├── Header (Title + Subtitle)
│   ├── Profile Manager (Dropdown + New Profile Button)
│   ├── Diagnostics Tab (Input Form + Output Gauge)
│   └── Analytics Tab (Treeview Table + Canvas Graph)
├── Data Layer
│   ├── _load_database() - JSON file I/O
│   ├── _save_database() - Persistence
│   └── bmi_profiles.json structure
└── Visualization
    ├── _draw_trend_graph() - Custom vector rendering
    └── _draw_placeholder_graph() - Empty state messaging
```

### Data Model
```json
{
  "username": [
    {
      "date": "2026-05-27 14:30",
      "weight": 56.0,
      "height": 159.0,
      "bmi": 22.2
    }
  ]
}
```

### BMI Categories
- **Underweight** - BMI < 18.5 (#3a86ff)
- **Normal Health** - BMI 18.5-24.9 (#38b000)
- **Overweight** - BMI 25.0-29.9 (#ffb703)
- **Obese State** - BMI ≥ 30.0 (#e63946)

---

## 🎨 Design System

### Color Palette
- **Background**: #090d16 (Deep canvas)
- **Card**: #131a2c (Panel background)
- **Cyan Accent**: #00f0ff (Primary highlight)
- **Purple Data**: #9d4edd (Trend line)
- **Text Light**: #f1f5f9 (Primary text)
- **Text Muted**: #64748b (Secondary text)

### Typography
- **Header**: Segoe UI 22px Bold (Title)
- **Labels**: Segoe UI 10-13px Bold
- **Data**: Courier New 10-56px (Monospace)

---

## 📋 Technical Stack

- **GUI Framework**: Tkinter (Python built-in)
- **Data Format**: JSON
- **Visualization**: Custom Canvas vector rendering
- **Threading**: Background daemon for placeholder support
- **UI Framework**: TTK with custom styling

---

## 🔧 Configuration

### Window Properties
- **Resolution**: 700x580 pixels
- **Centering**: Auto-centered on screen launch
- **Resizable**: Fixed dimensions (no resizing)
- **Theme**: Dark mode neon aesthetic

### Canvas Graph Settings
- **Padding**: 40x30 pixels (X, Y axes)
- **Grid Lines**: 4 horizontal axis markers with 4px dash pattern
- **Data Points**: 4px cyan nodes with highlighting
- **Trend Line**: 3px purple smooth curve

---

## 📁 File Structure

```
FitMetrix/
├── app.py                 # Main application
├── bmi_profiles.json      # Persistent data store
├── README.md              # This file
├── LICENSE                # MIT 2026
├── .gitignore             # Version control
├── run.bat                # Windows launcher
├── run.sh                 # Unix launcher
├── FitMetrix.spec         # PyInstaller config
└── dist/
    └── FitMetrix.exe      # Standalone Windows executable
```

---

## 🛠️ Development

### Building Executable
```bash
pip install pyinstaller
pyinstaller FitMetrix.spec
```

Output: `dist/FitMetrix.exe` (~12 MB standalone)

### Extending Features
All modifications follow the existing architecture:
- Add new tabs: Create frame in `_build_ui()`, add method like `_build_calc_panel()`
- New calculations: Extend `_evaluate_bmi()` logic
- Custom graphs: Modify `_draw_trend_graph()` canvas operations

---

## 📝 License

MIT License 2026 - See LICENSE file for details

---

## 🎓 Educational Value

This project demonstrates:
- Object-oriented Python GUI design patterns
- JSON data persistence architecture
- Custom widget creation and styling
- Canvas-based vector graphics rendering
- Multi-user application state management

---

**FitMetrix** | Advanced Health Analytics Desktop Application | Python Tkinter GUI Framework
