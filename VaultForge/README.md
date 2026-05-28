<div align="center">

# 🔐 VaultForge

**Cryptographically Secure Password Generator with Enterprise-Grade Security**

![Python](https://img.shields.io/badge/Python-3.13%2B-3776ab?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-informational?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT%202026-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)

*Hardware Entropy • Character Exclusion • Real-Time Strength Assessment • Clipboard Integration*

[Features](#-features) • [Quick Start](#-quick-start) • [Tech Stack](#-tech-stack) • [Usage](#-usage)

</div>

---

## 📖 About

**VaultForge** is a professional-grade password generator built with Python and Tkinter that prioritizes cryptographic security and user control. Unlike standard password generators that rely on vulnerable pseudo-random functions, VaultForge leverages the `secrets` module for hardware-entropy-based randomness—the gold standard for cryptographic applications.

This desktop application demonstrates advanced security practices including proper entropy generation, real-time constraint validation, and defensive programming patterns. Perfect for developers who need reliable key generation, security professionals validating password policies, or anyone serious about cybersecurity.

With its polished **Deep Ocean** user interface and intuitive controls, VaultForge makes enterprise-grade password generation accessible and enjoyable. The symmetric design and interactive option boxes provide visual feedback for every action, while the real-time strength evaluator ensures you always know the security profile of your generated key.

---

## ✨ Features

- ✅ **Hardware Entropy Generation** — Uses `secrets.choice()` for cryptographically secure randomness
- ✅ **Adjustable Length** — Generate passwords from 6 to 64 characters with interactive slider
- ✅ **Character Set Control** — Toggle uppercase, lowercase, digits, and symbols independently
- ✅ **Character Exclusion** — Filter out specific characters in real-time (ambiguous chars, etc.)
- ✅ **Real-Time Strength Assessment** — Dynamic Weak/Medium/Strong evaluation with color-coded bars
- ✅ **Live Re-evaluation** — Password regenerates instantly as constraints change
- ✅ **Clipboard Integration** — Single-click copy with 1.5-second visual feedback
- ✅ **Read-Only Protection** — Prevents accidental tampering with generated passwords
- ✅ **Professional UI** — Deep Ocean theme with symmetric design and visual dividers
- ✅ **Cross-Platform** — Works seamlessly on Windows, macOS, and Linux

---

## 🛠️ Tech Stack

### Core Framework
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.13+ | Application runtime |
| **Tkinter** | Built-in | GUI framework |
| **TTK** | Built-in | Themed widgets |

### Security
| Component | Purpose |
|-----------|---------|
| **`secrets`** | Cryptographic randomness (OS-level entropy) |
| **`string`** | Character set constants |

### Build & Distribution
| Tool | Purpose |
|------|---------|
| **PyInstaller 6.20.0** | Standalone executable generation |
| **Git** | Version control |

**All dependencies are built-in** — No external packages required!

---

## 📁 Project Structure

```
VaultForge/
├── app.py                    # Main application (270+ lines)
├── README.md                 # Project documentation
├── LICENSE                   # MIT License 2026
├── .gitignore               # Git exclusions
├── run.bat                  # Windows launcher script
├── run.sh                   # Unix launcher script
├── VaultForge.spec          # PyInstaller configuration
└── dist/
    └── VaultForge.exe       # Compiled standalone executable (~12 MB)
```

---

## 🚀 Quick Start

### Option 1: Run Python Source (Recommended for Development)

```bash
# Clone the OIBSIP repository
git clone https://github.com/LegendarySumit/OIBSIP.git
cd OIBSIP/VaultForge

# Run directly with Python
python app.py

# Or use platform-specific launcher
./run.sh          # Linux/macOS
run.bat           # Windows
```

### Option 2: Run Standalone Executable (Recommended for End Users)

```bash
# Navigate to VaultForge directory
cd VaultForge/dist

# Execute directly
./VaultForge.exe  # Windows
./VaultForge      # macOS/Linux
```

### Prerequisites

- **Python 3.8+** (tested on 3.13.12)
- **Tkinter** — Included with most Python distributions
- Windows/macOS/Linux operating system

---

## ⚙️ Configuration

VaultForge requires **zero configuration**. The application works out-of-the-box with sensible defaults:

| Setting | Default | Range | Purpose |
|---------|---------|-------|---------|
| **Password Length** | 16 characters | 6-64 | Initial password size |
| **Uppercase** | ✅ Enabled | On/Off | Include A-Z characters |
| **Lowercase** | ✅ Enabled | On/Off | Include a-z characters |
| **Digits** | ✅ Enabled | On/Off | Include 0-9 characters |
| **Symbols** | ✅ Enabled | On/Off | Include !@#$% etc. |
| **Exclusions** | Empty | Any string | Characters to filter out |

All settings update in real-time without application restart.

---

## 📚 Usage

### Step-by-Step Guide

**1. Adjust Password Length**
- Drag the slider or click to set desired length (6-64 characters)
- Real-time length indicator shows current value

**2. Configure Character Sets**
- Click checkboxes for Uppercase, Lowercase, Digits, Symbols
- Each option box shows the character range included
- Password regenerates automatically

**3. Exclude Specific Characters (Optional)**
- Type unwanted characters in exclusion field
- Examples: `0O1l` (removes ambiguous characters), `!@` (removes special chars)
- Password re-evaluates in real-time

**4. Monitor Strength**
- Check the color-coded strength bar:
  - 🔴 **Red** = Weak (< 8 chars or limited variety)
  - 🟠 **Orange** = Medium (12+ chars, 3 character types)
  - 🟢 **Green** = Strong (16+ chars, 4 character types)

**5. Generate & Copy**
- Click **"GENERATE FRESH CRYPTO KEY"** for new password
- Click **"COPY KEY TO CLIPBOARD"** to copy (feedback: ⚡ KEY COPIED SUCCESSFULLY!)
- Paste into password managers or destination applications

### Example Use Cases

**Scenario 1: Generate Strong Login Password**
```
Length: 20
Settings: All character sets enabled
Exclusion: (none)
Result: Strong entropy with full character variety
```

**Scenario 2: Remove Ambiguous Characters**
```
Length: 16
Settings: All enabled
Exclusion: 0O1l (removes zero/O, one/l confusion)
Result: User-friendly strong password
```

**Scenario 3: Alphanumeric Only (No Symbols)**
```
Length: 18
Settings: Uppercase ✅, Lowercase ✅, Digits ✅, Symbols ❌
Exclusion: (none)
Result: Enterprise system compatible password
```

---

## 🔐 Security Architecture

### Cryptographic Core

```python
# Hardware-entropy based generation
generated_chars = [secrets.choice(filtered_pool) for _ in range(target_length)]
password = "".join(generated_chars)
```

**Why `secrets` instead of `random`?**
- `random` module: Pseudo-random, predictable, NOT for cryptography
- `secrets` module: Cryptographically secure, uses OS entropy, production-grade

### Character Exclusion Pipeline

```python
# Real-time filtering of excluded characters
exclusions = self.exclude_entry.get()
filtered_pool = "".join([char for char in pool if char not in exclusions])
```

Ensures excluded characters never appear in generated passwords.

### Strength Evaluation Matrix

```python
variety_score = sum([has_upper, has_lower, has_digits, has_symbols])

if length < 8 or variety_score <= 1:
    strength = "Weak"
elif length < 12 or variety_score <= 3:
    strength = "Medium"
else:
    strength = "Strong"
```

Combines length AND variety for accurate assessment.

---

## 🎨 UI/UX Design

### Deep Ocean Color Palette

| Element | Color | Usage |
|---------|-------|-------|
| **Background** | `#0f1419` | Main window background |
| **Cards** | `#1a2332` | Component containers |
| **Accent Teal** | `#00d9ff` | Primary highlights & titles |
| **Accent Coral** | `#ff6b35` | Secondary accents & labels |
| **Text Light** | `#e8f4f8` | Primary typography |
| **Text Muted** | `#7a9ba8` | Secondary labels |
| **Strength Red** | `#ff4757` | Weak password indicator |
| **Strength Orange** | `#ffa502` | Medium password indicator |
| **Strength Green** | `#26de81` | Strong password indicator |

### Interactive Elements

- **Option Boxes** — Cyan-bordered containers with checkboxes and character ranges
- **Strength Bar** — Dynamic canvas visualization with real-time color updates
- **Slider Control** — Interactive length adjustment with numeric feedback
- **Clipboard Button** — Animated feedback with temporary status message

---

## 🔧 Building Standalone Executable

### With PyInstaller

```bash
# Install PyInstaller (if not already installed)
pip install pyinstaller

# Build from spec file
cd VaultForge
pyinstaller VaultForge.spec

# Executable location
# Output: dist/VaultForge.exe (~12 MB)
```

### Spec File Configuration

```python
# VaultForge.spec
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VaultForge',
    debug=False,
    console=False,  # No console window
    upx=True,       # UPX compression
)
```

**Key Settings:**
- `console=False` — GUI application only
- `upx=True` — Optimized binary size
- `name='VaultForge'` — Executable name

---

## 🧪 Testing

### Local Verification Checklist

```bash
# Run application
python app.py

# Test checklist:
□ Window launches and centers on screen
□ Slider adjusts length (6-64) smoothly
□ All 4 character toggles function
□ Exclusion field filters characters in real-time
□ Password regenerates with each change
□ Strength bar updates dynamically
□ Clipboard copy shows feedback animation
□ No external dependencies required
□ Cross-platform compatibility verified
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | 270+ |
| **Functions** | 8 |
| **Classes** | 1 (AegisVaultGenerator) |
| **Dependencies** | 0 external (all built-in) |
| **Executable Size** | ~12 MB |
| **Python Version** | 3.13.12 |
| **Build Tool** | PyInstaller 6.20.0 |
| **License** | MIT 2026 |

---

## 🐛 Troubleshooting

### Application Won't Launch

**Problem:** `ModuleNotFoundError: No module named 'tkinter'`

**Solution:**
```bash
# Tkinter is included with Python, but may need installation on Linux
sudo apt-get install python3-tk        # Debian/Ubuntu
sudo yum install python3-tkinter       # RHEL/CentOS
brew install python-tk                 # macOS
```

### Passwords Not Changing

**Problem:** Same password generated repeatedly

**Solution:**
- Change exclusion field or character toggles
- Password regenerates on any constraint change
- Click "GENERATE FRESH CRYPTO KEY" button explicitly

### Exclusion Field Not Working

**Problem:** Excluded characters still appearing in password

**Solution:**
- Ensure character is typed exactly (case-sensitive)
- Example: `O` (letter O) and `0` (zero) are different
- Clear field and try again

### Executable Won't Run

**Problem:** `VaultForge.exe` fails on target machine

**Solution:**
- Ensure Windows 7 SP1 or later
- Try running as Administrator
- Rebuild executable with: `pyinstaller VaultForge.spec --clean`

---

## 🔮 Future Enhancements

- [ ] Password history tracking with encryption
- [ ] Passphrase generation mode (dictionary words)
- [ ] Custom character set definitions
- [ ] Advanced entropy metrics display
- [ ] Integration with password managers (KeePass, 1Password)
- [ ] Batch password generation
- [ ] Password strength validation for popular services
- [ ] Multi-language support

---

## 📝 License

This project is licensed under the **MIT License 2026** — See [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**LegendarySumit**

- **GitHub:** [@LegendarySumit](https://github.com/LegendarySumit)
- **Project Repository:** [OIBSIP/VaultForge](https://github.com/LegendarySumit/OIBSIP/tree/master/VaultForge)
- **Release:** [vaultforge-v1.0.0](https://github.com/LegendarySumit/OIBSIP/releases/tag/vaultforge-v1.0.0)

---

<div align="center">

## 🔐 Enterprise-Grade Security, Now in Your Hands

**VaultForge: Because Your Passwords Deserve Cryptographic Security**

*Built with Python 3.13 • Tkinter GUI • PyInstaller 6.20.0*

---

**⭐ Star this repo if VaultForge helped you secure your passwords!**

</div>
