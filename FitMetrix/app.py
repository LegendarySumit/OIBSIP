import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# Neon Health Dashboard Theme
COLORS = {
    "bg_dark": "#090d16",       # Deep canvas
    "bg_card": "#131a2c",       # Panel background
    "accent_cyan": "#00f0ff",    # Primary highlight
    "accent_purple": "#9d4edd",  # Secondary data line
    "text_light": "#f1f5f9",     # Text primary
    "text_muted": "#64748b",     # Sub-labels
    "underweight": "#3a86ff",    # Category blue
    "normal": "#38b000",         # Category green
    "overweight": "#ffb703",     # Category yellow
    "obese": "#e63946"           # Category red
}

class AdvancedBMIDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("🧬 FitPulse Metrics Dashboard")
        self.root.geometry("700x580")
        self.root.configure(bg=COLORS["bg_dark"])
        self.root.resizable(False, False)
        
        # Center Window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 700) // 2
        y = (self.root.winfo_screenheight() - 580) // 2
        self.root.geometry(f"700x580+{x}+{y}")

        # Data Architecture Initialization
        self.db_file = "bmi_profiles.json"
        self.db = self._load_database()
        self.current_user = None

        self._configure_styles()
        self._build_ui()
        self._refresh_user_dropdown()

    def _load_database(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def _save_database(self):
        with open(self.db_file, "w") as f:
            json.dump(self.db, f, indent=4)

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=COLORS["bg_dark"])
        style.configure("Card.TFrame", background=COLORS["bg_card"], relief="flat")
        style.configure("TLabel", background=COLORS["bg_dark"], foreground=COLORS["text_light"], font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=COLORS["bg_card"], foreground=COLORS["text_light"])
        style.configure("TNotebook", background=COLORS["bg_dark"], borderwidth=0)
        style.configure("TNotebook.Tab", background=COLORS["bg_card"], foreground=COLORS["text_muted"], padding=[15, 5], font=("Segoe UI", 10, "bold"))
        style.map("TNotebook.Tab", background=[("selected", COLORS["bg_dark"])], foreground=[("selected", COLORS["accent_cyan"])])

    def _build_ui(self):
        # --- HEADER SECTION ---
        header_frame = ttk.Frame(self.root, padding=(15, 10, 15, 5))
        header_frame.pack(fill="x")
        
        # Project Title
        tk.Label(header_frame, text="🧬 FitMetrix", font=("Segoe UI", 22, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_cyan"]).pack(anchor="center")
        
        # Salutation Subtitle
        tk.Label(header_frame, text="Advanced Biometric Tracking & Health Analytics Dashboard", font=("Segoe UI", 9), bg=COLORS["bg_dark"], fg=COLORS["text_muted"]).pack(anchor="center", pady=(2, 0))

        # --- USER MANAGEMENT BAR ---
        user_bar = ttk.Frame(self.root, padding=(15, 6, 15, 8))
        user_bar.pack(fill="x")
        
        tk.Label(user_bar, text="Active Profile:", font=("Segoe UI", 10, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_cyan"]).pack(side="left", padx=(0, 8))
        
        self.user_var = tk.StringVar(value="Username")
        self.user_combo = ttk.Combobox(user_bar, textvariable=self.user_var, state="readonly", width=18)
        self.user_combo.pack(side="left", padx=(0, 8))
        self.user_combo.bind("<<ComboboxSelected>>", self._on_user_changed)
        
        new_user_btn = tk.Button(user_bar, text="+ New Profile", font=("Segoe UI", 9, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"], relief="flat", command=self._create_profile)
        new_user_btn.pack(side="left", padx=0)

        # --- MAIN NOTEBOOK INTERFACE ---
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=(0, 8))

        # Panel 1: Core Diagnostics
        self.calc_panel = ttk.Frame(self.notebook, padding=20, style="TFrame")
        self.notebook.add(self.calc_panel, text=" DIAGNOSTICS ")

        # Panel 2: Historical Metrics & Analytics
        self.analytics_panel = ttk.Frame(self.notebook, padding=20, style="TFrame")
        self.notebook.add(self.analytics_panel, text=" HISTORICAL ANALYTICS ")

        self._build_calc_panel()
        self._build_analytics_panel()

    def _build_calc_panel(self):
        # Split into Left (Inputs) and Right (Active Output Gauge)
        left_frame = ttk.Frame(self.calc_panel, style="TFrame")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        right_frame = ttk.Frame(self.calc_panel, style="Card.TFrame", padding=20)
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # --- LEFT PANEL: INPUT FORM ---
        tk.Label(left_frame, text="Body Dimensions Input", font=("Segoe UI", 13, "bold"), bg=COLORS["bg_dark"], fg=COLORS["accent_cyan"]).pack(anchor="w", pady=(0, 20))
        
        # Input Fields Container
        input_container = tk.Frame(left_frame, bg=COLORS["bg_card"], highlightbackground=COLORS["accent_cyan"], highlightthickness=2)
        input_container.pack(fill="both", expand=True, pady=(0, 15))
        
        # Weight Field
        tk.Label(input_container, text="Body Weight (kg)", font=("Segoe UI", 9, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"]).pack(anchor="w", padx=12, pady=(12, 4))
        self.weight_entry = tk.Entry(input_container, font=("Segoe UI", 11), bg=COLORS["bg_dark"], fg=COLORS["text_light"], bd=1, relief="solid", insertbackground=COLORS["accent_cyan"])
        self.weight_entry.pack(fill="x", padx=12, pady=(0, 12), ipady=6)

        # Height Field
        tk.Label(input_container, text="Height (cm)", font=("Segoe UI", 9, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"]).pack(anchor="w", padx=12, pady=(8, 4))
        self.height_entry = tk.Entry(input_container, font=("Segoe UI", 11), bg=COLORS["bg_dark"], fg=COLORS["text_light"], bd=1, relief="solid", insertbackground=COLORS["accent_cyan"])
        self.height_entry.pack(fill="x", padx=12, pady=(0, 12), ipady=6)

        # Action Button
        calc_btn = tk.Button(left_frame, text="RUN METRIC TEST", font=("Segoe UI", 10, "bold"), bg=COLORS["accent_cyan"], fg=COLORS["bg_dark"], relief="flat", activebackground="#00d4e6", command=self._evaluate_bmi)
        calc_btn.pack(fill="x", ipady=8)

        # --- RIGHT PANEL: DIAGNOSTIC OUTPUT ---
        tk.Label(right_frame, text="Diagnostic Output", font=("Segoe UI", 13, "bold"), bg=COLORS["bg_card"], fg=COLORS["accent_cyan"]).pack(pady=(0, 25))
        
        # BMI Display
        self.bmi_display = tk.Label(right_frame, text="00.0", font=("Courier New", 56, "bold"), bg=COLORS["bg_card"], fg=COLORS["text_muted"])
        self.bmi_display.pack()

        self.status_lbl = tk.Label(right_frame, text="Awaiting Input", font=("Segoe UI", 12, "bold"), bg=COLORS["bg_card"], fg=COLORS["text_muted"])
        self.status_lbl.pack(pady=(15, 8))

        self.range_lbl = tk.Label(right_frame, text="Select or create a profile to record structural telemetry.", font=("Segoe UI", 9), bg=COLORS["bg_card"], fg=COLORS["text_muted"], wraplength=250, justify="center")
        self.range_lbl.pack(pady=5)

    def _build_analytics_panel(self):
        # Left Panel: History Treeview | Right Panel: Rendered Vector Graph
        list_frame = ttk.Frame(self.analytics_panel, style="TFrame")
        list_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        graph_frame = ttk.Frame(self.analytics_panel, style="TFrame")
        graph_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Logs Header
        tk.Label(list_frame, text="Historical Log", font=("Segoe UI", 12, "bold"), bg=COLORS["bg_dark"], fg=COLORS["text_light"]).pack(anchor="w", pady=(0, 10))
        
        # Configure Treeview style
        style = ttk.Style()
        style.configure("Treeview", background=COLORS["bg_card"], foreground=COLORS["text_light"], fieldbackground=COLORS["bg_card"], borderwidth=0)
        style.configure("Treeview.Heading", background=COLORS["bg_card"], foreground=COLORS["accent_cyan"], borderwidth=0)
        style.map("Treeview", background=[("selected", COLORS["bg_dark"])], foreground=[("selected", COLORS["accent_cyan"])])
        
        # Treeview with 3 columns
        self.history_tree = ttk.Treeview(list_frame, columns=("#", "Date", "BMI"), height=12, show="headings", style="Treeview")
        self.history_tree.column("#", width=40, anchor="center")
        self.history_tree.column("Date", width=120, anchor="w")
        self.history_tree.column("BMI", width=60, anchor="center")
        
        self.history_tree.heading("#", text="#")
        self.history_tree.heading("Date", text="Date & Time")
        self.history_tree.heading("BMI", text="BMI")
        
        self.history_tree.pack(fill="both", expand=True, pady=(0, 10))
        
        del_btn = tk.Button(list_frame, text="Clear Entry", font=("Segoe UI", 9, "bold"), bg=COLORS["obese"], fg=COLORS["text_light"], relief="flat", command=self._delete_entry)
        del_btn.pack(fill="x")

        # Trend Canvas
        tk.Label(graph_frame, text="BMI Chronological Trend Line", font=("Segoe UI", 12, "bold"), bg=COLORS["bg_dark"], fg=COLORS["text_light"]).pack(anchor="w", pady=(0, 10))
        self.graph_canvas = tk.Canvas(graph_frame, bg=COLORS["bg_card"], bd=0, highlightthickness=0)
        self.graph_canvas.pack(fill="both", expand=True)

    def _refresh_user_dropdown(self):
        profiles = list(self.db.keys())
        self.user_combo["values"] = profiles
        if profiles:
            if not self.current_user or self.current_user not in profiles:
                self.current_user = profiles[0]
            self.user_var.set(self.current_user)
            self._on_user_changed()
        else:
            self.current_user = None
            self.user_var.set("Username")
            self.history_box.delete(0, tk.END)
            self._draw_placeholder_graph()

    def _create_profile(self):
        # Abstract popup logic for rapid inline modal entry
        popup = tk.Toplevel(self.root)
        popup.title("New Profile")
        popup.geometry("260x140")
        popup.configure(bg=COLORS["bg_dark"])
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        tk.Label(popup, text="Enter Unique Username:", bg=COLORS["bg_dark"], fg=COLORS["text_light"]).pack(pady=10)
        entry = tk.Entry(popup, bg=COLORS["bg_card"], fg=COLORS["text_light"], bd=0, insertbackground="white", justify="center")
        entry.pack(fill="x", padx=20, pady=5, ipady=4)
        entry.focus_set()

        def submit():
            name = entry.get().strip()
            if name:
                if name in self.db:
                    messagebox.showerror("Error", "Profile designation already exists.")
                else:
                    self.db[name] = []
                    self._save_database()
                    self.current_user = name
                    self._refresh_user_dropdown()
                    popup.destroy()

        tk.Button(popup, text="Initialize", bg=COLORS["accent_cyan"], fg=COLORS["bg_dark"], relief="flat", command=submit).pack(pady=10)

    def _on_user_changed(self, event=None):
        self.current_user = self.user_var.get()
        self._update_analytics_view()

    def _evaluate_bmi(self):
        if not self.current_user:
            messagebox.showwarning("System Notice", "Please generate or select an active user profile before running diagnostics.")
            return
        
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Validation Error", "Invalid input vectors. Weight and height properties must be standard numeric arrays.")
            return

        if w <= 0 or h <= 0:
            messagebox.showerror("Validation Error", "Physical constraints cannot register as zero or less.")
            return

        # Core Mathematical Vector Formula
        bmi = w / ((h / 100) ** 2)
        bmi = round(bmi, 1)

        # Structural Threshold Boundaries Logic
        if bmi < 18.5:
            status, color = "UNDERWEIGHT", COLORS["underweight"]
            rng = "Below optimal weight profile thresholds (< 18.5)."
        elif bmi < 25.0:
            status, color = "NORMAL HEALTH", COLORS["normal"]
            rng = "Target biometric baseline registered (18.5 - 24.9)."
        elif bmi < 30.0:
            status, color = "OVERWEIGHT", COLORS["overweight"]
            rng = "Elevated baseline limits tracked (25.0 - 29.9)."
        else:
            status, color = "OBESE STATE", COLORS["obese"]
            rng = "Critical saturation threshold exceeded (≥ 30.0)."

        # UI updates
        self.bmi_display.config(text=f"{bmi:.1f}", fg=color)
        self.status_lbl.config(text=status, fg=color)
        self.range_lbl.config(text=rng, fg=COLORS["text_light"])

        # Commit Metric Data Point to JSON Struct
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        data_point = {"date": timestamp, "weight": w, "height": h, "bmi": bmi}
        self.db[self.current_user].append(data_point)
        self._save_database()
        self._update_analytics_view()

    def _update_analytics_view(self):
        # Clear existing Treeview items
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        if not self.current_user or not self.db.get(self.current_user):
            self._draw_placeholder_graph()
            return

        records = self.db[self.current_user]
        for idx, item in enumerate(records):
            self.history_tree.insert("", tk.END, values=(f"{idx+1:02d}", item['date'], f"{item['bmi']}"))
        
        self._draw_trend_graph(records)

    def _delete_entry(self):
        selected = self.history_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select a history entry to delete.")
            return
        
        # Get the item and extract the serial number (first column)
        item_id = selected[0]
        values = self.history_tree.item(item_id, "values")
        serial_num = int(values[0]) - 1  # Convert to 0-based index
        
        if 0 <= serial_num < len(self.db[self.current_user]):
            del self.db[self.current_user][serial_num]
            self._save_database()
            self._update_analytics_view()

    def _draw_placeholder_graph(self):
        self.graph_canvas.delete("all")
        # Simple approach - use fixed center coordinates
        # Canvas should be approximately 300x400 pixels
        self.graph_canvas.create_text(150, 200, text="Telemetry data missing.\n\nRun Diagnostics\nto plot vectors.", fill=COLORS["accent_cyan"], font=("Segoe UI", 10, "bold"), justify="center", anchor="center")

    def _draw_trend_graph(self, records):
        self.graph_canvas.delete("all")
        self.root.update_idletasks()
        
        w = self.graph_canvas.winfo_width()
        h = self.graph_canvas.winfo_height()
        
        # Absolute structural safety pads
        padding_x, padding_y = 40, 30
        graph_w, graph_h = w - (padding_x * 2), h - (padding_y * 2)

        bmis = [r["bmi"] for r in records]
        points_count = len(bmis)

        if points_count < 2:
            # Single entry - show message to add more
            val = bmis[0]
            self.graph_canvas.create_text(150, 200, text=f"Metric: {val}\n\nAdd additional entries\nto see trend.", fill=COLORS["accent_cyan"], font=("Segoe UI", 10, "bold"), justify="center", anchor="center")
            return

        # Calculate limits for standard auto-scaling window
        min_y, max_y = min(bmis) - 2, max(bmis) + 2
        # Safety bound check to prevent Division-by-Zero errors on flat data lines
        if min_y == max_y: 
            min_y -= 5
            max_y += 5

        # Render Axis grid lines
        for i in range(4):
            val_y = min_y + (max_y - min_y) * (i / 3)
            y_pos = h - padding_y - ( (val_y - min_y) / (max_y - min_y) * graph_h )
            self.graph_canvas.create_line(padding_x, y_pos, w - padding_x, y_pos, fill="#1e293b", dash=(4,4))
            self.graph_canvas.create_text(padding_x - 15, y_pos, text=f"{val_y:.0f}", fill=COLORS["text_muted"], font=("Arial", 8))

        # Vector Coordinate Translation Mapping Routine
        coords = []
        for i, val in enumerate(bmis):
            cx = padding_x + (i / (points_count - 1)) * graph_w
            cy = h - padding_y - ( (val - min_y) / (max_y - min_y) * graph_h )
            coords.append((cx, cy))

        # Render Chronological Vector Paths
        for i in range(len(coords) - 1):
            self.graph_canvas.create_line(coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1], fill=COLORS["accent_purple"], width=3, smooth=True)

        # Plot Highlight Nodes
        for cx, cy in coords:
            self.graph_canvas.create_oval(cx-4, cy-4, cx+4, cy+4, fill=COLORS["accent_cyan"], outline=COLORS["bg_card"], width=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedBMIDashboard(root)
    root.mainloop()
