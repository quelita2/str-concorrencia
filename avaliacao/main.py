import os
import signal
import psutil
import tkinter as tk
from tkinter import ttk


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("800x500")

        # Configuração da grade principal
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Barra de CPU e filtro
        self.top_frame = tk.Frame(root)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        # Barra de CPU
        self.cpu_label = tk.Label(self.top_frame, text="Uso total da CPU:")
        self.cpu_label.pack(side=tk.LEFT, padx=5)

        self.cpu_bar = ttk.Progressbar(self.top_frame, orient="horizontal", length=200, mode="determinate")
        self.cpu_bar.pack(side=tk.LEFT, padx=5)

        self.cpu_percent_label = tk.Label(self.top_frame, text="0%")
        self.cpu_percent_label.pack(side=tk.LEFT, padx=5)

        # Campo de filtro
        self.filter_label = tk.Label(self.top_frame, text="Filtrar por nome:")
        self.filter_label.pack(side=tk.LEFT, padx=5)

        self.filter_entry = tk.Entry(self.top_frame)
        self.filter_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.filter_button = tk.Button(self.top_frame, text="Aplicar Filtro", command=self.apply_filter)
        self.filter_button.pack(side=tk.LEFT, padx=5)

        # Tabela de processos
        self.tree = ttk.Treeview(root, columns=("PID", "Nome", "CPU%", "Status", "Prioridade", "PPID"), show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPU%", text="CPU%")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Prioridade", text="Prioridade")
        self.tree.heading("PPID", text="PPID")
        self.tree.column("PID", width=80, anchor="center")
        self.tree.column("Nome", width=200, anchor="center")
        self.tree.column("CPU%", width=80, anchor="center")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.column("Prioridade", width=100, anchor="center")
        self.tree.column("PPID", width=80, anchor="center")
        self.tree.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        # Botões de ação
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.kill_button = tk.Button(self.button_frame, text="Matar Processo", command=self.kill_process)
        self.kill_button.pack(side=tk.LEFT, padx=5)

        self.suspend_button = tk.Button(self.button_frame, text="Suspender Processo", command=self.suspend_process)
        self.suspend_button.pack(side=tk.LEFT, padx=5)

        self.resume_button = tk.Button(self.button_frame, text="Continuar Processo", command=self.resume_process)
        self.resume_button.pack(side=tk.LEFT, padx=5)

        # Atualização automática
        self.filtered_name = None
        self.update_processes()

    def update_processes(self):
        # Limpar tabela
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Preencher tabela
        for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "status", "ppid", "nice"]):
            try:
                if self.filtered_name and self.filtered_name.lower() not in proc.info["name"].lower():
                    continue

                # Ajustar CPU% para 0 se o processo estiver suspenso
                cpu_percent = proc.info["cpu_percent"]
                if proc.info["status"] == "stopped":
                    cpu_percent = 0.0

                self.tree.insert("", tk.END, values=(
                    proc.info["pid"],
                    proc.info["name"],
                    cpu_percent,
                    proc.info["status"],
                    proc.info["nice"],
                    proc.info["ppid"]
                ))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Atualizar barra de uso da CPU
        total_cpu_percent = psutil.cpu_percent(interval=None)
        self.cpu_bar["value"] = total_cpu_percent
        self.cpu_percent_label["text"] = f"{total_cpu_percent:.1f}%"

        # Atualizar novamente após 1 segundo
        self.root.after(1000, self.update_processes)

    def apply_filter(self):
        self.filtered_name = self.filter_entry.get().strip()
        self.update_processes()

    def get_selected_pid(self):
        selected_item = self.tree.focus()
        if selected_item:
            return int(self.tree.item(selected_item, "values")[0])
        return None

    def kill_process(self):
        pid = self.get_selected_pid()
        if pid:
            try:
                os.kill(pid, signal.SIGKILL)
                print(f"Processo {pid} terminado.")
            except PermissionError:
                print(f"Permissão negada para matar o processo {pid}.")

    def suspend_process(self):
        pid = self.get_selected_pid()
        if pid:
            try:
                os.kill(pid, signal.SIGSTOP)
                print(f"Processo {pid} suspenso.")
            except PermissionError:
                print(f"Permissão negada para suspender o processo {pid}.")

    def resume_process(self):
        pid = self.get_selected_pid()
        if pid:
            try:
                os.kill(pid, signal.SIGCONT)
                print(f"Processo {pid} retomado.")
            except PermissionError:
                print(f"Permissão negada para continuar o processo {pid}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
