import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

# Cyberpunk Stealth Security Palette - Deep Ocean Theme
COLORS = {
    "bg_dark": "#0f1419",         # Deep ocean background
    "bg_card": "#1a2332",         # Card component frame
    "accent_cyan": "#00d9ff",      # Bright teal accent
    "accent_purple": "#ff6b35",    # Warm coral/orange accent
    "text_light": "#e8f4f8",       # Cool white typography
    "text_muted": "#7a9ba8",       # Cool muted gray
    "strength_weak": "#ff4757",    # Warm red
    "strength_medium": "#ffa502",  # Warm orange
    "strength_strong": "#26de81"   # Fresh green
}

def center_window(window: tk.Tk, width: int, height: int) -> None:
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = max((screen_width - width) // 2, 0)
    y = max((screen_height - height) // 2, 0)
    window.geometry(f"{width}x{height}+{x}+{y}")

class AegisVaultGenerator:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("🔐 VaultForge")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg_dark"])
        center_window(self.root, 480, 580)

        # Core Option Variable Initializations
        self.length_var = tk.IntVar(value=16)
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        
        self._configure_styles()
        self._build_ui()
        self.generate_password()  # Generate initial strong password on launch

    def _configure_styles(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure("TFrame", background=COLORS["bg_dark"])
        style.configure("Card.TFrame", background=COLORS["bg_card"], relief="flat")
        style.configure("TLabel", background=COLORS["bg_dark"], foreground=COLORS["text_light"], font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=COLORS["bg_card"], foreground=COLORS["text_light"])
        
        # Option Box Styles (Interactive checkbox containers)
        style.configure("Option.TFrame", background=COLORS["bg_dark"], relief="flat", borderwidth=1)
        style.map("Option.TFrame", background=[("active", COLORS["bg_card"])])
        
        # Checkbutton / Control Styles
        style.configure("TCheckbutton", background=COLORS["bg_card"], foreground=COLORS["text_light"], font=("Segoe UI", 9))
        style.map("TCheckbutton", 
                  background=[("active", COLORS["bg_card"])],
                  foreground=[("active", COLORS["accent_cyan"])])
        
        # Core Action Trigger Button
        style.configure("Action.TButton", background=COLORS["accent_purple"], foreground=COLORS["text_light"], font=("Segoe UI", 11, "bold"), borderwidth=0, padding=10)
        style.map("Action.TButton", background=[("active", COLORS["accent_cyan"])], foreground=[("active", COLORS["bg_dark"])])

    def _build_ui(self) -> None:
        main_container = ttk.Frame(self.root, padding=20)
        main_container.pack(fill="both", expand=True)

        # --- HEADER TITLE SECTION ---
        header_frame = ttk.Frame(main_container)
        header_frame.pack(fill="x", pady=(0, 15))
        tk.Label(header_frame, text="⚡ VAULTFORGE ⚡", font=("Courier New", 16, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_cyan"]).pack(anchor="center")
        tk.Label(header_frame, text="Cryptographically Secure Key Generator", font=("Segoe UI", 9), bg=COLORS["bg_dark"], fg=COLORS["text_muted"]).pack(anchor="center")

        # --- TELEMETRY OUTPUT CARD ---
        output_card = ttk.Frame(main_container, style="Card.TFrame", padding=15)
        output_card.pack(fill="x", pady=(0, 15))

        # Dynamic Output String Box
        self.password_display = tk.Entry(output_card, font=("Courier New", 14, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_cyan"], bd=0, justify="center", insertbackground="white")
        self.password_display.pack(fill="x", ipady=10, pady=(5, 10))
        
        # Clipboard Trigger Component
        util_frame = ttk.Frame(output_card, style="Card.TFrame")
        util_frame.pack(fill="x")

        self.copy_btn = tk.Button(util_frame, text="📋 COPY KEY TO CLIPBOARD", font=("Segoe UI", 9, "bold"), bg=COLORS["bg_dark"], fg=COLORS["text_light"], activebackground=COLORS["accent_cyan"], activeforeground=COLORS["bg_dark"], relief="flat", bd=0, cursor="hand2", padx=6, pady=6, command=self.copy_to_clipboard)
        self.copy_btn.pack(fill="x")

        # --- PARAMETERS CONTROL PANEL CARD ---
        control_card = ttk.Frame(main_container, style="Card.TFrame", padding=0)
        control_card.pack(fill="both", expand=True, pady=(0, 15))

        # Title Section with Divider
        title_frame = ttk.Frame(control_card, style="Card.TFrame")
        title_frame.pack(fill="x", padx=20, pady=(20, 15))
        tk.Label(title_frame, text="⚙️ VAULT POLICIES & CONSTRAINTS", font=("Segoe UI", 11, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"]).pack(anchor="w")
        
        # Top Divider
        divider1 = tk.Canvas(control_card, height=1, bg=COLORS["accent_cyan"], highlightthickness=0)
        divider1.pack(fill="x", padx=20, pady=(0, 15))

        # --- PASSWORD LENGTH SLIDER SECTION ---
        length_section = ttk.Frame(control_card, style="Card.TFrame")
        length_section.pack(fill="x", padx=20, pady=(0, 15))
        
        length_label_frame = ttk.Frame(length_section, style="Card.TFrame")
        length_label_frame.pack(fill="x", pady=(0, 8))
        tk.Label(length_label_frame, text="📏 Character Array Length:", bg=COLORS["bg_card"], fg=COLORS["text_light"], font=("Segoe UI", 9, "bold")).pack(side="left")
        self.length_indicator = tk.Label(length_label_frame, text="16", font=("Courier New", 14, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"])
        self.length_indicator.pack(side="right")

        slider = tk.Scale(length_section, from_=6, to=64, variable=self.length_var, orient="horizontal", bg=COLORS["bg_card"], fg=COLORS["text_light"], highlightthickness=0, troughcolor=COLORS["bg_dark"], activebackground=COLORS["accent_cyan"], command=self._on_slider_move, length=200)
        slider.pack(fill="x")

        # Middle Divider
        divider2 = tk.Canvas(control_card, height=1, bg=COLORS["accent_purple"], highlightthickness=0)
        divider2.pack(fill="x", padx=20, pady=15)

        # --- CHARACTER COMPOSITION OPTIONS ---
        options_label = tk.Label(control_card, text="🔤 Character Composition Flags", bg=COLORS["bg_card"], fg=COLORS["text_muted"], font=("Segoe UI", 8, "bold"))
        options_label.pack(anchor="w", padx=20, pady=(0, 10))

        # Character Composition Grid - Individual Boxes
        checkbox_frame = ttk.Frame(control_card, style="Card.TFrame")
        checkbox_frame.pack(fill="both", padx=20, pady=(0, 15))
        
        # Create 2x2 symmetric grid with individual option boxes
        self._create_option_box(checkbox_frame, "🅰️ Uppercase", "[A-Z]", self.include_upper, 0, 0)
        self._create_option_box(checkbox_frame, "🅰️ Lowercase", "[a-z]", self.include_lower, 0, 1)
        self._create_option_box(checkbox_frame, "🔢 Numerals", "[0-9]", self.include_digits, 1, 0)
        self._create_option_box(checkbox_frame, "🔣 Symbols", "[!@#$]", self.include_symbols, 1, 1)

        # Middle Divider
        divider3 = tk.Canvas(control_card, height=1, bg=COLORS["accent_cyan"], highlightthickness=0)
        divider3.pack(fill="x", padx=20, pady=15)

        # --- EXCLUSION FILTER SECTION ---
        exclusion_label = tk.Label(control_card, text="🚫 Explicit Character Exclusion Array", bg=COLORS["bg_card"], fg=COLORS["text_muted"], font=("Segoe UI", 8, "bold"))
        exclusion_label.pack(anchor="w", padx=20, pady=(0, 8))
        
        # Create styled exclusion container
        exclusion_container = tk.Frame(control_card, bg=COLORS["bg_dark"], highlightbackground=COLORS["accent_purple"], highlightthickness=1)
        exclusion_container.pack(fill="x", padx=20, pady=(0, 0))
        
        self.exclude_entry = tk.Entry(exclusion_container, font=("Courier New", 11), bg=COLORS["bg_dark"], fg=COLORS["accent_purple"], bd=0, insertbackground=COLORS["accent_cyan"], relief="flat")
        self.exclude_entry.pack(fill="x", ipady=8, padx=10, pady=10)
        self.exclude_entry.bind("<KeyRelease>", lambda e: self.generate_password())

        # --- ENTROPY STRENGTH EVALUATOR ---
        self.strength_canvas = tk.Canvas(main_container, height=6, bg=COLORS["bg_dark"], highlightthickness=0)
        self.strength_canvas.pack(fill="x", pady=(0, 15))

        self.strength_label = tk.Label(main_container, text="STRENGTH ASSESSMENT: OPTIMAL", font=("Segoe UI", 10, "bold"), bg=COLORS["bg_dark"], fg=COLORS["text_muted"])
        self.strength_label.pack(pady=(0, 10))

        # --- MAIN ACTION EXECUTION COMMAND ---
        generate_btn = ttk.Button(main_container, text="GENERATE FRESH CRYPTO KEY", style="Action.TButton", command=self.generate_password)
        generate_btn.pack(fill="x")

    def _on_slider_move(self, value: str) -> None:
        self.length_indicator.config(text=str(value))
        self.generate_password()

    def _create_option_box(self, parent: tk.Widget, label: str, chars: str, var: tk.BooleanVar, row: int, col: int) -> None:
        """Creates an interactive styled option box for character set selection."""
        # Individual option container
        option_box = tk.Frame(parent, bg=COLORS["bg_dark"], highlightbackground=COLORS["accent_cyan"], highlightthickness=1, relief="flat")
        option_box.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
        
        # Configure grid weights for symmetric layout
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        
        # Checkbox with label inside the box
        checkbox = ttk.Checkbutton(option_box, text=label, variable=var, command=self.generate_password, style="TCheckbutton")
        checkbox.pack(fill="x", padx=10, pady=6)
        
        # Character set indicator
        char_label = tk.Label(option_box, text=chars, font=("Courier New", 9, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_purple"])
        char_label.pack(fill="x", padx=10, pady=(0, 6))

    def generate_password(self) -> None:
        """Validates configuration states, maps character strings, and handles structural generation."""
        pool = ""
        if self.include_upper.get(): pool += string.ascii_uppercase
        if self.include_lower.get(): pool += string.ascii_lowercase
        if self.include_digits.get(): pool += string.digits
        if self.include_symbols.get(): pool += string.punctuation

        # Scrub excluded characters from generation pool
        exclusions = self.exclude_entry.get()
        filtered_pool = "".join([char for char in pool if char not in exclusions])

        # Defensive UI adjustment for blank character selection sets
        if not filtered_pool:
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "[ SELECT CHARACTER SETS ]")
            self.password_display.config(state="readonly")
            self._update_strength_ui(0)
            return

        target_length = self.length_var.get()
        
        # Production Implementation: Cryptographically strong pseudo-random number generation
        generated_chars = [secrets.choice(filtered_pool) for _ in range(target_length)]
        password = "".join(generated_chars)

        # Update read-only field contents securely
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state="readonly")
        
        self._evaluate_strength(password)

    def _evaluate_strength(self, password: str) -> None:
        """Runs validation rule matrices to assess mathematical password strength."""
        length = len(password)
        
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digits = any(c in string.digits for c in password)
        has_symbols = any(c in string.punctuation for c in password)
        
        variety_score = sum([has_upper, has_lower, has_digits, has_symbols])
        
        # Structural password validation scaling rules
        if length < 8 or variety_score <= 1:
            self._update_strength_ui(1)  # Weak
        elif length < 12 or variety_score <= 3:
            self._update_strength_ui(2)  # Medium
        else:
            self._update_strength_ui(3)  # Strong

    def _update_strength_ui(self, rank_state: int) -> None:
        self.strength_canvas.delete("all")
        self.root.update_idletasks()
        w = self.strength_canvas.winfo_width()

        if rank_state == 0:
            self.strength_label.config(text="STATUS: AWAITING SELECTION CRITERIA", fg=COLORS["text_muted"])
            self.strength_canvas.create_rectangle(0, 0, w, 6, fill=COLORS["bg_card"], width=0)
        elif rank_state == 1:
            self.strength_label.config(text="CRITICAL ALERT: VULNERABLE KEY PRESET", fg=COLORS["strength_weak"])
            self.strength_canvas.create_rectangle(0, 0, w // 3, 6, fill=COLORS["strength_weak"], width=0)
        elif rank_state == 2:
            self.strength_label.config(text="WARNING STATE: MEDIUM ENTROPY PROFILE", fg=COLORS["strength_medium"])
            self.strength_canvas.create_rectangle(0, 0, (w // 3) * 2, 6, fill=COLORS["strength_medium"], width=0)
        else:
            self.strength_label.config(text="VAULT SECURITY STATUS: SYSTEM OPTIMAL", fg=COLORS["strength_strong"])
            self.strength_canvas.create_rectangle(0, 0, w, 6, fill=COLORS["strength_strong"], width=0)

    def copy_to_clipboard(self) -> None:
        """Invokes safe system clipboard pipeline transactions."""
        password_text = self.password_display.get()
        if password_text and password_text != "[ SELECT CHARACTER SETS ]":
            self.root.clipboard_clear()
            self.root.clipboard_append(password_text)
            
            # Temporary non-blocking UI alert state confirmation
            self.copy_btn.config(text="⚡ KEY COPIED SUCCESSFULLY! ⚡", fg=COLORS["strength_strong"])
            self.root.after(1500, lambda: self.copy_btn.config(text="📋 COPY KEY TO CLIPBOARD", fg=COLORS["text_light"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = AegisVaultGenerator(root)
    root.mainloop()
