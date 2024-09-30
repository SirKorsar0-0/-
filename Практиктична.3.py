list = {
    "a": "T",
    "b": "T",
    "c": "T",
    "d": "T",
    "e": "T",
    "f": "T",
    "g": "T",
    "h": "T",
    "i": "T",
    "j": "T",
}
list["b"] = "F"
list["g"] = "F"
del list["c"]
list["d"] = 0
print(list)
