# -*- coding: utf-8 -*-
import secrets
import time

import tomllib
from rich.console import Console
from wakepy import keep
from pyfiglet import Figlet

console = Console()

fig = Figlet(font="slant")

with open(
    "/Users/evanbaird/Projects/Projects/wakeypy/pyproject.toml",
    mode="rb",
) as fp:
    loading = tomllib.load(fp)
    version = "v." + loading["tool"]["poetry"]["version"]


def do_something():
    """
    Running a simple subprocess to stay awake.

    :return:

    """
    with keep.presenting():
        while True:
            second = 60
            second += 10
            time.sleep(second)


status = " [green]Press Ctrl-C to exit[/green]"


def rando_dots():
    return "dots" + str(secrets.choice(range(2, 9)))


try:
    with console.status(status, spinner=rando_dots()):
        console.print(
            fig.renderText("WakeyPy"),
            style="bold magenta"
        )
        console.print(f"[bold blue]{version}[/bold blue] :desktop_computer:")
        console.print(
            ":white_heavy_check_mark: System will continue running program\n"
            ":white_heavy_check_mark: Presentation mode is on. Screensaver and Screenlock will be prevented.",
            style="green",
        )
        {do_something()}
except KeyboardInterrupt:
    console.print("[bold red]Successfully Exited.[/] [blue]Good Bye!:waving_hand_medium-dark_skin_tone:[/]")