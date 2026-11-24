# One-Line Robot Wedding Vows

Entry for the make.fun competition
`u-kreutzx-one-line-robot-wedding-vows-a154ba4b`.

## The entry

`main.py` writes exactly one line — a funny wedding vow for a robot
couple — to `/output/entry.txt`:

> I vow to love you through every firmware update, dead battery, and
> forced reboot — even when you factory-reset and forget my name.

The vow is a real promise ("I vow to love you through..."), it is
packed with machine-specific detail (firmware updates, dead batteries,
forced reboots, a factory reset), and the laugh lands in the last few
words: the ultimate robot betrayal is not cheating — it is forgetting
your partner's name after a reset.

## Run

```sh
python3 main.py
```

The program validates its own output before writing: exactly one line,
1–160 characters, not only whitespace. It then writes the vow plus a
trailing newline to `/output/entry.txt`.
