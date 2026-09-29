from logs import create_log_entry, get_next_id
from database import save_logs, load_logs

import questionary as q

from time import sleep

import sys

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console


print()
print(Panel.fit("[bold cyan]               ModLogium               [/bold cyan]", border_style="bold cyan", subtitle="Version 1.0"))
print()


def main():

    while True:

        menuSelection = q.select(
            "What do you want to do?",
            choices=[
                "Create new entry",
                "View logs",
                "Settings",
                "Exit"
            ]
        ).ask()

        if menuSelection == "Create new entry":

            print()
            username = q.text(
                "Username:",
                validate=lambda text: True if len(text.strip()) > 0 else "Invalid entry.").ask()

            print()
            userID = q.text(
                "User ID:",
                validate=lambda text: True if len(text.strip()) > 0 else "Invalid Entry.").ask()

            print()
            action = q.text(
                "Moderation action:",
                validate=lambda text: True if len(text.strip()) > 0 else "Invalid Entry.").ask()

            print()
            reason = q.text(
                "Reason:",
                validate=lambda text: True if len(text.strip()) > 0 else "Invalid Entry.").ask()

            print()
            moderator = q.text(
                "Logged by (moderator):",
                validate=lambda text: True if len(text.strip()) > 0 else "Invalid Entry.").ask()

            print()
            confirmation = q.select(
                "Are you sure you want to create this log entry? This action can not be undone.",
                choices=[
                    "Yes",
                    "No"
                ]).ask()

            if confirmation == "Yes":
    
                console = Console()

                console.print()

                with console.status("[bold green]Saving log entry...", spinner="dots"):
                    logs = load_logs()
                    log_id = get_next_id(logs)
                    newEntry = create_log_entry(
                        log_id, username, userID, action, reason, moderator
                    )

                    logs.append(newEntry)
                    logs.sort(key=lambda x: int(x["id"]))
                    save_logs(logs)

                    sleep(1)


                console.print("Entry has been logged [bold green]successfully[/bold green].\n")

            else:
                pass

        if menuSelection == "View logs":

            logs = load_logs()

            if not logs:
                print()
                print("[bold red]No logs found.[/bold red]")
                print()

            else:
                logsTable = Table(
                    title="Moderation Logs", header_style="bold cyan"
                )

                logsTable.add_column("ID", style="bold")
                logsTable.add_column("Username", overflow="wrap")
                logsTable.add_column("User ID", overflow="wrap")
                logsTable.add_column("Action", overflow="wrap")
                logsTable.add_column("Reason", overflow="wrap")
                logsTable.add_column("Moderator", overflow="wrap")
                logsTable.add_column("Date", style="dim", overflow="wrap")

                for log in logs:
                    logsTable.add_row(
                        log["id"],
                        log["username"],
                        log["userID"],
                        log["action"],
                        log["reason"],
                        log["moderator"],
                        log["date"]
                    )

                print()
                print(logsTable)
                print()

        if menuSelection == "Settings":
            print()
            print("This feature is currently [red]unavailable[/red]. :(")
            print()

        if menuSelection == "Exit":

            print()
            print("[bold red]ModLogium has been closed.[/bold red]")
            print()
            break


if __name__ == "__main__":
    main()