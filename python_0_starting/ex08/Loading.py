import os
import time
from time import sleep


def get_terminal_size():
    """
    Return the current terminal width and height.

    Attempts to read the terminal size from the operating system.
    If the size cannot be determined (e.g. no attached terminal),
    returns a safe default size of 80 columns by 20 rows.
    """
    try:
        return os.get_terminal_size(0)
    except OSError:
        return os.terminal_size((80, 20))


def ft_tqdm(lst: range):
    """
    Iterate over a range while displaying a dynamic progress bar.

    This generator mimics basic tqdm behavior by rendering a
    terminal progress bar that updates in-place. The bar adapts
    to the terminal width, shows percentage completed, elapsed
    time, estimated remaining time, and iteration speed.

    The display is throttled to avoid excessive redraws and
    remains stable for large iteration counts.

    Yields:
        None: One value per iteration, allowing use in a for-loop.
    """
    columns, _ = get_terminal_size()
    total = len(lst)
    start_time = time.time()
    update_every = 13
    CLEAR_LINE = "\033[2K"

    # prepare a line to overwrite
    print()
    print("\033[F", end="")

    for i, _ in enumerate(lst):
        if i == 0 or (i + 1) % update_every == 0 or i + 1 == total:
            now = time.time()
            progress = (i + 1) / total

            elapsed_time = now - start_time
            remaining_time = (
                (elapsed_time / (i + 1)) * (total - (i + 1))
                if i > 0 else 0
            )
            it_per_sec = (
                (i + 1) / elapsed_time
                if elapsed_time > 0 else 0
            )

            # fixed-width right-hand side (tqdm-style)
            elapsed_str = \
                f"{int(elapsed_time//60):02d}:{int(elapsed_time 
                                                   % 60):02d}"
            remaining_str = \
                f"{int(remaining_time//60):02d}:{int(remaining_time % 60):02d}"
            speed_str = f"{it_per_sec:6.2f}it/s"

            right = (
                f"{i + 1:>{len(str(i))}}/{total} "
                f"[{elapsed_str}<{remaining_str}, {speed_str}]"
            )

            left = f"{progress * 100:3.0f}%|"

            # dynamically clamp bar width to terminal size
            bar_length = max(1, columns - len(left) - len(right) - 2)

            filled = int(progress * bar_length)
            bar = "█" * filled + " " * (bar_length - filled)

            line = f"{left}{bar}| {right}"

            print(f"\r{CLEAR_LINE}{line}", end="", flush=True)

        sleep(0.00001)
        yield
