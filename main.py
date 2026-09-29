from logs import create_log_entry, get_next_id, search_logs
from database import save_logs, load_logs

import questionary as q

from time import sleep

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown


console = Console()

def main_menu():

    console.clear()
    
    print()
    print(Panel.fit("[bold cyan]               ModLogium               [/bold cyan]", border_style="bold cyan", subtitle="Version 1.1.0"))
    print()

def exitquest():

    exitrequest = q.press_any_key_to_continue("Press any key to continue.").ask()

    main_menu()

def buildLogTable(logs_to_show):

    if not logs_to_show:
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

        for log in logs_to_show:
            logsTable.add_row(
                str(log["id"]),
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

def main():

    main_menu()

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
                print()

                with console.status("[bold yellow]Saving log entry...", spinner="dots"):
                    logs = load_logs()
                    log_id = get_next_id(logs)
                    newEntry = create_log_entry(
                        log_id, username, userID, action, reason, moderator
                    )

                    logs.append(newEntry)
                    logs.sort(key=lambda x: int(x["id"]))

                    success = save_logs(logs)
                    sleep(1)

                if success:
                    print("[bold green]Success:[/bold green] Log has been saved.")
                else:
                    print("[bold red]Error 100:[/bold red] Failed to save log.")
                
                print()
                exitquest()


        if menuSelection == "View logs":
            
            print()
            slctLogsView = q.select(
                "Select what logs you want to see:",
                choices=[
                    "View all logs",
                    "Search logs"
                ]
            ).ask()

            if slctLogsView == "View all logs":
                logs = load_logs()
                buildLogTable(logs)

                exitquest()

            if slctLogsView == "Search logs":
                
                logs = load_logs()
                query = q.text("What do you want to search for?").ask()

                results = search_logs(logs, query)
                buildLogTable(results)

                exitquest()


        if menuSelection == "Settings":
            print()
            print("This feature is currently [red]unavailable[/red]. :(")
            print()

            exitquest()


        if menuSelection == "Exit":

            confirmation = q.confirm("Are you sure?").ask()

            if confirmation == True:
                print()
                print("[bold red]ModLogium has been closed.[/bold red]")
                print()

                sleep(3)
                console = Console()
                console.clear()
                break

            else:
                main_menu()


if __name__ == "__main__":
    main()