# 🔐 AegisVault - Secure Pass Engine

**VaultForge** is a cryptographically secure password generator built with Python and Tkinter. It leverages the `secrets` module for hardware-entropy-based randomness instead of standard pseudo-random generation, making it ideal for generating high-assurance cryptographic keys and authentication tokens.

## ✨ Features

### 🛡️ Cryptographic Security
- **Hardware Entropy**: Uses `secrets.choice()` for non-deterministic, OS-level randomness
- **Entropy Evaluation**: Real-time strength assessment (Weak/Medium/Strong) based on length and character variety
- **No Standard RNG**: Replaces vulnerable `random` module with production-grade `secrets` module

### 🎛️ Advanced Controls
- **Adjustable Length**: Generate passwords from 6 to 64 characters via interactive slider
- **Character Set Toggles**: Enable/disable uppercase, lowercase, digits, and symbols independently
- **Explicit Exclusion**: Filter out specific characters in real-time (e.g., exclude ambiguous characters like 0/O, l/1)
- **Live Re-evaluation**: Password regenerates instantly as you modify constraints

### 🖥️ User Experience
- **Neon Cyberpunk UI**: Dark stealth aesthetic with cyan/purple accent palette
- **Clipboard Integration**: Single-click copy with 1.5-second visual feedback
- **Strength Visualization**: Real-time color-coded strength bar (Red/Amber/Green)
- **Read-only Display**: Prevents accidental user tampering with generated key

## 🏗️ Architecture

### Core Components

**Cryptographic Core**
```python
# Production-grade random generation using secrets module
generated_chars = [secrets.choice(filtered_pool) for _ in range(target_length)]
password = "".join(generated_chars)
```

**Character Exclusion Pipeline**
```python
# Live filtering of excluded characters from generation pool
exclusions = self.exclude_entry.get()
filtered_pool = "".join([char for char in pool if char not in exclusions])
```

**Strength Evaluation Matrix**
```python
variety_score = sum([has_upper, has_lower, has_digits, has_symbols])
if length < 8 or variety_score <= 1: strength = "Weak"
elif length < 12 or variety_score <= 3: strength = "Medium"
else: strength = "Strong"
```

**Read-only Protection**
```python
self.password_display.config(state="normal")
self.password_display.insert(0, password)
self.password_display.config(state="readonly")  # Data integrity
```

### UI Framework
- **Tkinter**: Cross-platform desktop GUI
- **TTK Styling**: Custom theme with neon cyberpunk palette
- **Canvas Elements**: Real-time strength visualization with dynamic bars
- **Event Binding**: `<KeyRelease>` triggers for live constraint re-evaluation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (tested on Python 3.10+)
- Tkinter (included with most Python distributions)

### Installation
```bash
# Clone or navigate to the VaultForge directory
cd VaultForge

# Run the application
python app.py

# Or use platform-specific launcher
./run.sh         # Linux/macOS
run.bat          # Windows
```

### Usage
1. **Adjust Length**: Drag slider to set desired password length (6-64 characters)
2. **Configure Character Sets**: Toggle uppercase, lowercase, digits, symbols as needed
3. **Exclude Characters**: Type unwanted characters in the exclusion field (e.g., "0O1l" to remove ambiguous chars)
4. **Generate**: Click "GENERATE FRESH CRYPTO KEY" or modify any setting to auto-regenerate
5. **Copy**: Click "COPY KEY TO CLIPBOARD" to copy password to system clipboard
6. **Evaluate**: Check the strength bar and assessment label to verify entropy level

## 🎨 Color Palette

| Element | Color | Purpose |
|---------|-------|---------|
| Background | `#0a0e17` | Deep terminal aesthetic |
| Cards | `#121824` | UI component frames |
| Accent Cyan | `#00f0ff` | Primary highlights |
| Accent Purple | `#a855f7` | Secondary accents |
| Text Light | `#f1f5f9` | Primary typography |
| Text Muted | `#64748b` | Secondary labels |
| Weak Strength | `#ff4a4a` | Warning red |
| Medium Strength | `#ffb703` | Alert amber |
| Strong Strength | `#39ff14` | Security green |

## 📋 Dependencies

### Built-in (No External Installation Required)
- `tkinter` - GUI framework
- `ttk` - Themed Tkinter widgets
- `messagebox` - Dialog components
- `secrets` - Cryptographic randomness
- `string` - Character set constants

## 🔧 Building Executable

### Using PyInstaller
```bash
# Install PyInstaller
pip install pyinstaller

# Build from spec file
pyinstaller VaultForge.spec

# Executable location: dist/VaultForge.exe
```

## 🧪 Testing

### Local Verification
```bash
python app.py
```

Verify:
- ✅ Window launches and centers on screen
- ✅ Slider adjusts length (6-64)
- ✅ Character toggles (uppercase, lowercase, digits, symbols)
- ✅ Exclusion field filters characters in real-time
- ✅ Password regenerates with each constraint change
- ✅ Strength bar updates dynamically
- ✅ Clipboard copy shows feedback animation
- ✅ No external dependencies required

## 📦 File Structure

```
VaultForge/
├── app.py                    # Main application
├── README.md                 # This file
├── LICENSE                   # MIT License
├── .gitignore                # Git exclusions
├── run.bat                   # Windows launcher
├── run.sh                    # Unix launcher
├── VaultForge.spec           # PyInstaller config
└── dist/
    └── VaultForge.exe        # Compiled executable
```

## 🎓 Educational Value

VaultForge demonstrates key software engineering practices:

1. **Cryptographic Awareness**: Uses `secrets` module instead of `random`, highlighting the importance of proper randomness sources
2. **Event-Driven UI**: Real-time constraint re-evaluation with `<KeyRelease>` binding
3. **State Management**: Defensive programming with read-only widgets and validation
4. **Cross-Platform Design**: Works on Windows, macOS, and Linux without modification
5. **Security Best Practices**: Entropy evaluation, character exclusion, clipboard integration

## 📝 License

MIT License 2026 - See LICENSE file for details

## 🤝 Development

### Contributing
This is part of the OIBSIP (Open Innovation By Skill In Programming) initiative

### Future Enhancements
- Password history tracking (local encrypted storage)
- Passphrase generation mode
- Custom character set definitions
- Advanced entropy metrics
- Integration with password managers

## 📞 Support

For issues or questions, refer to the comprehensive code documentation in `app.py`

---

**⚡ AegisVault: Cryptographically Secure Key Generation On Demand ⚡**
